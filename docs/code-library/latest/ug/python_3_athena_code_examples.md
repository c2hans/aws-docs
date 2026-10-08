---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_athena_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Athena examples using SDK for Python (Boto3)
<a name="python_3_athena_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Athena.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello Athena
<a name="athena_Hello_python_3_topic"></a>

The following code example shows how to get started using Athena.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
def hello_athena(athena_client: BaseClient) -> None:
    """
    Lists Amazon Athena workgroups. Demonstrates basic connectivity to the
    Athena service.

    :param athena_client: A Boto3 Athena client.
    """
    print("Listing Athena workgroups...\n")
    try:
        workgroup_count = 0
        next_token = None
        while True:
            kwargs = dict()
            if next_token is not None:
                kwargs["NextToken"] = next_token
            response = athena_client.list_work_groups(**kwargs)
            for wg in response.get("WorkGroups", list()):
                name = wg.get("Name", "Unknown")
                state = wg.get("State", "Unknown")
                print(f"  Workgroup: {name} (State: {state})")
                workgroup_count += 1
            next_token = response.get("NextToken", None)
            if next_token is None:
                break
        print(f"\nFound {workgroup_count} workgroup(s).")
    except ClientError as err:
        logger.error(
            "Error listing Athena workgroups. %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    hello_athena(boto3.client("athena"))
```
+  For API details, see [ListWorkGroups](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListWorkGroups) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn Athena basics
<a name="athena_Scenario_python_3_topic"></a>

The following code example shows how to learn Athena basics.
+ Create an Athena workgroup.
+ Verify the workgroup configuration.
+ Create a database and table using DDL queries.
+ Run SELECT queries and retrieve results.
+ Create, list, and delete named queries.
+ List query executions.
+ Clean up all resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).
Run an interactive scenario at a command prompt.

```
class AthenaScenario:
    """Runs the Amazon Athena basics scenario."""

    def __init__(
        self,
        athena_wrapper: AthenaWrapper,
        cf_client: BaseClient,
        s3_client: BaseClient,
    ) -> None:
        """
        Initializes the scenario.

        :param athena_wrapper: An AthenaWrapper instance for Athena operations.
        :param cf_client: A Boto3 CloudFormation client.
        :param s3_client: A Boto3 S3 client.
        """
        self.athena_wrapper = athena_wrapper
        self.cf_client = cf_client
        self.s3_client = s3_client
        self.stack_name = ""
        self.bucket_name = ""
        self.workgroup_name = ""
        self.database_name = ""
        self.named_query_id = ""

    def run(self) -> None:
        """Orchestrates the complete Athena basics scenario."""
        print(DASHES)
        print("Welcome to the Amazon Athena Basics Scenario!")
        print(
            "This scenario demonstrates how to use Amazon Athena to create "
            "workgroups, run SQL queries, manage named queries, and more."
        )
        print(DASHES)

        try:
            self.setup()
            self.step1_verify_workgroup()
            self.step2_create_database()
            self.step3_create_table()
            self.step4_run_select_query()
            self.step5_create_named_query()
            self.step6_list_named_queries()
            self.step7_execute_named_query()
            self.step8_list_query_executions()
        finally:
            self.cleanup()

        print(DASHES)
        print("Amazon Athena Basics scenario complete!")
        print(DASHES)

    # ---- Setup ---------------------------------------------------------------

    def setup(self) -> None:
        """Deploys the CloudFormation stack and creates the Athena workgroup."""
        print(DASHES)
        print("Setting up resources...")
        print(DASHES)

        # Deploy CloudFormation stack for S3 bucket.
        unique_suffix = uuid.uuid4().hex[:8]
        self.stack_name = f"athena-basics-stack-{unique_suffix}"
        self.workgroup_name = f"athena-basics-wg-{unique_suffix}"
        self.database_name = f"{DATABASE_PREFIX}_{unique_suffix}"

        template_body = json.dumps(
            {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Description": "S3 bucket for Athena basics scenario query results.",
                "Resources": {
                    "ResultsBucket": {
                        "Type": "AWS::S3::Bucket",
                        "Properties": {
                            "BucketName": f"{self.stack_name}-results",
                        },
                    }
                },
                "Outputs": {
                    "BucketName": {
                        "Value": {"Ref": "ResultsBucket"},
                        "Description": "Name of the S3 results bucket.",
                    }
                },
            }
        )

        print(f"Creating CloudFormation stack '{self.stack_name}'...")
        self.cf_client.create_stack(
            StackName=self.stack_name,
            TemplateBody=template_body,
        )

        # Wait for stack creation.
        waiter = self.cf_client.get_waiter("stack_create_complete")
        print("Waiting for stack creation to complete...")
        waiter.wait(
            StackName=self.stack_name,
            WaiterConfig={"Delay": 10, "MaxAttempts": 60},
        )

        # Retrieve bucket name from outputs.
        response = self.cf_client.describe_stacks(StackName=self.stack_name)
        outputs = response["Stacks"][0].get("Outputs", list())
        for output in outputs:
            if output["OutputKey"] == "BucketName":
                self.bucket_name = output["OutputValue"]
                break

        print(f"CloudFormation stack '{self.stack_name}' created successfully.")
        print(f"S3 bucket for query results: {self.bucket_name}")

        # Create Athena workgroup.
        output_location = f"s3://{self.bucket_name}/athena-results/"
        print(f"\nCreating Athena workgroup '{self.workgroup_name}'...")
        self.athena_wrapper.create_work_group(
            name=self.workgroup_name,
            output_location=output_location,
        )
        print(f"Workgroup '{self.workgroup_name}' created successfully.")
        print(DASHES)

    # ---- Step 1 --------------------------------------------------------------

    def step1_verify_workgroup(self) -> None:
        """Verifies the workgroup configuration."""
        print(DASHES)
        print("Step 1: Verifying workgroup configuration")

        wg = self.athena_wrapper.get_work_group(self.workgroup_name)
        config = wg.get("Configuration", dict())
        result_config = config.get("ResultConfiguration", dict())

        print(f"  Workgroup: {wg.get('Name')}")
        print(f"  State: {wg.get('State')}")
        print(f"  Output location: {result_config.get('OutputLocation', 'N/A')}")
        print(
            f"  Enforce configuration: "
            f"{config.get('EnforceWorkGroupConfiguration', 'N/A')}"
        )
        print(
            f"  CloudWatch metrics enabled: "
            f"{config.get('PublishCloudWatchMetricsEnabled', 'N/A')}"
        )
        print(DASHES)

    # ---- Step 2 --------------------------------------------------------------

    def step2_create_database(self) -> None:
        """Creates a database using a DDL query."""
        print(DASHES)
        print(f"Step 2: Creating database '{self.database_name}'")

        query = f"CREATE DATABASE IF NOT EXISTS {self.database_name}"
        print(f"Running query: {query}")

        execution_id = self.athena_wrapper.start_query_execution(
            query_string=query, work_group=self.workgroup_name
        )
        print(f"Query execution ID: {execution_id}")
        print("Waiting for query to complete...")

        result = self.athena_wrapper.wait_for_query_to_complete(execution_id)
        exec_time = result.get("Statistics", dict()).get(
            "EngineExecutionTimeInMillis", 0
        )
        print(f"Query completed successfully. (Execution time: {exec_time}ms)")
        print(f"Database '{self.database_name}' created.")
        print(DASHES)

    # ---- Step 3 --------------------------------------------------------------

    def step3_create_table(self) -> None:
        """Creates a table with sample data using CTAS."""
        print(DASHES)
        print(f"Step 3: Creating table '{TABLE_NAME}' with sample data")

        query = f"""
        CREATE TABLE {self.database_name}.{TABLE_NAME} AS
        SELECT * FROM (
            VALUES
                (1, 'The Shawshank Redemption', 1994, 9.3),
                (2, 'The Godfather', 1972, 9.2),
                (3, 'The Dark Knight', 2008, 9.0),
                (4, 'Pulp Fiction', 1994, 8.9),
                (5, 'Forrest Gump', 1994, 8.8),
                (6, 'Inception', 2010, 8.8),
                (7, 'The Matrix', 1999, 8.7),
                (8, 'Goodfellas', 1990, 8.7),
                (9, 'The Silence of the Lambs', 1991, 8.6),
                (10, 'Saving Private Ryan', 1998, 8.6)
        ) AS t(id, title, year, rating)
        """
        print("Running CTAS query to create table with 10 movie records...")

        execution_id = self.athena_wrapper.start_query_execution(
            query_string=query,
            work_group=self.workgroup_name,
            database=self.database_name,
        )
        print(f"Query execution ID: {execution_id}")
        print("Waiting for query to complete...")

        result = self.athena_wrapper.wait_for_query_to_complete(execution_id)
        exec_time = result.get("Statistics", dict()).get(
            "EngineExecutionTimeInMillis", 0
        )
        print(f"Query completed successfully. (Execution time: {exec_time}ms)")
        print(f"Table '{self.database_name}.{TABLE_NAME}' created with sample data.")
        print(DASHES)

    # ---- Step 4 --------------------------------------------------------------

    def step4_run_select_query(self) -> None:
        """Runs a SELECT query and retrieves results."""
        print(DASHES)
        print("Step 4: Running analytical query")

        query = (
            f"SELECT title, year, rating FROM {self.database_name}.{TABLE_NAME} "
            "WHERE rating >= 9.0 ORDER BY rating DESC"
        )
        print(f"Query: {query}")

        execution_id = self.athena_wrapper.start_query_execution(
            query_string=query,
            work_group=self.workgroup_name,
            database=self.database_name,
        )
        print(f"Query execution ID: {execution_id}")
        print("Waiting for query to complete...")

        result = self.athena_wrapper.wait_for_query_to_complete(execution_id)
        stats = result.get("Statistics", dict())
        exec_time = stats.get("EngineExecutionTimeInMillis", 0)
        data_scanned = stats.get("DataScannedInBytes", 0)
        print(
            f"Query completed successfully. "
            f"(Execution time: {exec_time}ms, Data scanned: {data_scanned} bytes)"
        )

        # Retrieve and display results.
        query_results = self.athena_wrapper.get_query_results(execution_id)
        columns = query_results["columns"]
        rows = query_results["rows"]

        print("\nQuery Results:")
        header = " | ".join(f"{c:<30}" for c in columns)
        print(f"  {header}")
        print(f"  {'-' * len(header)}")
        for row in rows:
            row_str = " | ".join(f"{v:<30}" for v in row)
            print(f"  {row_str}")
        print(f"\n{len(rows)} rows returned.")
        print(DASHES)

    # ---- Step 5 --------------------------------------------------------------

    def step5_create_named_query(self) -> None:
        """Creates a named (saved) query."""
        print(DASHES)
        print("Step 5: Creating a named (saved) query")

        self.named_query_id = self.athena_wrapper.create_named_query(
            name="top-rated-movies",
            description="Returns movies with a rating of 9.0 or higher",
            database=self.database_name,
            query_string=(
                "SELECT title, year, rating FROM movies "
                "WHERE rating >= 9.0 ORDER BY rating DESC"
            ),
            work_group=self.workgroup_name,
        )
        print("Named query 'top-rated-movies' created successfully.")
        print(f"Named Query ID: {self.named_query_id}")
        print("Description: Returns movies with a rating of 9.0 or higher")
        print(DASHES)

    # ---- Step 6 --------------------------------------------------------------

    def step6_list_named_queries(self) -> None:
        """Lists named queries in the workgroup."""
        print(DASHES)
        print("Step 6: Listing named queries in workgroup")

        named_query_ids = self.athena_wrapper.list_named_queries(self.workgroup_name)
        print(
            f"Found {len(named_query_ids)} named query ID(s) in workgroup "
            f"'{self.workgroup_name}':"
        )
        for nq_id in named_query_ids:
            print(f"  - {nq_id}")
        if self.named_query_id in named_query_ids:
            print("Verified: Our saved query is in the list.")
        print(DASHES)

    # ---- Step 7 --------------------------------------------------------------

    def step7_execute_named_query(self) -> None:
        """Executes the saved named query and retrieves results."""
        print(DASHES)
        print("Step 7: Executing the saved named query")

        # Retrieve the query string from the saved named query.
        named_query = self.athena_wrapper.get_named_query(self.named_query_id)
        query_string = named_query["QueryString"]
        print("Running named query 'top-rated-movies'...")

        execution_id = self.athena_wrapper.start_query_execution(
            query_string=query_string,
            work_group=self.workgroup_name,
            database=self.database_name,
        )
        print(f"Query execution ID: {execution_id}")
        self.athena_wrapper.wait_for_query_to_complete(execution_id)
        print("Query completed successfully.")

        query_results = self.athena_wrapper.get_query_results(execution_id)
        columns = query_results["columns"]
        rows = query_results["rows"]

        print("\nResults:")
        header = " | ".join(f"{c:<30}" for c in columns)
        print(f"  {header}")
        print(f"  {'-' * len(header)}")
        for row in rows:
            row_str = " | ".join(f"{v:<30}" for v in row)
            print(f"  {row_str}")
        print(f"\n{len(rows)} rows returned.")
        print(DASHES)

    # ---- Step 8 --------------------------------------------------------------

    def step8_list_query_executions(self) -> None:
        """Lists query executions in the workgroup."""
        print(DASHES)
        print("Step 8: Listing query executions in workgroup")

        execution_ids = self.athena_wrapper.list_query_executions(self.workgroup_name)
        print(
            f"Found {len(execution_ids)} query execution(s) in workgroup "
            f"'{self.workgroup_name}':"
        )
        for i, eid in enumerate(execution_ids, 1):
            print(f"  {i}. {eid}")
        print("All queries were executed during this scenario.")
        print(DASHES)

    # ---- Cleanup -------------------------------------------------------------

    def cleanup(self) -> None:
        """Cleans up all resources created during the scenario."""
        print(DASHES)
        print("Cleaning up resources...")

        # 1. Delete the named query.
        if self.named_query_id:
            try:
                print(f"\nDeleting named query '{self.named_query_id}'...")
                self.athena_wrapper.delete_named_query(self.named_query_id)
                print("Named query deleted.")
            except ClientError as err:
                logger.error("Error deleting named query: %s", err)

        # 2. Drop the table and database via Athena queries.
        if self.workgroup_name:
            try:
                print(f"\nDropping table '{self.database_name}.{TABLE_NAME}'...")
                drop_table_id = self.athena_wrapper.start_query_execution(
                    query_string=f"DROP TABLE IF EXISTS {self.database_name}.{TABLE_NAME}",
                    work_group=self.workgroup_name,
                )
                self.athena_wrapper.wait_for_query_to_complete(drop_table_id)
                print("Table dropped.")
            except (ClientError, RuntimeError) as err:
                logger.error("Error dropping table: %s", err)

            try:
                print(f"\nDropping database '{self.database_name}'...")
                drop_db_id = self.athena_wrapper.start_query_execution(
                    query_string=f"DROP DATABASE IF EXISTS {self.database_name}",
                    work_group=self.workgroup_name,
                )
                self.athena_wrapper.wait_for_query_to_complete(drop_db_id)
                print("Database dropped.")
            except (ClientError, RuntimeError) as err:
                logger.error("Error dropping database: %s", err)

        # 3. Delete the Athena workgroup.
        if self.workgroup_name:
            try:
                print(f"\nDeleting workgroup '{self.workgroup_name}'...")
                self.athena_wrapper.delete_work_group(
                    name=self.workgroup_name, recursive=True
                )
                print("Workgroup deleted.")
            except ClientError as err:
                logger.error("Error deleting workgroup: %s", err)

        # 4. Delete the CloudFormation stack (and S3 bucket).
        if self.stack_name:
            try:
                # Empty the S3 bucket first.
                if self.bucket_name:
                    print(f"\nEmptying S3 bucket '{self.bucket_name}'...")
                    self._empty_bucket(self.bucket_name)

                print(f"\nDeleting CloudFormation stack '{self.stack_name}'...")
                self.cf_client.delete_stack(StackName=self.stack_name)
                waiter = self.cf_client.get_waiter("stack_delete_complete")
                print("Waiting for stack deletion...")
                waiter.wait(
                    StackName=self.stack_name,
                    WaiterConfig={"Delay": 10, "MaxAttempts": 60},
                )
                print("Stack deleted successfully.")
            except ClientError as err:
                logger.error("Error deleting CloudFormation stack: %s", err)

        print("\nAll resources cleaned up successfully.")
        print(DASHES)

    def _empty_bucket(self, bucket_name: str) -> None:
        """
        Deletes all objects in the specified S3 bucket.

        :param bucket_name: The name of the S3 bucket to empty.
        """
        try:
            paginator = self.s3_client.get_paginator("list_objects_v2")
            page_iterator = paginator.paginate(Bucket=bucket_name)
            for page in page_iterator:
                contents = page.get("Contents", list())
                if contents:
                    objects = [{"Key": obj["Key"]} for obj in contents]
                    self.s3_client.delete_objects(
                        Bucket=bucket_name,
                        Delete={"Objects": objects},
                    )
            logger.info("Emptied bucket '%s'.", bucket_name)
        except ClientError as err:
            logger.error("Error emptying bucket '%s': %s", bucket_name, err)
```
Create a class that wraps Athena operations.

```
class AthenaWrapper:
    """Encapsulates Amazon Athena operations."""

    def __init__(self, athena_client: BaseClient) -> None:
        """
        Initializes the AthenaWrapper with an Athena client.

        :param athena_client: A Boto3 Amazon Athena client.
        """
        self.athena_client = athena_client

    @classmethod
    def from_client(cls) -> "AthenaWrapper":
        """Creates an AthenaWrapper with a default Athena client."""
        athena_client = boto3.client("athena")
        return cls(athena_client)
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateNamedQuery)
  + [CreateWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateWorkGroup)
  + [DeleteNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteNamedQuery)
  + [DeleteWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteWorkGroup)
  + [GetNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetNamedQuery)
  + [GetQueryExecution](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetQueryExecution)
  + [GetQueryResults](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetQueryResults)
  + [GetWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetWorkGroup)
  + [ListNamedQueries](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListNamedQueries)
  + [ListQueryExecutions](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListQueryExecutions)
  + [StartQueryExecution](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/StartQueryExecution)

## Actions
<a name="actions"></a>

### `CreateNamedQuery`
<a name="athena_CreateNamedQuery_python_3_topic"></a>

The following code example shows how to use `CreateNamedQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def create_named_query(
        self,
        name: str,
        description: str,
        database: str,
        query_string: str,
        work_group: str,
    ) -> str:
        """
        Creates a named (saved) query in the specified workgroup.

        :param name: The name for the query.
        :param description: A description of the query.
        :param database: The database to which the query belongs.
        :param query_string: The SQL query string.
        :param work_group: The workgroup in which to save the query.
        :return: The named query ID.
        :raises ClientError: If the named query could not be created.
        """
        try:
            response = self.athena_client.create_named_query(
                Name=name,
                Description=description,
                Database=database,
                QueryString=query_string,
                WorkGroup=work_group,
            )
            named_query_id = response["NamedQueryId"]
            logger.info("Created named query '%s'. ID: %s", name, named_query_id)
            return named_query_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request creating named query '%s'. "
                    "The query name, database, or query string is invalid. "
                    "%s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateNamedQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateWorkGroup`
<a name="athena_CreateWorkGroup_python_3_topic"></a>

The following code example shows how to use `CreateWorkGroup`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def create_work_group(
        self,
        name: str,
        output_location: str,
        description: str = "Created by Athena basics scenario",
    ) -> None:
        """
        Creates an Athena workgroup with the specified name and configuration.

        :param name: The name for the new workgroup.
        :param output_location: The S3 location for query results (e.g., s3://bucket/prefix/).
        :param description: A description for the workgroup.
        :raises ClientError: If the workgroup could not be created.
        """
        try:
            self.athena_client.create_work_group(
                Name=name,
                Configuration={
                    "ResultConfiguration": {
                        "OutputLocation": output_location,
                    },
                    "EnforceWorkGroupConfiguration": True,
                    "PublishCloudWatchMetricsEnabled": True,
                },
                Description=description,
            )
            logger.info("Created workgroup '%s'.", name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request creating workgroup '%s'. The name may already "
                    "exist or the configuration is invalid. %s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateWorkGroup) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteNamedQuery`
<a name="athena_DeleteNamedQuery_python_3_topic"></a>

The following code example shows how to use `DeleteNamedQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def delete_named_query(self, named_query_id: str) -> None:
        """
        Deletes a named query by its ID.

        :param named_query_id: The unique ID of the named query to delete.
        :raises ClientError: If the named query could not be deleted.
        """
        try:
            self.athena_client.delete_named_query(NamedQueryId=named_query_id)
            logger.info("Deleted named query '%s'.", named_query_id)
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request deleting named query '%s'. "
                    "The named query ID was not found or is invalid. %s: %s",
                    named_query_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteNamedQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteWorkGroup`
<a name="athena_DeleteWorkGroup_python_3_topic"></a>

The following code example shows how to use `DeleteWorkGroup`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def delete_work_group(self, name: str, recursive: bool = True) -> None:
        """
        Deletes the specified workgroup.

        :param name: The name of the workgroup to delete.
        :param recursive: If True, deletes the workgroup even if it contains
                          named queries or query executions.
        :raises ClientError: If the workgroup could not be deleted.
        """
        try:
            self.athena_client.delete_work_group(
                WorkGroup=name, RecursiveDeleteOption=recursive
            )
            logger.info("Deleted workgroup '%s'.", name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request deleting workgroup '%s'. "
                    "It may be the primary workgroup or contain resources "
                    "without RecursiveDeleteOption. %s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteWorkGroup) in *AWS SDK for Python (Boto3) API Reference*.

### `GetNamedQuery`
<a name="athena_GetNamedQuery_python_3_topic"></a>

The following code example shows how to use `GetNamedQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_named_query(self, named_query_id: str) -> Dict[str, Any]:
        """
        Returns the details of a single named (saved) query, including its
        SQL query string.

        :param named_query_id: The unique ID of the named query.
        :return: A dictionary containing the named query details.
        :raises ClientError: If the named query could not be retrieved.
        """
        try:
            response = self.athena_client.get_named_query(NamedQueryId=named_query_id)
            named_query = response["NamedQuery"]
            logger.info("Retrieved named query '%s'.", named_query_id)
            return named_query
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving named query '%s'. "
                    "The named query ID was not found or is invalid. %s: %s",
                    named_query_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetNamedQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `GetQueryExecution`
<a name="athena_GetQueryExecution_python_3_topic"></a>

The following code example shows how to use `GetQueryExecution`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_query_execution(self, query_execution_id: str) -> Dict[str, Any]:
        """
        Returns information about a single query execution.

        :param query_execution_id: The unique ID of the query execution.
        :return: A dictionary containing the query execution details.
        :raises ClientError: If the query execution information could not be retrieved.
        """
        try:
            response = self.athena_client.get_query_execution(
                QueryExecutionId=query_execution_id
            )
            query_execution = response["QueryExecution"]
            logger.info(
                "Retrieved query execution '%s'. State: %s",
                query_execution_id,
                query_execution["Status"]["State"],
            )
            return query_execution
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving query execution '%s'. "
                    "The execution ID is invalid or not found. %s: %s",
                    query_execution_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetQueryExecution](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetQueryExecution) in *AWS SDK for Python (Boto3) API Reference*.

### `GetQueryResults`
<a name="athena_GetQueryResults_python_3_topic"></a>

The following code example shows how to use `GetQueryResults`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_query_results(self, query_execution_id: str) -> Dict[str, Any]:
        """
        Retrieves the results of a completed query execution using pagination.

        :param query_execution_id: The unique ID of the query execution.
        :return: A dictionary with 'columns' (list of column names) and 'rows'
                 (list of lists of string values).
        :raises ClientError: If the query results could not be retrieved.
        """
        try:
            paginator = self.athena_client.get_paginator("get_query_results")
            page_iterator = paginator.paginate(QueryExecutionId=query_execution_id)
            columns = list()
            rows = list()
            first_page = True
            for page in page_iterator:
                result_set = page.get("ResultSet", dict())
                # Extract column names from metadata on first page
                if first_page:
                    column_info = result_set.get("ResultSetMetadata", dict()).get(
                        "ColumnInfo", list()
                    )
                    columns = [col["Name"] for col in column_info]
                    first_page = False
                page_rows = result_set.get("Rows", list())
                for row in page_rows:
                    data = row.get("Data", list())
                    row_values = [datum.get("VarCharValue", "") for datum in data]
                    rows.append(row_values)
            # Athena always returns the column header as the first row of the
            # result set for SELECT-style queries. Drop it unconditionally when
            # there are named columns and at least one row, rather than
            # comparing values (a data row could coincidentally match the
            # header names).
            if columns and rows:
                rows = rows[1:]
            logger.info(
                "Retrieved %d result rows for query '%s'.",
                len(rows),
                query_execution_id,
            )
            return {"columns": columns, "rows": rows}
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving results for query '%s'. "
                    "The execution ID is invalid or the query has not completed. "
                    "%s: %s",
                    query_execution_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetQueryResults](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetQueryResults) in *AWS SDK for Python (Boto3) API Reference*.

### `GetWorkGroup`
<a name="athena_GetWorkGroup_python_3_topic"></a>

The following code example shows how to use `GetWorkGroup`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_work_group(self, name: str) -> Dict[str, Any]:
        """
        Returns information about the specified workgroup.

        :param name: The name of the workgroup.
        :return: A dictionary containing the workgroup details.
        :raises ClientError: If the workgroup information could not be retrieved.
        """
        try:
            response = self.athena_client.get_work_group(WorkGroup=name)
            work_group = response["WorkGroup"]
            logger.info("Retrieved workgroup '%s'.", name)
            return work_group
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving workgroup '%s'. The workgroup "
                    "was not found or the name is invalid. %s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetWorkGroup) in *AWS SDK for Python (Boto3) API Reference*.

### `ListNamedQueries`
<a name="athena_ListNamedQueries_python_3_topic"></a>

The following code example shows how to use `ListNamedQueries`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def list_named_queries(self, work_group: str) -> List[str]:
        """
        Lists named query IDs in the specified workgroup using pagination.

        :param work_group: The name of the workgroup.
        :return: A list of named query IDs.
        :raises ClientError: If the named queries could not be listed.
        """
        try:
            paginator = self.athena_client.get_paginator("list_named_queries")
            page_iterator = paginator.paginate(WorkGroup=work_group)
            named_query_ids = list()
            for page in page_iterator:
                named_query_ids.extend(page.get("NamedQueryIds", list()))
            logger.info(
                "Found %d named query ID(s) in workgroup '%s'.",
                len(named_query_ids),
                work_group,
            )
            return named_query_ids
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request listing named queries for workgroup '%s'. "
                    "%s: %s",
                    work_group,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListNamedQueries](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListNamedQueries) in *AWS SDK for Python (Boto3) API Reference*.

### `ListQueryExecutions`
<a name="athena_ListQueryExecutions_python_3_topic"></a>

The following code example shows how to use `ListQueryExecutions`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def list_query_executions(self, work_group: str) -> List[str]:
        """
        Lists query execution IDs for the specified workgroup using pagination.

        :param work_group: The name of the workgroup.
        :return: A list of query execution IDs.
        :raises ClientError: If the query executions could not be listed.
        """
        try:
            paginator = self.athena_client.get_paginator("list_query_executions")
            page_iterator = paginator.paginate(WorkGroup=work_group)
            execution_ids = list()
            for page in page_iterator:
                execution_ids.extend(page.get("QueryExecutionIds", list()))
            logger.info(
                "Found %d query execution(s) in workgroup '%s'.",
                len(execution_ids),
                work_group,
            )
            return execution_ids
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request listing query executions for workgroup '%s'. "
                    "%s: %s",
                    work_group,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListQueryExecutions](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListQueryExecutions) in *AWS SDK for Python (Boto3) API Reference*.

### `StartQueryExecution`
<a name="athena_StartQueryExecution_python_3_topic"></a>

The following code example shows how to use `StartQueryExecution`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def start_query_execution(
        self,
        query_string: str,
        work_group: str,
        database: Optional[str] = None,
    ) -> str:
        """
        Runs a SQL query using Amazon Athena.

        :param query_string: The SQL query to execute.
        :param work_group: The workgroup in which to run the query.
        :param database: The database context for the query (optional).
        :return: The query execution ID.
        :raises ClientError: If the query could not be started.
        """
        try:
            params: Dict[str, Any] = dict()
            params["QueryString"] = query_string
            params["WorkGroup"] = work_group
            if database is not None:
                params["QueryExecutionContext"] = {"Database": database}
            response = self.athena_client.start_query_execution(**params)
            query_execution_id = response["QueryExecutionId"]
            logger.info("Started query execution. ID: %s", query_execution_id)
            return query_execution_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request starting query execution. The query string, "
                    "database, or workgroup is invalid. %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [StartQueryExecution](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/StartQueryExecution) in *AWS SDK for Python (Boto3) API Reference*.
