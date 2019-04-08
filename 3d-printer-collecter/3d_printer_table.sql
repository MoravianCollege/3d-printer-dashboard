DROP DATABASE printer;

CREATE DATABASE printer;

USE printer;


CREATE TABLE job_history(
  printer VARCHAR(50) ,
  filename VARCHAR(50) ,
  starttime VARCHAR(50)PRIMARY KEY,
  endtime VARCHAR(50),
  time_elapsed INT(50),
  status VARCHAR(15),
  extruder1_temp FLOAT(50),
  extruder2_temp FLOAT(50),
  bedtemp FLOAT(50)
);


INSERT INTO job_history(printer,filename,starttime,endtime,time_elapsed,status,extruder1_temp,extruder2_temp,bedtemp) VALUES
('gutenberg', 'example1', '12-12-18-0' ,'12-13-18-0' , '5500','printing','19.3','23.3','22.2');

INSERT INTO job_history(printer,filename,starttime,endtime,time_elapsed,status,extruder1_temp,extruder2_temp,bedtemp) VALUES
('xerox', 'example2', '12-12-18-1000' ,'12-13-18-0' , '10000','printing','19.8','23.1','24.2');
