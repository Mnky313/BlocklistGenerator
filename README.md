Python script within a docker container to download a list of blocklists (Designed for ONLY domains, not hosts format however it should convert hosts format. Ignroes ABP format)

# How to run

Clone repo
Modify app/blocklists.txt to add/remove lists.

create .env file with the OutputPath variable.

Example .env:

```
OutputPath=/path/to/output.txt
```

build and run the container

`docker compose up -d`

You can also modify the script (app/grab_lists.py) to run at a different time, currently it runs at 02:00 every day.