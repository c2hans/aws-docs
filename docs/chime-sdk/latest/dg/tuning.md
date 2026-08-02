---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/tuning.html
---

# Tuning resource utilization for the Amazon Chime SDK
<a name="tuning"></a>

When creating the `VideoFxProcessor`, you can supply the optional `processingBudgetPerFrame` parameter and control the amount of CPU and GPU that the filters use.

```
let videoFxProcessor: VideoFxProcessor | undefined = undefined;
const processingBudgetPerFrame = {{50}};
try {
  videoFxProcessor = await VideoFxProcessor.create(logger, videoFxConfig, processingBudgetPerFrame);
} catch (error) {
  logger.warn(error.toString());
}
```

The `VideoFxProcessor` requires time to process a frame. The amount of time depends on the device, the browser, and what else is running in the browser or on the device. The processor uses the concept of a *budget* to target the amount of time used to process and render each frame.

Processing time is in milliseconds. As an example of how to use a budget, 1 second has 1000ms. Targeting 15 frames per second of video capture results in a total budget of 1000ms/15fps = 66ms. You can set a budget of 50% of that, or 33ms, by supplying the value `50` in the `processingBudgetPerFrame` parameter, as shown in the example above.

The `VideoFxProcessor` then tries to process the frames within the budget specified. If processing runs over budget, the processor reduces visual quality to stay within budget. The processor continues to reduce visual quality to a minimum, at which point it stops reducing. This processing duration is measured continually, so if more resources become available, such as another app closing and freeing up CPU, the processor raises visual quality again until it hits the budget, or maximum visual quality is achieved.

If you don't supply a value to `processingBudgetPerFrame`, the `VideoFxProcessor` defaults to `50`.
