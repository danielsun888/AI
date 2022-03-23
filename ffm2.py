import ffmpy
ff = ffmpy.FFmpeg(
    inputs={'test.mp4': None},
    outputs={'output.avi': None}
 )
ff.run()