---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/run-automations-from-command-prompt.html
---

# Run automations from command prompt
<a name="run-automations-from-command-prompt"></a>

Although we recommend running automation jobs through the web interface, you can run automation scripts manually from a command line on the automation server. This provides additional options where organizations cannot or do not want to use the combination of AWS CMF Credentials Manager, AWS Secrets Manager and AWS Systems Manager in the environment, or if Cloud Migration Factory on AWS users need to provide multi-factor authentication (MFA) one-time access codes to logon to Cloud Migration Factory on AWS.

When scripts are run from the command line, job history and logs are not available from within the **Jobs** view in the web interface. Log output will only be directed to the command-line output only. The scripts can still access the Cloud Migration Factory on AWS APIs to read and update records, and other functions available through the APIs.

We recommend storing scripts in the scripts library or another central location to ensure that you are accessing and using the latest version of the script, or the version that is currently approved for use.

## Manually running an automation package
<a name="manually-running-an-automation-package"></a>

This section describes the steps to download a package from Cloud Migration Factory on AWS and manually run it on the automation server. You can also follow the process for other script source locations by replacing steps 1 and 2 with the source specific download steps.

1. If scripts are stored in Cloud Migration Factory on AWS, follow the steps covered in [Download script packages](scripts-management.md#download-script-packages) to obtain the automation package zip file.

1. Copy the zip file to a location on the automation server, such as `c:\migrations\scripts`, and unzip the contents.

1. Copy the `FactoryEndpoints.json` file to each of the unzipped script folder. Configure the file with the specific API endpoints for the Cloud Migration Factory instance that contains the servers, or other records this automation job will reference. Refer to [Creation of the FactoryEndpoints.json](#creation-of-the-factoryendpoints.json) for more information on how to create this file.

1. From the command line, ensure that you are within the root directory of the unzipped package, and run the following command:

```
python [package master script file] [script arguments]
```

 *package master script file -* this can be obtained from the `Package-Structure.yml` under the `MasterFileName` key.

 *script arguments* - information about the arguments is provided in the `Package-Structure.yml` under the `Arguments` key.

1. The scripts will request credentials required for Cloud Migration Factory on AWS APIs and the remote server. Any credentials manually entered are cached in memory for the duration of this process to avoid entering the same credentials again. If you enter script arguments to access secrets stored using the Credentials Manager feature, then access to AWS Secrets Manager and associated secrets is required. If secret retrieval fails for any reason, the script will prompt for user credentials.

## Creation of the FactoryEndpoints.json
<a name="creation-of-the-factoryendpoints.json"></a>

We recommended creating this file once when deploying Cloud Migration Factory on AWS solution, as the content does not change after initial deployment, and stored in a central location on the automation server. This file provides the automation scripts with the Cloud Migration Factory on AWS API endpoints and other key parameters. An example of the default contents of the file is shown here:

```
{
 "UserApi": "cmfuserapi",
 "VpceId": "",
 "ToolsApi": "cmftoolsapi",
 "Region": "us-east-1",
 "UserPoolId": "us-east-1_AbCdEfG",
 "UserPoolClientId": "123456abcdef7890ghijk",
 "LoginApi": "cmfloginapi"
}
```

**Note**
Most information required to compose this file for a deployed AWS Cloud Migration Factory instance is available from the AWS CloudFormation **Outputs** tab of the deployed stack, except the `UserPoolClientId`. Obtain this value by completing the following steps:

1. Navigate to the Amazon Cognito console.

1. Open the **User pool configuration**.

1. Select **App integration**, which will provide the **App client configuration**.

```
{
 "UserApi": <UserApi-value>,
 "Region": <Region-value>,
 "UserPoolId": <UserPoolId-value>,
 "UserPoolClientId": <Amazon-Cognito-user-pool-app-clients-console>,
 "LoginApi": <LoginApi-value>
}
```

Replace {{<LoginApi-value>}}, {{<UserApi-value>}}, {{<Region-value>}}, and {{<UserPoolId-value>}} with the corresponding values you retrieved from the AWS CloudFormation Outputs console. Do not add a forward slash (/) to the end of the URLs.

The file has an optional `DefaultUser` key. You can set the value for this key to the default user ID to be used to access the Cloud Migration Factory on AWS instance to avoid having to enter it every time. When prompted for the Cloud Migration Factory user ID, you can either enter a user ID or use the default value by pressing the enter key. You can only do this when the scripts are run manually.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
