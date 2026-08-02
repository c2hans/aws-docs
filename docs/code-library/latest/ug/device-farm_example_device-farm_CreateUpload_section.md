---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/device-farm_example_device-farm_CreateUpload_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateUpload` with a CLI
<a name="device-farm_example_device-farm_CreateUpload_section"></a>

The following code examples show how to use `CreateUpload`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Upload and test device packages](device-farm_example_device-farm_Scenario_DeviceTesting_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create an upload**
The following command creates an upload for an Android app:

```
aws devicefarm create-upload --project-arn {{"arn:aws:devicefarm:us-west-2:123456789012:project:070fc3ca-7ec1-4741-9c1f-d3e044efc506"}} --name {{app.apk}} --type {{ANDROID_APP}}
```
You can get the project ARN from the output of create-project or list-projects.
Output:

```
{
    "upload": {
        "status": "INITIALIZED",
        "name": "app.apk",
        "created": 1503614408.769,
        "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aproject%3A070fc3ca-c7e1-4471-91cf-d3e4efc50604/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aupload%3A070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514/app.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170824T224008Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAEXAMPLEPBUMBC3GA%2F20170824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=05050370c38894ef5bd09f5d009f36fc8f96fa4bb04e1bba9aca71b8dbe49a0f",
        "type": "ANDROID_APP",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:upload:070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514"
    }
}
```
Use the signed URL in the output to upload a file to Device Farm:

```
curl -T app.apk "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aproject%3A070fc3ca-c7e1-4471-91cf-d3e4efc50604/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aupload%3A070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514/app.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170824T224008Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAEXAMPLEPBUMBC3GA%2F20170824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=05050370c38894ef5bd09f5d009f36fc8f96fa4bb04e1bba9aca71b8dbe49a0f"
```
+  For API details, see [CreateUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-upload.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates an AWS Device Farm upload for an Android app. You can get the project ARN from the output of New-DFProject or Get-DFProjectList. Use the signed URL in the New-DFUpload output to upload a file to Device Farm.**

```
New-DFUpload -ContentType "application/octet-stream" -ProjectArn "arn:aws:devicefarm:us-west-2:123456789012:project:EXAMPLEa-7ec1-4741-9c1f-d3e04EXAMPLE" -Name "app.apk" -Type ANDROID_APP
```
+  For API details, see [CreateUpload](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates an AWS Device Farm upload for an Android app. You can get the project ARN from the output of New-DFProject or Get-DFProjectList. Use the signed URL in the New-DFUpload output to upload a file to Device Farm.**

```
New-DFUpload -ContentType "application/octet-stream" -ProjectArn "arn:aws:devicefarm:us-west-2:123456789012:project:EXAMPLEa-7ec1-4741-9c1f-d3e04EXAMPLE" -Name "app.apk" -Type ANDROID_APP
```
+  For API details, see [CreateUpload](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
