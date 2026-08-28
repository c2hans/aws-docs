---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-explicit.html
---

# Supply credentials in code using the AWS SDK for Java 2.x
<a name="credentials-explicit"></a>

If the default credential chain or a specific or custom provider or provider chain doesn't work for your application, you can supply temporary credentials directly in code. These can be [IAM role credentials](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) as[ described above](credentials-temporary.md#credentials-temporary-from-portal) or temporary credentials retrieved from AWS Security Token Service (AWS STS). If you retrieved temporary credentials using AWS STS, provide them to an AWS service client as shown in the following code example.

1. Assume a role by calling `StsClient.assumeRole()`.

1. Create a [StaticCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/StaticCredentialsProvider.html) object and supply it with the `AwsSessionCredentials` object.

1. Configure the service client builder with the `StaticCredentialsProvider` and build the client.

The following example creates an Amazon S3 service client using temporary credentials returned by AWS STS for an IAM assumed role.

```
    // The AWS IAM Identity Center identity (user) who executes this method does not have permission to list buckets.
    // The identity is configured in the [default] profile.
    public static void assumeRole(String roleArn, String roleSessionName) {
        // The IAM role represented by the 'roleArn' parameter can be assumed by identities in two different accounts
        // and the role permits the user to only list buckets.

        // The SDK's default credentials provider chain will find the single sign-on settings in the [default] profile.
        // The identity configured with the [default] profile needs permission to call AssumeRole on the STS service.
        try {
            Credentials tempRoleCredentials;
            try (StsClient stsClient = StsClient.create()) {
                AssumeRoleRequest roleRequest = AssumeRoleRequest.builder()
                        .roleArn(roleArn)
                        .roleSessionName(roleSessionName)
                        .build();

                AssumeRoleResponse roleResponse = stsClient.assumeRole(roleRequest);
                tempRoleCredentials = roleResponse.credentials();
            }
            // Use the following temporary credential items for the S3 client.
            String key = tempRoleCredentials.accessKeyId();
            String secKey = tempRoleCredentials.secretAccessKey();
            String secToken = tempRoleCredentials.sessionToken();

            // List all buckets in the account associated with the assumed role
            // by using the temporary credentials retrieved by invoking stsClient.assumeRole().
            StaticCredentialsProvider staticCredentialsProvider = StaticCredentialsProvider.create(
                    AwsSessionCredentials.create(key, secKey, secToken));
            try (S3Client s3 = S3Client.builder()
                    .credentialsProvider(staticCredentialsProvider)
                    .build()) {
                List<Bucket> buckets = s3.listBuckets().buckets();
                for (Bucket bucket : buckets) {
                    System.out.println("bucket name: " + bucket.name());
                }
            }
        } catch (StsException | S3Exception e) {
            logger.error(e.getMessage());
            System.exit(1);
        }
    }
```

## Permission set
<a name="credentials-explicit-permission-set"></a>

The following permission set defined in AWS IAM Identity Center allows the identity (user) to perform the following two operations

1. The `GetObject` operation of the Amazon Simple Storage Service.

1. The `AssumeRole` operation of the AWS Security Token Service.

Without assuming the role, the `s3.listBuckets()` method shown in the example would fail.

------
#### [ JSON ]

****

```
{
	"Version":"2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"s3:GetObject",
				"sts:AssumeRole"
			],
			"Resource": [
				"*"
			]
		}
	]
}
```

------

## Assumed role
<a name="credentials-explicit-role-to-assume"></a>

### Assumed role permissions policy
<a name="credentials-explicit-role-policy"></a>

The following permissions policy is attached to the role that is assume in the previous example. This permissions policy permits the ability to list all buckets in the same account as the role.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------

### Assumed role trust policy
<a name="credentials-explicit-trust-policy"></a>

The following trust policy is attached to the role that is assume in the previous example. The policy allows the role to be assumed by identities (users) in two accounts.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{111122223333}}:root",
                    "arn:aws:iam::{{555555555555}}:root"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
