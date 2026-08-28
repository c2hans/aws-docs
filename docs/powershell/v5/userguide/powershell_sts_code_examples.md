---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_sts_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# AWS STS examples using Tools for PowerShell V5
<a name="powershell_sts_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with AWS STS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Convert-STSAuthorizationMessage`
<a name="sts_DecodeAuthorizationMessage_powershell_topic"></a>

The following code example shows how to use `Convert-STSAuthorizationMessage`.

**Tools for PowerShell V5**
**Example 1: Decodes the additional information contained in the supplied encoded message content that was returned in response to a request. The additional information is encoded because details of the authorization status can constitute privileged information that the user who requested the action should not see.**

```
Convert-STSAuthorizationMessage -EncodedMessage "...encoded message..."
```
+  For API details, see [DecodeAuthorizationMessage](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-STSFederationToken`
<a name="sts_GetFederationToken_powershell_topic"></a>

The following code example shows how to use `Get-STSFederationToken`.

**Tools for PowerShell V5**
**Example 1: Requests a federated token valid for one hour using "Bob" as the name of the federated user. This name can be used to reference the federated user name in a resource-based policy (such as an Amazon S3 bucket policy). The supplied IAM policy, in JSON format, is used to scope down the permissions that are available to the IAM user. The supplied policy cannot grant more permissions than those granted to the requesting user, with the final permissions for the federated user being the most restrictive set based on the intersection of the passed policy and the IAM user policy.**

```
Get-STSFederationToken -Name "Bob" -Policy "...JSON policy..." -DurationInSeconds 3600
```
+  For API details, see [GetFederationToken](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-STSSessionToken`
<a name="sts_GetSessionToken_powershell_topic"></a>

The following code example shows how to use `Get-STSSessionToken`.

**Tools for PowerShell V5**
**Example 1: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for a set period of time. The credentials used to request temporary credentials are inferred from the current shell defaults. To specify other credentials, use the -ProfileName or -AccessKey/-SecretKey parameters.**

```
Get-STSSessionToken
```
**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```
**Example 2: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for one hour. The credentials used to make the request are obtained from the specified profile.**

```
Get-STSSessionToken -DurationInSeconds 3600 -ProfileName myprofile
```
**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```
**Example 3: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for one hour using the identification number of the MFA device associated with the account whose credentials are specified in the profile 'myprofilename' and the value provided by the device.**

```
Get-STSSessionToken -DurationInSeconds 3600 -ProfileName myprofile -SerialNumber YourMFADeviceSerialNumber -TokenCode 123456
```
**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```
+  For API details, see [GetSessionToken](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Use-STSRole`
<a name="sts_AssumeRole_powershell_topic"></a>

The following code example shows how to use `Use-STSRole`.

**Tools for PowerShell V5**
**Example 1: Returns a set of temporary credentials (access key, secret key and session token) that can be used for one hour to access AWS resources that the requesting user might not normally have access to. The returned credentials have the permissions that are allowed by the access policy of the role being assumed and the policy that was supplied (you cannot use the supplied policy to grant permissions in excess of those defined by the access policy of the role being assumed).**

```
Use-STSRole -RoleSessionName "Bob" -RoleArn "arn:aws:iam::123456789012:role/demo" -Policy "...JSON policy..." -DurationInSeconds 3600
```
**Example 2: Returns a set of temporary credentials, valid for one hour, that have the same permissions that are defined in the access policy of the role being assumed.**

```
Use-STSRole -RoleSessionName "Bob" -RoleArn "arn:aws:iam::123456789012:role/demo" -DurationInSeconds 3600
```
**Example 3: Returns a set of temporary credentials supplying the serial number and generated token from an MFA associated with the user credentials used to execute the cmdlet.**

```
Use-STSRole -RoleSessionName "Bob" -RoleArn "arn:aws:iam::123456789012:role/demo" -DurationInSeconds 3600 -SerialNumber "GAHT12345678" -TokenCode "123456"
```
**Example 4: Returns a set of temporary credentials that have assumed a role defined in a customer account. For each role that the third party can assume, the customer account must create a role using an identifier that must be passed in the -ExternalId parameter each time the role is assumed.**

```
Use-STSRole -RoleSessionName "Bob" -RoleArn "arn:aws:iam::123456789012:role/demo" -DurationInSeconds 3600 -ExternalId "ABC123"
```
+  For API details, see [AssumeRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Use-STSWebIdentityRole`
<a name="sts_AssumeRoleWithWebIdentity_powershell_topic"></a>

The following code example shows how to use `Use-STSWebIdentityRole`.

**Tools for PowerShell V5**
**Example 1: Returns a temporary set of credentials, valid for one hour, for a user who has been authenticated with the Login with Amazon identity provider. The credentials assume the access policy associated with the role identified by the role ARN. Optionally, you can pass a JSON policy to the -Policy parameter that further refine the access permissions (you cannot grant more permissions than are available in the permissions associated with the role). The value supplied to the -WebIdentityToken is the unique user identifier that was returned by the identity provider. **

```
Use-STSWebIdentityRole -DurationInSeconds 3600 -ProviderId "www.amazon.com" -RoleSessionName "app1" -RoleArn "arn:aws:iam::123456789012:role/FederatedWebIdentityRole" -WebIdentityToken "Atza...DVI0r1"
```
+  For API details, see [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
