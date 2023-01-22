Select 'begin; Insert into public.[table_name] ([column_name]) Select \'' + table_schema + '.' + table_name + '.' + column_name + '\' as referenceName, ' + '\'' + Case when data_type in ('integer', 'smallint','bigint','numeric') then 'sum_column' 
else 

'commit;' as Query
from information_schema.column C
where (table_schema like '[placeholder]')
order by table_name asc, column_name asc
