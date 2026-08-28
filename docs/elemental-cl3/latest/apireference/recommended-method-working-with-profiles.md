---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/recommended-method-working-with-profiles.html
---

# Recommended Method for Working with Profiles
<a name="recommended-method-working-with-profiles"></a>

The body of a POST or PUT profile request can contain a lot of elements (attributes of the profile). We recommend that you follow the procedures in this section to create the body.

## Create a Profile Base
<a name="profile-create-a-base"></a>

1. Use the Conductor Live web interface to create a profile that contains most of the content you want:
   + The desired inputs, including the desired number and types of video, audio, and caption streams as well as the desired hot backup fields.
   + The desired output groups.
   + Within each output group, the desired outputs.
   + Within each output, the desired video, audio and captioning.

   Give the profile a descriptive name, perhaps including the term “template” and including a description of the inputs, outputs, codecs used, and so on.

   See the [AWS Elemental Conductor Live User Guide](https://docs.aws.amazon.com/elemental-cl3/latest/ug/) for information on the contents of a profile.

1. Do a GET Profile List and make a note of the ID for this profile.

## Create a Template
<a name="profile-create-a-template"></a>

1. Use the GET Profile command to get this profile with the clean parameter set to `true`. For example, to get the profile that has the ID 2, use this command.

   ```
   GET http://198.51.100.0/profiles/2.xml?clean=true
   ```

   The response removes the ID, which makes it valid for re-use in a POST or PUT.

1. Inspect the XML document that is returned. You will notice that it is structured as shown below.Make sure that it has all the information that you want in the template.

1. You can now store this XML as a template and re-use it in the body of a POST.

## Re-use the Template
<a name="profile-reuse-the-template"></a>

Templates can be used for current version of Conductor Live up to two major versions back. When the profile is uploaded, it is migrated to the current version with field selections and values maintained.

1. To re-use the template, you must:
   + Change the <name>. This name must be unique.
   + Change the <permalink>. This must be the <name> converted to lowercase and with spaces converted to underscores. For example, if the <name> is “Profile A”, then the <permalink> must be “profile\_a”.
   + If you are on version 3.2 or higher, you must enter default values for all channel parameters. For more information, see [POST: Create a Profile](post-create-a-profile.md).

1. Change any other elements, as desired. Include this XML in the body of a POST or PUT request. For more information, see [POST: Create a Profile](post-create-a-profile.md).

## XML Structure of a Profile
<a name="profile-xml-structure"></a>

```
<profile href=> //information about the profile and Conductor Live product and version
  <name>aa</name>
  <permalink>bb</permalink>
  <description>cc</description>
  <input>
    .
    .
    .
  <network_input>
    .
    .
    .
  </network_input>
  <video_selector>   //one or more
    .
    .
    .
  </video_selector>
  <audio_selector>    // one or more
    .
    .
    .
  </audio_selector>
    .
    .
    .
  <caption_selector>    // zero or more
    .
    .
    .
  </caption_selector>
    .
    .
    .
  <stream_assembly>    //one or more
    <video_description>
       .
       .
       .
      <h264_settings> //where h264 could be the name of any codec
         .
         .
         .
      </h264_settings>
         .
         .
         .
    </video_description>
    <audio_description>
       .
       .
       .
      <aac_settings> //where aac could be the name of any audio codec
         .
         .
         .
      </aac_settings>
         .
         .
         .
    </audio_description>
  </stream_assembly>
  <output_group>
    <archive_group_settings>    //where "archive" could be any output group type
       .
       .
       .
    </archive_group_settings>
    <output>
       .
       .
       .
    </output>
  </output_group>
</profile>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
