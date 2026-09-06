---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/example-bg-filter.html
---

# Example background filter for the Amazon Chime SDK
<a name="example-bg-filter"></a>

The following example shows how to implement the filters.

```
import {
    VideoFxConfig,
    VideoFxTypeConversion,
    VideoTransformDevice,
    DefaultVideoTransformDevice,
    Logger,
    VideoFxProcessor,
    MeetingSession
} from 'amazon-chime-sdk-js';

let videoTransformDevice: VideoTransformDevice | undefined = undefined;
let videoFxProcessor: VideoFxProcessor | undefined = undefined;

const videoFxConfig: VideoFxConfig = {
    backgroundBlur: {
        isEnabled: {{false}},
        strength: "{{medium}}"
    },
    backgroundReplacement: {
        isEnabled: false,
        backgroundImageURL: '{{space.jpg}}',
        defaultColor: undefined,
    }
}

export const addEffectsToMeeting = async (videoInputDevice: MediaDeviceInfo, meetingSession: MeetingSession, logger: Logger): Promise<void> => {
    try {
        videoFxProcessor = await VideoFxProcessor.create(logger, videoFxConfig);
    } catch (error) {
        logger.error(error.toString());
        return;
    }

    videoTransformDevice = new DefaultVideoTransformDevice(
        logger,
        videoInputDevice,
        [videoFxProcessor]
    );

    await meetingSession.audioVideo.startVideoInput(videoTransformDevice);
}

export const enableReplacement = async (logger: Logger) => {
    videoFxConfig.backgroundBlur.isEnabled = {{false}};
    videoFxConfig.backgroundReplacement.isEnabled = {{true}};
    await updateVideoFxConfig(videoFxConfig, logger);
}

export const enableBlur = async (logger: Logger) => {
    videoFxConfig.backgroundReplacement.isEnabled = {{false}};
    videoFxConfig.backgroundBlur.isEnabled = {{true}};
    await updateVideoFxConfig(videoFxConfig, logger);
}

export const pauseEffects = async (logger: Logger) => {
    videoFxConfig.backgroundReplacement.isEnabled = {{false}};
    videoFxConfig.backgroundBlur.isEnabled = {{false}};
    await updateVideoFxConfig(videoFxConfig, logger);

}

export const setReplacementImage = async (newImageUrl: string, logger: Logger) => {
    videoFxConfig.backgroundReplacement.backgroundImageURL = {{newImageUrl}};
    videoFxConfig.backgroundReplacement.defaultColor = undefined;
    await updateVideoFxConfig(videoFxConfig, logger);
}

export const setReplacementDefaultColor = async (newHexColor: string, logger: Logger) => {
    videoFxConfig.backgroundReplacement.defaultColor = {{newHexColor}};
    videoFxConfig.backgroundReplacement.backgroundImageURL = undefined;
    await updateVideoFxConfig(videoFxConfig, logger);
}

export const setBlurStrength = async (newStrength: number, logger: Logger) => {
    videoFxConfig.backgroundBlur.strength = VideoFxTypeConversion.useBackgroundBlurStrengthType(newStrength);
    await updateVideoFxConfig(videoFxConfig, logger);

}

export const updateVideoFxConfig = async (config: VideoFxConfig, logger: Logger) => {
    try {
        await videoFxProcessor.setEffectConfig(videoFxConfig);
    } catch (error) {
        logger.error(error.toString())
    }
}

export const turnOffEffects = () => {
    const innerDevice = await videoTransformDevice?.intrinsicDevice();
    await videoTransformDevice?.stop();
    videoTransformDevice = undefined;
    videoFxProcessor = undefined;
    await meetingSession.audioVideo.startVideoInput(innerDevice);
}
```
