/*
Problem Statement: How to identify Serializable Isolation violation error on tables due to transformation or query executuion in Redshift Datawarehouse?
Example Issue:
{
    "name": "error",
    "length": 110,
    "severity": "ERROR",
    "code": "XX000",
    "detail": "Serializable isolation violation on table - {}, transactions forming the cycle are: {} (pid:{})" }
*/
--Solution:
-- Will show the order of queries from all the transactions combined:

Select btrim(text), xid, starttime 
from svl_statementtext 
where xid in ([placeholder]) order by starttime;

-- Create a view using query from below, to see which queries got aborted: https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_get_tbl_reads_and_writes.sql

-- Operation 'A' will indicate aborted, The last column can be used to check for aborted queries, aborted = 1 indicates it:
Select btrim(username) as username, w.*, btrim(q.querytxt), q.aborted
from [placeholder schema].v_get_tbl_reads_and _writes w
join stl_query q on q.query = w.query
join pg_user on q.userid = usesysid
where w.xid in ([placeholder])
order by statement_starttime;

-- Query to show which transaction mentioned in the error is aborted:
Select *
from stl_tr_conflict 
where xact_id in ([placeholder]);

-- Shows table name:
Select * from svv_table_info 
where table_id = [placeholder];


-- Get queries for aborted transactions:
Select xid, text as query_text, starttime, endtime, 
  Case xid
  When xid = [aborted_xid] then 1 
  else 0
  END as aborted,
  from svl_statementtext where xid IN ([placeholder])
  order by starttime;




