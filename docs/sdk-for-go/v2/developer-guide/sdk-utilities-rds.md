---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-rds.html
---

# Amazon RDS Utilities
<a name="sdk-utilities-rds"></a>

## IAM Authentication
<a name="iam-authentication"></a>

 The [auth](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/rds/auth) package provides utilities for generating authentication tokens for connecting to Amazon RDS MySQL and PostgreSQL database instances. Using the [BuildAuthToken](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/rds/auth#BuildAuthToken) method, you generate a database authorization token by providing the database endpoint, AWS Region, username, and a [aws.CredentialProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#CredentialsProvider) implementation that returns IAM credentials with permission to connect to the database using IAM database authentication. To learn more about configuring Amazon RDS with IAM authentication, see the following Amazon RDS Developer Guide resources:
+  [Enabling and disabling IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html)
+  [Creating and using an IAM policy for IAM database access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.html)
+  [Creating a database account using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html)

 The following example shows how to generate an authentication token to connect to an Amazon RDS database:

```
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
import "github.com/aws/aws-sdk-go-v2/feature/rds/auth"

// ...

cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    panic("configuration error: " + err.Error())
}

authenticationToken, err := auth.BuildAuthToken(
    context.TODO(),
    "mydb.123456789012.us-east-1.rds.amazonaws.com:3306", // Database Endpoint (With Port)
    "us-east-1", // AWS Region
    "jane_doe", // Database Account
    cfg.Credentials,
)
if err != nil {
    panic("failed to create authentication token: " + err.Error())
}
```
