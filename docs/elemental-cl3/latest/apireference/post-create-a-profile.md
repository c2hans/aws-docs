---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/post-create-a-profile.html
---

# POST: Create a Profile
<a name="post-create-a-profile"></a>

Create a profile.

## HTTP Request and Response
<a name="post-create-a-profile-http-request-response"></a>

### Request URL
<a name="post-create-a-profile-http-request-response-url"></a>

```
POST http://<Conductor IP address>/profiles
```

### Call Header
<a name="post-create-a-profile-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

  When POSTing xml for a profile originally created with an earlier version of Conductor Live, set content-type to application/vnd.elemental\+xml;version=n.n.n, where n.n.n is the number of the Conductor Live version used to create the profile. For example, if the profile was created with Conductor Live version 3.2.1, use:

  ```
  content-type: application/vnd.elemental+xml;version=3.2.1
  ```

  For more information on using profiles created with earlier software versions, see Versioning, [Header Content for User Authentication](header-content-user.md).

If you are implementing user authentication, you must also include three authorization headers as described on [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="post-create-a-profile-http-request-response-request-body"></a>

The request body contains XML content. For more information, see [XML Structure of a Profile](recommended-method-working-with-profiles.md#profile-xml-structure).

### Response
<a name="post-create-a-profile-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: The newly assigned ID for the group.

The response is identical to the response to a GET Profile. See below for an example.

## Example
<a name="post-create-a-profile-example"></a>

### Response
<a name="post-create-a-profile-example-response"></a>

The response to a valid request presents the new `profile `element with all the information from the new profile.

In this example, the input type is “network\_input,” and the URI of that input has been set to a channel parameter “input network location,” and the default value is udp://255.255.255.255:5001. For information on channel parameters, see the section on setting up channels in the Conductor Live User Guide. For information on how these parameters are set in a channel, see [POST: Create a Channel](post-create-a-channel.md).

```
POST http://198.51.100.0/channels
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.2.1
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<profile>
  <id>9</id>
  <name>Profile X</name>
  <permalink>profile_x</permalink>
  <description/>
  {{<parameters>
    <parameter>
      <name>input network location</name>
      <default>udp://255.255.255.255:5001</default>
    </parameter>
  </parameters>}}
  <input>
    <network_input>
      {{<uri>{{input network location}}</uri>}}
    </network_input>
    <name>input_1</name>
.
.
.
    </input>
.
.
.
</profile>
```

### Creating a Profile for a Channel Used by an MPTS
<a name="post-create-a-profile-example-create-profile-used-by-mpts"></a>

For important information on the requirements for creating a profile that will be used to create a channel that will become an SPTS in an MPTS output, see [Setting up MPTS outputs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html) in the AWS Elemental Conductor Live User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
