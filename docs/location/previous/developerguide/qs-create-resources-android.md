---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-create-resources-android.html
---

# Create Amazon Location resources for your app
<a name="qs-create-resources-android"></a>

If you do not already have them, you must create the Amazon Location resources that your application will use. Here, you create a map resource to display maps in your application, a place index to search for locations on the map, and a tracker to track an object across the map.

**To add location resources to your application**

1. Choose the map style that you want to use.

   1. In the Amazon Location console, on the [Maps](https://console.aws.amazon.com/location/maps/home) page, choose **Create map** to preview map styles.

   1. Add a **Name** and **Description** for the new map resource. Make a note of the name that you use for the map resource. You will need it when creating your script file later in the tutorial.

   1. We recommend you choose the HERE map style for your map.
**Note**
Choosing a map style also chooses which map data provider that you will use. If your application is tracking or routing assets that you use in your business, such as delivery vehicles or employees, you may only use HERE as your geolocation provider. For more information, see section 82 of the [AWS service terms](https://aws.amazon.com/service-terms).

   1. Agree to the **Amazon Location Terms and Conditions**, then choose **Create map**. You can interact with the map that you've chosen: zoom in, zoom out, or pan in any direction.

   1. Make a note of the Amazon Resource Name (ARN) that is shown for your new map resource. You'll use it to create the correct authentication later in this tutorial.

1. Choose the place index that you want to use.

   1. In the Amazon Location console on the [**Place indexes**](https://console.aws.amazon.com/location/places/home) page, choose **Create place index**.

   1. Add a **Name** and **Description** for the new place index resource. Make a note of the name that you use for the place index resource. You will need it when creating your script file later in the tutorial.

   1. Choose a data provider.
**Note**
In most cases, choose the data provider that matches the map provider that you already chose. This helps to ensure that the searches will match the maps.
If your application is tracking or routing assets that you use in your business, such as delivery vehicles or employees, you may only use HERE as your geolocation provider. For more information, see section 82 of the [AWS service terms](https://aws.amazon.com/service-terms).

   1. Choose the **Data storage option**. For this tutorial, the results are not stored, so you can choose ** No, single use only**.

   1. Agree to the **Amazon Location Terms and Conditions**, then choose **Create place index**.

   1. Make a note of the ARN that is shown for your new place index resource. You'll use it to create the correct authentication in the next section of this tutorial.

1. To create a tracker using the Amazon Location console.

   1.  Open the [Amazon Location Service console](https://console.aws.amazon.com/location/).

   1.  In the left navigation pane, choose **Trackers**.

   1.  Choose **Create tracker**.

   1.  Fill in the all the required fields.

   1.  Under **Position filtering**, we recommend you use the default setting: **TimeBased**.

   1.  Choose **Create tracker** to finish.
