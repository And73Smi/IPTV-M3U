@echo off
echo The filename:and-5.m3u8 %~n1
echo The extention:mp3_to_m3u.m3u %~x1

REM Make new directories in the same folder.
md media\%~n1\hls

REM Get the cover jpg and preview gif from video
ffmpeg -i %~n1%~x1  -ss 20.00 -vframes 1 ./media/%~n1/hls/cover_h1.jpg
ffmpeg -i %~n1%~x1  -ss 20.00 -vframes 1 -s 760x428 ./media/%~n1/hls/cover_l1.jpg
ffmpeg -ss 00:00:10 -t 3 -i %~n1%~x1 -s 640x360 -r  2 ./media/%~n1/hls/preview.gif

REM Start to work on videos
ffmpeg -i %~n1%~x1 -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -threads 5 -preset ultrafast -f hls ./media/%~n1/hls/360_out.m3u8
ffmpeg -i %~n1%~x1 -profile:v baseline -level 3.0 -s 800x480 -start_number 0 -hls_time 10 -hls_list_size 0 -threads 5 -preset ultrafast -f hls ./media/%~n1/hls/480_out.m3u8
ffmpeg -i %~n1%~x1 -profile:v baseline -level 3.0 -s 1280x720 -start_number 0 -hls_time 10 -hls_list_size 0 -threads 5 -preset ultrafast -f hls ./media/%~n1/hls/720_out.m3u8
ffmpeg -i %~n1%~x1 -profile:v baseline -level 3.0 -s 1920x1080 -start_number 0 -hls_time 10 -hls_list_size 0 -threads 5 -preset ultrafast -f hls ./media/%~n1/hls/1080_out.m3u8

REM Check if any error
if %ERRORLEVEL% == 0 goto :next
echo "Errors encountered during execution. Exited with status: %errorlevel%"
goto :endofscript

:next
echo "Generating overall m3u8 play list...."
REM Generate an overall play list.
(
echo #EXTM3U
echo #EXT-X-STREAM-INF:BANDWIDTH=375000,RESOLUTION=640x360
echo 360_out.m3u8
echo #EXT-X-STREAM-INF:BANDWIDTH=750000,RESOLUTION=854x480
echo 480_out.m3u8
echo #EXT-X-STREAM-INF:BANDWIDTH=2000000,RESOLUTION=1280x720
echo 720_out.m3u8
echo #EXT-X-STREAM-INF:BANDWIDTH=3500000,RESOLUTION=1920x1080
echo 1080_out.m3u8
) > ./media/%~n1/hls/%~n1.m3u8
echo "Overall m3u8 play list generated."

goto :endofscript

:endofscript
echo "Work complete."

REM Brought to you by Duke Yin www.dukeyin.com
pause