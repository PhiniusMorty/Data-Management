-- Creating a sample dynamic query for reference

Select 'begin; Insert into public.[table_name] ([column_name]) Select \'' + table_schema + '.' + table_name + '.' + column_name + '\' as referenceName, ' + '\'' + Case when data_type in ('integer', 'smallint','bigint','numeric') then 'sum_column' 
else 'count rows' END + '\'' + ' as Metric_operation, ' + 'count(1) as Total_rows_table_redshift ' + 'from ' + table_schema + '.' + '"' + table_name + '";' + 'commit;' as Query
from information_schema.column
where (table_schema like '[placeholder]')
order by table_name asc, column_name asc;
