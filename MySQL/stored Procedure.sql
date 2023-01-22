# Drop procedure storedPorc;

Create procedure storedProc()
begin

Declare var1 int;
Declare var2 varchar(200);
Declare done INT Default False;
Declare cursor_list Cursor For Select * from [table_name];
Declare CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

truncate table [schema].[table_name];
commit;

Open Cursor_list;
  Loop_list: LOOP
    FETCH cusrsor_list into var2;
    IF done then 
      LEAVE loop_list;
    END IF;
  
  SET @quer1 = var2;
  Prepare stmt_name From @query1;
    Execute stmt_name;
  commit;
  
  DEALLOCATE PREPARE stmt_name;
  
  END LOOP loop_list;
  
  Close cursor_list;
  
END;
