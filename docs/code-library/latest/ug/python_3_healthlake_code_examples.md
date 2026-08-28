---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_healthlake_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# HealthLake examples using SDK for Python (Boto3)
<a name="python_3_healthlake_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with HealthLake.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateFHIRDatastore`
<a name="healthlake_CreateFHIRDatastore_python_3_topic"></a>

The following code example shows how to use `CreateFHIRDatastore`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def create_fhir_datastore(
        self,
        datastore_name: str,
        sse_configuration: dict[str, any] = None,
        identity_provider_configuration: dict[str, any] = None,
    ) -> dict[str, str]:
        """
        Creates a new HealthLake data store.
        When creating a SMART on FHIR data store, the following parameters are required:
        - sse_configuration: The server-side encryption configuration for a SMART on FHIR-enabled data store.
        - identity_provider_configuration: The identity provider configuration for a SMART on FHIR-enabled data store.

        :param datastore_name: The name of the data store.
        :param sse_configuration: The server-side encryption configuration for a SMART on FHIR-enabled data store.
        :param identity_provider_configuration: The identity provider configuration for a SMART on FHIR-enabled data store.
        :return: A dictionary containing the data store information.
        """
        try:
            parameters = {"DatastoreName": datastore_name, "DatastoreTypeVersion": "R4"}
            if (
                sse_configuration is not None
                and identity_provider_configuration is not None
            ):
                # Creating a SMART on FHIR-enabled data store
                parameters["SseConfiguration"] = sse_configuration
                parameters[
                    "IdentityProviderConfiguration"
                ] = identity_provider_configuration

            response = self.health_lake_client.create_fhir_datastore(**parameters)
            return response
        except ClientError as err:
            logger.exception(
                "Couldn't create data store %s. Here's why %s",
                datastore_name,
                err.response["Error"]["Message"],
            )
            raise
```
The following code shows an example of parameters for a SMART on FHIR-enabled HealthLake data store.

```
            sse_configuration = {
                "KmsEncryptionConfig": {"CmkType": "AWS_OWNED_KMS_KEY"}
            }
            # TODO: Update the metadata to match your environment.
            metadata = {
                "issuer": "https://ehr.example.com",
                "jwks_uri": "https://ehr.example.com/.well-known/jwks.json",
                "authorization_endpoint": "https://ehr.example.com/auth/authorize",
                "token_endpoint": "https://ehr.token.com/auth/token",
                "token_endpoint_auth_methods_supported": [
                    "client_secret_basic",
                    "foo",
                ],
                "grant_types_supported": ["client_credential", "foo"],
                "registration_endpoint": "https://ehr.example.com/auth/register",
                "scopes_supported": ["openId", "profile", "launch"],
                "response_types_supported": ["code"],
                "management_endpoint": "https://ehr.example.com/user/manage",
                "introspection_endpoint": "https://ehr.example.com/user/introspect",
                "revocation_endpoint": "https://ehr.example.com/user/revoke",
                "code_challenge_methods_supported": ["S256"],
                "capabilities": [
                    "launch-ehr",
                    "sso-openid-connect",
                    "client-public",
                ],
            }
            # TODO: Update the IdpLambdaArn.
            identity_provider_configuration = {
                "AuthorizationStrategy": "SMART_ON_FHIR_V1",
                "FineGrainedAuthorizationEnabled": True,
                "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
                "Metadata": json.dumps(metadata),
            }
            data_store = self.create_fhir_datastore(
                datastore_name, sse_configuration, identity_provider_configuration
            )
```
+  For API details, see [CreateFHIRDatastore](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/CreateFHIRDatastore) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `DeleteFHIRDatastore`
<a name="healthlake_DeleteFHIRDatastore_python_3_topic"></a>

The following code example shows how to use `DeleteFHIRDatastore`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def delete_fhir_datastore(self, datastore_id: str) -> None:
        """
        Deletes a HealthLake data store.
        :param datastore_id: The data store ID.
        """
        try:
            self.health_lake_client.delete_fhir_datastore(DatastoreId=datastore_id)
        except ClientError as err:
            logger.exception(
                "Couldn't delete data store with ID %s. Here's why %s",
                datastore_id,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteFHIRDatastore](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DeleteFHIRDatastore) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `DescribeFHIRDatastore`
<a name="healthlake_DescribeFHIRDatastore_python_3_topic"></a>

The following code example shows how to use `DescribeFHIRDatastore`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def describe_fhir_datastore(self, datastore_id: str) -> dict[str, any]:
        """
        Describes a HealthLake data store.
        :param datastore_id: The data store ID.
        :return: The data store description.
        """
        try:
            response = self.health_lake_client.describe_fhir_datastore(
                DatastoreId=datastore_id
            )
            return response["DatastoreProperties"]
        except ClientError as err:
            logger.exception(
                "Couldn't describe data store with ID %s. Here's why %s",
                datastore_id,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeFHIRDatastore](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DescribeFHIRDatastore) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `DescribeFHIRExportJob`
<a name="healthlake_DescribeFHIRExportJob_python_3_topic"></a>

The following code example shows how to use `DescribeFHIRExportJob`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def describe_fhir_export_job(
        self, datastore_id: str, job_id: str
    ) -> dict[str, any]:
        """
        Describes a HealthLake export job.
        :param datastore_id: The data store ID.
        :param job_id: The export job ID.
        :return: The export job description.
        """
        try:
            response = self.health_lake_client.describe_fhir_export_job(
                DatastoreId=datastore_id, JobId=job_id
            )
            return response["ExportJobProperties"]
        except ClientError as err:
            logger.exception(
                "Couldn't describe export job with ID %s. Here's why %s",
                job_id,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeFHIRExportJob](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DescribeFHIRExportJob) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `DescribeFHIRImportJob`
<a name="healthlake_DescribeFHIRImportJob_python_3_topic"></a>

The following code example shows how to use `DescribeFHIRImportJob`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def describe_fhir_import_job(
        self, datastore_id: str, job_id: str
    ) -> dict[str, any]:
        """
        Describes a HealthLake import job.
        :param datastore_id: The data store ID.
        :param job_id: The import job ID.
        :return: The import job description.
        """
        try:
            response = self.health_lake_client.describe_fhir_import_job(
                DatastoreId=datastore_id, JobId=job_id
            )
            return response["ImportJobProperties"]
        except ClientError as err:
            logger.exception(
                "Couldn't describe import job with ID %s. Here's why %s",
                job_id,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeFHIRImportJob](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DescribeFHIRImportJob) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `ListFHIRDatastores`
<a name="healthlake_ListFHIRDatastores_python_3_topic"></a>

The following code example shows how to use `ListFHIRDatastores`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def list_fhir_datastores(self) -> list[dict[str, any]]:
        """
        Lists all HealthLake data stores.
        :return: A list of data store descriptions.
        """
        try:
            next_token = None
            datastores = []

            # Loop through paginated results.
            while True:
                parameters = {}
                if next_token is not None:
                    parameters["NextToken"] = next_token
                response = self.health_lake_client.list_fhir_datastores(**parameters)
                datastores.extend(response["DatastorePropertiesList"])
                if "NextToken" in response:
                    next_token = response["NextToken"]
                else:
                    break

            return datastores
        except ClientError as err:
            logger.exception(
                "Couldn't list data stores. Here's why %s", err.response["Error"]["Message"]
            )
            raise
```
+  For API details, see [ListFHIRDatastores](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListFHIRDatastores) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `ListFHIRExportJobs`
<a name="healthlake_ListFHIRExportJobs_python_3_topic"></a>

The following code example shows how to use `ListFHIRExportJobs`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def list_fhir_export_jobs(
        self,
        datastore_id: str,
        job_name: str = None,
        job_status: str = None,
        submitted_before: datetime = None,
        submitted_after: datetime = None,
    ) -> list[dict[str, any]]:
        """
        Lists HealthLake export jobs satisfying the conditions.
        :param datastore_id: The data store ID.
        :param job_name: The export job name.
        :param job_status: The export job status.
        :param submitted_before: The export job submitted before the specified date.
        :param submitted_after: The export job submitted after the specified date.
        :return: A list of export jobs.
        """
        try:
            parameters = {"DatastoreId": datastore_id}
            if job_name is not None:
                parameters["JobName"] = job_name
            if job_status is not None:
                parameters["JobStatus"] = job_status
            if submitted_before is not None:
                parameters["SubmittedBefore"] = submitted_before
            if submitted_after is not None:
                parameters["SubmittedAfter"] = submitted_after
            next_token = None
            jobs = []
            # Loop through paginated results.
            while True:
                if next_token is not None:
                    parameters["NextToken"] = next_token
                response = self.health_lake_client.list_fhir_export_jobs(**parameters)
                jobs.extend(response["ExportJobPropertiesList"])
                if "NextToken" in response:
                    next_token = response["NextToken"]
                else:
                    break
            return jobs
        except ClientError as err:
            logger.exception(
                "Couldn't list export jobs. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListFHIRExportJobs](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListFHIRExportJobs) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `ListFHIRImportJobs`
<a name="healthlake_ListFHIRImportJobs_python_3_topic"></a>

The following code example shows how to use `ListFHIRImportJobs`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def list_fhir_import_jobs(
        self,
        datastore_id: str,
        job_name: str = None,
        job_status: str = None,
        submitted_before: datetime = None,
        submitted_after: datetime = None,
    ) -> list[dict[str, any]]:
        """
        Lists HealthLake import jobs satisfying the conditions.
        :param datastore_id: The data store ID.
        :param job_name: The import job name.
        :param job_status: The import job status.
        :param submitted_before: The import job submitted before the specified date.
        :param submitted_after: The import job submitted after the specified date.
        :return: A list of import jobs.
        """
        try:
            parameters = {"DatastoreId": datastore_id}
            if job_name is not None:
                parameters["JobName"] = job_name
            if job_status is not None:
                parameters["JobStatus"] = job_status
            if submitted_before is not None:
                parameters["SubmittedBefore"] = submitted_before
            if submitted_after is not None:
                parameters["SubmittedAfter"] = submitted_after
            next_token = None
            jobs = []
            # Loop through paginated results.
            while True:
                if next_token is not None:
                    parameters["NextToken"] = next_token
                response = self.health_lake_client.list_fhir_import_jobs(**parameters)
                jobs.extend(response["ImportJobPropertiesList"])
                if "NextToken" in response:
                    next_token = response["NextToken"]
                else:
                    break
            return jobs
        except ClientError as err:
            logger.exception(
                "Couldn't list import jobs. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListFHIRImportJobs](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListFHIRImportJobs) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `ListTagsForResource`
<a name="healthlake_ListTagsForResource_python_3_topic"></a>

The following code example shows how to use `ListTagsForResource`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def list_tags_for_resource(self, resource_arn: str) -> dict[str, str]:
        """
        Lists the tags for a HealthLake resource.
        :param resource_arn: The resource ARN.
        :return: The tags for the resource.
        """
        try:
            response = self.health_lake_client.list_tags_for_resource(
                ResourceARN=resource_arn
            )
            return response["Tags"]
        except ClientError as err:
            logger.exception(
                "Couldn't list tags for resource %s. Here's why %s",
                resource_arn,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListTagsForResource) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `StartFHIRExportJob`
<a name="healthlake_StartFHIRExportJob_python_3_topic"></a>

The following code example shows how to use `StartFHIRExportJob`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def start_fhir_export_job(
        self,
        job_name: str,
        datastore_id: str,
        output_s3_uri: str,
        kms_key_id: str,
        data_access_role_arn: str,
    ) -> dict[str, str]:
        """
        Starts a HealthLake export job.
        :param job_name: The export job name.
        :param datastore_id: The data store ID.
        :param output_s3_uri: The output S3 URI.
        :param kms_key_id: The KMS key ID associated with the output S3 bucket.
        :param data_access_role_arn: The data access role ARN.
        :return: The export job.
        """
        try:
            response = self.health_lake_client.start_fhir_export_job(
                OutputDataConfig={
                    "S3Configuration": {"S3Uri": output_s3_uri, "KmsKeyId": kms_key_id}
                },
                DataAccessRoleArn=data_access_role_arn,
                DatastoreId=datastore_id,
                JobName=job_name,
            )

            return response
        except ClientError as err:
            logger.exception(
                "Couldn't start export job. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [StartFHIRExportJob](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/StartFHIRExportJob) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `StartFHIRImportJob`
<a name="healthlake_StartFHIRImportJob_python_3_topic"></a>

The following code example shows how to use `StartFHIRImportJob`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def start_fhir_import_job(
        self,
        job_name: str,
        datastore_id: str,
        input_s3_uri: str,
        job_output_s3_uri: str,
        kms_key_id: str,
        data_access_role_arn: str,
    ) -> dict[str, str]:
        """
        Starts a HealthLake import job.
        :param job_name: The import job name.
        :param datastore_id: The data store ID.
        :param input_s3_uri: The input S3 URI.
        :param job_output_s3_uri: The job output S3 URI.
        :param kms_key_id: The KMS key ID associated with the output S3 bucket.
        :param data_access_role_arn: The data access role ARN.
        :return: The import job.
        """
        try:
            response = self.health_lake_client.start_fhir_import_job(
                JobName=job_name,
                InputDataConfig={"S3Uri": input_s3_uri},
                JobOutputDataConfig={
                    "S3Configuration": {
                        "S3Uri": job_output_s3_uri,
                        "KmsKeyId": kms_key_id,
                    }
                },
                DataAccessRoleArn=data_access_role_arn,
                DatastoreId=datastore_id,
            )
            return response
        except ClientError as err:
            logger.exception(
                "Couldn't start import job. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [StartFHIRImportJob](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/StartFHIRImportJob) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `TagResource`
<a name="healthlake_TagResource_python_3_topic"></a>

The following code example shows how to use `TagResource`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def tag_resource(self, resource_arn: str, tags: list[dict[str, str]]) -> None:
        """
        Tags a HealthLake resource.
        :param resource_arn: The resource ARN.
        :param tags: The tags to add to the resource.
        """
        try:
            self.health_lake_client.tag_resource(ResourceARN=resource_arn, Tags=tags)
        except ClientError as err:
            logger.exception(
                "Couldn't tag resource %s. Here's why %s",
                resource_arn,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/TagResource) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

### `UntagResource`
<a name="healthlake_UntagResource_python_3_topic"></a>

The following code example shows how to use `UntagResource`.

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)

    def untag_resource(self, resource_arn: str, tag_keys: list[str]) -> None:
        """
        Untags a HealthLake resource.
        :param resource_arn: The resource ARN.
        :param tag_keys: The tag keys to remove from the resource.
        """
        try:
            self.health_lake_client.untag_resource(
                ResourceARN=resource_arn, TagKeys=tag_keys
            )
        except ClientError as err:
            logger.exception(
                "Couldn't untag resource %s. Here's why %s",
                resource_arn,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/UntagResource) in *AWS SDK for Python (Boto3) API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
