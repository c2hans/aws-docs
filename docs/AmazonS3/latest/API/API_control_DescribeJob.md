---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html
---

# DescribeJob
<a name="API_control_DescribeJob"></a>

Retrieves the configuration parameters and status for a Batch Operations job. For more information, see [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html) in the *Amazon S3 User Guide*.

Permissions
To use the `DescribeJob` operation, you must have permission to perform the `s3:DescribeJob` action.

Related actions include:
+  [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)
+  [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html)
+  [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html)
+  [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)

## Request Syntax
<a name="API_control_DescribeJob_RequestSyntax"></a>

```
GET /v20180820/jobs/{{id}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_DescribeJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_DescribeJob_RequestSyntax) **   <a name="AmazonS3-control_DescribeJob-request-uri-uri-JobId"></a>
The ID for the job whose information you want to retrieve.
Length Constraints: Minimum length of 5. Maximum length of 36.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [x-amz-account-id](#API_control_DescribeJob_RequestSyntax) **   <a name="AmazonS3-control_DescribeJob-request-header-AccountId"></a>
The AWS account ID associated with the S3 Batch Operations job.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DescribeJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_DescribeJob_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DescribeJobResult>
   <Job>
      <ConfirmationRequired>boolean</ConfirmationRequired>
      <CreationTime>timestamp</CreationTime>
      <Description>string</Description>
      <FailureReasons>
         <JobFailure>
            <FailureCode>string</FailureCode>
            <FailureReason>string</FailureReason>
         </JobFailure>
      </FailureReasons>
      <GeneratedManifestDescriptor>
         <Format>string</Format>
         <Location>
            <ETag>string</ETag>
            <ObjectArn>string</ObjectArn>
            <ObjectVersionId>string</ObjectVersionId>
         </Location>
      </GeneratedManifestDescriptor>
      <JobArn>string</JobArn>
      <JobId>string</JobId>
      <Manifest>
         <Location>
            <ETag>string</ETag>
            <ObjectArn>string</ObjectArn>
            <ObjectVersionId>string</ObjectVersionId>
         </Location>
         <Spec>
            <Fields>
               <member>string</member>
            </Fields>
            <Format>string</Format>
         </Spec>
      </Manifest>
      <ManifestGenerator>
         <S3JobManifestGenerator>
            <EnableManifestOutput>boolean</EnableManifestOutput>
            <ExpectedBucketOwner>string</ExpectedBucketOwner>
            <Filter>
               <CreatedAfter>timestamp</CreatedAfter>
               <CreatedBefore>timestamp</CreatedBefore>
               <EligibleForReplication>boolean</EligibleForReplication>
               <KeyNameConstraint>
                  <MatchAnyPrefix>
                     <member>string</member>
                  </MatchAnyPrefix>
                  <MatchAnySubstring>
                     <member>string</member>
                  </MatchAnySubstring>
                  <MatchAnySuffix>
                     <member>string</member>
                  </MatchAnySuffix>
               </KeyNameConstraint>
               <MatchAnyObjectEncryption>
                  <ObjectEncryption>
                     <DSSE-KMS>
                        <KmsKeyArn>string</KmsKeyArn>
                     </DSSE-KMS>
                     <NOT-SSE>
                     </NOT-SSE>
                     <SSE-C>
                     </SSE-C>
                     <SSE-KMS>
                        <BucketKeyEnabled>boolean</BucketKeyEnabled>
                        <KmsKeyArn>string</KmsKeyArn>
                     </SSE-KMS>
                     <SSE-S3>
                     </SSE-S3>
                  </ObjectEncryption>
               </MatchAnyObjectEncryption>
               <MatchAnyStorageClass>
                  <member>string</member>
               </MatchAnyStorageClass>
               <ObjectReplicationStatuses>
                  <member>string</member>
               </ObjectReplicationStatuses>
               <ObjectSizeGreaterThanBytes>long</ObjectSizeGreaterThanBytes>
               <ObjectSizeLessThanBytes>long</ObjectSizeLessThanBytes>
            </Filter>
            <ManifestOutputLocation>
               <Bucket>string</Bucket>
               <ExpectedManifestBucketOwner>string</ExpectedManifestBucketOwner>
               <ManifestEncryption>
                  <SSE-KMS>
                     <KeyId>string</KeyId>
                  </SSE-KMS>
                  <SSE-S3>
                  </SSE-S3>
               </ManifestEncryption>
               <ManifestFormat>string</ManifestFormat>
               <ManifestPrefix>string</ManifestPrefix>
            </ManifestOutputLocation>
            <SourceBucket>string</SourceBucket>
         </S3JobManifestGenerator>
      </ManifestGenerator>
      <Operation>
         <LambdaInvoke>
            <FunctionArn>string</FunctionArn>
            <InvocationSchemaVersion>string</InvocationSchemaVersion>
            <UserArguments>
               <entry>
                  <key>string</key>
                  <value>string</value>
               </entry>
            </UserArguments>
         </LambdaInvoke>
         <S3ComputeObjectChecksum>
            <ChecksumAlgorithm>string</ChecksumAlgorithm>
            <ChecksumType>string</ChecksumType>
         </S3ComputeObjectChecksum>
         <S3DeleteObjectTagging>
         </S3DeleteObjectTagging>
         <S3InitiateRestoreObject>
            <ExpirationInDays>integer</ExpirationInDays>
            <GlacierJobTier>string</GlacierJobTier>
         </S3InitiateRestoreObject>
         <S3PutObjectAcl>
            <AccessControlPolicy>
               <AccessControlList>
                  <Grants>
                     <S3Grant>
                        <Grantee>
                           <DisplayName>string</DisplayName>
                           <Identifier>string</Identifier>
                           <TypeIdentifier>string</TypeIdentifier>
                        </Grantee>
                        <Permission>string</Permission>
                     </S3Grant>
                  </Grants>
                  <Owner>
                     <DisplayName>string</DisplayName>
                     <ID>string</ID>
                  </Owner>
               </AccessControlList>
               <CannedAccessControlList>string</CannedAccessControlList>
            </AccessControlPolicy>
         </S3PutObjectAcl>
         <S3PutObjectCopy>
            <AccessControlGrants>
               <S3Grant>
                  <Grantee>
                     <DisplayName>string</DisplayName>
                     <Identifier>string</Identifier>
                     <TypeIdentifier>string</TypeIdentifier>
                  </Grantee>
                  <Permission>string</Permission>
               </S3Grant>
            </AccessControlGrants>
            <BucketKeyEnabled>boolean</BucketKeyEnabled>
            <CannedAccessControlList>string</CannedAccessControlList>
            <ChecksumAlgorithm>string</ChecksumAlgorithm>
            <MetadataDirective>string</MetadataDirective>
            <ModifiedSinceConstraint>timestamp</ModifiedSinceConstraint>
            <NewObjectMetadata>
               <CacheControl>string</CacheControl>
               <ContentDisposition>string</ContentDisposition>
               <ContentEncoding>string</ContentEncoding>
               <ContentLanguage>string</ContentLanguage>
               <ContentLength>long</ContentLength>
               <ContentMD5>string</ContentMD5>
               <ContentType>string</ContentType>
               <HttpExpiresDate>timestamp</HttpExpiresDate>
               <RequesterCharged>boolean</RequesterCharged>
               <SSEAlgorithm>string</SSEAlgorithm>
               <UserMetadata>
                  <entry>
                     <key>string</key>
                     <value>string</value>
                  </entry>
               </UserMetadata>
            </NewObjectMetadata>
            <NewObjectTagging>
               <S3Tag>
                  <Key>string</Key>
                  <Value>string</Value>
               </S3Tag>
            </NewObjectTagging>
            <ObjectLockLegalHoldStatus>string</ObjectLockLegalHoldStatus>
            <ObjectLockMode>string</ObjectLockMode>
            <ObjectLockRetainUntilDate>timestamp</ObjectLockRetainUntilDate>
            <RedirectLocation>string</RedirectLocation>
            <RequesterPays>boolean</RequesterPays>
            <SSEAwsKmsKeyId>string</SSEAwsKmsKeyId>
            <StorageClass>string</StorageClass>
            <TargetKeyPrefix>string</TargetKeyPrefix>
            <TargetResource>string</TargetResource>
            <UnModifiedSinceConstraint>timestamp</UnModifiedSinceConstraint>
         </S3PutObjectCopy>
         <S3PutObjectLegalHold>
            <LegalHold>
               <Status>string</Status>
            </LegalHold>
         </S3PutObjectLegalHold>
         <S3PutObjectRetention>
            <BypassGovernanceRetention>boolean</BypassGovernanceRetention>
            <Retention>
               <Mode>string</Mode>
               <RetainUntilDate>timestamp</RetainUntilDate>
            </Retention>
         </S3PutObjectRetention>
         <S3PutObjectTagging>
            <TagSet>
               <S3Tag>
                  <Key>string</Key>
                  <Value>string</Value>
               </S3Tag>
            </TagSet>
         </S3PutObjectTagging>
         <S3ReplicateObject>
         </S3ReplicateObject>
         <S3UpdateObjectEncryption>
            <ObjectEncryption>
               <SSE-KMS>
                  <BucketKeyEnabled>boolean</BucketKeyEnabled>
                  <KMSKeyArn>string</KMSKeyArn>
               </SSE-KMS>
            </ObjectEncryption>
         </S3UpdateObjectEncryption>
      </Operation>
      <Priority>integer</Priority>
      <ProgressSummary>
         <NumberOfTasksFailed>long</NumberOfTasksFailed>
         <NumberOfTasksSucceeded>long</NumberOfTasksSucceeded>
         <Timers>
            <ElapsedTimeInActiveSeconds>long</ElapsedTimeInActiveSeconds>
         </Timers>
         <TotalNumberOfTasks>long</TotalNumberOfTasks>
      </ProgressSummary>
      <Report>
         <Bucket>string</Bucket>
         <Enabled>boolean</Enabled>
         <ExpectedBucketOwner>string</ExpectedBucketOwner>
         <Format>string</Format>
         <Prefix>string</Prefix>
         <ReportScope>string</ReportScope>
      </Report>
      <RoleArn>string</RoleArn>
      <Status>string</Status>
      <StatusUpdateReason>string</StatusUpdateReason>
      <SuspendedCause>string</SuspendedCause>
      <SuspendedDate>timestamp</SuspendedDate>
      <TerminationDate>timestamp</TerminationDate>
   </Job>
</DescribeJobResult>
```

## Response Elements
<a name="API_control_DescribeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DescribeJobResult](#API_control_DescribeJob_ResponseSyntax) **   <a name="AmazonS3-control_DescribeJob-response-DescribeJobResult"></a>
Root level tag for the DescribeJobResult parameters.
Required: Yes

 ** [Job](#API_control_DescribeJob_ResponseSyntax) **   <a name="AmazonS3-control_DescribeJob-response-Job"></a>
Contains the configuration parameters and status for the job specified in the `Describe Job` request.
Type: [JobDescriptor](API_control_JobDescriptor.md) data type

## Errors
<a name="API_control_DescribeJob_Errors"></a>

 ** BadRequestException **

HTTP Status Code: 400

 ** InternalServiceException **

HTTP Status Code: 500

 ** NotFoundException **

HTTP Status Code: 400

 ** TooManyRequestsException **

HTTP Status Code: 400

## See Also
<a name="API_control_DescribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DescribeJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DescribeJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
