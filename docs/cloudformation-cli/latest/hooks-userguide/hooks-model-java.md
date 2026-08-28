---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model-java.html
---

# Modeling custom CloudFormation Hooks using Java
<a name="hooks-model-java"></a>

Modeling custom CloudFormation Hooks involves creating a schema that defines the Hook, its properties, and their attributes. This tutorial walks you through modeling custom Hooks using Java.

## Step 1: Add project dependencies
<a name="model-hook-project-dependencies"></a>

Java based Hooks projects rely on Maven's `pom.xml` file as a dependency. Expand the following section and copy the source code into the `pom.xml` file in the root of the project.

### Hook project dependencies (pom.xml)
<a name="hook-java-dependencies"></a>

```
<?xml version="1.0" encoding="UTF-8"?>
<project
    xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.mycompany.testing.mytesthook</groupId>
    <artifactId>mycompany-testing-mytesthook-handler</artifactId>
    <name>mycompany-testing-mytesthook-handler</name>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <aws.java.sdk.version>2.16.1</aws.java.sdk.version>
        <checkstyle.version>8.36.2</checkstyle.version>
        <commons-io.version>2.8.0</commons-io.version>
        <jackson.version>2.11.3</jackson.version>
        <maven-checkstyle-plugin.version>3.1.1</maven-checkstyle-plugin.version>
        <mockito.version>3.6.0</mockito.version>
        <spotbugs.version>4.1.4</spotbugs.version>
        <spotless.version>2.5.0</spotless.version>
        <maven-javadoc-plugin.version>3.2.0</maven-javadoc-plugin.version>
        <maven-source-plugin.version>3.2.1</maven-source-plugin.version>
        <cfn.generate.args/>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>software.amazon.awssdk</groupId>
                <artifactId>bom</artifactId>
                <version>2.16.1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <!-- https://mvnrepository.com/artifact/software.amazon.cloudformation/aws-cloudformation-rpdk-java-plugin -->
        <dependency>
            <groupId>software.amazon.cloudformation</groupId>
            <artifactId>aws-cloudformation-rpdk-java-plugin</artifactId>
            <version>[2.0.0,3.0.0)</version>
        </dependency>

        <!-- AWS Java SDK v2 Dependencies -->
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>sdk-core</artifactId>
        </dependency>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>cloudformation</artifactId>
        </dependency>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>s3</artifactId>
        </dependency>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>utils</artifactId>
        </dependency>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>apache-client</artifactId>
        </dependency>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>sqs</artifactId>
        </dependency>

        <!-- Test dependency for Java Providers -->
        <dependency>
            <groupId>software.amazon.cloudformation</groupId>
            <artifactId>cloudformation-cli-java-plugin-testing-support</artifactId>
            <version>1.0.0</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-s3 -->
        <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>aws-java-sdk-s3</artifactId>
            <version>1.12.85</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/commons-io/commons-io -->
        <dependency>
            <groupId>commons-io</groupId>
            <artifactId>commons-io</artifactId>
            <version>${commons-io.version}</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.commons/commons-lang3 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
            <version>3.9</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.commons/commons-collections4 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-collections4</artifactId>
            <version>4.4</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.google.guava/guava -->
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>29.0-jre</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-cloudformation -->
        <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>aws-java-sdk-cloudformation</artifactId>
            <version>1.11.555</version>
            <scope>test</scope>
        </dependency>

        <!-- https://mvnrepository.com/artifact/commons-codec/commons-codec -->
        <dependency>
            <groupId>commons-codec</groupId>
            <artifactId>commons-codec</artifactId>
            <version>1.14</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/software.amazon.cloudformation/aws-cloudformation-resource-schema -->
        <dependency>
            <groupId>software.amazon.cloudformation</groupId>
            <artifactId>aws-cloudformation-resource-schema</artifactId>
            <version>[2.0.5, 3.0.0)</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.dataformat/jackson-databind -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>${jackson.version}</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.dataformat/jackson-dataformat-cbor -->
        <dependency>
            <groupId>com.fasterxml.jackson.dataformat</groupId>
            <artifactId>jackson-dataformat-cbor</artifactId>
            <version>${jackson.version}</version>
        </dependency>

        <dependency>
            <groupId>com.fasterxml.jackson.datatype</groupId>
            <artifactId>jackson-datatype-jsr310</artifactId>
            <version>${jackson.version}</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.module/jackson-modules-java8 -->
        <dependency>
            <groupId>com.fasterxml.jackson.module</groupId>
            <artifactId>jackson-modules-java8</artifactId>
            <version>${jackson.version}</version>
            <type>pom</type>
            <scope>runtime</scope>
        </dependency>

         <!-- https://mvnrepository.com/artifact/org.json/json -->
        <dependency>
            <groupId>org.json</groupId>
            <artifactId>json</artifactId>
            <version>20180813</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-core -->
        <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>aws-java-sdk-core</artifactId>
            <version>1.11.1034</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.amazonaws/aws-lambda-java-core -->
        <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>aws-lambda-java-core</artifactId>
            <version>1.2.0</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.amazonaws/aws-lambda-java-log4j2 -->
        <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>aws-lambda-java-log4j2</artifactId>
            <version>1.2.0</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.google.code.gson/gson -->
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.8.8</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/org.projectlombok/lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.4</version>
            <scope>provided</scope>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-api -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>2.17.1</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.17.1</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-slf4j-impl -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j-impl</artifactId>
            <version>2.17.1</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/org.assertj/assertj-core -->
        <dependency>
            <groupId>org.assertj</groupId>
            <artifactId>assertj-core</artifactId>
            <version>3.12.2</version>
            <scope>test</scope>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.5.0-M1</version>
            <scope>test</scope>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.mockito/mockito-core -->
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>3.6.0</version>
            <scope>test</scope>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.mockito/mockito-junit-jupiter -->
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-junit-jupiter</artifactId>
            <version>3.6.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <compilerArgs>
                        <arg>-Xlint:all,-options,-processing</arg>
                    </compilerArgs>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>2.3</version>
                <configuration>
                    <createDependencyReducedPom>false</createDependencyReducedPom>
                    <filters>
                        <filter>
                            <artifact>*:*</artifact>
                            <excludes>
                                <exclude>**/Log4j2Plugins.dat</exclude>
                            </excludes>
                        </filter>
                    </filters>
                </configuration>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>1.6.0</version>
                <executions>
                    <execution>
                        <id>generate</id>
                        <phase>generate-sources</phase>
                        <goals>
                            <goal>exec</goal>
                        </goals>
                        <configuration>
                            <executable>cfn</executable>
                            <commandlineArgs>generate ${cfn.generate.args}</commandlineArgs>
                            <workingDirectory>${project.basedir}</workingDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>build-helper-maven-plugin</artifactId>
                <version>3.0.0</version>
                <executions>
                    <execution>
                        <id>add-source</id>
                        <phase>generate-sources</phase>
                        <goals>
                            <goal>add-source</goal>
                        </goals>
                        <configuration>
                            <sources>
                                <source>${project.basedir}/target/generated-sources/rpdk</source>
                            </sources>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>2.4</version>
            </plugin>
            <plugin>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M3</version>
            </plugin>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>0.8.4</version>
                <configuration>
                    <excludes>
                        <exclude>**/BaseHookConfiguration*</exclude>
                        <exclude>**/BaseHookHandler*</exclude>
                        <exclude>**/HookHandlerWrapper*</exclude>
                        <exclude>**/ResourceModel*</exclude>
                        <exclude>**/TypeConfigurationModel*</exclude>
                        <exclude>**/model/**/*</exclude>
                    </excludes>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>prepare-agent</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>report</id>
                        <phase>test</phase>
                        <goals>
                            <goal>report</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>jacoco-check</id>
                        <goals>
                            <goal>check</goal>
                        </goals>
                        <configuration>
                            <rules>
                                <rule>
                                    <element>PACKAGE</element>
                                    <limits>
                                        <limit>
                                            <counter>BRANCH</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>0.8</minimum>
                                        </limit>
                                        <limit>
                                            <counter>INSTRUCTION</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>0.8</minimum>
                                        </limit>
                                    </limits>
                                </rule>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
        <resources>
            <resource>
                <directory>${project.basedir}</directory>
                <includes>
                    <include>mycompany-testing-mytesthook.json</include>
                </includes>
            </resource>
            <resource>
                <directory>${project.basedir}/target/loaded-target-schemas</directory>
                <includes>
                    <include>**/*.json</include>
                </includes>
            </resource>
        </resources>
    </build>
</project>
```

## Step 2: Generate the Hook project package
<a name="model-hook-project-package-java"></a>

Generate your Hook project package. The CloudFormation CLI creates empty handler functions that correspond to specific Hook actions in the target lifecycle as defined in the Hook specification.

```
cfn generate
```

The command returns the following output.

```
Generated files for MyCompany::Testing::MyTestHook
```

**Note**
Make sure your Lambda runtimes are up-to-date to avoid using a deprecated version. For more information, see [Updating Lambda runtimes for resource types and Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/runtime-update.html).

## Step 3: Add Hook handlers
<a name="model-hook-project-add-handler-java"></a>

Add your own Hook handler runtime code to the handlers that you choose to implement. For example, you can add the following code for logging.

```
logger.log("Internal testing Hook triggered for target: " + request.getHookContext().getTargetName());
```

The CloudFormation CLI generates a Plain Old Java Objects (Java POJO). The following are output examples generated from `AWS::S3::Bucket`.

**Example AwsS3BucketTargetModel.java**

```
package com.mycompany.testing.mytesthook.model.aws.s3.bucket;

import...

@Data
@NoArgsConstructor
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@JsonAutoDetect(fieldVisibility = Visibility.ANY, getterVisibility = Visibility.NONE, setterVisibility = Visibility.NONE)
public class AwsS3BucketTargetModel extends ResourceHookTargetModel<AwsS3Bucket> {

    @JsonIgnore
    private static final TypeReference<AwsS3Bucket> TARGET_REFERENCE =
        new TypeReference<AwsS3Bucket>() {};

    @JsonIgnore
    private static final TypeReference<AwsS3BucketTargetModel> MODEL_REFERENCE =
        new TypeReference<AwsS3BucketTargetModel>() {};

    @JsonIgnore
    public static final String TARGET_TYPE_NAME = "AWS::S3::Bucket";

    @JsonIgnore
    public TypeReference<AwsS3Bucket> getHookTargetTypeReference() {
        return TARGET_REFERENCE;
    }

    @JsonIgnore
    public TypeReference<AwsS3BucketTargetModel> getTargetModelTypeReference() {
        return MODEL_REFERENCE;
    }
}
```

**Example AwsS3Bucket.java**

```
package com.mycompany.testing.mytesthook.model.aws.s3.bucket;

import ...

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@JsonAutoDetect(fieldVisibility = Visibility.ANY, getterVisibility = Visibility.NONE, setterVisibility = Visibility.NONE)
public class AwsS3Bucket extends ResourceHookTarget {
    @JsonIgnore
    public static final String TYPE_NAME = "AWS::S3::Bucket";

    @JsonIgnore
    public static final String IDENTIFIER_KEY_ID = "/properties/Id";

    @JsonProperty("InventoryConfigurations")
    private List<InventoryConfiguration> inventoryConfigurations;

    @JsonProperty("WebsiteConfiguration")
    private WebsiteConfiguration websiteConfiguration;

    @JsonProperty("DualStackDomainName")
    private String dualStackDomainName;

    @JsonProperty("AccessControl")
    private String accessControl;

    @JsonProperty("AnalyticsConfigurations")
    private List<AnalyticsConfiguration> analyticsConfigurations;

    @JsonProperty("AccelerateConfiguration")
    private AccelerateConfiguration accelerateConfiguration;

    @JsonProperty("PublicAccessBlockConfiguration")
    private PublicAccessBlockConfiguration publicAccessBlockConfiguration;

    @JsonProperty("BucketName")
    private String bucketName;

    @JsonProperty("RegionalDomainName")
    private String regionalDomainName;

    @JsonProperty("OwnershipControls")
    private OwnershipControls ownershipControls;

    @JsonProperty("ObjectLockConfiguration")
    private ObjectLockConfiguration objectLockConfiguration;

    @JsonProperty("ObjectLockEnabled")
    private Boolean objectLockEnabled;

    @JsonProperty("LoggingConfiguration")
    private LoggingConfiguration loggingConfiguration;

    @JsonProperty("ReplicationConfiguration")
    private ReplicationConfiguration replicationConfiguration;

    @JsonProperty("Tags")
    private List<Tag> tags;

    @JsonProperty("DomainName")
    private String domainName;

    @JsonProperty("BucketEncryption")
    private BucketEncryption bucketEncryption;

    @JsonProperty("WebsiteURL")
    private String websiteURL;

    @JsonProperty("NotificationConfiguration")
    private NotificationConfiguration notificationConfiguration;

    @JsonProperty("LifecycleConfiguration")
    private LifecycleConfiguration lifecycleConfiguration;

    @JsonProperty("VersioningConfiguration")
    private VersioningConfiguration versioningConfiguration;

    @JsonProperty("MetricsConfigurations")
    private List<MetricsConfiguration> metricsConfigurations;

    @JsonProperty("IntelligentTieringConfigurations")
    private List<IntelligentTieringConfiguration> intelligentTieringConfigurations;

    @JsonProperty("CorsConfiguration")
    private CorsConfiguration corsConfiguration;

    @JsonProperty("Id")
    private String id;

    @JsonProperty("Arn")
    private String arn;

    @JsonIgnore
    public JSONObject getPrimaryIdentifier() {
        final JSONObject identifier = new JSONObject();
        if (this.getId() != null) {
            identifier.put(IDENTIFIER_KEY_ID, this.getId());
        }

        // only return the identifier if it can be used, i.e. if all components are present
        return identifier.length() == 1 ? identifier : null;
    }

    @JsonIgnore
    public List<JSONObject> getAdditionalIdentifiers() {
        final List<JSONObject> identifiers = new ArrayList<JSONObject>();
        // only return the identifiers if any can be used
        return identifiers.isEmpty() ? null : identifiers;
    }
}
```

**Example BucketEncryption.java**

```
package software.amazon.testing.mytesthook.model.aws.s3.bucket;

import ...

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonAutoDetect(fieldVisibility = Visibility.ANY, getterVisibility = Visibility.NONE, setterVisibility = Visibility.NONE)
public class BucketEncryption {
    @JsonProperty("ServerSideEncryptionConfiguration")
    private List<ServerSideEncryptionRule> serverSideEncryptionConfiguration;

}
```

**Example ServerSideEncryptionRule.java**

```
package com.mycompany.testing.mytesthook.model.aws.s3.bucket;

import ...

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonAutoDetect(fieldVisibility = Visibility.ANY, getterVisibility = Visibility.NONE, setterVisibility = Visibility.NONE)
public class ServerSideEncryptionRule {
    @JsonProperty("BucketKeyEnabled")
    private Boolean bucketKeyEnabled;

    @JsonProperty("ServerSideEncryptionByDefault")
    private ServerSideEncryptionByDefault serverSideEncryptionByDefault;

}
```

**Example ServerSideEncryptionByDefault.java**

```
package com.mycompany.testing.mytesthook.model.aws.s3.bucket;

import ...

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonAutoDetect(fieldVisibility = Visibility.ANY, getterVisibility = Visibility.NONE, setterVisibility = Visibility.NONE)
public class ServerSideEncryptionByDefault {
    @JsonProperty("SSEAlgorithm")
    private String sSEAlgorithm;

    @JsonProperty("KMSMasterKeyID")
    private String kMSMasterKeyID;

}
```

With the POJOs generated, you can now write the handlers that actually implement the Hook’s functionality. For this example, implement the `preCreate` and `preUpdate` invocation point for the handlers.

## Step 4: Implement Hook handlers
<a name="model-hook-project-code-handler-java"></a>

**Topics**
+ [Coding the API client builder](#java-code-api-client-builder)
+ [Coding the API request maker](#code-the-api-request-maker)
+ [Implementing the helper code](#implement-helper-code)
+ [Implementing the base handler](#implement-base-hook-handler)
+ [Implementing the `preCreate` handler](#implementing-precreate-handler)
+ [Coding the `preCreate` handler](#coding-the-precreate-handler)
+ [Updating the `preCreate` test](#updating-the-precreate-handler)
+ [Implementing the `preUpdate` handler](#implementing-preupdate-handler)
+ [Coding the `preUpdate` handler](#coding-preupdate-handler)
+ [Updating the `preUpdate` test](#update-the-preupdate-handler)
+ [Implementing the `preDelete` handler](#implement-the-predelete-hander)
+ [Coding the `preDelete` handler](#code-the-predelete-handler)
+ [Updating the `preDelete` handler](#update-the-predelete-handler)

### Coding the API client builder
<a name="java-code-api-client-builder"></a>

1. In your IDE, open the `ClientBuilder.java` file, located in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `ClientBuilder.java` file with the following code.
**Example ClientBuilder.java**

   ```
   package com.awscommunity.kms.encryptionsettings;

   import software.amazon.awssdk.services.ec2.Ec2Client;
   import software.amazon.cloudformation.HookLambdaWrapper;

   /**
    * Describes static HTTP clients (to consume less memory) for API calls that
    * this hook makes to a number of AWS services.
    */
   public final class ClientBuilder {

       private ClientBuilder() {
       }

       /**
        * Create an HTTP client for Amazon EC2.
        *
        * @return Ec2Client An {@link Ec2Client} object.
        */
       public static Ec2Client getEc2Client() {
           return Ec2Client.builder().httpClient(HookLambdaWrapper.HTTP_CLIENT).build();
       }
   }
   ```

### Coding the API request maker
<a name="code-the-api-request-maker"></a>

1. In your IDE, open the `Translator.java` file, located in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `Translator.java` file with the following code.
**Example Translator.java**

   ```
   package com.mycompany.testing.mytesthook;

   import software.amazon.awssdk.services.s3.model.GetBucketEncryptionRequest;
   import software.amazon.awssdk.services.s3.model.ListBucketsRequest;
   import software.amazon.awssdk.services.sqs.model.ListQueuesRequest;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

   /**
    * This class is a centralized placeholder for
    *  - api request construction
    *  - object translation to/from aws sdk
    */

   public class Translator {

       static ListBucketsRequest translateToListBucketsRequest(final HookTargetModel targetModel) {
           return ListBucketsRequest.builder().build();
       }

       static ListQueuesRequest translateToListQueuesRequest(final String nextToken) {
           return ListQueuesRequest.builder().nextToken(nextToken).build();
       }

       static ListBucketsRequest createListBucketsRequest() {
           return ListBucketsRequest.builder().build();
       }

       static ListQueuesRequest createListQueuesRequest() {
           return createListQueuesRequest(null);
       }

       static ListQueuesRequest createListQueuesRequest(final String nextToken) {
           return ListQueuesRequest.builder().nextToken(nextToken).build();
       }

       static GetBucketEncryptionRequest createGetBucketEncryptionRequest(final String bucket) {
           return GetBucketEncryptionRequest.builder().bucket(bucket).build();
       }
   }
   ```

### Implementing the helper code
<a name="implement-helper-code"></a>

1. In your IDE, open the `AbstractTestBase.java` file, located in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `AbstractTestBase.java` file with the following code.
**Example Translator.java**

   ```
   package com.mycompany.testing.mytesthook;

   import com.google.common.collect.ImmutableMap;
   import org.mockito.Mockito;
   import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
   import software.amazon.awssdk.auth.credentials.AwsSessionCredentials;
   import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
   import software.amazon.awssdk.awscore.AwsRequest;
   import software.amazon.awssdk.awscore.AwsRequestOverrideConfiguration;
   import software.amazon.awssdk.awscore.AwsResponse;
   import software.amazon.awssdk.core.SdkClient;
   import software.amazon.awssdk.core.pagination.sync.SdkIterable;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.Credentials;
   import software.amazon.cloudformation.proxy.LoggerProxy;
   import software.amazon.cloudformation.proxy.OperationStatus;
   import software.amazon.cloudformation.proxy.ProgressEvent;
   import software.amazon.cloudformation.proxy.ProxyClient;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

   import javax.annotation.Nonnull;
   import java.time.Duration;
   import java.util.concurrent.CompletableFuture;
   import java.util.function.Function;
   import java.util.function.Supplier;

   import static org.assertj.core.api.Assertions.assertThat;

   @lombok.Getter
   public class AbstractTestBase {
       protected final AwsSessionCredentials awsSessionCredential;
       protected final AwsCredentialsProvider v2CredentialsProvider;
       protected final AwsRequestOverrideConfiguration configuration;
       protected final LoggerProxy loggerProxy;
       protected final Supplier<Long> awsLambdaRuntime = () -> Duration.ofMinutes(15).toMillis();
       protected final AmazonWebServicesClientProxy proxy;
       protected final Credentials mockCredentials =
           new Credentials("mockAccessId", "mockSecretKey", "mockSessionToken");

       @lombok.Setter
       private SdkClient serviceClient;

       protected AbstractTestBase() {
           loggerProxy = Mockito.mock(LoggerProxy.class);
           awsSessionCredential = AwsSessionCredentials.create(mockCredentials.getAccessKeyId(),
               mockCredentials.getSecretAccessKey(), mockCredentials.getSessionToken());
           v2CredentialsProvider = StaticCredentialsProvider.create(awsSessionCredential);
           configuration = AwsRequestOverrideConfiguration.builder()
               .credentialsProvider(v2CredentialsProvider)
               .build();
           proxy = new AmazonWebServicesClientProxy(
               loggerProxy,
               mockCredentials,
               awsLambdaRuntime
           ) {
               @Override
               public <ClientT> ProxyClient<ClientT> newProxy(@Nonnull Supplier<ClientT> client) {
                   return new ProxyClient<ClientT>() {
                       @Override
                       public <RequestT extends AwsRequest, ResponseT extends AwsResponse>
                           ResponseT injectCredentialsAndInvokeV2(RequestT request,
                                                                  Function<RequestT, ResponseT> requestFunction) {
                           return proxy.injectCredentialsAndInvokeV2(request, requestFunction);
                       }

                       @Override
                       public <RequestT extends AwsRequest, ResponseT extends AwsResponse> CompletableFuture<ResponseT>
                           injectCredentialsAndInvokeV2Async(RequestT request, Function<RequestT, CompletableFuture<ResponseT>> requestFunction) {
                           return proxy.injectCredentialsAndInvokeV2Async(request, requestFunction);
                       }

                       @Override
                       public <RequestT extends AwsRequest, ResponseT extends AwsResponse, IterableT extends SdkIterable<ResponseT>>
                           IterableT
                           injectCredentialsAndInvokeIterableV2(RequestT request, Function<RequestT, IterableT> requestFunction) {
                           return proxy.injectCredentialsAndInvokeIterableV2(request, requestFunction);
                       }

                       @SuppressWarnings("unchecked")
                       @Override
                       public ClientT client() {
                           return (ClientT) serviceClient;
                       }
                   };
               }
           };
       }

       protected void assertResponse(final ProgressEvent<HookTargetModel, CallbackContext> response, final OperationStatus expectedStatus, final String expectedMsg) {
           assertThat(response).isNotNull();
           assertThat(response.getStatus()).isEqualTo(expectedStatus);
           assertThat(response.getCallbackContext()).isNull();
           assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
           assertThat(response.getMessage()).isNotNull();
           assertThat(response.getMessage()).isEqualTo(expectedMsg);
       }

       protected HookTargetModel createHookTargetModel(final Object resourceProperties) {
           return HookTargetModel.of(ImmutableMap.of("ResourceProperties", resourceProperties));
       }

       protected HookTargetModel createHookTargetModel(final Object resourceProperties, final Object previousResourceProperties) {
           return HookTargetModel.of(
                   ImmutableMap.of(
                       "ResourceProperties", resourceProperties,
                       "PreviousResourceProperties", previousResourceProperties
                   )
           );
       }
   }
   ```

### Implementing the base handler
<a name="implement-base-hook-handler"></a>

1. In your IDE, open the `BaseHookHandlerStd.java` file, located in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `BaseHookHandlerStd.java` file with the following code.
**Example Translator.java**

   ```
   package com.mycompany.testing.mytesthook;

   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import com.mycompany.testing.mytesthook.model.aws.sqs.queue.AwsSqsQueue;
   import software.amazon.awssdk.services.s3.S3Client;
   import software.amazon.awssdk.services.sqs.SqsClient;
   import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.Logger;
   import software.amazon.cloudformation.proxy.ProgressEvent;
   import software.amazon.cloudformation.proxy.ProxyClient;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

   public abstract class BaseHookHandlerStd extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {
       public static final String HOOK_TYPE_NAME = "MyCompany::Testing::MyTestHook";

       protected Logger logger;

       @Override
       public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
               final AmazonWebServicesClientProxy proxy,
               final HookHandlerRequest request,
               final CallbackContext callbackContext,
               final Logger logger,
               final TypeConfigurationModel typeConfiguration
       ) {
           this.logger = logger;

           final String targetName = request.getHookContext().getTargetName();

           final ProgressEvent<HookTargetModel, CallbackContext> result;
           if (AwsS3Bucket.TYPE_NAME.equals(targetName)) {
               result = handleS3BucketRequest(
                       proxy,
                       request,
                       callbackContext != null ? callbackContext : new CallbackContext(),
                       proxy.newProxy(ClientBuilder::createS3Client),
                       typeConfiguration
               );
           } else if (AwsSqsQueue.TYPE_NAME.equals(targetName)) {
               result = handleSqsQueueRequest(
                       proxy,
                       request,
                       callbackContext != null ? callbackContext : new CallbackContext(),
                       proxy.newProxy(ClientBuilder::createSqsClient),
                       typeConfiguration
               );
           } else {
               throw new UnsupportedTargetException(targetName);
           }

           log(
               String.format(
                   "Result for [%s] invocation for target [%s] returned status [%s] with message [%s]",
                   request.getHookContext().getInvocationPoint(),
                   targetName,
                   result.getStatus(),
                   result.getMessage()
               )
           );

           return result;
       }

       protected abstract ProgressEvent<HookTargetModel, CallbackContext> handleS3BucketRequest(
               final AmazonWebServicesClientProxy proxy,
               final HookHandlerRequest request,
               final CallbackContext callbackContext,
               final ProxyClient<S3Client> proxyClient,
               final TypeConfigurationModel typeConfiguration
       );

       protected abstract ProgressEvent<HookTargetModel, CallbackContext> handleSqsQueueRequest(
               final AmazonWebServicesClientProxy proxy,
               final HookHandlerRequest request,
               final CallbackContext callbackContext,
               final ProxyClient<SqsClient> proxyClient,
               final TypeConfigurationModel typeConfiguration
       );

       protected void log(final String message) {
           if (logger != null) {
               logger.log(message);
           } else {
               System.out.println(message);
           }
       }
   }
   ```

### Implementing the `preCreate` handler
<a name="implementing-precreate-handler"></a>

The `preCreate` handler verifies the server-side encryption settings for either an `AWS::S3::Bucket` or `AWS::SQS::Queue` resource.
+ For an `AWS::S3::Bucket` resource, the Hook will only pass if the following is true:
  + The Amazon S3 bucket encryption is set.
  + The Amazon S3 bucket key is enabled for the bucket.
  + The encryption algorithm set for the Amazon S3 bucket is the correct algorithm required.
  + The AWS Key Management Service key ID is set.
+ For an `AWS::SQS::Queue` resource, the Hook will only pass if the following is true:
  + The AWS Key Management Service key ID is set.

### Coding the `preCreate` handler
<a name="coding-the-precreate-handler"></a>

1. In your IDE, open the `PreCreateHookHandler.java` file, located in the `src/main/java/software/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `PreCreateHookHandler.java` file with the following code.

   ```
   package com.mycompany.testing.mytesthook;

   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3BucketTargetModel;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.BucketEncryption;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionByDefault;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionRule;
   import com.mycompany.testing.mytesthook.model.aws.sqs.queue.AwsSqsQueue;
   import com.mycompany.testing.mytesthook.model.aws.sqs.queue.AwsSqsQueueTargetModel;
   import org.apache.commons.collections.CollectionUtils;
   import org.apache.commons.lang3.StringUtils;
   import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
   import software.amazon.cloudformation.proxy.HandlerErrorCode;
   import software.amazon.cloudformation.proxy.Logger;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.hook.HookStatus;
   import software.amazon.cloudformation.proxy.hook.HookProgressEvent;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

   import java.util.List;

   public class PreCreateHookHandler extends BaseHookHandler<TypeConfigurationModel, CallbackContext> {

       @Override
       public HookProgressEvent<CallbackContext> handleRequest(
           final AmazonWebServicesClientProxy proxy,
           final HookHandlerRequest request,
           final CallbackContext callbackContext,
           final Logger logger,
           final TypeConfigurationModel typeConfiguration) {

           final String targetName = request.getHookContext().getTargetName();
           if ("AWS::S3::Bucket".equals(targetName)) {
               final ResourceHookTargetModel<AwsS3Bucket> targetModel = request.getHookContext().getTargetModel(AwsS3BucketTargetModel.class);

               final AwsS3Bucket bucket = targetModel.getResourceProperties();
               final String encryptionAlgorithm = typeConfiguration.getEncryptionAlgorithm();

               return validateS3BucketEncryption(bucket, encryptionAlgorithm);

           } else if ("AWS::SQS::Queue".equals(targetName)) {
               final ResourceHookTargetModel<AwsSqsQueue> targetModel = request.getHookContext().getTargetModel(AwsSqsQueueTargetModel.class);

               final AwsSqsQueue queue = targetModel.getResourceProperties();
               return validateSQSQueueEncryption(queue);
           } else {
               throw new UnsupportedTargetException(targetName);
           }
       }

       private HookProgressEvent<CallbackContext> validateS3BucketEncryption(final AwsS3Bucket bucket, final String requiredEncryptionAlgorithm) {
           HookStatus resultStatus = null;
           String resultMessage = null;

           if (bucket != null) {
               final BucketEncryption bucketEncryption = bucket.getBucketEncryption();
               if (bucketEncryption != null) {
                   final List<ServerSideEncryptionRule> serverSideEncryptionRules = bucketEncryption.getServerSideEncryptionConfiguration();
                   if (CollectionUtils.isNotEmpty(serverSideEncryptionRules)) {
                       for (final ServerSideEncryptionRule rule : serverSideEncryptionRules) {
                           final Boolean bucketKeyEnabled = rule.getBucketKeyEnabled();
                           if (bucketKeyEnabled) {
                               final ServerSideEncryptionByDefault serverSideEncryptionByDefault = rule.getServerSideEncryptionByDefault();

                               final String encryptionAlgorithm = serverSideEncryptionByDefault.getSSEAlgorithm();
                               final String kmsKeyId = serverSideEncryptionByDefault.getKMSMasterKeyID(); // "KMSMasterKeyID" is name of the property for an AWS::S3::Bucket;

                               if (!StringUtils.equals(encryptionAlgorithm, requiredEncryptionAlgorithm) && StringUtils.isBlank(kmsKeyId)) {
                                   resultStatus = HookStatus.FAILED;
                                   resultMessage = "KMS Key ID not set and SSE Encryption Algorithm is incorrect for bucket with name: " + bucket.getBucketName();
                               } else if (!StringUtils.equals(encryptionAlgorithm, requiredEncryptionAlgorithm)) {
                                   resultStatus = HookStatus.FAILED;
                                   resultMessage = "SSE Encryption Algorithm is incorrect for bucket with name: " + bucket.getBucketName();
                               } else if (StringUtils.isBlank(kmsKeyId)) {
                                   resultStatus = HookStatus.FAILED;
                                   resultMessage = "KMS Key ID not set for bucket with name: " + bucket.getBucketName();
                               } else {
                                   resultStatus = HookStatus.SUCCESS;
                                   resultMessage = "Successfully invoked PreCreateHookHandler for target: AWS::S3::Bucket";
                               }
                           } else {
                               resultStatus = HookStatus.FAILED;
                               resultMessage = "Bucket key not enabled for bucket with name: " + bucket.getBucketName();
                           }

                           if (resultStatus == HookStatus.FAILED) {
                               break;
                           }
                       }
                   } else {
                       resultStatus = HookStatus.FAILED;
                       resultMessage = "No SSE Encryption configurations for bucket with name: " + bucket.getBucketName();
                   }
               } else {
                   resultStatus = HookStatus.FAILED;
                   resultMessage = "Bucket Encryption not enabled for bucket with name: " + bucket.getBucketName();
               }
           } else {
               resultStatus = HookStatus.FAILED;
               resultMessage = "Resource properties for S3 Bucket target model are empty";
           }

           return HookProgressEvent.<CallbackContext>builder()
                   .status(resultStatus)
                   .message(resultMessage)
                   .errorCode(resultStatus == HookStatus.FAILED ? HandlerErrorCode.ResourceConflict : null)
                   .build();
       }

       private HookProgressEvent<CallbackContext> validateSQSQueueEncryption(final AwsSqsQueue queue) {
           if (queue == null) {
               return HookProgressEvent.<CallbackContext>builder()
                       .status(HookStatus.FAILED)
                       .message("Resource properties for SQS Queue target model are empty")
                       .errorCode(HandlerErrorCode.ResourceConflict)
                       .build();
           }

           final String kmsKeyId = queue.getKmsMasterKeyId(); // "KmsMasterKeyId" is name of the property for an AWS::SQS::Queue
           if (StringUtils.isBlank(kmsKeyId)) {
               return HookProgressEvent.<CallbackContext>builder()
                       .status(HookStatus.FAILED)
                       .message("Server side encryption turned off for queue with name: " + queue.getQueueName())
                       .errorCode(HandlerErrorCode.ResourceConflict)
                       .build();
           }

           return HookProgressEvent.<CallbackContext>builder()
                       .status(HookStatus.SUCCESS)
                       .message("Successfully invoked PreCreateHookHandler for target: AWS::SQS::Queue")
                       .build();
       }
   }
   ```

### Updating the `preCreate` test
<a name="updating-the-precreate-handler"></a>

1. In your IDE, open the `PreCreateHandlerTest.java` file, located in the `src/test/java/software/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of `PreCreateHandlerTest.java` file with the following code.

   ```
   package com.mycompany.testing.mytesthook;

   import com.google.common.collect.ImmutableMap;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.BucketEncryption;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionByDefault;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionRule;
   import com.mycompany.testing.mytesthook.model.aws.sqs.queue.AwsSqsQueue;
   import org.junit.jupiter.api.BeforeEach;
   import org.junit.jupiter.api.Test;
   import org.junit.jupiter.api.extension.ExtendWith;
   import org.mockito.Mock;
   import org.mockito.junit.jupiter.MockitoExtension;
   import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.HandlerErrorCode;
   import software.amazon.cloudformation.proxy.Logger;
   import software.amazon.cloudformation.proxy.hook.HookContext;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.HookProgressEvent;
   import software.amazon.cloudformation.proxy.hook.HookStatus;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

   import java.util.Collections;
   import java.util.Map;

   import static org.assertj.core.api.Assertions.assertThat;
   import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
   import static org.mockito.Mockito.mock;

   @ExtendWith(MockitoExtension.class)
   public class PreCreateHookHandlerTest {

       @Mock
       private AmazonWebServicesClientProxy proxy;

       @Mock
       private Logger logger;

       @BeforeEach
       public void setup() {
           proxy = mock(AmazonWebServicesClientProxy.class);
           logger = mock(Logger.class);
       }

       @Test
       public void handleRequest_awsSqsQueueSuccess() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final AwsSqsQueue queue = buildSqsQueue("MyQueue", "KmsKey");
           final HookTargetModel targetModel = createHookTargetModel(queue);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::SQS::Queue").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.SUCCESS, "Successfully invoked PreCreateHookHandler for target: AWS::SQS::Queue");
       }

       @Test
       public void handleRequest_awsS3BucketSuccess() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final AwsS3Bucket bucket = buildAwsS3Bucket("amzn-s3-demo-bucket", true, "AES256", "KmsKey");
           final HookTargetModel targetModel = createHookTargetModel(bucket);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.SUCCESS, "Successfully invoked PreCreateHookHandler for target: AWS::S3::Bucket");
       }

       @Test
       public void handleRequest_awsS3BucketFail_bucketKeyNotEnabled() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final AwsS3Bucket bucket = buildAwsS3Bucket("amzn-s3-demo-bucket", false, "AES256", "KmsKey");
           final HookTargetModel targetModel = createHookTargetModel(bucket);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.FAILED, "Bucket key not enabled for bucket with name: amzn-s3-demo-bucket");
       }

       @Test
       public void handleRequest_awsS3BucketFail_incorrectSSEEncryptionAlgorithm() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final AwsS3Bucket bucket = buildAwsS3Bucket("amzn-s3-demo-bucket", true, "SHA512", "KmsKey");
           final HookTargetModel targetModel = createHookTargetModel(bucket);
          final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.FAILED, "SSE Encryption Algorithm is incorrect for bucket with name: amzn-s3-demo-bucket");
       }

       @Test
       public void handleRequest_awsS3BucketFail_kmsKeyIdNotSet() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final AwsS3Bucket bucket = buildAwsS3Bucket("amzn-s3-demo-bucket", true, "AES256", null);
           final HookTargetModel targetModel = createHookTargetModel(bucket);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.FAILED, "KMS Key ID not set for bucket with name: amzn-s3-demo-bucket");
       }

       @Test
       public void handleRequest_awsSqsQueueFail_serverSideEncryptionOff() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final AwsSqsQueue queue = buildSqsQueue("MyQueue", null);
           final HookTargetModel targetModel = createHookTargetModel(queue);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::SQS::Queue").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.FAILED, "Server side encryption turned off for queue with name: MyQueue");
       }

       @Test
       public void handleRequest_unsupportedTarget() {
           final PreCreateHookHandler handler = new PreCreateHookHandler();

           final Map<String, Object> unsupportedTarget = ImmutableMap.of("ResourceName", "MyUnsupportedTarget");
           final HookTargetModel targetModel = createHookTargetModel(unsupportedTarget);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::Unsupported::Target").targetModel(targetModel).build())
               .build();

           assertThatExceptionOfType(UnsupportedTargetException.class)
                   .isThrownBy(() -> handler.handleRequest(proxy, request, null, logger, typeConfiguration))
                   .withMessageContaining("Unsupported target")
                   .withMessageContaining("AWS::Unsupported::Target")
                   .satisfies(e -> assertThat(e.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest));
       }

       private void assertResponse(final HookProgressEvent<CallbackContext> response, final HookStatus expectedStatus, final String expectedErrorMsg) {
           assertThat(response).isNotNull();
           assertThat(response.getStatus()).isEqualTo(expectedStatus);
           assertThat(response.getCallbackContext()).isNull();
           assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
           assertThat(response.getMessage()).isNotNull();
           assertThat(response.getMessage()).isEqualTo(expectedErrorMsg);
       }

       private HookTargetModel createHookTargetModel(final Object resourceProperties) {
           return HookTargetModel.of(ImmutableMap.of("ResourceProperties", resourceProperties));
       }

       @SuppressWarnings("SameParameterValue")
       private AwsSqsQueue buildSqsQueue(final String queueName, final String kmsKeyId) {
           return AwsSqsQueue.builder()
                   .queueName(queueName)
                   .kmsMasterKeyId(kmsKeyId) // "KmsMasterKeyId" is name of the property for an AWS::SQS::Queue
                   .build();
       }

       @SuppressWarnings("SameParameterValue")
       private AwsS3Bucket buildAwsS3Bucket(
               final String bucketName,
               final Boolean bucketKeyEnabled,
               final String sseAlgorithm,
               final String kmsKeyId
       ) {
           return AwsS3Bucket.builder()
                   .bucketName(bucketName)
                   .bucketEncryption(
                       BucketEncryption.builder()
                           .serverSideEncryptionConfiguration(
                               Collections.singletonList(
                                   ServerSideEncryptionRule.builder()
                                       .bucketKeyEnabled(bucketKeyEnabled)
                                       .serverSideEncryptionByDefault(
                                           ServerSideEncryptionByDefault.builder()
                                               .sSEAlgorithm(sseAlgorithm)
                                               .kMSMasterKeyID(kmsKeyId) // "KMSMasterKeyID" is name of the property for an AWS::S3::Bucket
                                               .build()
                                       ).build()
                               )
                           ).build()
                   ).build();
       }
   }
   ```

### Implementing the `preUpdate` handler
<a name="implementing-preupdate-handler"></a>

Implement a `preUpdate` handler, which initiates before the update operations for all specified targets in the handler. The `preUpdate` handler accomplishes the following:
+ For an `AWS::S3::Bucket` resource, the Hook will only pass if the following is true:
  + The bucket encryption algorithm for an Amazon S3 bucket hasn't been modified.

### Coding the `preUpdate` handler
<a name="coding-preupdate-handler"></a>

1. In your IDE, open the `PreUpdateHookHandler.java` file, located in the `src/main/java/software/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `PreUpdateHookHandler.java` file with the following code.

   ```
   package com.mycompany.testing.mytesthook;

   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3BucketTargetModel;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionRule;
   import org.apache.commons.lang3.StringUtils;
   import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
   import software.amazon.cloudformation.proxy.HandlerErrorCode;
   import software.amazon.cloudformation.proxy.Logger;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.hook.HookStatus;
   import software.amazon.cloudformation.proxy.hook.HookProgressEvent;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

   import java.util.List;

   public class PreUpdateHookHandler extends BaseHookHandler<TypeConfigurationModel, CallbackContext> {

       @Override
       public HookProgressEvent<CallbackContext> handleRequest(
           final AmazonWebServicesClientProxy proxy,
           final HookHandlerRequest request,
           final CallbackContext callbackContext,
           final Logger logger,
           final TypeConfigurationModel typeConfiguration) {

           final String targetName = request.getHookContext().getTargetName();
           if ("AWS::S3::Bucket".equals(targetName)) {
               final ResourceHookTargetModel<AwsS3Bucket> targetModel = request.getHookContext().getTargetModel(AwsS3BucketTargetModel.class);

               final AwsS3Bucket bucketProperties = targetModel.getResourceProperties();
               final AwsS3Bucket previousBucketProperties = targetModel.getPreviousResourceProperties();

               return validateBucketEncryptionRulesNotUpdated(bucketProperties, previousBucketProperties);
           } else {
               throw new UnsupportedTargetException(targetName);
           }
       }

       private HookProgressEvent<CallbackContext> validateBucketEncryptionRulesNotUpdated(final AwsS3Bucket resourceProperties, final AwsS3Bucket previousResourceProperties) {
           final List<ServerSideEncryptionRule> bucketEncryptionConfigs = resourceProperties.getBucketEncryption().getServerSideEncryptionConfiguration();
           final List<ServerSideEncryptionRule> previousBucketEncryptionConfigs = previousResourceProperties.getBucketEncryption().getServerSideEncryptionConfiguration();

           if (bucketEncryptionConfigs.size() != previousBucketEncryptionConfigs.size()) {
               return HookProgressEvent.<CallbackContext>builder()
                       .status(HookStatus.FAILED)
                       .errorCode(HandlerErrorCode.NotUpdatable)
                       .message(
                           String.format(
                               "Current number of bucket encryption configs does not match previous. Current has %d configs while previously there were %d configs",
                               bucketEncryptionConfigs.size(),
                               previousBucketEncryptionConfigs.size()
                           )
                       ).build();
           }

           for (int i = 0; i < bucketEncryptionConfigs.size(); ++i) {
               final String currentEncryptionAlgorithm = bucketEncryptionConfigs.get(i).getServerSideEncryptionByDefault().getSSEAlgorithm();
               final String previousEncryptionAlgorithm = previousBucketEncryptionConfigs.get(i).getServerSideEncryptionByDefault().getSSEAlgorithm();

               if (!StringUtils.equals(currentEncryptionAlgorithm, previousEncryptionAlgorithm)) {
                   return HookProgressEvent.<CallbackContext>builder()
                       .status(HookStatus.FAILED)
                       .errorCode(HandlerErrorCode.NotUpdatable)
                       .message(
                           String.format(
                               "Bucket Encryption algorithm can not be changed once set. The encryption algorithm was changed to '%s' from '%s'.",
                               currentEncryptionAlgorithm,
                               previousEncryptionAlgorithm
                           )
                       )
                       .build();
               }
           }

           return HookProgressEvent.<CallbackContext>builder()
                       .status(HookStatus.SUCCESS)
                       .message("Successfully invoked PreUpdateHookHandler for target: AWS::SQS::Queue")
                       .build();
       }
   }
   ```

### Updating the `preUpdate` test
<a name="update-the-preupdate-handler"></a>

1. In your IDE, open the `PreUpdateHandlerTest.java` file in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `PreUpdateHandlerTest.java` file with the following code.

   ```
   package com.mycompany.testing.mytesthook;

   import com.google.common.collect.ImmutableMap;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.BucketEncryption;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionByDefault;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.ServerSideEncryptionRule;
   import org.junit.jupiter.api.BeforeEach;
   import org.junit.jupiter.api.Test;
   import org.junit.jupiter.api.extension.ExtendWith;
   import org.mockito.Mock;
   import org.mockito.junit.jupiter.MockitoExtension;
   import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.HandlerErrorCode;
   import software.amazon.cloudformation.proxy.Logger;
   import software.amazon.cloudformation.proxy.hook.HookContext;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.HookProgressEvent;
   import software.amazon.cloudformation.proxy.hook.HookStatus;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

   import java.util.Arrays;
   import java.util.stream.Stream;

   import static org.assertj.core.api.Assertions.assertThat;
   import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
   import static org.mockito.Mockito.mock;

   @ExtendWith(MockitoExtension.class)
   public class PreUpdateHookHandlerTest {

       @Mock
       private AmazonWebServicesClientProxy proxy;

       @Mock
       private Logger logger;

       @BeforeEach
       public void setup() {
           proxy = mock(AmazonWebServicesClientProxy.class);
           logger = mock(Logger.class);
       }

       @Test
       public void handleRequest_awsS3BucketSuccess() {
           final PreUpdateHookHandler handler = new PreUpdateHookHandler();

           final ServerSideEncryptionRule serverSideEncryptionRule = buildServerSideEncryptionRule("AES256");
           final AwsS3Bucket resourceProperties = buildAwsS3Bucket("amzn-s3-demo-bucket", serverSideEncryptionRule);
           final AwsS3Bucket previousResourceProperties = buildAwsS3Bucket("amzn-s3-demo-bucket", serverSideEncryptionRule);
           final HookTargetModel targetModel = createHookTargetModel(resourceProperties, previousResourceProperties);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.SUCCESS, "Successfully invoked PreUpdateHookHandler for target: AWS::SQS::Queue");
       }

       @Test
       public void handleRequest_awsS3BucketFail_bucketEncryptionConfigsDontMatch() {
           final PreUpdateHookHandler handler = new PreUpdateHookHandler();

           final ServerSideEncryptionRule[] serverSideEncryptionRules = Stream.of("AES256", "SHA512", "AES32")
                   .map(this::buildServerSideEncryptionRule)
                   .toArray(ServerSideEncryptionRule[]::new);

           final AwsS3Bucket resourceProperties = buildAwsS3Bucket("amzn-s3-demo-bucket", serverSideEncryptionRules[0]);
           final AwsS3Bucket previousResourceProperties = buildAwsS3Bucket("amzn-s3-demo-bucket", serverSideEncryptionRules);
           final HookTargetModel targetModel = createHookTargetModel(resourceProperties, previousResourceProperties);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.FAILED, "Current number of bucket encryption configs does not match previous. Current has 1 configs while previously there were 3 configs");
       }

       @Test
       public void handleRequest_awsS3BucketFail_bucketEncryptionAlgorithmDoesNotMatch() {
           final PreUpdateHookHandler handler = new PreUpdateHookHandler();

           final AwsS3Bucket resourceProperties = buildAwsS3Bucket("amzn-s3-demo-bucket", buildServerSideEncryptionRule("SHA512"));
           final AwsS3Bucket previousResourceProperties = buildAwsS3Bucket("amzn-s3-demo-bucket", buildServerSideEncryptionRule("AES256"));
           final HookTargetModel targetModel = createHookTargetModel(resourceProperties, previousResourceProperties);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(targetModel).build())
               .build();

           final HookProgressEvent<CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
           assertResponse(response, HookStatus.FAILED, String.format("Bucket Encryption algorithm can not be changed once set. The encryption algorithm was changed to '%s' from '%s'.", "SHA512", "AES256"));
       }

       @Test
       public void handleRequest_unsupportedTarget() {
           final PreUpdateHookHandler handler = new PreUpdateHookHandler();

           final Object resourceProperties = ImmutableMap.of("FileSizeLimit", 256);
           final Object previousResourceProperties = ImmutableMap.of("FileSizeLimit", 512);
           final HookTargetModel targetModel = createHookTargetModel(resourceProperties, previousResourceProperties);
           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().encryptionAlgorithm("AES256").build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
               .hookContext(HookContext.builder().targetName("AWS::Unsupported::Target").targetModel(targetModel).build())
               .build();

           assertThatExceptionOfType(UnsupportedTargetException.class)
                   .isThrownBy(() -> handler.handleRequest(proxy, request, null, logger, typeConfiguration))
                   .withMessageContaining("Unsupported target")
                   .withMessageContaining("AWS::Unsupported::Target")
                   .satisfies(e -> assertThat(e.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest));
       }

       private void assertResponse(final HookProgressEvent<CallbackContext> response, final HookStatus expectedStatus, final String expectedErrorMsg) {
           assertThat(response).isNotNull();
           assertThat(response.getStatus()).isEqualTo(expectedStatus);
           assertThat(response.getCallbackContext()).isNull();
           assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
           assertThat(response.getMessage()).isNotNull();
           assertThat(response.getMessage()).isEqualTo(expectedErrorMsg);
       }

       private HookTargetModel createHookTargetModel(final Object resourceProperties, final Object previousResourceProperties) {
           return HookTargetModel.of(
                   ImmutableMap.of(
                       "ResourceProperties", resourceProperties,
                       "PreviousResourceProperties", previousResourceProperties
                   )
           );
       }

       @SuppressWarnings("SameParameterValue")
       private AwsS3Bucket buildAwsS3Bucket(
               final String bucketName,
               final ServerSideEncryptionRule ...serverSideEncryptionRules
               ) {
           return AwsS3Bucket.builder()
                   .bucketName(bucketName)
                   .bucketEncryption(
                       BucketEncryption.builder()
                           .serverSideEncryptionConfiguration(
                                   Arrays.asList(serverSideEncryptionRules)
                           ).build()
                   ).build();
       }

       private ServerSideEncryptionRule buildServerSideEncryptionRule(final String encryptionAlgorithm) {
           return ServerSideEncryptionRule.builder()
                   .bucketKeyEnabled(true)
                   .serverSideEncryptionByDefault(
                           ServerSideEncryptionByDefault.builder()
                                   .sSEAlgorithm(encryptionAlgorithm)
                                   .build()
                   ).build();
       }
   }
   ```

### Implementing the `preDelete` handler
<a name="implement-the-predelete-hander"></a>

Implement a `preDelete` handler, which initiates before the delete operations for all specified targets in the handler. The `preDelete` handler accomplishes the following:
+ For an `AWS::S3::Bucket` resource, the Hook will only pass if the following is true:
  + Verifies that the minimum required complaint resources will exist in the account after delete the resource.
  + The minimum required complaint resources amount is set in the Hook’s type configuration.

### Coding the `preDelete` handler
<a name="code-the-predelete-handler"></a>

1. In your IDE, open the `PreDeleteHookHandler.java` file in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `PreDeleteHookHandler.java` file with the following code.

   ```
   package com.mycompany.testing.mytesthook;

   import com.google.common.annotations.VisibleForTesting;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3BucketTargetModel;
   import com.mycompany.testing.mytesthook.model.aws.sqs.queue.AwsSqsQueue;
   import com.mycompany.testing.mytesthook.model.aws.sqs.queue.AwsSqsQueueTargetModel;
   import org.apache.commons.lang3.StringUtils;
   import org.apache.commons.lang3.math.NumberUtils;
   import software.amazon.awssdk.services.cloudformation.CloudFormationClient;
   import software.amazon.awssdk.services.cloudformation.model.CloudFormationException;
   import software.amazon.awssdk.services.cloudformation.model.DescribeStackResourceRequest;
   import software.amazon.awssdk.services.s3.S3Client;
   import software.amazon.awssdk.services.s3.model.Bucket;
   import software.amazon.awssdk.services.s3.model.S3Exception;
   import software.amazon.awssdk.services.sqs.SqsClient;
   import software.amazon.awssdk.services.sqs.model.GetQueueAttributesRequest;
   import software.amazon.awssdk.services.sqs.model.GetQueueUrlRequest;
   import software.amazon.awssdk.services.sqs.model.ListQueuesRequest;
   import software.amazon.awssdk.services.sqs.model.ListQueuesResponse;
   import software.amazon.awssdk.services.sqs.model.QueueAttributeName;
   import software.amazon.awssdk.services.sqs.model.SqsException;
   import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
   import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
   import software.amazon.cloudformation.proxy.HandlerErrorCode;
   import software.amazon.cloudformation.proxy.OperationStatus;
   import software.amazon.cloudformation.proxy.ProgressEvent;
   import software.amazon.cloudformation.proxy.ProxyClient;
   import software.amazon.cloudformation.proxy.hook.HookContext;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
   import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

   import java.util.ArrayList;
   import java.util.Collection;
   import java.util.HashSet;
   import java.util.List;
   import java.util.Objects;
   import java.util.stream.Collectors;

   public class PreDeleteHookHandler extends BaseHookHandlerStd {

       private ProxyClient<S3Client> s3Client;
       private ProxyClient<SqsClient> sqsClient;

       @Override
       protected ProgressEvent<HookTargetModel, CallbackContext> handleS3BucketRequest(
               final AmazonWebServicesClientProxy proxy,
               final HookHandlerRequest request,
               final CallbackContext callbackContext,
               final ProxyClient<S3Client> proxyClient,
               final TypeConfigurationModel typeConfiguration
       ) {
           final HookContext hookContext = request.getHookContext();
           final String targetName = hookContext.getTargetName();
           if (!AwsS3Bucket.TYPE_NAME.equals(targetName)) {
               throw new RuntimeException(String.format("Request target type [%s] is not 'AWS::S3::Bucket'", targetName));
           }
           this.s3Client = proxyClient;

           final String encryptionAlgorithm = typeConfiguration.getEncryptionAlgorithm();
           final int minBuckets = NumberUtils.toInt(typeConfiguration.getMinBuckets());

           final ResourceHookTargetModel<AwsS3Bucket> targetModel = hookContext.getTargetModel(AwsS3BucketTargetModel.class);
           final List<String> buckets = listBuckets().stream()
                   .filter(b -> !StringUtils.equals(b, targetModel.getResourceProperties().getBucketName()))
                   .collect(Collectors.toList());

           final List<String> compliantBuckets = new ArrayList<>();
           for (final String bucket : buckets) {
               if (getBucketSSEAlgorithm(bucket).contains(encryptionAlgorithm)) {
                   compliantBuckets.add(bucket);
               }

               if (compliantBuckets.size() >= minBuckets) {
                   return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                           .status(OperationStatus.SUCCESS)
                           .message("Successfully invoked PreDeleteHookHandler for target: AWS::S3::Bucket")
                           .build();
               }
           }

           return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                   .status(OperationStatus.FAILED)
                   .errorCode(HandlerErrorCode.NonCompliant)
                   .message(String.format("Failed to meet minimum of [%d] encrypted buckets.", minBuckets))
                   .build();
       }

       @Override
       protected ProgressEvent<HookTargetModel, CallbackContext> handleSqsQueueRequest(
               final AmazonWebServicesClientProxy proxy,
               final HookHandlerRequest request,
               final CallbackContext callbackContext,
               final ProxyClient<SqsClient> proxyClient,
               final TypeConfigurationModel typeConfiguration
       ) {
           final HookContext hookContext = request.getHookContext();
           final String targetName = hookContext.getTargetName();
           if (!AwsSqsQueue.TYPE_NAME.equals(targetName)) {
               throw new RuntimeException(String.format("Request target type [%s] is not 'AWS::SQS::Queue'", targetName));
           }
           this.sqsClient = proxyClient;
           final int minQueues = NumberUtils.toInt(typeConfiguration.getMinQueues());

           final ResourceHookTargetModel<AwsSqsQueue> targetModel = hookContext.getTargetModel(AwsSqsQueueTargetModel.class);

           final String queueName = Objects.toString(targetModel.getResourceProperties().get("QueueName"), null);

           String targetQueueUrl = null;
           if (queueName != null) {
               try {
                   targetQueueUrl = sqsClient.injectCredentialsAndInvokeV2(
                           GetQueueUrlRequest.builder().queueName(
                                   queueName
                           ).build(),
                           sqsClient.client()::getQueueUrl
                   ).queueUrl();
               } catch (SqsException e) {
                   log(String.format("Error while calling GetQueueUrl API for queue name [%s]: %s", queueName, e.getMessage()));
               }
           } else {
               log("Queue name is empty, attempting to get queue's physical ID");
               try {
                   final ProxyClient<CloudFormationClient> cfnClient = proxy.newProxy(ClientBuilder::createCloudFormationClient);
                   targetQueueUrl = cfnClient.injectCredentialsAndInvokeV2(
                           DescribeStackResourceRequest.builder()
                                   .stackName(hookContext.getTargetLogicalId())
                                   .logicalResourceId(hookContext.getTargetLogicalId())
                                   .build(),
                           cfnClient.client()::describeStackResource
                   ).stackResourceDetail().physicalResourceId();
               } catch (CloudFormationException e) {
                   log(String.format("Error while calling DescribeStackResource API for queue name: %s", e.getMessage()));
               }
           }

           // Creating final variable for the filter lambda
           final String finalTargetQueueUrl = targetQueueUrl;

           final List<String> compliantQueues = new ArrayList<>();

           String nextToken = null;
           do {
               final ListQueuesRequest req = Translator.createListQueuesRequest(nextToken);
               final ListQueuesResponse res = sqsClient.injectCredentialsAndInvokeV2(req, sqsClient.client()::listQueues);
               final List<String> queueUrls = res.queueUrls().stream()
                       .filter(q -> !StringUtils.equals(q, finalTargetQueueUrl))
                       .collect(Collectors.toList());

               for (final String queueUrl : queueUrls) {
                   if (isQueueEncrypted(queueUrl)) {
                       compliantQueues.add(queueUrl);
                   }

                   if (compliantQueues.size() >= minQueues) {
                       return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                           .status(OperationStatus.SUCCESS)
                           .message("Successfully invoked PreDeleteHookHandler for target: AWS::SQS::Queue")
                           .build();
                   }
                   nextToken = res.nextToken();
               }
           } while (nextToken != null);

           return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                   .status(OperationStatus.FAILED)
                   .errorCode(HandlerErrorCode.NonCompliant)
                   .message(String.format("Failed to meet minimum of [%d] encrypted queues.", minQueues))
                   .build();
       }

       private List<String> listBuckets() {
           try {
               return s3Client.injectCredentialsAndInvokeV2(Translator.createListBucketsRequest(), s3Client.client()::listBuckets)
                       .buckets()
                       .stream()
                       .map(Bucket::name)
                       .collect(Collectors.toList());
           } catch (S3Exception e) {
               throw new CfnGeneralServiceException("Error while calling S3 ListBuckets API", e);
           }
       }

       @VisibleForTesting
       Collection<String> getBucketSSEAlgorithm(final String bucket) {
           try {
               return s3Client.injectCredentialsAndInvokeV2(Translator.createGetBucketEncryptionRequest(bucket), s3Client.client()::getBucketEncryption)
                       .serverSideEncryptionConfiguration()
                       .rules()
                       .stream()
                       .filter(r -> Objects.nonNull(r.applyServerSideEncryptionByDefault()))
                       .map(r -> r.applyServerSideEncryptionByDefault().sseAlgorithmAsString())
                       .collect(Collectors.toSet());
           } catch (S3Exception e) {
               return new HashSet<>();
           }
       }

       @VisibleForTesting
       boolean isQueueEncrypted(final String queueUrl) {
           try {
               final GetQueueAttributesRequest request = GetQueueAttributesRequest.builder()
                       .queueUrl(queueUrl)
                       .attributeNames(QueueAttributeName.KMS_MASTER_KEY_ID)
                       .build();
               final String kmsKeyId = sqsClient.injectCredentialsAndInvokeV2(request, sqsClient.client()::getQueueAttributes)
                       .attributes()
                       .get(QueueAttributeName.KMS_MASTER_KEY_ID);

               return StringUtils.isNotBlank(kmsKeyId);
           } catch (SqsException e) {
               throw new CfnGeneralServiceException("Error while calling SQS GetQueueAttributes API", e);
           }
       }
   }
   ```

### Updating the `preDelete` handler
<a name="update-the-predelete-handler"></a>

1. In your IDE, open the `PreDeleteHookHandler.java` file in the `src/main/java/com/mycompany/testing/mytesthook` folder.

1. Replace the entire contents of the `PreDeleteHookHandler.java` file with the following code.

   ```
   package com.mycompany.testing.mytesthook;

   import com.google.common.collect.ImmutableList;
   import com.google.common.collect.ImmutableMap;
   import com.mycompany.testing.mytesthook.model.aws.s3.bucket.AwsS3Bucket;
   import org.junit.jupiter.api.BeforeEach;
   import org.junit.jupiter.api.Test;
   import org.junit.jupiter.api.extension.ExtendWith;
   import org.mockito.Mock;
   import org.mockito.Mockito;
   import org.mockito.junit.jupiter.MockitoExtension;
   import software.amazon.awssdk.services.s3.S3Client;
   import software.amazon.awssdk.services.s3.model.Bucket;
   import software.amazon.awssdk.services.s3.model.GetBucketEncryptionRequest;
   import software.amazon.awssdk.services.s3.model.GetBucketEncryptionResponse;
   import software.amazon.awssdk.services.s3.model.ListBucketsRequest;
   import software.amazon.awssdk.services.s3.model.ListBucketsResponse;
   import software.amazon.awssdk.services.s3.model.S3Exception;
   import software.amazon.awssdk.services.s3.model.ServerSideEncryptionByDefault;
   import software.amazon.awssdk.services.s3.model.ServerSideEncryptionConfiguration;
   import software.amazon.awssdk.services.s3.model.ServerSideEncryptionRule;
   import software.amazon.awssdk.services.sqs.SqsClient;
   import software.amazon.awssdk.services.sqs.model.GetQueueAttributesRequest;
   import software.amazon.awssdk.services.sqs.model.GetQueueAttributesResponse;
   import software.amazon.awssdk.services.sqs.model.GetQueueUrlRequest;
   import software.amazon.awssdk.services.sqs.model.GetQueueUrlResponse;
   import software.amazon.awssdk.services.sqs.model.ListQueuesRequest;
   import software.amazon.awssdk.services.sqs.model.ListQueuesResponse;
   import software.amazon.awssdk.services.sqs.model.QueueAttributeName;
   import software.amazon.cloudformation.proxy.Logger;
   import software.amazon.cloudformation.proxy.OperationStatus;
   import software.amazon.cloudformation.proxy.ProgressEvent;
   import software.amazon.cloudformation.proxy.hook.HookContext;
   import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
   import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

   import java.util.Arrays;
   import java.util.Collection;
   import java.util.HashMap;
   import java.util.List;
   import java.util.stream.Collectors;

   import static org.mockito.ArgumentMatchers.any;
   import static org.mockito.Mockito.mock;
   import static org.mockito.Mockito.never;
   import static org.mockito.Mockito.times;
   import static org.mockito.Mockito.verify;
   import static org.mockito.Mockito.when;

   @ExtendWith(MockitoExtension.class)
   public class PreDeleteHookHandlerTest extends AbstractTestBase {

       @Mock private S3Client s3Client;
       @Mock private SqsClient sqsClient;
       @Mock private Logger logger;

       @BeforeEach
       public void setup() {
           s3Client = mock(S3Client.class);
           sqsClient = mock(SqsClient.class);
           logger = mock(Logger.class);
       }

       @Test
       public void handleRequest_awsS3BucketSuccess() {
           final PreDeleteHookHandler handler = Mockito.spy(new PreDeleteHookHandler());

           final List<Bucket> bucketList = ImmutableList.of(
                   Bucket.builder().name("bucket1").build(),
                   Bucket.builder().name("bucket2").build(),
                   Bucket.builder().name("toBeDeletedBucket").build(),
                   Bucket.builder().name("bucket3").build(),
                   Bucket.builder().name("bucket4").build(),
                   Bucket.builder().name("bucket5").build()
           );
           final ListBucketsResponse mockResponse = ListBucketsResponse.builder().buckets(bucketList).build();
           when(s3Client.listBuckets(any(ListBucketsRequest.class))).thenReturn(mockResponse);
           when(s3Client.getBucketEncryption(any(GetBucketEncryptionRequest.class)))
                   .thenReturn(buildGetBucketEncryptionResponse("AES256"))
                   .thenReturn(buildGetBucketEncryptionResponse("AES256", "aws:kms"))
                   .thenThrow(S3Exception.builder().message("No Encrypt").build())
                   .thenReturn(buildGetBucketEncryptionResponse("aws:kms"))
                   .thenReturn(buildGetBucketEncryptionResponse("AES256"));
           setServiceClient(s3Client);

           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder()
                   .encryptionAlgorithm("AES256")
                   .minBuckets("3")
                   .build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
                   .hookContext(
                       HookContext.builder()
                           .targetName("AWS::S3::Bucket")
                           .targetModel(
                               createHookTargetModel(
                                   AwsS3Bucket.builder()
                                       .bucketName("toBeDeletedBucket")
                                       .build()
                               )
                           )
                           .build())
                   .build();

           final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

           verify(s3Client, times(5)).getBucketEncryption(any(GetBucketEncryptionRequest.class));
           verify(handler, never()).getBucketSSEAlgorithm("toBeDeletedBucket");

           assertResponse(response, OperationStatus.SUCCESS, "Successfully invoked PreDeleteHookHandler for target: AWS::S3::Bucket");
       }

       @Test
       public void handleRequest_awsSqsQueueSuccess() {
           final PreDeleteHookHandler handler = Mockito.spy(new PreDeleteHookHandler());

           final List<String> queueUrls = ImmutableList.of(
                   "https://queue1.queue",
                   "https://queue2.queue",
                   "https://toBeDeletedQueue.queue",
                   "https://queue3.queue",
                   "https://queue4.queue",
                   "https://queue5.queue"
           );

           when(sqsClient.getQueueUrl(any(GetQueueUrlRequest.class)))
                   .thenReturn(GetQueueUrlResponse.builder().queueUrl("https://toBeDeletedQueue.queue").build());
           when(sqsClient.listQueues(any(ListQueuesRequest.class)))
                   .thenReturn(ListQueuesResponse.builder().queueUrls(queueUrls).build());
           when(sqsClient.getQueueAttributes(any(GetQueueAttributesRequest.class)))
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(ImmutableMap.of(QueueAttributeName.KMS_MASTER_KEY_ID, "kmsKeyId")).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(new HashMap<>()).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(ImmutableMap.of(QueueAttributeName.KMS_MASTER_KEY_ID, "kmsKeyId")).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(new HashMap<>()).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(ImmutableMap.of(QueueAttributeName.KMS_MASTER_KEY_ID, "kmsKeyId")).build());
           setServiceClient(sqsClient);

           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder()
                   .minQueues("3")
                   .build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
                   .hookContext(
                       HookContext.builder()
                           .targetName("AWS::SQS::Queue")
                           .targetModel(
                               createHookTargetModel(
                                   ImmutableMap.of("QueueName", "toBeDeletedQueue")
                               )
                           )
                           .build())
                   .build();

           final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

           verify(sqsClient, times(5)).getQueueAttributes(any(GetQueueAttributesRequest.class));
           verify(handler, never()).isQueueEncrypted("toBeDeletedQueue");

           assertResponse(response, OperationStatus.SUCCESS, "Successfully invoked PreDeleteHookHandler for target: AWS::SQS::Queue");
       }

       @Test
       public void handleRequest_awsS3BucketFailed() {
           final PreDeleteHookHandler handler = Mockito.spy(new PreDeleteHookHandler());

           final List<Bucket> bucketList = ImmutableList.of(
                   Bucket.builder().name("bucket1").build(),
                   Bucket.builder().name("bucket2").build(),
                   Bucket.builder().name("toBeDeletedBucket").build(),
                   Bucket.builder().name("bucket3").build(),
                   Bucket.builder().name("bucket4").build(),
                   Bucket.builder().name("bucket5").build()
           );
           final ListBucketsResponse mockResponse = ListBucketsResponse.builder().buckets(bucketList).build();
           when(s3Client.listBuckets(any(ListBucketsRequest.class))).thenReturn(mockResponse);
           when(s3Client.getBucketEncryption(any(GetBucketEncryptionRequest.class)))
                   .thenReturn(buildGetBucketEncryptionResponse("AES256"))
                   .thenReturn(buildGetBucketEncryptionResponse("AES256", "aws:kms"))
                   .thenThrow(S3Exception.builder().message("No Encrypt").build())
                   .thenReturn(buildGetBucketEncryptionResponse("aws:kms"))
                   .thenReturn(buildGetBucketEncryptionResponse("AES256"));
           setServiceClient(s3Client);

           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder()
                   .encryptionAlgorithm("AES256")
                   .minBuckets("10")
                   .build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
                   .hookContext(
                       HookContext.builder()
                           .targetName("AWS::S3::Bucket")
                           .targetModel(
                               createHookTargetModel(
                                   AwsS3Bucket.builder()
                                       .bucketName("toBeDeletedBucket")
                                       .build()
                               )
                           )
                           .build())
                   .build();

           final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

           verify(s3Client, times(5)).getBucketEncryption(any(GetBucketEncryptionRequest.class));
           verify(handler, never()).getBucketSSEAlgorithm("toBeDeletedBucket");

           assertResponse(response, OperationStatus.FAILED, "Failed to meet minimum of [10] encrypted buckets.");
       }

       @Test
       public void handleRequest_awsSqsQueueFailed() {
           final PreDeleteHookHandler handler = Mockito.spy(new PreDeleteHookHandler());

           final List<String> queueUrls = ImmutableList.of(
                   "https://queue1.queue",
                   "https://queue2.queue",
                   "https://toBeDeletedQueue.queue",
                   "https://queue3.queue",
                   "https://queue4.queue",
                   "https://queue5.queue"
           );

           when(sqsClient.getQueueUrl(any(GetQueueUrlRequest.class)))
                   .thenReturn(GetQueueUrlResponse.builder().queueUrl("https://toBeDeletedQueue.queue").build());
           when(sqsClient.listQueues(any(ListQueuesRequest.class)))
                   .thenReturn(ListQueuesResponse.builder().queueUrls(queueUrls).build());
           when(sqsClient.getQueueAttributes(any(GetQueueAttributesRequest.class)))
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(ImmutableMap.of(QueueAttributeName.KMS_MASTER_KEY_ID, "kmsKeyId")).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(new HashMap<>()).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(ImmutableMap.of(QueueAttributeName.KMS_MASTER_KEY_ID, "kmsKeyId")).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(new HashMap<>()).build())
                   .thenReturn(GetQueueAttributesResponse.builder().attributes(ImmutableMap.of(QueueAttributeName.KMS_MASTER_KEY_ID, "kmsKeyId")).build());
           setServiceClient(sqsClient);

           final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder()
                   .minQueues("10")
                   .build();

           final HookHandlerRequest request = HookHandlerRequest.builder()
                   .hookContext(
                       HookContext.builder()
                           .targetName("AWS::SQS::Queue")
                           .targetModel(
                               createHookTargetModel(
                                   ImmutableMap.of("QueueName", "toBeDeletedQueue")
                               )
                           )
                           .build())
                   .build();

           final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

           verify(sqsClient, times(5)).getQueueAttributes(any(GetQueueAttributesRequest.class));
           verify(handler, never()).isQueueEncrypted("toBeDeletedQueue");

           assertResponse(response, OperationStatus.FAILED, "Failed to meet minimum of [10] encrypted queues.");
       }

       private GetBucketEncryptionResponse buildGetBucketEncryptionResponse(final String ...sseAlgorithm) {
           return buildGetBucketEncryptionResponse(
                   Arrays.stream(sseAlgorithm)
                       .map(a -> ServerSideEncryptionRule.builder().applyServerSideEncryptionByDefault(
                           ServerSideEncryptionByDefault.builder()
                               .sseAlgorithm(a)
                               .build()
                           ).build()
                       )
                       .collect(Collectors.toList())
           );
       }

       private GetBucketEncryptionResponse buildGetBucketEncryptionResponse(final Collection<ServerSideEncryptionRule> rules) {
           return GetBucketEncryptionResponse.builder()
                   .serverSideEncryptionConfiguration(
                       ServerSideEncryptionConfiguration.builder().rules(
                           rules
                       ).build()
                   ).build();
       }
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
