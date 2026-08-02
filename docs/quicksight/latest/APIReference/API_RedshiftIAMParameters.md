---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RedshiftIAMParameters.html
---

# RedshiftIAMParameters
<a name="API_RedshiftIAMParameters"></a>

A structure that grants Quick Sight access to your cluster and make a call to the `redshift:GetClusterCredentials` API. For more information on the `redshift:GetClusterCredentials` API, see [https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html).

## Contents
<a name="API_RedshiftIAMParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RoleArn **   <a name="QS-Type-RedshiftIAMParameters-RoleArn"></a>
Use the `RoleArn` structure to allow Quick Sight to call `redshift:GetClusterCredentials` on your cluster. The calling principal must have `iam:PassRole` access to pass the role to Quick Sight. The role's trust policy must allow the Quick Sight service principal to assume the role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** AutoCreateDatabaseUser **   <a name="QS-Type-RedshiftIAMParameters-AutoCreateDatabaseUser"></a>
Automatically creates a database user. If your database doesn't have a `DatabaseUser`, set this parameter to `True`. If there is no `DatabaseUser`, Quick Sight can't connect to your cluster. The `RoleArn` that you use for this operation must grant access to `redshift:CreateClusterUser` to successfully create the user.
Type: Boolean
Required: No

 ** DatabaseGroups **   <a name="QS-Type-RedshiftIAMParameters-DatabaseGroups"></a>
A list of groups whose permissions will be granted to Quick Sight to access the cluster. These permissions are combined with the permissions granted to Quick Sight by the `DatabaseUser`. If you choose to include this parameter, the `RoleArn` must grant access to `redshift:JoinGroup`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** DatabaseUser **   <a name="QS-Type-RedshiftIAMParameters-DatabaseUser"></a>
The user whose permissions and group memberships will be used by Quick Sight to access the cluster. If this user already exists in your database, Amazon Quick Sight is granted the same permissions that the user has. If the user doesn't exist, set the value of `AutoCreateDatabaseUser` to `True` to create a new user with PUBLIC permissions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_RedshiftIAMParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RedshiftIAMParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RedshiftIAMParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RedshiftIAMParameters)
