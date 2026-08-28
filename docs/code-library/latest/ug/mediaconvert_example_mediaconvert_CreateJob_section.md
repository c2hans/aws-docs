---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/mediaconvert_example_mediaconvert_CreateJob_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateJob` with an AWS SDK or CLI
<a name="mediaconvert_example_mediaconvert_CreateJob_section"></a>

The following code examples show how to use `CreateJob`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/MediaConvert#code-examples).
Set up the file locations, client, and wrapper.

```
        // MediaConvert role Amazon Resource Name (ARN).
        // For information on creating this role, see
        // https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-the-iam-role-in-mediaconvert-configured.html.
        var mediaConvertRole = _configuration["mediaConvertRoleARN"];

        // Include the file input and output locations in settings.json or settings.local.json.
        var fileInput = _configuration["fileInput"];
        var fileOutput = _configuration["fileOutput"];

        AmazonMediaConvertClient mcClient = new AmazonMediaConvertClient();

        var wrapper = new MediaConvertWrapper(mcClient);
```

```
        Console.WriteLine(new string('-', 80));
        Console.WriteLine($"Creating job for input file {fileInput}.");
        var jobId = await wrapper.CreateJob(mediaConvertRole!, fileInput!, fileOutput!);
        Console.WriteLine($"Created job with Job ID: {jobId}");
        Console.WriteLine(new string('-', 80));
```
Create the job using the wrapper method and return the job ID.

```
    /// <summary>
    /// Create a job to convert a media file.
    /// </summary>
    /// <param name="mediaConvertRole">The Amazon Resource Name (ARN) of the media convert role, as specified here:
    /// https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-the-iam-role-in-mediaconvert-configured.html</param>
    /// <param name="fileInput">The Amazon Simple Storage Service (Amazon S3) location of the input media file.</param>
    /// <param name="fileOutput">The Amazon S3 location for the output media file.</param>
    /// <returns>The ID of the new job.</returns>
    public async Task<string> CreateJob(string mediaConvertRole, string fileInput,
        string fileOutput)
    {
        CreateJobRequest createJobRequest = new CreateJobRequest
        {
            Role = mediaConvertRole
        };

        createJobRequest.UserMetadata.Add("Customer", "Amazon");

        JobSettings jobSettings = new JobSettings
        {
            AdAvailOffset = 0,
            TimecodeConfig = new TimecodeConfig
            {
                Source = TimecodeSource.EMBEDDED
            }
        };
        createJobRequest.Settings = jobSettings;

        #region OutputGroup

        OutputGroup ofg = new OutputGroup
        {
            Name = "File Group",
            OutputGroupSettings = new OutputGroupSettings
            {
                Type = OutputGroupType.FILE_GROUP_SETTINGS,
                FileGroupSettings = new FileGroupSettings
                {
                    Destination = fileOutput
                }
            }
        };

        Output output = new Output
        {
            NameModifier = "_1"
        };

        #region VideoDescription

        VideoDescription vdes = new VideoDescription
        {
            ScalingBehavior = ScalingBehavior.DEFAULT,
            TimecodeInsertion = VideoTimecodeInsertion.DISABLED,
            AntiAlias = AntiAlias.ENABLED,
            Sharpness = 50,
            AfdSignaling = AfdSignaling.NONE,
            DropFrameTimecode = DropFrameTimecode.ENABLED,
            RespondToAfd = RespondToAfd.NONE,
            ColorMetadata = ColorMetadata.INSERT,
            CodecSettings = new VideoCodecSettings
            {
                Codec = VideoCodec.H_264
            }
        };
        output.VideoDescription = vdes;

        H264Settings h264 = new H264Settings
        {
            InterlaceMode = H264InterlaceMode.PROGRESSIVE,
            NumberReferenceFrames = 3,
            Syntax = H264Syntax.DEFAULT,
            Softness = 0,
            GopClosedCadence = 1,
            GopSize = 90,
            Slices = 1,
            GopBReference = H264GopBReference.DISABLED,
            SlowPal = H264SlowPal.DISABLED,
            SpatialAdaptiveQuantization = H264SpatialAdaptiveQuantization.ENABLED,
            TemporalAdaptiveQuantization = H264TemporalAdaptiveQuantization.ENABLED,
            FlickerAdaptiveQuantization = H264FlickerAdaptiveQuantization.DISABLED,
            EntropyEncoding = H264EntropyEncoding.CABAC,
            Bitrate = 5000000,
            FramerateControl = H264FramerateControl.SPECIFIED,
            RateControlMode = H264RateControlMode.CBR,
            CodecProfile = H264CodecProfile.MAIN,
            Telecine = H264Telecine.NONE,
            MinIInterval = 0,
            AdaptiveQuantization = H264AdaptiveQuantization.HIGH,
            CodecLevel = H264CodecLevel.AUTO,
            FieldEncoding = H264FieldEncoding.PAFF,
            SceneChangeDetect = H264SceneChangeDetect.ENABLED,
            QualityTuningLevel = H264QualityTuningLevel.SINGLE_PASS,
            FramerateConversionAlgorithm =
                H264FramerateConversionAlgorithm.DUPLICATE_DROP,
            UnregisteredSeiTimecode = H264UnregisteredSeiTimecode.DISABLED,
            GopSizeUnits = H264GopSizeUnits.FRAMES,
            ParControl = H264ParControl.SPECIFIED,
            NumberBFramesBetweenReferenceFrames = 2,
            RepeatPps = H264RepeatPps.DISABLED,
            FramerateNumerator = 30,
            FramerateDenominator = 1,
            ParNumerator = 1,
            ParDenominator = 1
        };
        output.VideoDescription.CodecSettings.H264Settings = h264;

        #endregion VideoDescription

        #region AudioDescription

        AudioDescription ades = new AudioDescription
        {
            LanguageCodeControl = AudioLanguageCodeControl.FOLLOW_INPUT,
            // This name matches one specified in the following Inputs.
            AudioSourceName = "Audio Selector 1",
            CodecSettings = new AudioCodecSettings
            {
                Codec = AudioCodec.AAC
            }
        };

        AacSettings aac = new AacSettings
        {
            AudioDescriptionBroadcasterMix = AacAudioDescriptionBroadcasterMix.NORMAL,
            RateControlMode = AacRateControlMode.CBR,
            CodecProfile = AacCodecProfile.LC,
            CodingMode = AacCodingMode.CODING_MODE_2_0,
            RawFormat = AacRawFormat.NONE,
            SampleRate = 48000,
            Specification = AacSpecification.MPEG4,
            Bitrate = 64000
        };
        ades.CodecSettings.AacSettings = aac;
        output.AudioDescriptions.Add(ades);

        #endregion AudioDescription

        #region Mp4 Container

        output.ContainerSettings = new ContainerSettings
        {
            Container = ContainerType.MP4
        };
        Mp4Settings mp4 = new Mp4Settings
        {
            CslgAtom = Mp4CslgAtom.INCLUDE,
            FreeSpaceBox = Mp4FreeSpaceBox.EXCLUDE,
            MoovPlacement = Mp4MoovPlacement.PROGRESSIVE_DOWNLOAD
        };
        output.ContainerSettings.Mp4Settings = mp4;

        #endregion Mp4 Container

        ofg.Outputs.Add(output);
        createJobRequest.Settings.OutputGroups.Add(ofg);

        #endregion OutputGroup

        #region Input

        Input input = new Input
        {
            FilterEnable = InputFilterEnable.AUTO,
            PsiControl = InputPsiControl.USE_PSI,
            FilterStrength = 0,
            DeblockFilter = InputDeblockFilter.DISABLED,
            DenoiseFilter = InputDenoiseFilter.DISABLED,
            TimecodeSource = InputTimecodeSource.EMBEDDED,
            FileInput = fileInput
        };

        AudioSelector audsel = new AudioSelector
        {
            Offset = 0,
            DefaultSelection = AudioDefaultSelection.NOT_DEFAULT,
            ProgramSelection = 1,
            SelectorType = AudioSelectorType.TRACK
        };
        audsel.Tracks.Add(1);
        input.AudioSelectors.Add("Audio Selector 1", audsel);

        input.VideoSelector = new VideoSelector
        {
            ColorSpace = ColorSpace.FOLLOW
        };

        createJobRequest.Settings.Inputs.Add(input);

        #endregion Input

        CreateJobResponse createJobResponse =
            await _amazonMediaConvert.CreateJobAsync(createJobRequest);

        var jobId = createJobResponse.Job.Id;

        return jobId;
    }
```
+  For API details, see [CreateJob](https://docs.aws.amazon.com/goto/DotNetSDKV3/mediaconvert-2017-08-29/CreateJob) in *AWS SDK for .NET API Reference*.

------
#### [ C\+\+ ]

**SDK for C\+\+**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/mediaconvert#code-examples).

```
//! Create an AWS Elemental MediaConvert job.
/*!
  \param mediaConvertRole: An Amazon Resource Name (ARN) for the AWS Identity and
                           Access Management (IAM) role for the job.
  \param fileInput: A URI to an input file that is stored in Amazon Simple Storage Service
                    (Amazon S3) or on an HTTP(S) server.
  \param fileOutput: A URI for an Amazon S3 output location and the output file name base.
  \param jobSettingsFile: An optional JSON settings file.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */

bool AwsDoc::MediaConvert::createJob(const Aws::String &mediaConvertRole,
                                     const Aws::String &fileInput,
                                     const Aws::String &fileOutput,
                                     const Aws::String &jobSettingsFile,
                                     const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::MediaConvert::Model::CreateJobRequest createJobRequest;

    createJobRequest.SetRole(mediaConvertRole);
    Aws::Http::HeaderValueCollection hvc;
    hvc.emplace("Customer", "Amazon");
    createJobRequest.SetUserMetadata(hvc);

    if (!jobSettingsFile.empty()) // Use a JSON file for the job settings.
    {
        std::ifstream jobSettingsStream(jobSettingsFile, std::ios::ate);
        if (!jobSettingsStream) {
            std::cerr << "Unable to open the job template file." << std::endl;
            return false;
        }
        std::vector<char> buffer(jobSettingsStream.tellg());
        jobSettingsStream.seekg(0);
        jobSettingsStream.read(buffer.data(), buffer.size());
        std::string jobSettingsJSON(buffer.data(), buffer.size());
        size_t pos = jobSettingsJSON.find(INPUT_FILE_PLACEHOLDER);
        if (pos != std::string::npos) {
            jobSettingsJSON.replace(pos, strlen(INPUT_FILE_PLACEHOLDER), fileInput);
        }

        pos = jobSettingsJSON.find(OUTPUT_FILE_PLACEHOLDER);
        if (pos != std::string::npos) {
            jobSettingsJSON.replace(pos, strlen(OUTPUT_FILE_PLACEHOLDER), fileOutput);
        }
        Aws::Utils::Json::JsonValue jsonValue(jobSettingsJSON);
        Aws::MediaConvert::Model::JobSettings jobSettings(jsonValue);

        createJobRequest.SetSettings(jobSettings);
    }
    else { // Configure the job settings programmatically.
        Aws::MediaConvert::Model::JobSettings jobSettings;
        jobSettings.SetAdAvailOffset(0);
        Aws::MediaConvert::Model::TimecodeConfig timecodeConfig;
        timecodeConfig.SetSource(Aws::MediaConvert::Model::TimecodeSource::EMBEDDED);
        jobSettings.SetTimecodeConfig(timecodeConfig);

        // Configure the output group.
        Aws::MediaConvert::Model::OutputGroup outputGroup;
        outputGroup.SetName("File Group");
        Aws::MediaConvert::Model::OutputGroupSettings outputGroupSettings;
        outputGroupSettings.SetType(
                Aws::MediaConvert::Model::OutputGroupType::FILE_GROUP_SETTINGS);
        Aws::MediaConvert::Model::FileGroupSettings fileGroupSettings;
        fileGroupSettings.SetDestination(fileOutput);
        outputGroupSettings.SetFileGroupSettings(fileGroupSettings);
        outputGroup.SetOutputGroupSettings(outputGroupSettings);

        Aws::MediaConvert::Model::Output output;
        output.SetNameModifier("_1");

        Aws::MediaConvert::Model::VideoDescription videoDescription;
        videoDescription.SetScalingBehavior(
                Aws::MediaConvert::Model::ScalingBehavior::DEFAULT);
        videoDescription.SetTimecodeInsertion(
                Aws::MediaConvert::Model::VideoTimecodeInsertion::DISABLED);
        videoDescription.SetAntiAlias(Aws::MediaConvert::Model::AntiAlias::ENABLED);
        videoDescription.SetSharpness(50);
        videoDescription.SetAfdSignaling(Aws::MediaConvert::Model::AfdSignaling::NONE);
        videoDescription.SetDropFrameTimecode(
                Aws::MediaConvert::Model::DropFrameTimecode::ENABLED);
        videoDescription.SetRespondToAfd(Aws::MediaConvert::Model::RespondToAfd::NONE);
        videoDescription.SetColorMetadata(
                Aws::MediaConvert::Model::ColorMetadata::INSERT);

        Aws::MediaConvert::Model::VideoCodecSettings videoCodecSettings;
        videoCodecSettings.SetCodec(Aws::MediaConvert::Model::VideoCodec::H_264);
        Aws::MediaConvert::Model::H264Settings h264Settings;
        h264Settings.SetNumberReferenceFrames(3);
        h264Settings.SetSyntax(Aws::MediaConvert::Model::H264Syntax::DEFAULT);
        h264Settings.SetSoftness(0);
        h264Settings.SetGopClosedCadence(1);
        h264Settings.SetGopSize(90);
        h264Settings.SetSlices(1);
        h264Settings.SetGopBReference(
                Aws::MediaConvert::Model::H264GopBReference::DISABLED);
        h264Settings.SetSlowPal(Aws::MediaConvert::Model::H264SlowPal::DISABLED);
        h264Settings.SetSpatialAdaptiveQuantization(
                Aws::MediaConvert::Model::H264SpatialAdaptiveQuantization::ENABLED);
        h264Settings.SetTemporalAdaptiveQuantization(
                Aws::MediaConvert::Model::H264TemporalAdaptiveQuantization::ENABLED);
        h264Settings.SetFlickerAdaptiveQuantization(
                Aws::MediaConvert::Model::H264FlickerAdaptiveQuantization::DISABLED);
        h264Settings.SetEntropyEncoding(
                Aws::MediaConvert::Model::H264EntropyEncoding::CABAC);
        h264Settings.SetBitrate(5000000);
        h264Settings.SetFramerateControl(
                Aws::MediaConvert::Model::H264FramerateControl::SPECIFIED);
        h264Settings.SetRateControlMode(
                Aws::MediaConvert::Model::H264RateControlMode::CBR);
        h264Settings.SetCodecProfile(Aws::MediaConvert::Model::H264CodecProfile::MAIN);
        h264Settings.SetTelecine(Aws::MediaConvert::Model::H264Telecine::NONE);
        h264Settings.SetMinIInterval(0);
        h264Settings.SetAdaptiveQuantization(
                Aws::MediaConvert::Model::H264AdaptiveQuantization::HIGH);
        h264Settings.SetCodecLevel(Aws::MediaConvert::Model::H264CodecLevel::AUTO);
        h264Settings.SetFieldEncoding(
                Aws::MediaConvert::Model::H264FieldEncoding::PAFF);
        h264Settings.SetSceneChangeDetect(
                Aws::MediaConvert::Model::H264SceneChangeDetect::ENABLED);
        h264Settings.SetQualityTuningLevel(
                Aws::MediaConvert::Model::H264QualityTuningLevel::SINGLE_PASS);
        h264Settings.SetFramerateConversionAlgorithm(
                Aws::MediaConvert::Model::H264FramerateConversionAlgorithm::DUPLICATE_DROP);
        h264Settings.SetUnregisteredSeiTimecode(
                Aws::MediaConvert::Model::H264UnregisteredSeiTimecode::DISABLED);
        h264Settings.SetGopSizeUnits(
                Aws::MediaConvert::Model::H264GopSizeUnits::FRAMES);
        h264Settings.SetParControl(Aws::MediaConvert::Model::H264ParControl::SPECIFIED);
        h264Settings.SetNumberBFramesBetweenReferenceFrames(2);
        h264Settings.SetRepeatPps(Aws::MediaConvert::Model::H264RepeatPps::DISABLED);
        h264Settings.SetFramerateNumerator(30);
        h264Settings.SetFramerateDenominator(1);
        h264Settings.SetParNumerator(1);
        h264Settings.SetParDenominator(1);
        videoCodecSettings.SetH264Settings(h264Settings);
        videoDescription.SetCodecSettings(videoCodecSettings);
        output.SetVideoDescription(videoDescription);

        Aws::MediaConvert::Model::AudioDescription audioDescription;
        audioDescription.SetLanguageCodeControl(
                Aws::MediaConvert::Model::AudioLanguageCodeControl::FOLLOW_INPUT);
        audioDescription.SetAudioSourceName(AUDIO_SOURCE_NAME);
        Aws::MediaConvert::Model::AudioCodecSettings audioCodecSettings;
        audioCodecSettings.SetCodec(Aws::MediaConvert::Model::AudioCodec::AAC);
        Aws::MediaConvert::Model::AacSettings aacSettings;
        aacSettings.SetAudioDescriptionBroadcasterMix(
                Aws::MediaConvert::Model::AacAudioDescriptionBroadcasterMix::NORMAL);
        aacSettings.SetRateControlMode(
                Aws::MediaConvert::Model::AacRateControlMode::CBR);
        aacSettings.SetCodecProfile(Aws::MediaConvert::Model::AacCodecProfile::LC);
        aacSettings.SetCodingMode(
                Aws::MediaConvert::Model::AacCodingMode::CODING_MODE_2_0);
        aacSettings.SetRawFormat(Aws::MediaConvert::Model::AacRawFormat::NONE);
        aacSettings.SetSampleRate(48000);
        aacSettings.SetSpecification(Aws::MediaConvert::Model::AacSpecification::MPEG4);
        aacSettings.SetBitrate(64000);
        audioCodecSettings.SetAacSettings(aacSettings);
        audioDescription.SetCodecSettings(audioCodecSettings);
        Aws::Vector<Aws::MediaConvert::Model::AudioDescription> audioDescriptions;
        audioDescriptions.emplace_back(audioDescription);
        output.SetAudioDescriptions(audioDescriptions);

        Aws::MediaConvert::Model::ContainerSettings mp4container;
        mp4container.SetContainer(Aws::MediaConvert::Model::ContainerType::MP4);
        Aws::MediaConvert::Model::Mp4Settings mp4Settings;
        mp4Settings.SetCslgAtom(Aws::MediaConvert::Model::Mp4CslgAtom::INCLUDE);
        mp4Settings.SetFreeSpaceBox(Aws::MediaConvert::Model::Mp4FreeSpaceBox::EXCLUDE);
        mp4Settings.SetMoovPlacement(
                Aws::MediaConvert::Model::Mp4MoovPlacement::PROGRESSIVE_DOWNLOAD);
        mp4container.SetMp4Settings(mp4Settings);
        output.SetContainerSettings(mp4container);

        outputGroup.AddOutputs(output);
        jobSettings.AddOutputGroups(outputGroup);

        // Configure inputs.
        Aws::MediaConvert::Model::Input input;
        input.SetFilterEnable(Aws::MediaConvert::Model::InputFilterEnable::AUTO);
        input.SetPsiControl(Aws::MediaConvert::Model::InputPsiControl::USE_PSI);
        input.SetFilterStrength(0);
        input.SetDeblockFilter(Aws::MediaConvert::Model::InputDeblockFilter::DISABLED);
        input.SetDenoiseFilter(Aws::MediaConvert::Model::InputDenoiseFilter::DISABLED);
        input.SetTimecodeSource(
                Aws::MediaConvert::Model::InputTimecodeSource::EMBEDDED);
        input.SetFileInput(fileInput);

        Aws::MediaConvert::Model::AudioSelector audioSelector;
        audioSelector.SetOffset(0);
        audioSelector.SetDefaultSelection(
                Aws::MediaConvert::Model::AudioDefaultSelection::NOT_DEFAULT);
        audioSelector.SetProgramSelection(1);
        audioSelector.SetSelectorType(
                Aws::MediaConvert::Model::AudioSelectorType::TRACK);
        audioSelector.AddTracks(1);
        input.AddAudioSelectors(AUDIO_SOURCE_NAME, audioSelector);

        Aws::MediaConvert::Model::VideoSelector videoSelector;
        videoSelector.SetColorSpace(Aws::MediaConvert::Model::ColorSpace::FOLLOW);
        input.SetVideoSelector(videoSelector);

        jobSettings.AddInputs(input);

        createJobRequest.SetSettings(jobSettings);
    }

    Aws::MediaConvert::MediaConvertClient client(clientConfiguration);
    Aws::MediaConvert::Model::CreateJobOutcome outcome = client.CreateJob(
            createJobRequest);
    if (outcome.IsSuccess()) {
        std::cout << "Job successfully created with ID - "
                  << outcome.GetResult().GetJob().GetId() << std::endl;
    }
    else {
        std::cerr << "Error CreateJob - " << outcome.GetError().GetMessage()
                  << std::endl;
    }

    return outcome.IsSuccess();
}
```
+  For API details, see [CreateJob](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconvert-2017-08-29/CreateJob) in *AWS SDK for C\+\+ API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To create a job**
The following `create-job` example creates a transcoding job with the settings that are specified in a file `job.json` that resides on the system that you send the command from. This JSON job specification might specify each setting individually, reference a job template, or reference output presets.

```
aws mediaconvert create-job \
    --endpoint-url {{https://abcd1234.mediaconvert.region-name-1.amazonaws.com}} \
    --region {{region-name-1}} \
    --cli-input-json {{file://~/job.json}}
```
You can use the AWS Elemental MediaConvert console to generate the JSON job specification by choosing your job settings, and then choosing **Show job JSON** at the bottom of the **Job** section.
To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.
If your request is successful, the service returns the JSON job specification that you sent with your request.
For more information, see [Working with AWS Elemental MediaConvert Jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-jobs.html) in the *AWS Elemental MediaConvert User Guide*.
+  For API details, see [CreateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/mediaconvert#code-examples).

```
package com.example.mediaconvert;

import java.net.URI;
import java.util.HashMap;
import java.util.Map;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.mediaconvert.MediaConvertClient;
import software.amazon.awssdk.services.mediaconvert.model.DescribeEndpointsResponse;
import software.amazon.awssdk.services.mediaconvert.model.DescribeEndpointsRequest;
import software.amazon.awssdk.services.mediaconvert.model.Output;
import software.amazon.awssdk.services.mediaconvert.model.MediaConvertException;
import software.amazon.awssdk.services.mediaconvert.model.OutputGroup;
import software.amazon.awssdk.services.mediaconvert.model.OutputGroupSettings;
import software.amazon.awssdk.services.mediaconvert.model.HlsGroupSettings;
import software.amazon.awssdk.services.mediaconvert.model.OutputGroupType;
import software.amazon.awssdk.services.mediaconvert.model.HlsDirectoryStructure;
import software.amazon.awssdk.services.mediaconvert.model.HlsManifestDurationFormat;
import software.amazon.awssdk.services.mediaconvert.model.HlsStreamInfResolution;
import software.amazon.awssdk.services.mediaconvert.model.HlsClientCache;
import software.amazon.awssdk.services.mediaconvert.model.HlsCaptionLanguageSetting;
import software.amazon.awssdk.services.mediaconvert.model.HlsManifestCompression;
import software.amazon.awssdk.services.mediaconvert.model.HlsCodecSpecification;
import software.amazon.awssdk.services.mediaconvert.model.HlsOutputSelection;
import software.amazon.awssdk.services.mediaconvert.model.HlsProgramDateTime;
import software.amazon.awssdk.services.mediaconvert.model.HlsTimedMetadataId3Frame;
import software.amazon.awssdk.services.mediaconvert.model.HlsSegmentControl;
import software.amazon.awssdk.services.mediaconvert.model.FileGroupSettings;
import software.amazon.awssdk.services.mediaconvert.model.ContainerSettings;
import software.amazon.awssdk.services.mediaconvert.model.VideoDescription;
import software.amazon.awssdk.services.mediaconvert.model.ContainerType;
import software.amazon.awssdk.services.mediaconvert.model.ScalingBehavior;
import software.amazon.awssdk.services.mediaconvert.model.VideoTimecodeInsertion;
import software.amazon.awssdk.services.mediaconvert.model.ColorMetadata;
import software.amazon.awssdk.services.mediaconvert.model.RespondToAfd;
import software.amazon.awssdk.services.mediaconvert.model.AfdSignaling;
import software.amazon.awssdk.services.mediaconvert.model.DropFrameTimecode;
import software.amazon.awssdk.services.mediaconvert.model.VideoCodecSettings;
import software.amazon.awssdk.services.mediaconvert.model.H264Settings;
import software.amazon.awssdk.services.mediaconvert.model.VideoCodec;
import software.amazon.awssdk.services.mediaconvert.model.CreateJobRequest;
import software.amazon.awssdk.services.mediaconvert.model.H264RateControlMode;
import software.amazon.awssdk.services.mediaconvert.model.H264QualityTuningLevel;
import software.amazon.awssdk.services.mediaconvert.model.H264SceneChangeDetect;
import software.amazon.awssdk.services.mediaconvert.model.AacAudioDescriptionBroadcasterMix;
import software.amazon.awssdk.services.mediaconvert.model.H264ParControl;
import software.amazon.awssdk.services.mediaconvert.model.AacRawFormat;
import software.amazon.awssdk.services.mediaconvert.model.H264QvbrSettings;
import software.amazon.awssdk.services.mediaconvert.model.H264FramerateConversionAlgorithm;
import software.amazon.awssdk.services.mediaconvert.model.H264CodecLevel;
import software.amazon.awssdk.services.mediaconvert.model.H264FramerateControl;
import software.amazon.awssdk.services.mediaconvert.model.AacCodingMode;
import software.amazon.awssdk.services.mediaconvert.model.H264Telecine;
import software.amazon.awssdk.services.mediaconvert.model.H264FlickerAdaptiveQuantization;
import software.amazon.awssdk.services.mediaconvert.model.H264GopSizeUnits;
import software.amazon.awssdk.services.mediaconvert.model.H264CodecProfile;
import software.amazon.awssdk.services.mediaconvert.model.H264GopBReference;
import software.amazon.awssdk.services.mediaconvert.model.AudioTypeControl;
import software.amazon.awssdk.services.mediaconvert.model.AntiAlias;
import software.amazon.awssdk.services.mediaconvert.model.H264SlowPal;
import software.amazon.awssdk.services.mediaconvert.model.H264SpatialAdaptiveQuantization;
import software.amazon.awssdk.services.mediaconvert.model.H264Syntax;
import software.amazon.awssdk.services.mediaconvert.model.M3u8Settings;
import software.amazon.awssdk.services.mediaconvert.model.InputDenoiseFilter;
import software.amazon.awssdk.services.mediaconvert.model.H264TemporalAdaptiveQuantization;
import software.amazon.awssdk.services.mediaconvert.model.CreateJobResponse;
import software.amazon.awssdk.services.mediaconvert.model.H264UnregisteredSeiTimecode;
import software.amazon.awssdk.services.mediaconvert.model.H264EntropyEncoding;
import software.amazon.awssdk.services.mediaconvert.model.InputPsiControl;
import software.amazon.awssdk.services.mediaconvert.model.ColorSpace;
import software.amazon.awssdk.services.mediaconvert.model.H264RepeatPps;
import software.amazon.awssdk.services.mediaconvert.model.H264FieldEncoding;
import software.amazon.awssdk.services.mediaconvert.model.M3u8NielsenId3;
import software.amazon.awssdk.services.mediaconvert.model.InputDeblockFilter;
import software.amazon.awssdk.services.mediaconvert.model.InputRotate;
import software.amazon.awssdk.services.mediaconvert.model.H264DynamicSubGop;
import software.amazon.awssdk.services.mediaconvert.model.TimedMetadata;
import software.amazon.awssdk.services.mediaconvert.model.JobSettings;
import software.amazon.awssdk.services.mediaconvert.model.AudioDefaultSelection;
import software.amazon.awssdk.services.mediaconvert.model.VideoSelector;
import software.amazon.awssdk.services.mediaconvert.model.AacSpecification;
import software.amazon.awssdk.services.mediaconvert.model.Input;
import software.amazon.awssdk.services.mediaconvert.model.OutputSettings;
import software.amazon.awssdk.services.mediaconvert.model.H264AdaptiveQuantization;
import software.amazon.awssdk.services.mediaconvert.model.AudioLanguageCodeControl;
import software.amazon.awssdk.services.mediaconvert.model.InputFilterEnable;
import software.amazon.awssdk.services.mediaconvert.model.AudioDescription;
import software.amazon.awssdk.services.mediaconvert.model.H264InterlaceMode;
import software.amazon.awssdk.services.mediaconvert.model.AudioCodecSettings;
import software.amazon.awssdk.services.mediaconvert.model.AacSettings;
import software.amazon.awssdk.services.mediaconvert.model.AudioCodec;
import software.amazon.awssdk.services.mediaconvert.model.AacRateControlMode;
import software.amazon.awssdk.services.mediaconvert.model.AacCodecProfile;
import software.amazon.awssdk.services.mediaconvert.model.HlsIFrameOnlyManifest;
import software.amazon.awssdk.services.mediaconvert.model.FrameCaptureSettings;
import software.amazon.awssdk.services.mediaconvert.model.AudioSelector;
import software.amazon.awssdk.services.mediaconvert.model.M3u8PcrControl;
import software.amazon.awssdk.services.mediaconvert.model.InputTimecodeSource;
import software.amazon.awssdk.services.mediaconvert.model.HlsSettings;
import software.amazon.awssdk.services.mediaconvert.model.M3u8Scte35Source;

/**
 * Create a MediaConvert job. Must supply MediaConvert access role Amazon
 * Resource Name (ARN), and a
 * valid video input file via Amazon S3 URL.
 *
 * Also, set up your development environment, including your credentials.
 *
 * For information, see this documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 */
public class CreateJob {
        public static void main(String[] args) {
                final String usage = """

                                Usage:
                                    <mcRoleARN> <fileInput>\s

                                Where:
                                    mcRoleARN - The MediaConvert Role ARN.\s
                                    fileInput -  The URL of an Amazon S3 bucket where the input file is located.\s
                                """;

                if (args.length != 2) {
                        System.out.println(usage);
                        System.exit(1);
                }

                String mcRoleARN = args[0];
                String fileInput = args[1];
                Region region = Region.US_WEST_2;
                MediaConvertClient mc = MediaConvertClient.builder()
                                .region(region)
                                .build();

                String id = createMediaJob(mc, mcRoleARN, fileInput);
                System.out.println("MediaConvert job created. Job Id = " + id);
                mc.close();
        }

        public static String createMediaJob(MediaConvertClient mc, String mcRoleARN, String fileInput) {

                String s3path = fileInput.substring(0, fileInput.lastIndexOf('/') + 1) + "javasdk/out/";
                String fileOutput = s3path + "index";
                String thumbsOutput = s3path + "thumbs/";
                String mp4Output = s3path + "mp4/";

                try {
                        System.out.println("MediaConvert role arn: " + mcRoleARN);
                        System.out.println("MediaConvert input file: " + fileInput);
                        System.out.println("MediaConvert output path: " + s3path);

                        // output group Preset HLS low profile
                        Output hlsLow = createOutput("hls_low", "_low", "_$dt$", 750000, 7, 1920, 1080, 640);
                        // output group Preset HLS media profile
                        Output hlsMedium = createOutput("hls_medium", "_medium", "_$dt$", 1200000, 7, 1920, 1080, 1280);
                        // output group Preset HLS high profole
                        Output hlsHigh = createOutput("hls_high", "_high", "_$dt$", 3500000, 8, 1920, 1080, 1920);

                        OutputGroup appleHLS = OutputGroup.builder().name("Apple HLS").customName("Example")
                                        .outputGroupSettings(OutputGroupSettings.builder()
                                                        .type(OutputGroupType.HLS_GROUP_SETTINGS)
                                                        .hlsGroupSettings(HlsGroupSettings.builder()
                                                                        .directoryStructure(
                                                                                        HlsDirectoryStructure.SINGLE_DIRECTORY)
                                                                        .manifestDurationFormat(
                                                                                        HlsManifestDurationFormat.INTEGER)
                                                                        .streamInfResolution(
                                                                                        HlsStreamInfResolution.INCLUDE)
                                                                        .clientCache(HlsClientCache.ENABLED)
                                                                        .captionLanguageSetting(
                                                                                        HlsCaptionLanguageSetting.OMIT)
                                                                        .manifestCompression(
                                                                                        HlsManifestCompression.NONE)
                                                                        .codecSpecification(
                                                                                        HlsCodecSpecification.RFC_4281)
                                                                        .outputSelection(
                                                                                        HlsOutputSelection.MANIFESTS_AND_SEGMENTS)
                                                                        .programDateTime(HlsProgramDateTime.EXCLUDE)
                                                                        .programDateTimePeriod(600)
                                                                        .timedMetadataId3Frame(
                                                                                        HlsTimedMetadataId3Frame.PRIV)
                                                                        .timedMetadataId3Period(10)
                                                                        .destination(fileOutput)
                                                                        .segmentControl(HlsSegmentControl.SEGMENTED_FILES)
                                                                        .minFinalSegmentLength((double) 0)
                                                                        .segmentLength(4).minSegmentLength(0).build())
                                                        .build())
                                        .outputs(hlsLow, hlsMedium, hlsHigh).build();

                        OutputGroup fileMp4 = OutputGroup.builder().name("File Group").customName("mp4")
                                        .outputGroupSettings(OutputGroupSettings.builder()
                                                        .type(OutputGroupType.FILE_GROUP_SETTINGS)
                                                        .fileGroupSettings(FileGroupSettings.builder()
                                                                        .destination(mp4Output).build())
                                                        .build())
                                        .outputs(Output.builder().extension("mp4")
                                                        .containerSettings(ContainerSettings.builder()
                                                                        .container(ContainerType.MP4).build())
                                                        .videoDescription(VideoDescription.builder().width(1280)
                                                                        .height(720)
                                                                        .scalingBehavior(ScalingBehavior.DEFAULT)
                                                                        .sharpness(50).antiAlias(AntiAlias.ENABLED)
                                                                        .timecodeInsertion(
                                                                                        VideoTimecodeInsertion.DISABLED)
                                                                        .colorMetadata(ColorMetadata.INSERT)
                                                                        .respondToAfd(RespondToAfd.NONE)
                                                                        .afdSignaling(AfdSignaling.NONE)
                                                                        .dropFrameTimecode(DropFrameTimecode.ENABLED)
                                                                        .codecSettings(VideoCodecSettings.builder()
                                                                                        .codec(VideoCodec.H_264)
                                                                                        .h264Settings(H264Settings
                                                                                                        .builder()
                                                                                                        .rateControlMode(
                                                                                                                        H264RateControlMode.QVBR)
                                                                                                        .parControl(H264ParControl.INITIALIZE_FROM_SOURCE)
                                                                                                        .qualityTuningLevel(
                                                                                                                        H264QualityTuningLevel.SINGLE_PASS)
                                                                                                        .qvbrSettings(
                                                                                                                        H264QvbrSettings.builder()
                                                                                                                                        .qvbrQualityLevel(
                                                                                                                                                        8)
                                                                                                                                        .build())
                                                                                                        .codecLevel(H264CodecLevel.AUTO)
                                                                                                        .codecProfile(H264CodecProfile.MAIN)
                                                                                                        .maxBitrate(2400000)
                                                                                                        .framerateControl(
                                                                                                                        H264FramerateControl.INITIALIZE_FROM_SOURCE)
                                                                                                        .gopSize(2.0)
                                                                                                        .gopSizeUnits(H264GopSizeUnits.SECONDS)
                                                                                                        .numberBFramesBetweenReferenceFrames(
                                                                                                                        2)
                                                                                                        .gopClosedCadence(
                                                                                                                        1)
                                                                                                        .gopBReference(H264GopBReference.DISABLED)
                                                                                                        .slowPal(H264SlowPal.DISABLED)
                                                                                                        .syntax(H264Syntax.DEFAULT)
                                                                                                        .numberReferenceFrames(
                                                                                                                        3)
                                                                                                        .dynamicSubGop(H264DynamicSubGop.STATIC)
                                                                                                        .fieldEncoding(H264FieldEncoding.PAFF)
                                                                                                        .sceneChangeDetect(
                                                                                                                        H264SceneChangeDetect.ENABLED)
                                                                                                        .minIInterval(0)
                                                                                                        .telecine(H264Telecine.NONE)
                                                                                                        .framerateConversionAlgorithm(
                                                                                                                        H264FramerateConversionAlgorithm.DUPLICATE_DROP)
                                                                                                        .entropyEncoding(
                                                                                                                        H264EntropyEncoding.CABAC)
                                                                                                        .slices(1)
                                                                                                        .unregisteredSeiTimecode(
                                                                                                                        H264UnregisteredSeiTimecode.DISABLED)
                                                                                                        .repeatPps(H264RepeatPps.DISABLED)
                                                                                                        .adaptiveQuantization(
                                                                                                                        H264AdaptiveQuantization.HIGH)
                                                                                                        .spatialAdaptiveQuantization(
                                                                                                                        H264SpatialAdaptiveQuantization.ENABLED)
                                                                                                        .temporalAdaptiveQuantization(
                                                                                                                        H264TemporalAdaptiveQuantization.ENABLED)
                                                                                                        .flickerAdaptiveQuantization(
                                                                                                                        H264FlickerAdaptiveQuantization.DISABLED)
                                                                                                        .softness(0)
                                                                                                        .interlaceMode(H264InterlaceMode.PROGRESSIVE)
                                                                                                        .build())
                                                                                        .build())
                                                                        .build())
                                                        .audioDescriptions(AudioDescription.builder()
                                                                        .audioTypeControl(AudioTypeControl.FOLLOW_INPUT)
                                                                        .languageCodeControl(
                                                                                        AudioLanguageCodeControl.FOLLOW_INPUT)
                                                                        .codecSettings(AudioCodecSettings.builder()
                                                                                        .codec(AudioCodec.AAC)
                                                                                        .aacSettings(AacSettings
                                                                                                        .builder()
                                                                                                        .codecProfile(AacCodecProfile.LC)
                                                                                                        .rateControlMode(
                                                                                                                        AacRateControlMode.CBR)
                                                                                                        .codingMode(AacCodingMode.CODING_MODE_2_0)
                                                                                                        .sampleRate(44100)
                                                                                                        .bitrate(160000)
                                                                                                        .rawFormat(AacRawFormat.NONE)
                                                                                                        .specification(AacSpecification.MPEG4)
                                                                                                        .audioDescriptionBroadcasterMix(
                                                                                                                        AacAudioDescriptionBroadcasterMix.NORMAL)
                                                                                                        .build())
                                                                                        .build())
                                                                        .build())
                                                        .build())
                                        .build();
                        OutputGroup thumbs = OutputGroup.builder().name("File Group").customName("thumbs")
                                        .outputGroupSettings(OutputGroupSettings.builder()
                                                        .type(OutputGroupType.FILE_GROUP_SETTINGS)
                                                        .fileGroupSettings(FileGroupSettings.builder()
                                                                        .destination(thumbsOutput).build())
                                                        .build())
                                        .outputs(Output.builder().extension("jpg")
                                                        .containerSettings(ContainerSettings.builder()
                                                                        .container(ContainerType.RAW).build())
                                                        .videoDescription(VideoDescription.builder()
                                                                        .scalingBehavior(ScalingBehavior.DEFAULT)
                                                                        .sharpness(50).antiAlias(AntiAlias.ENABLED)
                                                                        .timecodeInsertion(
                                                                                        VideoTimecodeInsertion.DISABLED)
                                                                        .colorMetadata(ColorMetadata.INSERT)
                                                                        .dropFrameTimecode(DropFrameTimecode.ENABLED)
                                                                        .codecSettings(VideoCodecSettings.builder()
                                                                                        .codec(VideoCodec.FRAME_CAPTURE)
                                                                                        .frameCaptureSettings(
                                                                                                        FrameCaptureSettings
                                                                                                                        .builder()
                                                                                                                        .framerateNumerator(
                                                                                                                                        1)
                                                                                                                        .framerateDenominator(
                                                                                                                                        1)
                                                                                                                        .maxCaptures(10000000)
                                                                                                                        .quality(80)
                                                                                                                        .build())
                                                                                        .build())
                                                                        .build())
                                                        .build())
                                        .build();

                        Map<String, AudioSelector> audioSelectors = new HashMap<>();
                        audioSelectors.put("Audio Selector 1",
                                        AudioSelector.builder().defaultSelection(AudioDefaultSelection.DEFAULT)
                                                        .offset(0).build());

                        JobSettings jobSettings = JobSettings.builder().inputs(Input.builder()
                                        .audioSelectors(audioSelectors)
                                        .videoSelector(
                                                        VideoSelector.builder().colorSpace(ColorSpace.FOLLOW)
                                                                        .rotate(InputRotate.DEGREE_0).build())
                                        .filterEnable(InputFilterEnable.AUTO).filterStrength(0)
                                        .deblockFilter(InputDeblockFilter.DISABLED)
                                        .denoiseFilter(InputDenoiseFilter.DISABLED).psiControl(InputPsiControl.USE_PSI)
                                        .timecodeSource(InputTimecodeSource.EMBEDDED).fileInput(fileInput).build())
                                        .outputGroups(appleHLS, thumbs, fileMp4).build();

                        CreateJobRequest createJobRequest = CreateJobRequest.builder().role(mcRoleARN)
                                        .settings(jobSettings)
                                        .build();

                        CreateJobResponse createJobResponse = mc.createJob(createJobRequest);
                        return createJobResponse.job().id();

                } catch (MediaConvertException e) {
                        System.out.println(e.toString());
                        System.exit(0);
                }
                return "";
        }

        private final static Output createOutput(String customName,
                        String nameModifier,
                        String segmentModifier,
                        int qvbrMaxBitrate,
                        int qvbrQualityLevel,
                        int originWidth,
                        int originHeight,
                        int targetWidth) {

                int targetHeight = Math.round(originHeight * targetWidth / originWidth)
                                - (Math.round(originHeight * targetWidth / originWidth) % 4);
                Output output = null;
                try {
                        output = Output.builder().nameModifier(nameModifier).outputSettings(OutputSettings.builder()
                                        .hlsSettings(HlsSettings.builder().segmentModifier(segmentModifier)
                                                        .audioGroupId("program_audio")
                                                        .iFrameOnlyManifest(HlsIFrameOnlyManifest.EXCLUDE).build())
                                        .build())
                                        .containerSettings(ContainerSettings.builder().container(ContainerType.M3_U8)
                                                        .m3u8Settings(M3u8Settings.builder().audioFramesPerPes(4)
                                                                        .pcrControl(M3u8PcrControl.PCR_EVERY_PES_PACKET)
                                                                        .pmtPid(480).privateMetadataPid(503)
                                                                        .programNumber(1).patInterval(0).pmtInterval(0)
                                                                        .scte35Source(M3u8Scte35Source.NONE)
                                                                        .scte35Pid(500).nielsenId3(M3u8NielsenId3.NONE)
                                                                        .timedMetadata(TimedMetadata.NONE)
                                                                        .timedMetadataPid(502).videoPid(481)
                                                                        .audioPids(482, 483, 484, 485, 486, 487, 488,
                                                                                        489, 490, 491, 492)
                                                                        .build())
                                                        .build())
                                        .videoDescription(
                                                        VideoDescription.builder().width(targetWidth)
                                                                        .height(targetHeight)
                                                                        .scalingBehavior(ScalingBehavior.DEFAULT)
                                                                        .sharpness(50).antiAlias(AntiAlias.ENABLED)
                                                                        .timecodeInsertion(
                                                                                        VideoTimecodeInsertion.DISABLED)
                                                                        .colorMetadata(ColorMetadata.INSERT)
                                                                        .respondToAfd(RespondToAfd.NONE)
                                                                        .afdSignaling(AfdSignaling.NONE)
                                                                        .dropFrameTimecode(DropFrameTimecode.ENABLED)
                                                                        .codecSettings(VideoCodecSettings.builder()
                                                                                        .codec(VideoCodec.H_264)
                                                                                        .h264Settings(H264Settings
                                                                                                        .builder()
                                                                                                        .rateControlMode(
                                                                                                                        H264RateControlMode.QVBR)
                                                                                                        .parControl(H264ParControl.INITIALIZE_FROM_SOURCE)
                                                                                                        .qualityTuningLevel(
                                                                                                                        H264QualityTuningLevel.SINGLE_PASS)
                                                                                                        .qvbrSettings(H264QvbrSettings
                                                                                                                        .builder()
                                                                                                                        .qvbrQualityLevel(
                                                                                                                                        qvbrQualityLevel)
                                                                                                                        .build())
                                                                                                        .codecLevel(H264CodecLevel.AUTO)
                                                                                                        .codecProfile((targetHeight > 720
                                                                                                                        && targetWidth > 1280)
                                                                                                                                        ? H264CodecProfile.HIGH
                                                                                                                                        : H264CodecProfile.MAIN)
                                                                                                        .maxBitrate(qvbrMaxBitrate)
                                                                                                        .framerateControl(
                                                                                                                        H264FramerateControl.INITIALIZE_FROM_SOURCE)
                                                                                                        .gopSize(2.0)
                                                                                                        .gopSizeUnits(H264GopSizeUnits.SECONDS)
                                                                                                        .numberBFramesBetweenReferenceFrames(
                                                                                                                        2)
                                                                                                        .gopClosedCadence(
                                                                                                                        1)
                                                                                                        .gopBReference(H264GopBReference.DISABLED)
                                                                                                        .slowPal(H264SlowPal.DISABLED)
                                                                                                        .syntax(H264Syntax.DEFAULT)
                                                                                                        .numberReferenceFrames(
                                                                                                                        3)
                                                                                                        .dynamicSubGop(H264DynamicSubGop.STATIC)
                                                                                                        .fieldEncoding(H264FieldEncoding.PAFF)
                                                                                                        .sceneChangeDetect(
                                                                                                                        H264SceneChangeDetect.ENABLED)
                                                                                                        .minIInterval(0)
                                                                                                        .telecine(H264Telecine.NONE)
                                                                                                        .framerateConversionAlgorithm(
                                                                                                                        H264FramerateConversionAlgorithm.DUPLICATE_DROP)
                                                                                                        .entropyEncoding(
                                                                                                                        H264EntropyEncoding.CABAC)
                                                                                                        .slices(1)
                                                                                                        .unregisteredSeiTimecode(
                                                                                                                        H264UnregisteredSeiTimecode.DISABLED)
                                                                                                        .repeatPps(H264RepeatPps.DISABLED)
                                                                                                        .adaptiveQuantization(
                                                                                                                        H264AdaptiveQuantization.HIGH)
                                                                                                        .spatialAdaptiveQuantization(
                                                                                                                        H264SpatialAdaptiveQuantization.ENABLED)
                                                                                                        .temporalAdaptiveQuantization(
                                                                                                                        H264TemporalAdaptiveQuantization.ENABLED)
                                                                                                        .flickerAdaptiveQuantization(
                                                                                                                        H264FlickerAdaptiveQuantization.DISABLED)
                                                                                                        .softness(0)
                                                                                                        .interlaceMode(H264InterlaceMode.PROGRESSIVE)
                                                                                                        .build())
                                                                                        .build())
                                                                        .build())
                                        .audioDescriptions(AudioDescription.builder()
                                                        .audioTypeControl(AudioTypeControl.FOLLOW_INPUT)
                                                        .languageCodeControl(AudioLanguageCodeControl.FOLLOW_INPUT)
                                                        .codecSettings(AudioCodecSettings.builder()
                                                                        .codec(AudioCodec.AAC).aacSettings(AacSettings
                                                                                        .builder()
                                                                                        .codecProfile(AacCodecProfile.LC)
                                                                                        .rateControlMode(
                                                                                                        AacRateControlMode.CBR)
                                                                                        .codingMode(AacCodingMode.CODING_MODE_2_0)
                                                                                        .sampleRate(44100)
                                                                                        .bitrate(96000)
                                                                                        .rawFormat(AacRawFormat.NONE)
                                                                                        .specification(AacSpecification.MPEG4)
                                                                                        .audioDescriptionBroadcasterMix(
                                                                                                        AacAudioDescriptionBroadcasterMix.NORMAL)
                                                                                        .build())
                                                                        .build())
                                                        .build())
                                        .build();
                } catch (MediaConvertException e) {
                        e.printStackTrace();
                        System.exit(0);
                }
                return output;
        }
}
```
+  For API details, see [CreateJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconvert-2017-08-29/CreateJob) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/mediaconvert#code-examples).

```
suspend fun createMediaJob(
    mcClient: MediaConvertClient,
    mcRoleARN: String,
    fileInput1: String,
): String? {
    // Step 1: Describe endpoints to get the MediaConvert endpoint URL
    val describeResponse = mcClient.describeEndpoints(
        DescribeEndpointsRequest {
            maxResults = 1
        },
    )

    val endpointUrl = describeResponse.endpoints?.firstOrNull()?.url
        ?: error("No MediaConvert endpoint found")

    // Step 2: Create MediaConvert client with resolved endpoint
    val mediaConvert = MediaConvertClient.fromEnvironment {
        region = "us-west-2"
        endpointProvider = MediaConvertEndpointProvider {
            Endpoint(endpointUrl)
        }
    }

    // Output destination folder in S3 - put in 'output/' folder beside input
    val outputDestination = fileInput1.substringBeforeLast('/') + "/output/"

    // Step 3: Create the job request with minimal valid video codec settings
    val jobRequest = CreateJobRequest {
        role = mcRoleARN
        settings = JobSettings {
            inputs = listOf(
                Input {
                    fileInput = fileInput1
                },
            )
            outputGroups = listOf(
                OutputGroup {
                    outputGroupSettings = OutputGroupSettings {
                        type = OutputGroupType.FileGroupSettings
                        fileGroupSettings = FileGroupSettings {
                            destination = outputDestination
                        }
                    }
                    outputs = listOf(
                        Output {
                            containerSettings = ContainerSettings {
                                container = ContainerType.Mp4
                            }
                            videoDescription = VideoDescription {
                                width = 1280
                                height = 720
                                codecSettings = VideoCodecSettings {
                                    codec = VideoCodec.H264
                                    h264Settings = H264Settings {
                                        rateControlMode = H264RateControlMode.Qvbr
                                        qvbrSettings = H264QvbrSettings {
                                            qvbrQualityLevel = 7
                                        }
                                        maxBitrate = 5_000_000
                                        codecLevel = H264CodecLevel.Auto
                                        codecProfile = H264CodecProfile.Main
                                        framerateControl = H264FramerateControl.InitializeFromSource
                                    }
                                }
                            }
                        },
                    )
                },
            )
        }
    }

    // Step 4: Call MediaConvert to create the job
    val response = mediaConvert.createJob(jobRequest)

    // Return the job ID or null if not found
    return response.job?.id
}
```
+  For API details, see [CreateJob](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
