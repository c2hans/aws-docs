---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/job-settings-file.html
---

# Job settings file
<a name="job-settings-file"></a>

 By default, this solution creates an `assets01` folder in the root of the S3 bucket with a `job-settings.json` file*.* Video uploads to this folder invoke a workflow to apply job settings to the job created in MediaConvert.

## Changing the job settings file
<a name="changing-the-job-settings-file"></a>

 You can customize the `job-settings.json` file or replace it with a new MediaConvert job template. To make a new job template or to customize the existing `job-setting.json` job template, refer to [Working with AWS Elemental MediaConvert job templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html) in the *MediaConvert User Guide*.

 When your updated job template JSON file is ready, name the file `job-settings.json` and upload it to replace the one that is already in the `assets01` folder of the S3 source bucket.

## Working with multiple job settings files
<a name="working-with-multiple-job-settings-files"></a>

 To support different job settings, create additional folders at the root of the source S3 bucket and include different job setting for each folder. The following shows an example folder structure. With this example configuration in the source S3 bucket, `video-01.mp4` files are encoded with the settings stored in the `assets01` folder. Meanwhile, `video-02.mp4` and `video-03.mpg` files are encoded using the settings in the `assets02` folder:

```
assets01/
     job-settings.json
     video-01.mp4
assets02/
    job-settings.json
    video-02.mp4
    subfolder/video-03.mpg
```

**Important**
 You must name the settings file `job-settings.json`. There are no specific requirements for the folder names.

 Although you can export a completed job from MediaConvert to use as a job settings file, this solution doesn't support [input stitching or input clipping](https://docs.aws.amazon.com/mediaconvert/latest/ug/specifying-inputs.html) because it only launches on the upload of one video file source.

 If `AccelerationSettings` is not defined in the job settings JSON file, this solution will automatically add this and set it to `PREFERRED`.

 We recommend that you provide a [custom name for your output groups](https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-output-groups.html), especially if your job settings include more than one output group of the same type. For example, three HLS output groups. The solution uses the output group name as part of the output destination path, and having distinct names makes it easier to locate where each output is being written.
