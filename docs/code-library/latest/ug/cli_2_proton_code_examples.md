---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_proton_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Proton examples using AWS CLI
<a name="cli_2_proton_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Proton.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `cancel-service-instance-deployment`
<a name="proton_CancelServiceInstanceDeployment_cli_2_topic"></a>

The following code example shows how to use `cancel-service-instance-deployment`.

**AWS CLI**
**To cancel a service instance deployment**
The following `cancel-service-instance-deployment` example cancels a service instance deployment.

```
aws proton cancel-service-instance-deployment \
    --service-instance-name {{"instance-one"}} \
    --service-name {{"simple-svc"}}
```
Output:

```
{
    "serviceInstance": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/service-instance/instance-one",
        "createdAt": "2021-04-02T21:29:59.962000+00:00",
        "deploymentStatus": "CANCELLING",
        "environmentName": "simple-env",
        "lastDeploymentAttemptedAt": "2021-04-02T21:45:15.406000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T21:38:00.823000+00:00",
        "name": "instance-one",
        "serviceName": "simple-svc",
        "spec": "proton: ServiceSpec\npipeline:\n  my_sample_pipeline_optional_input: abc\n  my_sample_pipeline_required_input: '123'\ninstances:\n- name: my-instance\n  environment: MySimpleEnv\n  spec:\n    my_sample_service_instance_optional_input: def\n    my_sample_service_instance_required_input: '456'\n- name: my-other-instance\n  environment: MySimpleEnv\n  spec:\n    my_sample_service_instance_required_input: '789'\n",
        "templateMajorVersion": "1",
        "templateMinorVersion": "1",
        "templateName": "svc-simple"
    }
}
```
For more information, see [Update a service instance](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-instance-update.html) in the *The AWS Proton Administrator Guide* or [Update a service instance](https://docs.aws.amazon.com/proton/latest/userguide/ug-svc-instance-update.html) in the *The AWS Proton User Guide*.
+  For API details, see [CancelServiceInstanceDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/cancel-service-instance-deployment.html) in *AWS CLI Command Reference*.

### `cancel-service-pipeline-deployment`
<a name="proton_CancelServicePipelineDeployment_cli_2_topic"></a>

The following code example shows how to use `cancel-service-pipeline-deployment`.

**AWS CLI**
**To cancel a service pipeline deployment**
The following `cancel-service-pipeline-deployment` example cancels a service pipeline deployment.

```
aws proton cancel-service-pipeline-deployment \
    --service-name {{"simple-svc"}}
```
Output:

```
{
    "pipeline": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/pipeline",
        "createdAt": "2021-04-02T21:29:59.962000+00:00",
        "deploymentStatus": "CANCELLING",
        "lastDeploymentAttemptedAt": "2021-04-02T22:02:45.095000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T21:39:28.991000+00:00",
        "templateMajorVersion": "1",
        "templateMinorVersion": "1",
        "templateName": "svc-simple"
    }
}
```
For more information, see [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-pipeline-update.html) in the *The AWS Proton Administrator Guide* or [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html) in the *The AWS Proton User Guide*.
+  For API details, see [CancelServicePipelineDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/cancel-service-pipeline-deployment.html) in *AWS CLI Command Reference*.

### `create-service`
<a name="proton_CreateService_cli_2_topic"></a>

The following code example shows how to use `create-service`.

**AWS CLI**
**To create a service**
The following `create-service` example creates a service with a service pipeline.

```
aws proton create-service \
    --name {{"MySimpleService"}} \
    --template-name {{"fargate-service"}} \
    --template-major-version {{"1"}} \
    --branch-name {{"mainline"}} \
    --repository-connection-arn {{"arn:aws:codestar-connections:region-id:account-id:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --repository-id {{"myorg/myapp"}} \
    --spec {{file://spec.yaml}}
```
Contents of `spec.yaml`:

```
proton: ServiceSpec

pipeline:
    my_sample_pipeline_required_input: "hello"
    my_sample_pipeline_optional_input: "bye"

instances:
    - name: "acme-network-dev"
        environment: "ENV_NAME"
        spec:
            my_sample_service_instance_required_input: "hi"
            my_sample_service_instance_optional_input: "ho"
```
Output:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/MySimpleService",
        "createdAt": "2020-11-18T19:50:27.460000+00:00",
        "lastModifiedAt": "2020-11-18T19:50:27.460000+00:00",
        "name": "MySimpleService",
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "repositoryId": "myorg/myapp",
        "status": "CREATE_IN_PROGRESS",
        "templateName": "fargate-service"
    }
}
```
For more information, see [Create a service](https://docs.aws.amazon.com/proton/latest/adminguide/ag-create-svc.html) in the *The AWS Proton Administrator Guide* and [Create a service](https://docs.aws.amazon.com/proton/latest/userguide/ug-svc-create.html) in the *The AWS Proton User Guide*.
+  For API details, see [CreateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service.html) in *AWS CLI Command Reference*.

### `delete-service`
<a name="proton_DeleteService_cli_2_topic"></a>

The following code example shows how to use `delete-service`.

**AWS CLI**
**To delete a service**
The following `delete-service` example deletes a service.

```
aws proton delete-service \
    --name {{"simple-svc"}}
```
Output:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc",
        "branchName": "mainline",
        "createdAt": "2020-11-28T22:40:50.512000+00:00",
        "description": "Edit by updating description",
        "lastModifiedAt": "2020-11-29T00:30:39.248000+00:00",
        "name": "simple-svc",
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "repositoryId": "myorg/myapp",
        "status": "DELETE_IN_PROGRESS",
        "templateName": "fargate-service"
    }
}
```
For more information, see [Delete a service](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-delete.html) in the *The AWS Proton Administrator Guide*.
+  For API details, see [DeleteService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service.html) in *AWS CLI Command Reference*.

### `get-service-instance`
<a name="proton_GetServiceInstance_cli_2_topic"></a>

The following code example shows how to use `get-service-instance`.

**AWS CLI**
**To get service instance details**
The following `get-service-instance` example gets detail data for a service instance.

```
aws proton get-service-instance \
    --name {{"instance-one"}} \
    --service-name {{"simple-svc"}}
```
Output:

```
{
    "serviceInstance": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/service-instance/instance-one",
        "createdAt": "2020-11-28T22:40:50.512000+00:00",
        "deploymentStatus": "SUCCEEDED",
        "environmentName": "simple-env",
        "lastDeploymentAttemptedAt": "2020-11-28T22:40:50.512000+00:00",
        "lastDeploymentSucceededAt": "2020-11-28T22:40:50.512000+00:00",
        "name": "instance-one",
        "serviceName": "simple-svc",
        "spec": "proton: ServiceSpec\npipeline:\n  my_sample_pipeline_optional_input: hello world\n  my_sample_pipeline_required_input: pipeline up\ninstances:\n- name: instance-one\n  environment: my-simple-env\n  spec:\n    my_sample_service_instance_optional_input: Ola\n    my_sample_service_instance_required_input: Ciao\n",
        "templateMajorVersion": "1",
        "templateMinorVersion": "0",
        "templateName": "svc-simple"
    }
}
```
For more information, see [View service data](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-view.html) in the *The AWS Proton Administrator Guide* or [View service data](https://docs.aws.amazon.com/proton/latest/userguide/ug-svc-view.html) in the *The AWS Proton User Guide*.
+  For API details, see [GetServiceInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-instance.html) in *AWS CLI Command Reference*.

### `get-service`
<a name="proton_GetService_cli_2_topic"></a>

The following code example shows how to use `get-service`.

**AWS CLI**
**To get service details**
The following `get-service` example gets detail data for a service.

```
aws proton get-service \
    --name {{"simple-svc"}}
```
Output:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc",
        "branchName": "mainline",
        "createdAt": "2020-11-28T22:40:50.512000+00:00",
        "lastModifiedAt": "2020-11-28T22:44:51.207000+00:00",
        "name": "simple-svc",
        "pipeline": {
            "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/pipeline/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "createdAt": "2020-11-28T22:40:50.512000+00:00",
            "deploymentStatus": "SUCCEEDED",
            "lastDeploymentAttemptedAt": "2020-11-28T22:40:50.512000+00:00",
            "lastDeploymentSucceededAt": "2020-11-28T22:40:50.512000+00:00",
            "spec": "proton: ServiceSpec\npipeline:\n  my_sample_pipeline_required_input: hello\n  my_sample_pipeline_optional_input: bye\ninstances:\n- name: instance-svc-simple\n  environment: my-simple-env\n  spec:\n    my_sample_service_instance_required_input: hi\n    my_sample_service_instance_optional_input: ho\n",
            "templateMajorVersion": "1",
            "templateMinorVersion": "1",
            "templateName": "svc-simple"
        },
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "repositoryId": "myorg/myapp",
        "spec": "proton: ServiceSpec\npipeline:\n  my_sample_pipeline_required_input: hello\n  my_sample_pipeline_optional_input: bye\ninstances:\n- name: instance-svc-simple\n  environment: my-simple-env\n  spec:\n    my_sample_service_instance_required_input: hi\n    my_sample_service_instance_optional_input: ho\n",
        "status": "ACTIVE",
        "templateName": "svc-simple"
    }
}
```
For more information, see [View service data](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-view.html) in the *The AWS Proton Administrator Guide* or [View service data](https://docs.aws.amazon.com/proton/latest/userguide/ug-svc-view.html) in the *The AWS Proton User Guide*.
+  For API details, see [GetService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service.html) in *AWS CLI Command Reference*.

### `list-service-instances`
<a name="proton_ListServiceInstances_cli_2_topic"></a>

The following code example shows how to use `list-service-instances`.

**AWS CLI**
**Example 1: To list all service instances**
The following `list-service-instances` example lists service instances.

```
aws proton list-service-instances
```
Output:

```
{
    "serviceInstances": [
        {
            "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/service-instance/instance-one",
            "createdAt": "2020-11-28T22:40:50.512000+00:00",
            "deploymentStatus": "SUCCEEDED",
            "environmentArn": "arn:aws:proton:region-id:123456789012:environment/simple-env",
            "lastDeploymentAttemptedAt": "2020-11-28T22:40:50.512000+00:00",
            "lastDeploymentSucceededAt": "2020-11-28T22:40:50.512000+00:00",
            "name": "instance-one",
            "serviceName": "simple-svc",
            "templateMajorVersion": "1",
            "templateMinorVersion": "0",
            "templateName": "fargate-service"
        }
    ]
}
```
For more information, see [View service instance data](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-instance-view.html) in the *The AWS Proton Administrator Guide* or [View service instance data](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-view.html) in the *The AWS Proton User Guide*.
**Example 2: To list the specified service instance**
The following `get-service-instance` example gets a service instance.

```
aws proton get-service-instance \
    --name {{"instance-one"}} \
    --service-name {{"simple-svc"}}
```
Output:

```
{
    "serviceInstance": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/service-instance/instance-one",
        "createdAt": "2020-11-28T22:40:50.512000+00:00",
        "deploymentStatus": "SUCCEEDED",
        "environmentName": "simple-env",
        "lastDeploymentAttemptedAt": "2020-11-28T22:40:50.512000+00:00",
        "lastDeploymentSucceededAt": "2020-11-28T22:40:50.512000+00:00",
        "name": "instance-one",
        "serviceName": "simple-svc",
        "spec": "proton: ServiceSpec\npipeline:\n  my_sample_pipeline_optional_input: hello world\n  my_sample_pipeline_required_input: pipeline up\ninstances:\n- name: instance-one\n  environment: my-simple-env\n  spec:\n    my_sample_service_instance_optional_input: Ola\n    my_sample_service_instance_required_input: Ciao\n",
        "templateMajorVersion": "1",
        "templateMinorVersion": "0",
        "templateName": "svc-simple"
    }
}
```
For more information, see [View service instance data](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-instance-view.html) in the *The AWS Proton Administrator Guide* or [View service instance data](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-view.html) in the *The AWS Proton User Guide*.
+  For API details, see [ListServiceInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-instances.html) in *AWS CLI Command Reference*.

### `update-service-instance`
<a name="proton_UpdateServiceInstance_cli_2_topic"></a>

The following code example shows how to use `update-service-instance`.

**AWS CLI**
**To update a service instance to a new minor version**
The following `update-service-instance` example updates a service instance to a new minor version of its service template that adds a new instance named "my-other-instance" with a new required input.

```
aws proton update-service-instance \
    --service-name {{"simple-svc"}} \
    --spec {{"file://service-spec.yaml}} " \
    --template-major-version {{"1"}} \
    --template-minor-version {{"1"}} \
    --deployment-type {{"MINOR_VERSION"}} \
    --name {{"instance-one"}}
```
Contents of `service-spec.yaml`:

```
proton: ServiceSpec
pipeline:
    my_sample_pipeline_optional_input: "abc"
    my_sample_pipeline_required_input: "123"
instances:
    - name: "instance-one"
        environment: "simple-env"
        spec:
            my_sample_service_instance_optional_input: "def"
            my_sample_service_instance_required_input: "456"
    - name: "my-other-instance"
        environment: "simple-env"
        spec:
            my_sample_service_instance_required_input: "789"
```
Output:

```
{
    "serviceInstance": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/service-instance/instance-one",
        "createdAt": "2021-04-02T21:29:59.962000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "environmentName": "arn:aws:proton:region-id:123456789012:environment/simple-env",
        "lastDeploymentAttemptedAt": "2021-04-02T21:38:00.823000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T21:29:59.962000+00:00",
        "name": "instance-one",
        "serviceName": "simple-svc",
        "templateMajorVersion": "1",
        "templateMinorVersion": "0",
        "templateName": "svc-simple"
    }
}
```
For more information, see [Update a service instance](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-instance-update.html) in the *The AWS Proton Administrator Guide* or [Update a service instance](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html) in the *The AWS Proton User Guide*.
+  For API details, see [UpdateServiceInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-instance.html) in *AWS CLI Command Reference*.

### `update-service-pipeline`
<a name="proton_UpdateServicePipeline_cli_2_topic"></a>

The following code example shows how to use `update-service-pipeline`.

**AWS CLI**
**To update a service pipeline**
The following `update-service-pipeline` example updates a service pipeline to a new minor version of its service template.

```
aws proton update-service-pipeline \
    --service-name {{"simple-svc"}} \
    --spec {{"file://service-spec.yaml"}} \
    --template-major-version {{"1"}} \
    --template-minor-version {{"1"}} \
    --deployment-type {{"MINOR_VERSION"}}
```
Output:

```
{
    "pipeline": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/pipeline/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "createdAt": "2021-04-02T21:29:59.962000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "lastDeploymentAttemptedAt": "2021-04-02T21:39:28.991000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T21:29:59.962000+00:00",
        "spec": "proton: ServiceSpec\n\npipeline:\n  my_sample_pipeline_optional_input: \"abc\"\n  my_sample_pipeline_required_input: \"123\"\n\ninstances:\n  - name: \"my-instance\"\n    environment: \"MySimpleEnv\"\n    spec:\n      my_sample_service_instance_optional_input: \"def\"\n      my_sample_service_instance_required_input: \"456\"\n  - name: \"my-other-instance\"\n    environment: \"MySimpleEnv\"\n    spec:\n      my_sample_service_instance_required_input: \"789\"\n",
        "templateMajorVersion": "1",
        "templateMinorVersion": "0",
        "templateName": "svc-simple"
    }
}
```
For more information, see [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-pipeline-update.html) in the *The AWS Proton Administrator Guide* or [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html) in the *The AWS Proton User Guide*.
+  For API details, see [UpdateServicePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-pipeline.html) in *AWS CLI Command Reference*.

### `update-service`
<a name="proton_UpdateService_cli_2_topic"></a>

The following code example shows how to use `update-service`.

**AWS CLI**
**To update a service**
The following `update-service` example edits a service description.

```
aws proton update-service \
    --name {{"MySimpleService"}} \
    --description {{"Edit by updating description"}}
```
Output:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/MySimpleService",
        "branchName": "mainline",
        "createdAt": "2021-03-12T22:39:42.318000+00:00",
        "description": "Edit by updating description",
        "lastModifiedAt": "2021-03-12T22:44:21.975000+00:00",
        "name": "MySimpleService",
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "repositoryId": "myorg/myapp",
        "status": "ACTIVE",
        "templateName": "fargate-service"
    }
}
```
For more information, see [Edit a service](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-update.html) in the *The AWS Proton Administrator Guide* or [Edit a service](https://docs.aws.amazon.com/proton/latest/userguide/ug-svc-update.html) in the *The AWS Proton User Guide*.
+  For API details, see [UpdateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
