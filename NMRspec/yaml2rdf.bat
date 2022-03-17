@ECHO OFF
FOR %%f IN (.\jdx_files\output\*.yaml) DO (
	echo converting %%f to .ttl
   	linkml-convert -s .\model\schema\NMRspec.yaml -t ttl .\jdx_files\output\%%~nf.yaml -o .\jdx_files\output\%%~nf.ttl
)
echo all done