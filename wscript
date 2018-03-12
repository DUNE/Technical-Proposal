#!/usr/bin/env python

import os

top='.'

#-quiet

def options(opt):
    opt.load('tex')
    opt.add_option('--prompt-level', default=0,
                   help="pdfLaTeX prompt level.  Set to 1 for debugging.")


def configure(cfg):
#    cfg.find_program('dune-params', var='DUNEPARAMS')
    cfg.load('tex')
    cfg.find_program('chapters.sh', var='CHAPTERS',
                     path_list=[os.path.realpath(".")])
    pass


def build_params(bld):
    '''
    Build DUNE PARAMS.
    '''
    paramsxls = bld.path.find_resource('data/parameters.xls')
    paramspy = bld.path.find_resource('python/parameters.py')
    os.environ['PYTHONPATH'] = paramspy.parent.abspath()


    # generate files from parameter templates
    for tmpl in bld.path.ant_glob('**/templates/*.tex.j2'):
        tmp = tmpl.parent.parent
        gen_dir = tmp.make_node('generated')
        target = gen_dir.make_node(str(tmpl.change_ext('.tex', '.tex.j2')))
        rule='${DUNEPARAMS} render -f parameters.filter -t ${SRC[1].abspath()} -o ${TGT[0].abspath()} ${SRC[0].abspath()}'
        bld(rule=rule,
            source = [paramsxls, tmpl, paramspy], # last ones just for dependencies
            target = target, 
            shell = True)



def build(bld):

    prompt_level = bld.options.prompt_level

    #build_params(bld)

    voltexs = ["executive-summary.tex",
               "far-detector-single-phase.tex",
               "far-detector-dual-phase.tex",
               "software-computing.tex"]

    chaptex = bld.path.find_resource("chapters.tex")

    for voltex in voltexs:

        volname = voltex.replace(".tex","")
        voldir = bld.path.find_dir(volname)
        bld(features='tex', prompt=prompt_level,
            source = voltex,
            target = voltex.replace(".tex",".pdf"))

        bld.install_files('${PREFIX}',voltex.replace(".tex",".pdf"))

        for chtex in voldir.ant_glob("**/chapter*.tex"):
            chname = os.path.basename(str(chtex))
            chmaintex = bld.path.find_or_declare("%s-%s" % (volname, chname))

            bld(source=[chaptex, chtex],
                target=[chmaintex],
                rule="${CHAPTERS} ${SRC} ${TGT}")

            bld(features='tex',
                prompt = prompt_level,
                source = os.path.basename(str(chmaintex)),
                # name target as file name so can use --targets w/out full path
                target = os.path.basename(str(chmaintex.change_ext('pdf','tex'))))

            bld.install_files('${PREFIX}',chmaintex.change_ext('.pdf', '.tex'))
        # bld(features='tex',
        #     type='pdflatex',
        #     source = tex,
        #     outs = 'pdf',
        #     )
        # bld.install_files('${PREFIX}',tex.change_ext('.pdf', '.tex'))
    return


