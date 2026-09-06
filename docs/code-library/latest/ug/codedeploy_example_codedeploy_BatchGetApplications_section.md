---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_BatchGetApplications_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `BatchGetApplications` with a CLI
<a name="codedeploy_example_codedeploy_BatchGetApplications_section"></a>

The following code examples show how to use `BatchGetApplications`.

------
#### [ CLI ]

**AWS CLI**
**To get information about multiple applications**
The following `batch-get-applications` example displays information about multiple applications that are associated with the user's AWS account.

```
aws deploy batch-get-applications --application-names {{WordPress_App}} {{MyOther_App}}
```
Output:

```
{
    "applicationsInfo": [
        {
            "applicationName": "WordPress_App",
            "applicationId": "d9dd6993-f171-44fa-a811-211e4EXAMPLE",
            "createTime": 1407878168.078,
            "linkedToGitHub": false
        },
        {
            "applicationName": "MyOther_App",
            "applicationId": "8ca57519-31da-42b2-9194-8bb16EXAMPLE",
            "createTime": 1407453571.63,
            "linkedToGitHub": false
        }
    ]
}
```
+  For API details, see [BatchGetApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-applications.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets information about the specified applications.**

```
Get-CDApplicationBatch -ApplicationName CodeDeployDemoApplication, CodePipelineDemoApplication
```
**Output:**

```
ApplicationId                           ApplicationName              CreateTime              LinkedToGitHub
-------------                           ---------------              ----------              --------------
e07fb938-091e-4f2f-8963-4d3e8EXAMPLE    CodeDeployDemoApplication    7/20/2015 9:49:48 PM    False
1ecfd602-62f1-4038-8f0d-06688EXAMPLE    CodePipelineDemoApplication  8/13/2015 5:53:26 PM    False
```
+  For API details, see [BatchGetApplications](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified applications.**

```
Get-CDApplicationBatch -ApplicationName CodeDeployDemoApplication, CodePipelineDemoApplication
```
**Output:**

```
ApplicationId                           ApplicationName              CreateTime              LinkedToGitHub
-------------                           ---------------              ----------              --------------
e07fb938-091e-4f2f-8963-4d3e8EXAMPLE    CodeDeployDemoApplication    7/20/2015 9:49:48 PM    False
1ecfd602-62f1-4038-8f0d-06688EXAMPLE    CodePipelineDemoApplication  8/13/2015 5:53:26 PM    False
```
+  For API details, see [BatchGetApplications](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
