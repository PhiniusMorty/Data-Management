
Create or replace procedure [Schema].[proc_name] ( INOUT re_out refcursor)
  Language plpgsql
  AS $$
  
  Declare rec RECORD;
  
  Begin
  
  Execute 'Truncate table [Schema].[tabel_name]; ';
  For rec in select Query from public.query_redshift
    LOOP
    --Raise INFO 'a = %', rec.query;
    Execute rec.query;
    END LOOP;
    
  Open re_out for select table_name, total_rows_table_redshit
  from [Schema].[tabel_name];

END;
$$
