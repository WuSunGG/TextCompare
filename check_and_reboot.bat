@set service_is_ok=false
@for /F "delims=\t" %%i in ('netstat -ano^|findstr :8217') do @set service_is_ok=%%i
@if  "%service_is_ok%" neq "false" (echo %date% %time%: service is running ... >> service.log) else (echo %date% %time%: restart service ... >> service.log && %~dp0runserver.bat)


