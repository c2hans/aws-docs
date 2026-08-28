---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-add-tracking-android.html
---

# Add Amazon Location tracking to your application
<a name="qs-add-tracking-android"></a>

To add tracking to your sample application, follow these steps:

1. Add tracking and auth SDK dependencies to your project.

1. Include permission and service entries in your AndroidManifest.xml file.

1. Set up the start/stop tracking button code with compose.

1. Add code for creating a LocationTracker object and start and stop tracking.

1. Create a test route with Android Emulator.

1. **Add tracking and auth SDK dependencies to your project.**

   1. In the **Project** window, open **gradle** then open the `libs.versions.toml` file in the tree view. This will open the `libs.versions.toml` file for editing. Now add the below version and libraries data in the `libs.versions.toml` file.

      ```
      [versions]
       ...
       auth = "0.0.1"
       tracking = "0.0.1"

       [libraries]
       ...
       auth = { group = "software.amazon.location", name = "auth", version.ref = "auth" }
       tracking = { module = "software.amazon.location:tracking", version.ref = "tracking" }

       [plugins]
       ...
      ```

   1. After you finish editing the `libs.versions.toml` file, AndroidStudio must re-sync the project. At the top of the `libs.versions.toml` editing window, AndroidStudio prompts you to sync. Select 'Sync Now' to sync your project before continuing.

   1. In the Project window, open Gradle Scripts in the tree view and select the `build.gradle` file for your application module. This will open the `build.gradle` file for editing.

   1. At the bottom of the file, in the **dependencies** section, add the following dependency.

      ```
      dependencies {
          ...
          implementation(libs.auth)
          implementation(libs.tracking)
       }
      ```

   1. After you finish editing the Gradle dependencies, AndroidStudio must re-sync the project. At the top of the **build.gradle** editing window, AndroidStudio prompts you to sync. Select **SyncNow** to sync your project before continuing.

1. **Include permission and service entries in your AndroidManifest.xml file.**

   1. To include the correct permission and service entries in your `AndroidManifest.xml file`, update the file with the following code:

     ```
     <?xml version="1.0" encoding="utf-8"?>
     <manifest xmlns:android="http://schemas.android.com/apk/res/android"
         xmlns:tools="http://schemas.android.com/tools">

         <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
         <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
         <uses-permission android:name="android.permission.INTERNET"/>
         <application
             android:allowBackup="true"
             android:dataExtractionRules="@xml/data_extraction_rules"
             android:fullBackupContent="@xml/backup_rules"
             android:icon="@mipmap/ic_launcher"
             android:label="@string/app_name"
             android:roundIcon="@mipmap/ic_launcher_round"
             android:supportsRtl="true"
             android:theme="@style/Theme.AndroidQuickStartApp"
             tools:targetApi="31">
             <activity
                 android:name=".MainActivity"
                 android:exported="true"
                 android:label="@string/app_name"
                 android:theme="@style/Theme.AndroidQuickStartApp">
                 <intent-filter>
                     <action android:name="android.intent.action.MAIN" />

                     <category android:name="android.intent.category.LAUNCHER" />
                 </intent-filter>
             </activity>
         </application>

     </manifest>
     ```

1. **Set up the start/stop tracking button code with compose.**

   1. Add two images of Play and Pause in **res** under **drawable** named as **ic\_pause** and **ic\_play**. You can also access the image from [GitHub](https://github.com/aws-geospatial/amazon-location-samples-android/tree/main/quick-start/res/drawable).

   1. If it's not open already, open the `MapLoadScreen.kt` file, as in the previous procedure. Add the following code. This will create a compose Button view where we can click on it to **start** and **stop** tracking.

      ```
      // ...other imports
      import androidx.compose.material3.Button
      import androidx.compose.material3.ButtonDefaults

      @Composable
      fun MapLoadScreen(
          mapReadyCallback: OnMapReadyCallback,
          mainViewModel: MainViewModel,
          onStartStopTrackingClick: () -> Unit
      ) {
          Box(
              modifier = Modifier
                  .fillMaxWidth()
                  .fillMaxHeight(),
          ) {
              MapView(mapReadyCallback)
              Box(
                  modifier = Modifier
                      .align(Alignment.Center),
              ) {
                  Image(
                      painter = painterResource(id = R.drawable.red_marker),
                      contentDescription = "marker",
                      modifier = Modifier
                          .size(40.dp)
                          .align(Alignment.Center),
                  )
              }
              if (mainViewModel.isLabelAdded) {
                  Column(
                      modifier = Modifier.fillMaxSize(),
                      verticalArrangement = Arrangement.Bottom
                  ) {
                      Box(
                          modifier = Modifier
                              .fillMaxWidth()
                              .background(Color.White),
                      ) {
                          Text(
                              text = mainViewModel.label,
                              modifier = Modifier
                                  .padding(16.dp)
                                  .align(Alignment.Center)
                                  .testTag("label")
                                  .semantics {
                                      contentDescription = "label"
                                  },
                              fontSize = 14.sp,
                          )
                      }
                      Spacer(modifier = Modifier.height(80.dp))
                  }
              }
              Column(
                  modifier = Modifier
                      .fillMaxSize()
                      .padding(bottom = 16.dp),
                  horizontalAlignment = Alignment.CenterHorizontally,
                  verticalArrangement = Arrangement.Bottom,
              ) {
                  Button(
                      onClick = onStartStopTrackingClick,
                      modifier = Modifier
                          .padding(horizontal = 16.dp)
                  ) {
                      Text(
                          text = if (mainViewModel.isLocationTrackingForegroundActive) "Stop tracking" else "Start tracking",
                          color = Color.Black
                      )
                      Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                      Image(
                          painter = painterResource(id = if (mainViewModel.isLocationTrackingForegroundActive) R.drawable.ic_pause else R.drawable.ic_play),
                          contentDescription = if (mainViewModel.isLocationTrackingForegroundActive) "stop_tracking" else "start_tracking"
                      )
                  }
              }
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

1. **Add code for creating a LocationTracker object and start and stop tracking.**

   1. Add the following code inside the `MainViewModel.kt` file.

      ```
      ...
      var isLocationTrackingForegroundActive: Boolean by mutableStateOf(false)
      var locationTracker: LocationTracker? = null
      ```

   1. Add the following code to your `MainActivity.kt` file.

      ```
      // ...other imports
      import software.amazon.location.auth.AuthHelper
      import software.amazon.location.auth.LocationCredentialsProvider
      import software.amazon.location.tracking.LocationTracker
      import software.amazon.location.tracking.aws.LocationTrackingCallback
      import software.amazon.location.tracking.config.LocationTrackerConfig
      import software.amazon.location.tracking.database.LocationEntry
      import software.amazon.location.tracking.filters.DistanceLocationFilter
      import software.amazon.location.tracking.filters.TimeLocationFilter
      import software.amazon.location.tracking.util.TrackingSdkLogLevel

      class MainActivity : ComponentActivity(), OnMapReadyCallback,
          MapLibreMap.OnCameraMoveStartedListener, MapLibreMap.OnCameraIdleListener {

          private val mainViewModel: MainViewModel by viewModels()
          private val poolId = "{{YOUR_AWS_IDENTITY_POOL_ID}}"
          private val trackerName = "{{YOUR_AWS_TRACKER_NAME}}"
          private val region = "{{YOUR_AWS_REGION}}"
          private val mapName = "{{YOUR_AWS_MAP_NAME}}"
          private val apiKey = "{{YOUR_AWS_API_KEY}}"
          private val coroutineScope = MainScope()
          private lateinit var locationCredentialsProvider: LocationCredentialsProvider
          private lateinit var authHelper: AuthHelper

          override fun onCreate(savedInstanceState: Bundle?) {
              MapLibre.getInstance(this)
              super.onCreate(savedInstanceState)
              setContent {
                  TestMapAppTheme {
                      Surface(
                          modifier = Modifier.fillMaxSize(),
                          color = MaterialTheme.colorScheme.background
                      ) {
                          MapLoadScreen(this, mainViewModel, onStartStopTrackingClick = {
                              if (mainViewModel.isLocationTrackingForegroundActive) {
                                  mainViewModel.isLocationTrackingForegroundActive = false
                                  mainViewModel.locationTracker?.stop()
                              } else {
                                  if (checkLocationPermission(this)) return@MapLoadScreen
                                  mainViewModel.isLocationTrackingForegroundActive = true
                                  mainViewModel.locationTracker?.start(locationTrackingCallback = object :
                                      LocationTrackingCallback {
                                      override fun onLocationAvailabilityChanged(locationAvailable: Boolean) {
                                      }

                                      override fun onLocationReceived(location: LocationEntry) {
                                      }

                                      override fun onUploadSkipped(entries: LocationEntry) {
                                      }

                                      override fun onUploadStarted(entries: List{{LocationEntry}}) {
                                      }

                                      override fun onUploaded(entries: List{{LocationEntry}}) {
                                      }

                                  })
                              }
                          })
                      }
                  }
              }
              authenticateUser()
          }

          private fun authenticateUser() {
              coroutineScope.launch {
                  authHelper = AuthHelper(applicationContext)
                  locationCredentialsProvider = authHelper.authenticateWithCognitoIdentityPool(
                      poolId,
                  )
                  locationCredentialsProvider.let {
                      val config = LocationTrackerConfig(
                          trackerName = trackerName,
                          logLevel = TrackingSdkLogLevel.DEBUG,
                          latency = 1000,
                          frequency = 5000,
                          waitForAccurateLocation = false,
                          minUpdateIntervalMillis = 5000,
                      )
                      mainViewModel.locationTracker = LocationTracker(
                          applicationContext,
                          it,
                          config,
                      )
                      mainViewModel.locationTracker?.enableFilter(TimeLocationFilter())
                      mainViewModel.locationTracker?.enableFilter(DistanceLocationFilter())
                  }
              }
          }

          private fun checkLocationPermission(context: Context) = ActivityCompat.checkSelfPermission(
              context,
              Manifest.permission.ACCESS_FINE_LOCATION,
          ) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(
              context,
              Manifest.permission.ACCESS_COARSE_LOCATION,
          ) != PackageManager.PERMISSION_GRANTED

          override fun onMapReady(map: MapLibreMap) {
              map.setStyle(
                  Style.Builder()
                      .fromUri(
                          "https://maps.geo.$region.amazonaws.com/maps/v0/maps/$mapName/style-descriptor?key=$apiKey"
                      ),
              ) {
                  mainViewModel.mapLibreMap = map
                  map.uiSettings.isAttributionEnabled = true
                  map.uiSettings.isLogoEnabled = false
                  map.uiSettings.attributionGravity = Gravity.BOTTOM or Gravity.END
                  val initialPosition = LatLng(47.6160281982247, -122.32642111977668)
                  map.cameraPosition = CameraPosition.Builder()
                      .target(initialPosition)
                      .zoom(14.0)
                      .build()

                  map.addOnCameraMoveStartedListener(this)
                  map.addOnCameraIdleListener(this)
                  map.cameraPosition.target?.let { latLng ->
                      mainViewModel.reverseGeocode(
                          LatLng(
                              latLng.latitude,
                              latLng.longitude
                          ), apiKey
                      )
                  }
              }
          }

          override fun onCameraMoveStarted(p0: Int) {
              mainViewModel.label = ""
              mainViewModel.isLabelAdded = false
          }

          override fun onCameraIdle() {
              if (!mainViewModel.isLabelAdded) {
                  mainViewModel.mapLibreMap?.cameraPosition?.target?.let { latLng ->
                      mainViewModel.reverseGeocode(
                          LatLng(
                              latLng.latitude,
                              latLng.longitude
                          ), apiKey
                      )
                  }
              }
          }
      }
      ```

      The above code shows how to create a `LocationTracker` object with `AuthHelper` and how to start and stop tracking with LocationTracker.
      + `authenticateUser()`: This method creates AuthHelper and LocationTracker objects.
      + `onStartStopTrackingClick`: This callback is triggered when the user clicks on the start/stop tracking button, which will start/stop tracking with Tracking SDK.

1. **Create a test route with Android Emulator.**

   1. **Open Emulator** by launching the AVD using Android Studio.

   1. **Open Extended Controls** by clicking on the **More** (three dots) icon in the emulator toolbar.

   1. **Open Location** by selecting **Location** from the sidebar.

   1. **Create route** with GPX data or by clicking on the map and choosing source and destination data.

   1. **Start Simulation** by clicking on **PLAY ROUTE** to begin simulating the GPS route.

   1. **Test Application** by running your application and observing how it handles the simulated route.

This is the full demo of the Android Quick Start application.

## What's next
<a name="qs-android-whats-next"></a>

You have completed the quick start tutorial, and should have an idea of how Amazon Location Service is used to build applications.

The source code for this application is available on [GitHub](https://github.com/aws-geospatial/amazon-location-samples-android/tree/main/quick-start).

To get more out of Amazon Location, you can check out the following resources:
+ Dive deeper into the [concepts of Amazon Location Service](how-it-works.md)
+ Get more information about [how to use Amazon Location features and functionality](using-amazon-location.md)
+ See how to expand on this sample and build more complex applications by looking at [code examples using Amazon Location](samples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
