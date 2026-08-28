---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_temporary.html
---

# Use temporary credentials from AWS STS in the SDK for PHP
<a name="guide_credentials_temporary"></a>

 AWS Security Token Service (AWS STS) enables you to request limited privilege, **temporary credentials** for IAM users, or for users that you authenticate via identity federation. For deeper understanding, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*. You can use temporary security credentials to access most AWS services. For a list of the services that accept temporary security credentials, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

One common use case for temporary credentials is to grant mobile or client-side applications access to AWS resources by authenticating users through third-party identity providers (see [Web Identity Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)).

## Getting temporary credentials
<a name="getting-temporary-credentials"></a>

AWS STS has several operations that return temporary credentials, but the `GetSessionToken` operation is the simplest to demonstrate. The following snippet retrieves temporary credentials by calling the `getSessionToken` method of the PHP SDK's STS client.

```
$sdk = new Aws\Sdk([
    'region'   => 'us-east-1',
]);

$stsClient = $sdk->createSts();

$result = $stsClient->getSessionToken();
```

The result for `GetSessionToken` and the other AWS STS operations always contains a `'Credentials'` value. If you print the `$result` (for example by using `print_r($result)`), it looks like the following.

```
Array
(
    ...
    [Credentials] => Array
    (
        [SessionToken] => '<base64 encoded session token value>'
        [SecretAccessKey] => '<temporary secret access key value>'
        [Expiration] => 2013-11-01T01:57:52Z
        [AccessKeyId] => '<temporary access key value>'
    )
    ...
)
```

## Providing temporary credentials to the AWS SDK for PHP
<a name="providing-temporary-credentials-to-the-sdk-php"></a>

You can use temporary credentials with another AWS client by instantiating the client and passing in the values received from AWS STS directly.

```
use Aws\S3\S3Client;

$result = $stsClient->getSessionToken();

$s3Client = new S3Client([
    'version'     => '2006-03-01',
    'region'      => 'us-west-2',
    'credentials' => [
        'key'    => $result['Credentials']['AccessKeyId'],
        'secret' => $result['Credentials']['SecretAccessKey'],
        'token'  => $result['Credentials']['SessionToken']
    ]
]);
```

You can also construct an `Aws\Credentials\Credentials` object and use that when instantiating the client.

```
use Aws\Credentials\Credentials;
use Aws\S3\S3Client;

$result = $stsClient->getSessionToken();

$credentials = new Credentials(
    $result['Credentials']['AccessKeyId'],
    $result['Credentials']['SecretAccessKey'],
    $result['Credentials']['SessionToken']
);

$s3Client = new S3Client([
    'version'     => '2006-03-01',
    'region'      => 'us-west-2',
    'credentials' => $credentials
]);
```

However, the *best* way to provide temporary credentials is to use the `createCredentials()` helper method included with the `StsClient`. This method extracts the data from an AWS STS result and creates the `Credentials` object for you.

```
$result = $stsClient->getSessionToken();
$credentials = $stsClient->createCredentials($result);

$s3Client = new S3Client([
    'version'     => '2006-03-01',
    'region'      => 'us-west-2',
    'credentials' => $credentials
]);
```

For more information about why you might need to use temporary credentials in your application or project, see [Scenarios for Granting Temporary Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the AWS STS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
