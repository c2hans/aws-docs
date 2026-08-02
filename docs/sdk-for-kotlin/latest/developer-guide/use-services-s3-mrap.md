---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services-s3-mrap.html
---

# Work with Amazon S3 Multi-Region Access Points by using the SDK for Kotlin
<a name="use-services-s3-mrap"></a>

Amazon S3 Multi-Region Access Points provide a global endpoint that applications can use to fulfill requests from Amazon S3 buckets located in multiple AWS Regions. You can use Multi-Region Access Points to build multi-Region applications with the same architecture used in a single Region, and then run those applications anywhere in the world.

The Amazon S3 User Guide contains more background information about [Multi-Region Access Points](/AmazonS3/latest/userguide/MultiRegionAccessPoints.html).

## Work with Multi-Region Access Points
<a name="mrap-s3control-config"></a>

To create a Multi-Region Access Point, start by specifying one bucket in each AWS Region that you want to serve requests. The following snippet creates two buckets.

### Create buckets
<a name="_create_buckets"></a>

The following function creates two buckets to work with the Multi-Region Access Point. One bucket is in Region `us-east-1` and the other is in Region `us-west-1`.

The creation of the S3 client that passed in as the first argument is shown in the first example under [Work with objects and Multi-Region Access Points](#mrap-s3client-config).

```
        suspend fun setUpTwoBuckets(
            s3: S3Client,
            bucketName1: String,
            bucketName2: String,
        ) {
            println("Create two buckets in different regions.")
            // The shared aws config file configures the default Region to be us-east-1.
            s3.createBucket(
                CreateBucketRequest {
                    bucket = bucketName1
                },
            )
            s3.waitUntilBucketExists {
                bucket = bucketName1
            }
            println("  Bucket [$bucketName1] created.")

            // Override the S3Client to work with us-west-1 for the second bucket.
            s3.withConfig {
                region = "us-west-1"
            }.use { s3West ->
                s3West.createBucket(
                    CreateBucketRequest {
                        bucket = bucketName2
                        createBucketConfiguration = CreateBucketConfiguration {
                            locationConstraint = BucketLocationConstraint.UsWest1
                        }
                    },
                )
                s3West.waitUntilBucketExists {
                    bucket = bucketName2
                }
                println("  Bucket [$bucketName2] created.")
            }
        }
```

You use the Kotlin SDK’s [S3 control client](/sdk-for-kotlin/api/latest/s3control/aws.sdk.kotlin.services.s3control/-s3-control-client/index.html) to create, delete, and get information about Multi-Region Access Points.

Add a dependency on the S3 control artifact as shown in the following snippet. Replace {{X.Y.Z}} with the version you’re using in your app or with the [latest version available](https://github.com/awslabs/aws-sdk-kotlin/releases/latest).

```
...
implementation(platform("aws.sdk.kotlin:bom:{{X.Y.Z}}"))
implementation("aws.sdk.kotlin:s3control")
...
```

Configure the S3 control client to work with AWS Region `us-west-2` as shown in the following code. All S3 control client operations must target the `us-west-2` region.

```
        suspend fun createS3ControlClient(): S3ControlClient {
            // Configure your S3ControlClient to send requests to US West (Oregon).
            val s3Control = S3ControlClient.fromEnvironment {
                region = "us-west-2"
            }
            return s3Control
        }
```

Use the S3 control client to create a Multi-Region Access Point by specifying the bucket names (created previously) as shown in the following code.

```
    suspend fun createMrap(
        s3Control: S3ControlClient,
        accountIdParam: String,
        bucketName1: String,
        bucketName2: String,
        mrapName: String,
    ): String {
        println("Creating MRAP ...")
        val createMrapResponse: CreateMultiRegionAccessPointResponse =
            s3Control.createMultiRegionAccessPoint {
                accountId = accountIdParam
                clientToken = UUID.randomUUID().toString()
                details {
                    name = mrapName
                    regions = listOf(
                        Region {
                            bucket = bucketName1
                        },
                        Region {
                            bucket = bucketName2
                        },
                    )
                }
            }
        val requestToken: String? = createMrapResponse.requestTokenArn

        // Use the request token to check for the status of the CreateMultiRegionAccessPoint operation.
        if (requestToken != null) {
            waitForSucceededStatus(s3Control, requestToken, accountIdParam)
            println("MRAP created")
        }

        val getMrapResponse =
            s3Control.getMultiRegionAccessPoint(
                input = GetMultiRegionAccessPointRequest {
                    accountId = accountIdParam
                    name = mrapName
                },
            )
        val mrapAlias = getMrapResponse.accessPoint?.alias
        return "arn:aws:s3::$accountIdParam:accesspoint/$mrapAlias"
    }
```

Because the creation of a Multi-Region Access Point is an asynchronous operation, you use the token that you receive from the immediate response to check on the status of the creation process. After the status check returns a success message, you can use the `GetMultiRegionAccessPoint` operation to get the Multi-Region Access Point’s alias. The alias is the last component of the ARN, which you need for object-level operations.

### Use token to check status
<a name="_use_token_to_check_status"></a>

Use the `DescribeMultiRegionAccessPointOperation` to check the status of the last operation. After the `requestStatus` value becomes "SUCCEEDED", you can work with the Multi-Region Access Point.

```
        suspend fun waitForSucceededStatus(
            s3Control: S3ControlClient,
            requestToken: String,
            accountIdParam: String,
            timeBetweenChecks: Duration = 1.minutes,
        ) {
            var describeResponse: DescribeMultiRegionAccessPointOperationResponse
            describeResponse = s3Control.describeMultiRegionAccessPointOperation(
                input = DescribeMultiRegionAccessPointOperationRequest {
                    accountId = accountIdParam
                    requestTokenArn = requestToken
                },
            )

            var status: String? = describeResponse.asyncOperation?.requestStatus
            while (status != "SUCCEEDED") {
                delay(timeBetweenChecks)
                describeResponse = s3Control.describeMultiRegionAccessPointOperation(
                    input = DescribeMultiRegionAccessPointOperationRequest {
                        accountId = accountIdParam
                        requestTokenArn = requestToken
                    },
                )
                status = describeResponse.asyncOperation?.requestStatus
                println(status)
            }
        }
```

## Work with objects and Multi-Region Access Points
<a name="mrap-s3client-config"></a>

You use the [S3 client](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/index.html) to work with objects in Multi-Region Access Points. Many of the operations that you use on objects in buckets you can use on Multi-Region Access Points. For more information and a full list of operations, see [Multi-Region Access Point compatibility with S3 operations](/AmazonS3/latest/userguide/MrapOperations.html#mrap-operations-support).

Operations with Multi-Region Access Points are signed with the Asymmetric SigV4 (SigV4a) signing algorithm. To configure SigV4a, first add the following dependencies to your project. Replace {{X.Y.Z}} with the version you’re using in your app or with the latest version available ([aws-sdk-kotlin](https://github.com/awslabs/aws-sdk-kotlin/releases/latest), [smithy-kotlin](https://github.com/smithy-lang/smithy-kotlin/releases/latest)).

```
...
implementation(platform("aws.sdk.kotlin:bom:{{X.Y.Z}}"))
implementation(platform("aws.smithy.kotlin:bom:{{X.Y.Z}}"))

implementation("aws.smithy.kotlin:aws-signing-default")
implementation("aws.smithy.kotlin:http-auth-aws")
implementation("aws.sdk.kotlin:s3")
...
```

After you add the dependencies, configure the S3 client to use the SigV4a signing algorithm as shown in the following code.

```
        suspend fun createS3Client(): S3Client {
            // Configure your S3Client to use the Asymmetric SigV4 (SigV4a) signing algorithm.
            val sigV4aScheme = SigV4AsymmetricAuthScheme(DefaultAwsSigner)
            val s3 = S3Client.fromEnvironment {
                authSchemes = listOf(sigV4aScheme)
            }
            return s3
        }
```

After you configure the S3 client, operations that S3 supports for Multi-Region Access Points work the same. The only difference is that the bucket parameter must be the ARN of the Multi-Region Access Point. You can get the ARN from the Amazon S3 console or programmatically as shown previously in the `createMrap` function that returns an ARN.

The following code example shows the ARN used in a `GetObject` operation.

```
    suspend fun getObjectFromMrap(
        s3: S3Client,
        mrapArn: String,
        keyName: String,
    ): String? {
        val request = GetObjectRequest {
            bucket = mrapArn // Use the ARN instead of the bucket name for object operations.
            key = keyName
        }

        var stringObj: String? = null
        s3.getObject(request) { resp ->
            stringObj = resp.body?.decodeToString()
            if (stringObj != null) {
                println("Successfully read $keyName from $mrapArn")
            }
        }
        return stringObj
    }
```
