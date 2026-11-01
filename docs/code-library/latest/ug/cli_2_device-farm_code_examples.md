---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_device-farm_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Device Farm examples using AWS CLI
<a name="cli_2_device-farm_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Device Farm.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-device-pool`
<a name="device-farm_CreateDevicePool_cli_2_topic"></a>

The following code example shows how to use `create-device-pool`.

**AWS CLI**
**To create a device pool**
The following `create-device-pool` example creates an Android device pool for a project.

```
aws devicefarm create-device-pool \
    --name {{pool1}} \
    --rules {{file://device-pool-rules.json}} \
    --project-arn {{"arn:aws:devicefarm:us-west-2:123456789012:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
You can get the project ARN from the output of `create-project` or `list-projects`. The file `device-pool-rules.json` is a JSON document in the current folder that specifies the device platform.
Contents of `device-pool-rules.json`:

```
[
    {
        "attribute": "PLATFORM",
        "operator": "EQUALS",
        "value": "\"ANDROID\""
    }
]
```
Output:

```
{
    "devicePool": {
        "rules": [
            {
                "operator": "EQUALS",
                "attribute": "PLATFORM",
                "value": "\"ANDROID\""
            }
        ],
        "type": "PRIVATE",
        "name": "pool1",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:devicepool:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
}
```
For more information, see [Creating a device pool in AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-device-pool.html) in the *AWS Device Farm Developer Guide*.
+  For API details, see [CreateDevicePool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html) in *AWS CLI Command Reference*.

### `create-project`
<a name="device-farm_CreateProject_cli_2_topic"></a>

The following code example shows how to use `create-project`.

**AWS CLI**
**To create a project**
The following `create-project` example creates a new project named `my-project`.

```
aws devicefarm create-project \
    --name {{my-project}}
```
Output:

```
{
    "project": {
        "name": "myproject",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "created": 1503612890.057
    }
}
```
For more information, see [Creating a project in AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-project.html) in the *AWS Device Farm Developer Guide*.
+  For API details, see [CreateProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-project.html) in *AWS CLI Command Reference*.

### `create-upload`
<a name="device-farm_CreateUpload_cli_2_topic"></a>

The following code example shows how to use `create-upload`.

**AWS CLI**
**To create an upload**
The following `create-upload` example creates an upload for an Android app.

```
aws devicefarm create-upload \
    --project-arn {{"arn:aws:devicefarm:us-west-2:123456789012:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --name {{app.apk}} \
    --type {{ANDROID_APP}}
```
You can get the project ARN from the output of create-project or list-projects.
Output:

```
{
    "upload": {
        "status": "INITIALIZED",
        "name": "app.apk",
        "created": 1503614408.769,
        "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aproject%3A070fc3ca-c7e1-4471-91cf-d3e4efc50604/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aupload%3A070fc3ca-7ec1-4741-9c1f-d3e044efc506/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/app.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170824T224008Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAEXAMPLEPBUMBC3GA%2F20170824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=05050370c38894ef5bd09f5d009f36fc8f96fa4bb04e1bba9aca71b8dbe49a0f",
        "type": "ANDROID_APP",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:upload:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
}
```
Use the signed URL in the output to upload a file to Device Farm:

```
curl -T app.apk "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aproject%3A070fc3ca-c7e1-4471-91cf-d3e4efc50604/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aupload%3A070fc3ca-7ec1-4741-9c1f-d3e044efc506/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/app.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170824T224008Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAEXAMPLEPBUMBC3GA%2F20170824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=05050370c38894ef5bd09f5d009f36fc8f96fa4bb04e1bba9aca71b8dbe49a0f"
```
For more information, see [Creating a test run in Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html) in the *AWS Device Farm Developer Guide*.
+  For API details, see [CreateUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-upload.html) in *AWS CLI Command Reference*.

### `get-upload`
<a name="device-farm_GetUpload_cli_2_topic"></a>

The following code example shows how to use `get-upload`.

**AWS CLI**
**To view an upload**
The following `get-upload` example retrieves information about an upload.

```
aws devicefarm get-upload \
    --arn {{"arn:aws:devicefarm:us-west-2:123456789012:upload:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}}
```
You can get the upload ARN from the output of `create-upload`.
Output:

```
{
    "upload": {
        "status": "SUCCEEDED",
        "name": "app.apk",
        "created": 1505262773.186,
        "type": "ANDROID_APP",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:upload:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "metadata": "{\"device_admin\":false,\"activity_name\":\"ccom.example.client.LauncherActivity\",\"version_name\":\"1.0.2.94\",\"screens\":[\"small\",\"normal\",\"large\",\"xlarge\"],\"error_type\":null,\"sdk_version\":\"16\",\"package_name\":\"com.example.client\",\"version_code\":\"20994\",\"native_code\":[\"armeabi-v7a\"],\"target_sdk_version\":\"25\"}"
    }
}
```
For more information, see [Creating a test run in Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html) in the *AWS Device Farm Developer Guide*.
+  For API details, see [GetUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-upload.html) in *AWS CLI Command Reference*.

### `list-projects`
<a name="device-farm_ListProjects_cli_2_topic"></a>

The following code example shows how to use `list-projects`.

**AWS CLI**
**To list projects**
The following `list-projects` example retrieves a list of projects.

```
aws devicefarm list-projects
```
Output:

```
{
    "projects": [
        {
            "name": "myproject",
            "arn": "arn:aws:devicefarm:us-west-2:123456789012:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "created": 1503612890.057
        },
        {
            "name": "otherproject",
            "arn": "arn:aws:devicefarm:us-west-2:123456789012:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "created": 1505257519.337
        }
    ]
}
```
For more information, see [Projects in AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/projects.html) in the *AWS Device Farm Developer Guide*.
+  For API details, see [ListProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-projects.html) in *AWS CLI Command Reference*.
