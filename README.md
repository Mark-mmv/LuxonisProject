# LuxonisProject
###### Parser 500 newest apartments sereality.cz

# You need:
    docker 4.14.0 (or newer)
    

# How to use:

## 0) Preparation
    a) install Docker 4.14.0 (or newer)
    b) have virtualization enabled in your BIOS/UEFI (check it in your Task Manager>performance>CPU>Virtualisation)
    C) in directory (../LuxonisProject) enter command "docker-compose up"

## 1) Database PostgreSQL

    host: localhost(127.0.0.1:)
    
    port: 8081
        
    System: PostgreSQL
    
    Server: db_task
    
    Username: luxonis
    
    Password: 2022
    
    Database: apartments_db
        
        and viz. table "apartments500"
    
    
    
## 2) HTTP server:  port: 8081

    host: localhost(127.0.0.1:)
    
    port: 8080
