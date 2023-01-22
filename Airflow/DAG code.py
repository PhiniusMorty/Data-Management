"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""
#import sys

#sys.path.insert(1, '/{}/{}')
#import all modules

from __future__ import annotations

# [START tutorial]
# [START import_module]
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

# [END import_module]


# Default arguments:
default_args = {
  'owner': 'Ashish',
  'depends_on_past': False,
  'start_date': datetime(2022, 12, 15),
  'retries': 5  
  #"email": ["airflow@example.com"],
  #"email_on_failure": False,
  #"email_on_retry": False,
  #"retry_delay": timedelta(minutes=5),
  # 'queue': 'bash_queue',
  # 'pool': 'backfill',
  # 'priority_weight': 10,
  # 'end_date': datetime(2016, 1, 1),
  # 'wait_for_downstream': False,
  # 'sla': timedelta(hours=2),
  # 'execution_timeout': timedelta(seconds=300),
  # 'on_failure_callback': some_function,
  # 'on_success_callback': some_other_function,
  # 'on_retry_callback': another_function,
  # 'sla_miss_callback': yet_another_function,
  # 'trigger_rule': 'all_success'
}

# Add any functions or variables here

# [START instantiate_dag]
with DAG(
    #"tutorial",
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args=default_args,
    # [END default_args]
    dag_id = "sample DAG"
    description="A simple tutorial DAG",
    # At a schedule of 0th min every hour
    schedule= '0 */1 * * *', #timedelta(days=1)
    catchup=False,
    tags=["example"],
) as dag_id:
    # [END instantiate_dag]

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    # [START basic_task]
    # NOTE: you can also add for loop to dynamically create new tasks and if else conditions:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )
  
    t3 = PostgresOperator(
        task_id="redshift",
        postgres_conn_id = 'Redshift',
        sql = f" Begin; END;"
        
    )
    
    t4 = BranchPythonOperator(
        task_id = t4,
        python_callable = [Fucntion],
        #pool
        #provide_context = True,
        op_kwargs = { 
           # Key: Value
        }
    )
    
    end = BashOperator(
        task_id = "end",
        bash_command = "echo 'Skipping'"
    )
    
    # [END basic_task]
    
#########################Study More in the Block######Unknown Commands#################################    
    # [START documentation]
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG; OR
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this
    # [END documentation]

    # [START jinja_template]
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )

    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command,
    )
    # [END jinja_template]
####################################################################################################################  
    
  
  # Organizer:
    t1 >> [t2, t3]
    
# [END tutorial]
