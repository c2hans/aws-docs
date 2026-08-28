---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-add-map-android.html
---

# Add an Amazon Location interactive map to your application
<a name="qs-add-map-android"></a>

Now that you have created a basic application, you can add map control to your application. This tutorial uses API keys for managing the map view. The map control itself is part of the [MapLibre Native library](https://github.com/maplibre/maplibre-native), with the API key and MapLibre, and the map data comes from Amazon Location.

To add a map to your application you will have to perform the following actions:
+ Add the MapLibre dependency to your project.
+ Set up the map view code with compose.
+ Write code to show the map.

Use the following procedure to add the map to your app:

1. Add the MapLibre dependency to your project

   1. In AndroidStudio, select the **View** menu, and choose **Tool Windows**, **Project**. This will open the Project window, which gives you access to all the files in your project.

   1. In the **Project** window, open **gradle** then open the `libs.versions.toml` file in the tree view. This will open the `libs.versions.toml` file for editing. Now add the below version and libraries data in the `libs.versions.toml` file.

      ```
      [versions]
       ...
       auth = "0.2.4"
       tracking = "0.2.4"

       [libraries]
       ...
       auth = { group = "software.amazon.location", name = "auth", version.ref = "auth" }
       tracking = { module = "software.amazon.location:tracking", version.ref = "tracking" }

       [plugins]
       ...
      ```

   1. After you finish editing the `libs.versions.toml` file, AndroidStudio must re-sync the project. At the top of the `libs.versions.toml` editing window, AndroidStudio prompts you to sync. Select 'Sync Now' to sync your project before continuing.

   1. In the Project window, open Gradle Scripts in the tree view and select the `build.gradle` file for your application module. This will open the `build.gradle` file for editing.

   1. At the bottom of the file, in the dependencies section, add the following dependency.

      ```
      dependencies {
          ...
          implementation(libs.org.maplibre.gl)
       }
      ```

   1. After you finish adding the Gradle dependencies, Android Studio must re-sync the project. At the top of the **build.gradle** editing window, Android Studio, select **Sync Now** to sync your project before continuing.

1. Now you will set up the map view code with compose. Use the following steps:

   1. From the Project window, open App, Java, {{your package name}} in the tree view, and go to the **ui** folder, inside the **ui** folder create a **view** directory.

   1. Inside **view** directory create a `MapLoadScreen.kt` file.

   1. Add the following code to your `MapLoadScreen.kt` file.

      ```
      import androidx.compose.foundation.layout.Box
      import androidx.compose.foundation.layout.fillMaxHeight
      import androidx.compose.foundation.layout.fillMaxWidth
      import androidx.compose.runtime.Composable
      import androidx.compose.ui.Modifier
      import androidx.compose.ui.viewinterop.AndroidView
      import org.maplibre.android.maps.OnMapReadyCallback

       @Composable
       fun MapLoadScreen(
           mapReadyCallback: OnMapReadyCallback,
       ) {
           Box(
               modifier = Modifier
                   .fillMaxWidth()
                   .fillMaxHeight(),
           ) {
               MapView(mapReadyCallback)
           }
       }

       @Composable
       fun MapView(mapReadyCallback: OnMapReadyCallback) {
           AndroidView(
               factory = { context ->
                   val mapView = org.maplibre.android.maps.MapView(context)
                   mapView.onCreate(null)
                   mapView.getMapAsync(mapReadyCallback)
                   mapView
               },
           )
       }
      ```

1. Write code to show the map.

   1. Add the following code to your `MainActivity.kt` file.

      ```
      // ...other imports
      import org.maplibre.android.MapLibre
      import org.maplibre.android.camera.CameraPosition
      import org.maplibre.android.geometry.LatLng
      import org.maplibre.android.maps.MapLibreMap
      import org.maplibre.android.maps.OnMapReadyCallback
      import org.maplibre.android.maps.Style

       class MainActivity : ComponentActivity(), OnMapReadyCallback {
           private val region = "{{YOUR_AWS_REGION}}"
           private val mapName = "{{YOUR_AWS_MAP_NAME}}"
           private val apiKey = "{{YOUR_AWS_API_KEY}}"
           override fun onCreate(savedInstanceState: Bundle?) {
               MapLibre.getInstance(this)
               super.onCreate(savedInstanceState)
               setContent {
                   TestMapAppTheme {
                       Surface(
                           modifier = Modifier.fillMaxSize(),
                           color = MaterialTheme.colorScheme.background
                       ) {
                           MapLoadScreen(this)
                       }
                   }
               }
           }

           override fun onMapReady(map: MapLibreMap) {
               map.setStyle(
                   Style.Builder()
                       .fromUri(
                           "https://maps.geo.$region.amazonaws.com/maps/v0/maps/$mapName/style-descriptor?key=$apiKey"
                       ),
               ) {
                   map.uiSettings.isAttributionEnabled = true
                   map.uiSettings.isLogoEnabled = false
                   map.uiSettings.attributionGravity = Gravity.BOTTOM or Gravity.END
                   val initialPosition = LatLng(47.6160281982247, -122.32642111977668)
                   map.cameraPosition = CameraPosition.Builder()
                       .target(initialPosition)
                       .zoom(14.0)
                       .build()
               }
           }
       }
      ```

   1. Save the `MainActivity.kt` file. You can now build the application. To run it, you may have to set up a device to emulate it in AndroidStudio, or use the app on your device. Use this app to see how the map control behaves. You can pan by dragging it on the map and pinching it to zoom.

      In the next section, you will add a marker on the map and show the address of the location where the marker is as you move the map.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
