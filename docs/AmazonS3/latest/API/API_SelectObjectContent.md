---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html
---

# SelectObjectContent
<a name="API_SelectObjectContent"></a>

**Note**
This operation is not supported for directory buckets.

This action filters the contents of an Amazon S3 object based on a simple structured query language (SQL) statement. In the request, along with the SQL expression, you must also specify a data serialization format (JSON, CSV, or Apache Parquet) of the object. Amazon S3 uses this format to parse object data into records, and returns only records that match the specified SQL expression. You must also specify the data serialization format for the response.

This functionality is not supported for Amazon S3 on Outposts.

For more information about Amazon S3 Select, see [Selecting Content from Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html) and [SELECT Command](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-glacier-select-sql-reference-select.html) in the *Amazon S3 User Guide*.

Permissions
You must have the `s3:GetObject` permission for this operation. Amazon S3 Select does not support anonymous access. For more information about permissions, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) in the *Amazon S3 User Guide*.

Object Data Formats
You can use Amazon S3 Select to query objects that have the following format properties:
+  *CSV, JSON, and Parquet* - Objects must be in CSV, JSON, or Parquet format.
+  *UTF-8* - UTF-8 is the only encoding type Amazon S3 Select supports.
+  *GZIP or BZIP2* - CSV and JSON files can be compressed using GZIP or BZIP2. GZIP and BZIP2 are the only compression formats that Amazon S3 Select supports for CSV and JSON files. Amazon S3 Select supports columnar compression for Parquet using GZIP or Snappy. Amazon S3 Select does not support whole-object compression for Parquet objects.
+  *Server-side encryption* - Amazon S3 Select supports querying objects that are protected with server-side encryption.

  For objects that are encrypted with customer-provided encryption keys (SSE-C), you must use HTTPS, and you must use the headers that are documented in the [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html). For more information about SSE-C, see [Server-Side Encryption (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide*.

  For objects that are encrypted with Amazon S3 managed keys (SSE-S3) and AWS KMS keys (SSE-KMS), server-side encryption is handled transparently, so you don't need to specify anything. For more information about server-side encryption, including SSE-S3 and SSE-KMS, see [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) in the *Amazon S3 User Guide*.

Working with the Response Body
Given the response size is unknown, Amazon S3 Select streams the response as a series of messages and includes a `Transfer-Encoding` header with `chunked` as its value in the response. For more information, see [Appendix: SelectObjectContent Response](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTSelectObjectAppendix.html).

GetObject Support
The `SelectObjectContent` action does not support the following `GetObject` functionality. For more information, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).
+  `Range`: Although you can specify a scan range for an Amazon S3 Select request (see [SelectObjectContentRequest - ScanRange](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html#AmazonS3-SelectObjectContent-request-ScanRange) in the request parameters), you cannot specify the range of bytes of an object to return.
+ The `GLACIER`, `DEEP_ARCHIVE`, and `REDUCED_REDUNDANCY` storage classes, or the `ARCHIVE_ACCESS` and `DEEP_ARCHIVE_ACCESS` access tiers of the `INTELLIGENT_TIERING` storage class: You cannot query objects in the `GLACIER`, `DEEP_ARCHIVE`, or `REDUCED_REDUNDANCY` storage classes, nor objects in the `ARCHIVE_ACCESS` or `DEEP_ARCHIVE_ACCESS` access tiers of the `INTELLIGENT_TIERING` storage class. For more information about storage classes, see [Using Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) in the *Amazon S3 User Guide*.

Special Errors
For a list of special errors for this operation, see [List of SELECT Object Content Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#SelectObjectContentErrorCodeList)

The following operations are related to `SelectObjectContent`:
+  [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
+  [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
+  [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_SelectObjectContent_RequestSyntax"></a>

```
POST /{Key+}?select&select-type=2 HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-server-side-encryption-customer-algorithm: {{SSECustomerAlgorithm}}
x-amz-server-side-encryption-customer-key: {{SSECustomerKey}}
x-amz-server-side-encryption-customer-key-MD5: {{SSECustomerKeyMD5}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<SelectObjectContentRequest xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Expression>{{string}}</Expression>
   <ExpressionType>{{string}}</ExpressionType>
   <RequestProgress>
      <Enabled>{{boolean}}</Enabled>
   </RequestProgress>
   <InputSerialization>
      <CompressionType>{{string}}</CompressionType>
      <CSV>
         <AllowQuotedRecordDelimiter>{{boolean}}</AllowQuotedRecordDelimiter>
         <Comments>{{string}}</Comments>
         <FieldDelimiter>{{string}}</FieldDelimiter>
         <FileHeaderInfo>{{string}}</FileHeaderInfo>
         <QuoteCharacter>{{string}}</QuoteCharacter>
         <QuoteEscapeCharacter>{{string}}</QuoteEscapeCharacter>
         <RecordDelimiter>{{string}}</RecordDelimiter>
      </CSV>
      <JSON>
         <Type>{{string}}</Type>
      </JSON>
      <Parquet>
      </Parquet>
   </InputSerialization>
   <OutputSerialization>
      <CSV>
         <FieldDelimiter>{{string}}</FieldDelimiter>
         <QuoteCharacter>{{string}}</QuoteCharacter>
         <QuoteEscapeCharacter>{{string}}</QuoteEscapeCharacter>
         <QuoteFields>{{string}}</QuoteFields>
         <RecordDelimiter>{{string}}</RecordDelimiter>
      </CSV>
      <JSON>
         <RecordDelimiter>{{string}}</RecordDelimiter>
      </JSON>
   </OutputSerialization>
   <ScanRange>
      <End>{{long}}</End>
      <Start>{{long}}</Start>
   </ScanRange>
</SelectObjectContentRequest>
```

## URI Request Parameters
<a name="API_SelectObjectContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-header-Bucket"></a>
The S3 bucket.
Required: Yes

 ** [Key](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-uri-uri-Key"></a>
The object key.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-server-side-encryption-customer-algorithm](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-header-SSECustomerAlgorithm"></a>
The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created using a checksum algorithm. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide*.

 ** [x-amz-server-side-encryption-customer-key](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-header-SSECustomerKey"></a>
The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide*.

 ** [x-amz-server-side-encryption-customer-key-MD5](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-header-SSECustomerKeyMD5"></a>
The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide*.

## Request Body
<a name="API_SelectObjectContent_RequestBody"></a>

The request accepts the following data in XML format.

 ** [SelectObjectContentRequest](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-SelectObjectContentRequest"></a>
Root level tag for the SelectObjectContentRequest parameters.
Required: Yes

 ** [Expression](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-Expression"></a>
The expression that is used to query the object.
Type: String
Required: Yes

 ** [ExpressionType](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-ExpressionType"></a>
The type of the provided expression (for example, SQL).
Type: String
Valid Values: `SQL`
Required: Yes

 ** [InputSerialization](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-InputSerialization"></a>
Describes the format of the data in the object that is being queried.
Type: [InputSerialization](API_InputSerialization.md) data type
Required: Yes

 ** [OutputSerialization](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-OutputSerialization"></a>
Describes the format of the data that you want Amazon S3 to return in response.
Type: [OutputSerialization](API_OutputSerialization.md) data type
Required: Yes

 ** [RequestProgress](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-RequestProgress"></a>
Specifies if periodic request progress information should be enabled.
Type: [RequestProgress](API_RequestProgress.md) data type
Required: No

 ** [ScanRange](#API_SelectObjectContent_RequestSyntax) **   <a name="AmazonS3-SelectObjectContent-request-ScanRange"></a>
Specifies the byte range of the object to get the records from. A record is processed when its first byte is contained by the range. This parameter is optional, but when specified, it must not be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.
 `ScanRange`may be used in the following ways:
+  `<scanrange><start>50</start><end>100</end></scanrange>` - process only the records starting between the bytes 50 and 100 (inclusive, counting from zero)
+  `<scanrange><start>50</start></scanrange>` - process only the records starting after the byte 50
+  `<scanrange><end>50</end></scanrange>` - process only the records within the last 50 bytes of the file.
Type: [ScanRange](API_ScanRange.md) data type
Required: No

## Response Syntax
<a name="API_SelectObjectContent_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<Payload>
   <Records>
      <Payload>blob</Payload>
   </Records>
   <Stats>
      <Details>
         <BytesProcessed>long</BytesProcessed>
         <BytesReturned>long</BytesReturned>
         <BytesScanned>long</BytesScanned>
      </Details>
   </Stats>
   <Progress>
      <Details>
         <BytesProcessed>long</BytesProcessed>
         <BytesReturned>long</BytesReturned>
         <BytesScanned>long</BytesScanned>
      </Details>
   </Progress>
   <Cont>
   </Cont>
   <End>
   </End>
</Payload>
```

## Response Elements
<a name="API_SelectObjectContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [Payload](#API_SelectObjectContent_ResponseSyntax) **   <a name="AmazonS3-SelectObjectContent-response-Payload"></a>
Root level tag for the Payload parameters.
Required: Yes

 ** [Cont](#API_SelectObjectContent_ResponseSyntax) **   <a name="AmazonS3-SelectObjectContent-response-Cont"></a>
The Continuation Event.
Type: [ContinuationEvent](API_ContinuationEvent.md) data type

 ** [End](#API_SelectObjectContent_ResponseSyntax) **   <a name="AmazonS3-SelectObjectContent-response-End"></a>
The End Event.
Type: [EndEvent](API_EndEvent.md) data type

 ** [Progress](#API_SelectObjectContent_ResponseSyntax) **   <a name="AmazonS3-SelectObjectContent-response-Progress"></a>
The Progress Event.
Type: [ProgressEvent](API_ProgressEvent.md) data type

 ** [Records](#API_SelectObjectContent_ResponseSyntax) **   <a name="AmazonS3-SelectObjectContent-response-Records"></a>
The Records Event.
Type: [RecordsEvent](API_RecordsEvent.md) data type

 ** [Stats](#API_SelectObjectContent_ResponseSyntax) **   <a name="AmazonS3-SelectObjectContent-response-Stats"></a>
The Stats Event.
Type: [StatsEvent](API_StatsEvent.md) data type

## Examples
<a name="API_SelectObjectContent_Examples"></a>

### Example 1: CSV object
<a name="API_SelectObjectContent_Example_1"></a>

The following select request retrieves all records from an object with data stored in CSV format. The OutputSerialization element directs Amazon S3 to return results in CSV.

You can try different queries in the `Expression` element:
+ Assuming that you are not using column headers, you can identify columns using positional headers:

   `SELECT s._1, s._2 FROM S3Object s WHERE s._3 > 100`
+ If you have column headers and you set the `FileHeaderInfo` to `Use`, you can identify columns by name in the expression:

   `SELECT s.Id, s.FirstName, s.SSN FROM S3Object s`
+ You can specify functions in the SQL expression:

   `SELECT count(*) FROM S3Object s WHERE s._1 < 1`

```
POST /exampleobject.csv?select&select-type=2 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Tue, 17 Oct 2017 01:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from S3Object</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <CSV>
            <FileHeaderInfo>IGNORE</FileHeaderInfo>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
            <Comments>#</Comments>
        </CSV>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>
    </OutputSerialization>
</SelectRequest>
```

### Example
<a name="API_SelectObjectContent_Example_2"></a>

The following is a sample response.

```
HTTP/1.1 200 OK
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
Date: Tue, 17 Oct 2017 23:54:05 GMT

A series of messages
```

### Example 2: JSON object
<a name="API_SelectObjectContent_Example_3"></a>

The following select request retrieves all records from an object with data stored in JSON format. The OutputSerialization directs Amazon S3 to return results in CSV.

You can try different queries in the `Expression` element:
+ You can filter by string comparison using record keys:

   `SELECT s.country, s.city from S3Object s where s.city = 'Seattle'`
+ You can specify functions in the SQL expression:

   `SELECT count(*) FROM S3Object s`

```
POST /exampleobject.json?select&select-type=2 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Tue, 17 Oct 2017 01:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from S3Object</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <JSON>
            <Type>DOCUMENT</Type>
        </JSON>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>
    </OutputSerialization>
</SelectRequest>
```

### Example
<a name="API_SelectObjectContent_Example_4"></a>

The following is a sample response.

```
HTTP/1.1 200 OK
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
Date: Tue, 17 Oct 2017 23:54:05 GMT

A series of messages
```

### Example 3: Parquet object
<a name="API_SelectObjectContent_Example_5"></a>
+ The `InputSerialization` element describes the format of the data in the object that is being queried. It must specify `CSV`, `JSON`, or `Parquet`.
+ The `OutputSerialization ` element describes the format of the data that you want Amazon S3 to return in response to the query. It must specify `CSV`, `JSON`. Amazon S3 doesn't support outputting data in the `Parquet` format.
+ The format of the `InputSerialization` doesn't need to match the format of the `OutputSerialization`. So, for example, you can specify `JSON` in the `InputSerialization` and `CSV` in the `OutputSerialization`.

```
POST /exampleobject.parquet?select&select-type=2 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Tue, 17 Oct 2017 01:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from S3Object</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>NONE</CompressionType>
        <Parquet>
        </Parquet>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>
    </OutputSerialization>
</SelectRequest>
```

## See Also
<a name="API_SelectObjectContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/SelectObjectContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SelectObjectContent)
