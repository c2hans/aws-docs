---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_cognito-identity_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Amazon Cognito Identity examples using Tools for PowerShell V5
<a name="powershell_cognito-identity_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon Cognito Identity.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-CGIIdentityPool`
<a name="cognito-identity_DescribeIdentityPool_powershell_topic"></a>

The following code example shows how to use `Get-CGIIdentityPool`.

**Tools for PowerShell V5**
**Example 1: Retrieves information about a specific Identity Pool by its id.**

```
Get-CGIIdentityPool -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1
```
**Output:**

```
LoggedAt                       : 8/12/2015 4:29:40 PM
AllowUnauthenticatedIdentities : True
DeveloperProviderName          :
IdentityPoolId                 : us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1
IdentityPoolName               : CommonTests1
OpenIdConnectProviderARNs      : {}
SupportedLoginProviders        : {}
ResponseMetadata               : Amazon.Runtime.ResponseMetadata
ContentLength                  : 142
HttpStatusCode                 : OK
```
+  For API details, see [DescribeIdentityPool](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CGIIdentityPoolList`
<a name="cognito-identity_ListIdentityPools_powershell_topic"></a>

The following code example shows how to use `Get-CGIIdentityPoolList`.

**Tools for PowerShell V5**
**Example 1: Retrieves a list of existing Identity Pools.**

```
Get-CGIIdentityPoolList
```
**Output:**

```
IdentityPoolId                                                     IdentityPoolName
--------------                                                     ----------------
us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1                     CommonTests1
us-east-1:118d242d-204e-4b88-b803-EXAMPLEGUID2                     Tests2
us-east-1:15d49393-ab16-431a-b26e-EXAMPLEGUID3                     CommonTests13
```
+  For API details, see [ListIdentityPools](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CGIIdentityPoolRole`
<a name="cognito-identity_GetIdentityPoolRoles_powershell_topic"></a>

The following code example shows how to use `Get-CGIIdentityPoolRole`.

**Tools for PowerShell V5**
**Example 1: Gets the information about roles for a specific Identity Pool.**

```
Get-CGIIdentityPoolRole -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1
```
**Output:**

```
LoggedAt         : 8/12/2015 4:33:51 PM
IdentityPoolId   : us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1
Roles            : {[unauthenticated, arn:aws:iam::123456789012:role/CommonTests1Role]}
ResponseMetadata : Amazon.Runtime.ResponseMetadata
ContentLength    : 165
HttpStatusCode   : OK
```
+  For API details, see [GetIdentityPoolRoles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CGIIdentityPool`
<a name="cognito-identity_CreateIdentityPool_powershell_topic"></a>

The following code example shows how to use `New-CGIIdentityPool`.

**Tools for PowerShell V5**
**Example 1: Creates a new Identity Pool which allows unauthenticated identities.**

```
New-CGIIdentityPool -AllowUnauthenticatedIdentities $true -IdentityPoolName CommonTests13
```
**Output:**

```
LoggedAt                       : 8/12/2015 4:56:07 PM
AllowUnauthenticatedIdentities : True
DeveloperProviderName          :
IdentityPoolId                 : us-east-1:15d49393-ab16-431a-b26e-EXAMPLEGUID3
IdentityPoolName               : CommonTests13
OpenIdConnectProviderARNs      : {}
SupportedLoginProviders        : {}
ResponseMetadata               : Amazon.Runtime.ResponseMetadata
ContentLength                  : 136
HttpStatusCode                 : OK
```
+  For API details, see [CreateIdentityPool](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CGIIdentityPool`
<a name="cognito-identity_DeleteIdentityPool_powershell_topic"></a>

The following code example shows how to use `Remove-CGIIdentityPool`.

**Tools for PowerShell V5**
**Example 1: Deletes a specific Identity Pool.**

```
Remove-CGIIdentityPool -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1
```
+  For API details, see [DeleteIdentityPool](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-CGIIdentityPoolRole`
<a name="cognito-identity_SetIdentityPoolRoles_powershell_topic"></a>

The following code example shows how to use `Set-CGIIdentityPoolRole`.

**Tools for PowerShell V5**
**Example 1: Configures the specific Identity Pool to have an unauthenticated IAM role.**

```
Set-CGIIdentityPoolRole -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1 -Role @{ "unauthenticated" = "arn:aws:iam::123456789012:role/CommonTests1Role" }
```
+  For API details, see [SetIdentityPoolRoles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-CGIIdentityPool`
<a name="cognito-identity_UpdateIdentityPool_powershell_topic"></a>

The following code example shows how to use `Update-CGIIdentityPool`.

**Tools for PowerShell V5**
**Example 1: Updates some of the Identity Pool properties, in this case the name of the Identity Pool.**

```
Update-CGIIdentityPool -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1 -IdentityPoolName NewPoolName
```
**Output:**

```
LoggedAt                       : 8/12/2015 4:53:33 PM
AllowUnauthenticatedIdentities : False
DeveloperProviderName          :
IdentityPoolId                 : us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1
IdentityPoolName               : NewPoolName
OpenIdConnectProviderARNs      : {}
SupportedLoginProviders        : {}
ResponseMetadata               : Amazon.Runtime.ResponseMetadata
ContentLength                  : 135
HttpStatusCode                 : OK
```
+  For API details, see [UpdateIdentityPool](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
