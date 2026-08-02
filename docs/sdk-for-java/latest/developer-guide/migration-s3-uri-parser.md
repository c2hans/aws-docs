---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-uri-parser.html
---

# Changes in parsing Amazon S3 URIs from version 1 to version 2
<a name="migration-s3-uri-parser"></a>

This topic details the changes in parsing Amazon S3 URIs from version 1 (v1) to version 2 (v2.).

## High-level changes
<a name="migration-3-uri-parser-api-changes"></a>

To begin parsing an S3 URI in v1, you instantiate an `AmazonS3URI` by using a constructor. In v2 you call `parseUri()` on an instance of `S3Utilities`, to return an `S3URI`.

****

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.5871}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency>  <br />        <groupId>com.amazonaws</groupId><br />        <artifactId>s3</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.27.212}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>s3</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.services.s3 | software.amazon.awssdk.services.s3 |
| Class names | [AmazonS3URI](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3URI.html) | [S3URI](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Uri.html) |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

## API changes
<a name="migration-3-uri-parser-api-changes"></a>

| Behavior | v1 | v2 |
| --- | --- | --- |
| Parse an S3 URI. |  <pre>URI uri = URI.create( "https://s3.amazonaws.com");<br /><br />AmazonS3Uri s3Uri = <br />    new AmazonS3URI(uri, false);</pre>  |  <pre>S3Client s3Client = S3Client.create();<br />S3Utilities s3Utilities =<br />    s3Client.utilities();<br /><br />S3Uri s3Uri =<br />    s3Utilities.parseUri(uri);</pre>  |
| Retrieve the bucket name from an S3 URI. |  <pre>String bucket = s3Uri.getBucket();</pre>  |  <pre>Optional<String> bucket = s3Uri.bucket();</pre>  |
| Retrieve the key. |  <pre>String key = s3Uri.getKey();</pre>  |  <pre>Optional<String> key = s3Uri.key();</pre>  |
| Retrieve the region. |  <pre>String region = s3Uri.getRegion();</pre>  |  <pre>Optional<Region> region = s3Uri.region();<br /><br />String region;<br />if (s3Uri.region().isPresent()) {<br />    region = s3Uri.region().get().id();<br />}</pre>  |
| Retrieve whether the S3 URI is path style. |  <pre>boolean isPathStyle = s3Uri.isPathStyle();</pre>  |  <pre>boolean isPathStyle = s3Uri.isPathStyle();</pre>  |
| Retrieve the version ID. |  <pre>String versionId = s3Uri.getVersionId();</pre>  |  <pre>Optional<String> versionId = <br />    s3Uri.firstMatchingRawQueryParameter("versionId");</pre>  |
| Retrieve the query parameters. | N/A |  <pre>Map<String, List<String>> queryParams =<br />    s3Uri.rawQueryParameters();</pre>  |

### Behavior changes
<a name="migration-s3-uri-parser-behavior-changes"></a>

#### URL encoding
<a name="migration-s3-uri-parser-behavior-changes-URLencoding"></a>

v1 provides the option to pass in a flag to specify whether the URI should be URL encoded. The default value is `true`.

In v2, URL encoding is not supported. If you work with object keys or query parameters that have reserved or unsafe characters, you must URL encode them. For example you need to replace a whitespace `" "` with `%20`.
