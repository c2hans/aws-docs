---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/lz-manifest-file.html
---

# View the details of your landing zone manifest file
<a name="lz-manifest-file"></a>

The AWS Control Tower landing zone manifest file is a text file that describes your AWS Control Tower resources. The following sections show detailed definitions of entries in the landing zone manifest file.

To see a full landing zone schema example, see [Landing zone schemas](https://docs.aws.amazon.com/controltower/latest/userguide/landing-zone-schemas.html).

**governedRegions** – Regions to place under governance
+  **Type:** List of strings
+ **Required:** No
+ **Example:**

  ```
  "governedRegions": ["us-west-2","us-west-1"]
  ```

**organizationStructure** – Select the names of security and sandbox OUs to be created in your organization
+  **Type:** Object
+ **Required:** Yes
+ **Properties:**
+ **Example:**
  + `security` - an object with one required property, `name`, which takes a `String`
  + `sandbox` - an object with one required property, `name`, which takes a `String`

  ```
  "organizationStructure": {
         "security": {
             "name": "CORE"
         },
         "sandbox": {
             "name": "Sandbox"
         }
     }
  ```

**centralizedLogging** – Configuration for AWS CloudTrail
+  **Type:** Object
+ **Required:** Yes
+ **Properties:**
  + *accountId* - a `String` the represents the AWS account into which the logging resource should be deployed
  + *configurations* - an `Object` with three properties
    + `loggingBucket` - an object with one property, `retentionDays`, which takes a `Number`
    + `accessLoggingBucket` - an object with one property, `retentionDays`, which takes a `Number`
    + `kmsKeyArn` - an optional `String`
  + *enabled* - an optional `Boolean`
+ **Example:**

  ```
  "centralizedLogging": {
          "accountId": "222222222222",
          "configurations": {
              "loggingBucket": {
                  "retentionDays": 60
              },
              "accessLoggingBucket": {
                  "retentionDays": 60
              },
              "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
          },
          "enabled": true
     }
  ```

**securityRoles** – Choose where to deploy the logging resource
+  **Type:** Object
+ **Required:** Yes
+ **Properties:** *accountId* - a `String` that represents the AWS account into which the logging resource should be deployed
+ **Example:**

  ```
  "securityRoles": {
          "accountId": "333333333333"
     }
  ```

**accessManagement** – Choose whether to enable access management
+  **Type:** Object
+ **Required:** No
+ **Properties:** *enabled* - a Boolean
+ **Example:**

  ```
  "accessManagement": {
          "enabled": true
     }
  ```

**backup** – Configuration for AWS Backup with AWS Control Tower
+  **Type:** Object
+ **Required:** No
+ **Properties:**
  + *configurations* - an `Object` with three properties
    + `centralBackup` - an object with one property, `accountId`, which takes a `String`
    + `backupAdmin` - an object with one property, `accountId`, which takes a `String`
    + `kmsKeyArn` - an optional `String`
  + *enabled* - a `Boolean`
+ **Example:**

  ```
  "backup": {
      "configurations": {
          "centralBackup": {
              "accountId": "{{CENTRAL BACKUP ACCOUNT ID}}"
          },
          "backupAdmin": {
              "accountId": "{{BACKUP MANAGER ACCOUNT ID}}"
          },
          "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
      },
      "enabled": true
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
