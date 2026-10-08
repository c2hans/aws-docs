---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_dsql_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Aurora DSQL examples using AWS CLI
<a name="cli_2_dsql_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Aurora DSQL.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `generate-db-connect-auth-token`
<a name="dsql_GenerateDbConnectAuthToken_cli_2_topic"></a>

The following code example shows how to use `generate-db-connect-auth-token`.

**AWS CLI**
**To generate an IAM authentication token**
The following `generate-db-connect-auth-token` example generates IAM authentication token to connect to a database.

```
aws dsql generate-db-connect-auth-token \
    --hostname {{abc0def1baz2quux3quuux4.dsql.us-east-1.on.aws}} \
    --region {{us-east-1}} \
    --expires-in {{3600}}
```
Output:

```
'abc0def1baz2quux3quuux4.dsql.us-east-1.on.aws/?Action=DbConnect&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=access_key%2F20241107%2Fus-east-1%2Fdsql%2Faws4_request&X-Amz-Date=20241107T173933Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=b53dae15763139d6a5af5e318b117ff6e66c5ee859b14d44697d159cbe996077'
```
+  For API details, see [GenerateDbConnectAuthToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/generate-db-connect-auth-token.html) in *AWS CLI Command Reference*.
