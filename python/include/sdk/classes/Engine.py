
from ctypes import *
import BL2SDK






class  UIWorldBody_Data(Structure):
	_fields_ = []

class  UIWorldBody(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIWorldBody", UIWorldBody_Data),
	]


class  AActor_Data(Structure):
	_fields_ = [
		("VfTable_IIWorldBody", FPointer),
		("VfTable_IISpawnActor", FPointer),
		("VfTable_IIDamageCauser", FPointer),
		("Components", TArray_UActorComponentPtr),
		("AllComponents", TArray_UActorComponentPtr),
		("Location", FVector),
		("Rotation", FRotator),
		("DrawScale", c_float),
		("DrawScale3D", FVector),
		("PrePivot", FVector),
		("DetachFence", FRenderCommandFence),
		("CustomTimeDilation", c_float),
		("Physics", c_ubyte),
		("RemoteRole", c_ubyte),
		("Role", c_ubyte),
		("CollisionType", c_ubyte),
		("ReplicatedCollisionType", c_ubyte),
		("TickGroup", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Owner", POINTER(AActor)),
		("Base", POINTER(AActor)),
		("Timers", TArray_FTimerData),
		("bUseOrthonormalizedLighting", c_bool, 1),
		("bStatic", c_bool, 1),
		("bHidden", c_bool, 1),
		("bNoDelete", c_bool, 1),
		("bDeleteMe", c_bool, 1),
		("bTicked", c_bool, 1),
		("bOnlyOwnerSee", c_bool, 1),
		("bTickIsDisabled", c_bool, 1),
		("bWorldGeometry", c_bool, 1),
		("bIgnoreRigidBodyPawns", c_bool, 1),
		("bOrientOnSlope", c_bool, 1),
		("bIgnoreEncroachers", c_bool, 1),
		("bPushedByEncroachers", c_bool, 1),
		("bRouteBeginPlayEvenIfStatic", c_bool, 1),
		("bIsMoving", c_bool, 1),
		("bAlwaysEncroachCheck", c_bool, 1),
		("bCanStepUpOn", c_bool, 1),
		("bNetTemporary", c_bool, 1),
		("bOnlyRelevantToOwner", c_bool, 1),
		("bNetDirty", c_bool, 1),
		("bAlwaysRelevant", c_bool, 1),
		("bReplicateInstigator", c_bool, 1),
		("bReplicateMovement", c_bool, 1),
		("bSkipRotationReplication", c_bool, 1),
		("bForceRotationReplication", c_bool, 1),
		("bSkipActorPropertyReplication", c_bool, 1),
		("bUpdateSimulatedPosition", c_bool, 1),
		("bTearOff", c_bool, 1),
		("bOnlyDirtyReplication", c_bool, 1),
		("bSkipHiddenReplication", c_bool, 1),
		("bAllowFluidSurfaceInteraction", c_bool, 1),
		("bDemoRecording", c_bool, 1),
		("bDemoOwner", c_bool, 1),
		("bForceDemoRelevant", c_bool, 1),
		("bNetInitialRotation", c_bool, 1),
		("bReplicateRigidBodyLocation", c_bool, 1),
		("bKillDuringLevelTransition", c_bool, 1),
		("bExchangedRoles", c_bool, 1),
		("bConsiderAllStaticMeshComponentsForStreaming", c_bool, 1),
		("bPostRenderIfNotVisible", c_bool, 1),
		("bForceNetUpdate", c_bool, 1),
		("bPendingNetUpdate", c_bool, 1),
		("bHardAttach", c_bool, 1),
		("bIgnoreBaseRotation", c_bool, 1),
		("bSkipAttachedMoves", c_bool, 1),
		("bHurtEntry", c_bool, 1),
		("bGameRelevant", c_bool, 1),
		("bMovable", c_bool, 1),
		("bDestroyInPainVolume", c_bool, 1),
		("bCanBeDamaged", c_bool, 1),
		("bShouldBaseAtStartup", c_bool, 1),
		("bPendingDelete", c_bool, 1),
		("bCanTeleport", c_bool, 1),
		("bAlwaysTick", c_bool, 1),
		("bBlocksNavigation", c_bool, 1),
		("bCanTarget", c_bool, 1),
		("bCanTargetCheat", c_bool, 1),
		("BlockRigidBody", c_bool, 1),
		("bCollideWhenPlacing", c_bool, 1),
		("bCollideActors", c_bool, 1),
		("bCollideWorld", c_bool, 1),
		("bCollideComplex", c_bool, 1),
		("bBlockActors", c_bool, 1),
		("bProjTarget", c_bool, 1),
		("bBlocksTeleport", c_bool, 1),
		("bProjectileMoveSingleBlocking", c_bool, 1),
		("bTraceListeners", c_bool, 1),
		("bIsBlockingMesh", c_bool, 1),
		("bIsWillowInteractiveObject", c_bool, 1),
		("bIgnoreRadiusDamageCheck", c_bool, 1),
		("bNoEncroachCheck", c_bool, 1),
		("bCollideAsEncroacher", c_bool, 1),
		("bPhysRigidBodyOutOfWorldCheck", c_bool, 1),
		("bComponentOutsideWorld", c_bool, 1),
		("bForceOctreeSNFilter", c_bool, 1),
		("bRigidBodyWasAwake", c_bool, 1),
		("bCallRigidBodyWakeEvents", c_bool, 1),
		("bBounce", c_bool, 1),
		("bJustTeleported", c_bool, 1),
		("bNetInitial", c_bool, 1),
		("bNetOwner", c_bool, 1),
		("bHiddenEd", c_bool, 1),
		("bEditable", c_bool, 1),
		("bHiddenEdLayer", c_bool, 1),
		("bHiddenEdTemporary", c_bool, 1),
		("bHiddenEdLevel", c_bool, 1),
		("bEdShouldSnap", c_bool, 1),
		("bTempEditor", c_bool, 1),
		("bPathColliding", c_bool, 1),
		("bPathTemp", c_bool, 1),
		("bScriptInitialized", c_bool, 1),
		("bLockLocation", c_bool, 1),
		("bForceAllowKismetModification", c_bool, 1),
		("bTraceIgnoreRigidBodyForPawns", c_bool, 1),
		("bAutoMovePlayerOnInterpActor", c_bool, 1),
		("bMoveActorDoZeroExtentTrace", c_bool, 1),
		("bDebugEffectIsRelevant", c_bool, 1),
		("bLoadIfPhysXLevel0", c_bool, 1),
		("bLoadIfPhysXLevel1", c_bool, 1),
		("bLoadIfPhysXLevel2", c_bool, 1),
		("", c_ulong, 0),
		("NetTag", c_int),
		("NetUpdateTime", c_float),
		("NetUpdateFrequency", c_float),
		("NetPriority", c_float),
		("LastNetUpdateTime", c_float),
		("Instigator", POINTER(APawn)),
		("WorldInfo", POINTER(AWorldInfo)),
		("LifeSpan", c_float),
		("CreationTime", c_float),
		("LastRenderTime", c_float),
		("Touching", TArray_AActorPtr),
		("LatentFloat", c_float),
		("PhysicsVolume", POINTER(APhysicsVolume)),
		("Velocity", FVector),
		("Acceleration", FVector),
		("AngularVelocity", FVector),
		("BaseSkelComponent", POINTER(USkeletalMeshComponent)),
		("BaseBoneName", FName),
		("Attached", TArray_AActorPtr),
		("RelativeLocation", FVector),
		("RelativeRotation", FRotator),
		("CollisionComponent", POINTER(UPrimitiveComponent)),
		("OverlapTag", c_int),
		("RotationRate", FRotator),
		("GeneratedEvents", TArray_USequenceEventPtr),
		("LatentActions", TArray_USeqAct_LatentPtr),
		("MostRecentDamageTaken", c_float),
	]

class  AActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
	]


class  AInfo_Data(Structure):
	_fields_ = []

class  AInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
	]


class  AZoneInfo_Data(Structure):
	_fields_ = [
		("KillZ", c_float),
		("SoftKill", c_float),
		("KillZDamageType", POINTER(UClass)),
		("bSoftKillZ", c_bool, 1),
		("", c_ulong, 0),
	]

class  AZoneInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AZoneInfo", AZoneInfo_Data),
	]


class  AWorldInfo_Data(Structure):
	_fields_ = [
		("DefaultPostProcessSettings", FPostProcessSettings),
		("WorldPostProcessChain", POINTER(UPostProcessChain)),
		("bPersistPostProcessToNextLevel", c_bool, 1),
		("bFogEnabled", c_bool, 1),
		("bBumpOffsetEnabled", c_bool, 1),
		("bUseGammaCorrection", c_bool, 1),
		("bMapNeedsLightingFullyRebuilt", c_bool, 1),
		("bMapHasMultipleDominantLightsAffectingOnePrimitive", c_bool, 1),
		("bMapHasPathingErrors", c_bool, 1),
		("bRequestedBlockOnAsyncLoading", c_bool, 1),
		("bBegunPlay", c_bool, 1),
		("bPlayersOnly", c_bool, 1),
		("bPlayersOnlyPending", c_bool, 1),
		("bSuspendAI", c_bool, 1),
		("bStatusMenuOnly", c_bool, 1),
		("bDropDetail", c_bool, 1),
		("bAggressiveLOD", c_bool, 1),
		("bDontTickMind", c_bool, 1),
		("bStartup", c_bool, 1),
		("bPathsRebuilt", c_bool, 1),
		("bHasPathNodes", c_bool, 1),
		("bIsMenuLevel", c_bool, 1),
		("bDebugPauseExecution", c_bool, 1),
		("bDebugStepExecution", c_bool, 1),
		("bUseConsoleInput", c_bool, 1),
		("bNoDefaultInventoryForPlayer", c_bool, 1),
		("bNoPathWarnings", c_bool, 1),
		("bHighPriorityLoading", c_bool, 1),
		("bHighPriorityLoadingLocal", c_bool, 1),
		("bSupportDoubleBufferedPhysics", c_bool, 1),
		("bPhysicsIgnoreDeltaTime", c_bool, 1),
		("bEnableChanceOfPhysicsChunkOverride", c_bool, 1),
		("bLimitExplosionChunkSize", c_bool, 1),
		("bLimitDamageChunkSize", c_bool, 1),
		("bPrecomputeVisibility", c_bool, 1),
		("bPlaceCellsOnSurfaces", c_bool, 1),
		("bAllowTemporalAA", c_bool, 1),
		("bUseGlobalIllumination", c_bool, 1),
		("bForceNoPrecomputedLighting", c_bool, 1),
		("bAllowHostMigration", c_bool, 1),
		("bAssertOnGBXCheck", c_bool, 1),
		("bSupportsTimeOfDay", c_bool, 1),
		("", c_ulong, 0),
		("SquintModeKernelSize", c_float),
		("ShadowmapStreamingFactorMultiplier", c_float),
		("HighestPriorityPostProcessVolume", POINTER(APostProcessVolume)),
		("DefaultReverbSettings", FReverbSettings),
		("DefaultAmbientZoneSettings", FInteriorSettings),
		("FogStart", c_float),
		("FogEnd", c_float),
		("FogColor", FColor),
		("BumpEnd", c_float),
		("HighestPriorityReverbVolume", POINTER(AReverbVolume)),
		("MassiveLODOverrideVolumes", TArray_AMassiveLODOverrideVolumePtr),
		("WorldSoundManager", POINTER(AWorldSoundManager)),
		("PortalVolumes", TArray_APortalVolumePtr),
		("EnvironmentVolumes", TArray_AEnvironmentVolumePtr),
		("StreamingLevels", TArray_ULevelStreamingPtr),
		("LastTimeUnbuiltLightingWasEncountered", FDouble),
		("TimeDilation", c_float),
		("DemoPlayTimeDilation", c_float),
		("TimeSeconds", c_float),
		("RealTimeSeconds", c_float),
		("AudioTimeSeconds", c_float),
		("DeltaSeconds", c_float),
		("PauseDelay", c_float),
		("RealTimeToUnPause", c_float),
		("Pauser", POINTER(APlayerReplicationInfo)),
		("DefaultTexture", POINTER(UTexture2D)),
		("WireframeTexture", POINTER(UTexture2D)),
		("WhiteSquareTexture", POINTER(UTexture2D)),
		("LargeVertex", POINTER(UTexture2D)),
		("BSPVertex", POINTER(UTexture2D)),
		("DeferredExecs", TArray_FString),
		("GRI", POINTER(AGameReplicationInfo)),
		("NetMode", c_ubyte),
		("NextTravelType", c_ubyte),
		("VisibilityAggressiveness", c_ubyte),
		("LevelLightingQuality", c_ubyte),
		("ComputerName", FString),
		("EngineVersion", FString),
		("MinNetVersion", FString),
		("Game", POINTER(AGameInfo)),
		("StallZ", c_float),
		("WorldGravityZ", c_float),
		("DefaultGravityZ", c_float),
		("GlobalGravityZ", c_float),
		("RBPhysicsGravityScaling", c_float),
		("NavigationPointList", POINTER(ANavigationPoint)),
		("ControllerList", POINTER(AController)),
		("PawnList", POINTER(APawn)),
		("CoverList", POINTER(ACoverLink)),
		("PylonList", POINTER(APylon)),
		("NavMeshList", POINTER(AGBXNavMesh)),
		("MoveRepSize", c_float),
		("ReplicationViewers", TArray_FNetViewer),
		("NextURL", FString),
		("NextSwitchCountdown", c_float),
		("PackedLightAndShadowMapTextureSize", c_int),
		("DefaultColorScale", FVector),
		("DefaultGameType", POINTER(UClass)),
		("GameTypesSupportedOnThisMap", TArray_UClassPtr),
		("ClientDestroyedActorContent", TArray_UObjectPtr),
		("PreparingLevelNames", TArray_FName),
		("CommittedPersistentLevel", POINTER(ULevel)),
		("PersistentMapForcedObjects", POINTER(UObjectReferencer)),
		("Title", FString),
		("Author", FString),
		("MyMapInfo", POINTER(UMapInfo)),
		("EmitterPoolClassPath", FString),
		("MyEmitterPool", POINTER(AEmitterPool)),
		("DecalManagerClassPath", FString),
		("MyDecalManager", POINTER(ADecalManager)),
		("ParticleEventManagerClassPath", FString),
		("MyParticleEventManager", POINTER(AParticleEventManager)),
		("ParentLoader", FString),
		("MaxPhysicsDeltaTime", c_float),
		("MaxPhysicsSubsteps", c_int),
		("PhysicsProperties", FPhysXSceneProperties),
		("CompartmentRunFrames", TArray_FCompartmentRunList),
		("DefaultSkinWidth", c_float),
		("ApexLODResourceBudget", c_float),
		("DestructibleSettings", FApexModuleDestructibleSettings),
		("EmitterVertical", POINTER(UPhysicsLODVerticalEmitter)),
		("VerticalProperties", FPhysXVerticalProperties),
		("ChanceOfPhysicsChunkOverride", c_float),
		("MaxExplosionChunkSize", c_float),
		("MaxDamageChunkSize", c_float),
		("FractureExplosionVelScale", c_float),
		("MaxNumFacturedChunksToSpawnInAFrame", c_int),
		("NumFacturedChunksSpawnedThisFrame", c_int),
		("FracturedMeshWeaponDamage", c_float),
		("VisibilityCellSize", c_int),
		("CharacterLitIndirectBrightness", c_float),
		("CharacterLitIndirectContrastFactor", c_float),
		("CharacterShadowedIndirectBrightness", c_float),
		("CharacterShadowedIndirectContrastFactor", c_float),
		("CharacterLightingContrastFactor", c_float),
		("ScreenMessages", FMap_Mirror),
		("PriorityScreenMessages", TArray_FScreenMessageString),
		("LightmassSettings", FLightmassWorldInfoSettings),
		("Unknown1", c_ubyte, 0x),
		("Unknown2", c_ubyte, 0x),
		("PeerHostMigration", FHostMigrationState),
		("HostMigrationTimeout", c_float),
		("NavigationAreas", TArray_FNavigationArea),
		("HoldingCell", POINTER(AHoldingAreaDestination)),
		("PersonalTeleporterDestination", POINTER(ATeleporterDestination)),
		("PersonalReturnTeleporterLocation", POINTER(AActor)),
		("CommonsLevelName", FName),
		("TeleporterPlacedEventName", FName),
		("CombatMusic", POINTER(USoundCue)),
		("GBXCheckDisplayDuration", c_int),
		("TextureMovies", TArray_UTextureMoviePtr),
	]

class  AWorldInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AZoneInfo", AZoneInfo_Data),
		("AWorldInfo", AWorldInfo_Data),
	]


class  UDownloadableContentEnumerator_Data(Structure):
	_fields_ = [
		("DLCBundles", TArray_FOnlineContent),
		("NamedDLCBundles", TArray_FNamedOnlineContent),
		("NamedDLCCompatibilityBundles", TArray_FNamedOnlineContent),
		("bNeedsRefresh", c_bool, 1),
		("", c_ulong, 0),
		("CurrentEnumerationState", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("DLCRootDir", FString),
		("FindDLCDelegates", TArray_FScriptDelegate),
		("OldCompatibilityBundles", TArray_FCompatibilityOnlineContent),
		("__OnFindDLCComplete__Delegate", FScriptDelegate),
	]

class  UDownloadableContentEnumerator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDownloadableContentEnumerator", UDownloadableContentEnumerator_Data),
	]


class  UDownloadableContentManager_Data(Structure):
	_fields_ = [
		("DLCConfigCacheChanges", TArray_FPointer),
		("DlcOffers", TArray_FMarketplaceOffer),
		("InstalledContent", TArray_FInstalledContentInfo),
		("RejectedContent", TArray_FRejectedContentInfo),
		("CookInstanceGuid", FGuid),
		("NonPackageFilePathMapExtensions", TArray_FString),
		("NonPackageFilePathMap", FMap_Mirror),
		("AudioPackageFilePathmap", FMap_Mirror),
		("ClassesToReload", TArray_UClassPtr),
		("ObjectsToReload", TArray_UObjectPtr),
		("bCanInstallCompatibilityContent", c_bool, 1),
		("bCanEnumerateMarketplaceContent", c_bool, 1),
		("bCouldInstallCompatibilityContent", c_bool, 1),
		("bCouldEnumerateMarketplaceContent", c_bool, 1),
		("bRefreshRequestWhileBusy", c_bool, 1),
		("bDlcEnumOutstanding", c_bool, 1),
		("bDlcOfferEnumOutstanding", c_bool, 1),
		("bDlcOfferEnumInstallPending", c_bool, 1),
		("", c_ulong, 0),
		("LicensedSeasonPassIds", TArray_int),
		("LastRefreshStartTime", FDouble),
		("LastRefreshFinishTime", FDouble),
		("RefreshCount", c_int),
		("GameEngine", POINTER(UGameEngine)),
		("RefreshCompleteDelegates", TArray_FScriptDelegate),
		("__OnRefreshComplete__Delegate", FScriptDelegate),
	]

class  UDownloadableContentManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDownloadableContentManager", UDownloadableContentManager_Data),
	]


class  UDownloadableContentOfferEnumerator_Data(Structure):
	_fields_ = [
		("bHasBeenEnumerated", c_bool, 1),
		("", c_ulong, 0),
		("CurrentEnumerationState", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MarketplaceOffers", TArray_FMarketplaceOffer),
		("FindDlcOfferDelegates", TArray_FScriptDelegate),
		("__OnFindDlcOfferComplete__Delegate", FScriptDelegate),
	]

class  UDownloadableContentOfferEnumerator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDownloadableContentOfferEnumerator", UDownloadableContentOfferEnumerator_Data),
	]


class  UEngine_Data(Structure):
	_fields_ = [
		("TinyFont", POINTER(UFont)),
		("TinyFontName", FString),
		("SmallFont", POINTER(UFont)),
		("SmallFontName", FString),
		("MediumFont", POINTER(UFont)),
		("MediumFontName", FString),
		("LargeFont", POINTER(UFont)),
		("LargeFontName", FString),
		("NonShipMediumFont", POINTER(UFont)),
		("NonShipLargeFont", POINTER(UFont)),
		("SubtitleFont", POINTER(UFont)),
		("SubtitleFontName", FString),
		("GlyphFont", POINTER(UFont)),
		("GlyphFontName", FString),
		("AdditionalFonts", TArray_UFontPtr),
		("AdditionalFontNames", TArray_FString),
		("ConsoleClass", POINTER(UClass)),
		("ConsoleClassName", FString),
		("GameViewportClientClass", POINTER(UClass)),
		("GameViewportClientClassName", FString),
		("DataStoreClientClass", POINTER(UClass)),
		("DataStoreClientClassName", FString),
		("LocalPlayerClass", POINTER(UClass)),
		("LocalPlayerClassName", FString),
		("DefaultMaterial", POINTER(UMaterial)),
		("DefaultMaterialName", FString),
		("DefaultDecalMaterial", POINTER(UMaterial)),
		("DefaultDecalMaterialName", FString),
		("DefaultTexture", POINTER(UTexture)),
		("DefaultTextureName", FString),
		("WireframeMaterial", POINTER(UMaterial)),
		("WireframeMaterialName", FString),
		("EmissiveTexturedMaterial", POINTER(UMaterial)),
		("EmissiveTexturedMaterialName", FString),
		("GeomMaterial", POINTER(UMaterial)),
		("GeomMaterialName", FString),
		("DefaultFogVolumeMaterial", POINTER(UMaterial)),
		("DefaultFogVolumeMaterialName", FString),
		("TickMaterial", POINTER(UMaterial)),
		("TickMaterialName", FString),
		("CrossMaterial", POINTER(UMaterial)),
		("CrossMaterialName", FString),
		("LevelColorationLitMaterial", POINTER(UMaterial)),
		("LevelColorationLitMaterialName", FString),
		("LevelColorationUnlitMaterial", POINTER(UMaterial)),
		("LevelColorationUnlitMaterialName", FString),
		("LightingTexelDensityMaterial", POINTER(UMaterial)),
		("LightingTexelDensityName", FString),
		("ShadedLevelColorationLitMaterial", POINTER(UMaterial)),
		("ShadedLevelColorationLitMaterialName", FString),
		("ShadedLevelColorationUnlitMaterial", POINTER(UMaterial)),
		("ShadedLevelColorationUnlitMaterialName", FString),
		("RemoveSurfaceMaterial", POINTER(UMaterial)),
		("RemoveSurfaceMaterialName", FString),
		("VertexColorMaterial", POINTER(UMaterial)),
		("VertexColorMaterialName", FString),
		("VertexColorViewModeMaterial_ColorOnly", POINTER(UMaterial)),
		("VertexColorViewModeMaterialName_ColorOnly", FString),
		("VertexColorViewModeMaterial_AlphaAsColor", POINTER(UMaterial)),
		("VertexColorViewModeMaterialName_AlphaAsColor", FString),
		("VertexColorViewModeMaterial_RedOnly", POINTER(UMaterial)),
		("VertexColorViewModeMaterialName_RedOnly", FString),
		("VertexColorViewModeMaterial_GreenOnly", POINTER(UMaterial)),
		("VertexColorViewModeMaterialName_GreenOnly", FString),
		("VertexColorViewModeMaterial_BlueOnly", POINTER(UMaterial)),
		("VertexColorViewModeMaterialName_BlueOnly", FString),
		("HeatmapMaterial", POINTER(UMaterial)),
		("HeatmapMaterialName", FString),
		("BoneWeightMaterial", POINTER(UMaterial)),
		("BoneWeightMaterialName", FString),
		("TangentColorMaterial", POINTER(UMaterial)),
		("TangentColorMaterialName", FString),
		("FacebookIntegration", POINTER(UFacebookIntegration)),
		("FacebookIntegrationClassName", FString),
		("bCombineSimilarMappings", c_bool, 1),
		("bRenderLightMapDensityGrayscale", c_bool, 1),
		("bUseSound", c_bool, 1),
		("bUseAudioStreaming", c_bool, 1),
		("bUseBackgroundLevelStreaming", c_bool, 1),
		("bSubtitlesEnabled", c_bool, 1),
		("bSubtitlesForcedOff", c_bool, 1),
		("bSmoothFrameRate", c_bool, 1),
		("bSmoothFrameRateRuntimeToggle", c_bool, 1),
		("bCheckForMultiplePawnsSpawnedInAFrame", c_bool, 1),
		("bShouldGenerateSimpleLightmaps", c_bool, 1),
		("bForceStaticTerrain", c_bool, 1),
		("bForceCPUSkinning", c_bool, 1),
		("bUsePostProcessEffects", c_bool, 1),
		("bOnScreenKismetWarnings", c_bool, 1),
		("bEnableKismetLogging", c_bool, 1),
		("bAllowMatureLanguage", c_bool, 1),
		("bRenderTerrainCollisionAsOverlay", c_bool, 1),
		("bPauseOnLossOfFocus", c_bool, 1),
		("bCheckParticleRenderSize", c_bool, 1),
		("bEnableColorClear", c_bool, 1),
		("bAreConstraintsDirty", c_bool, 1),
		("bHasPendingGlobalReattach", c_bool, 1),
		("bEnableOnScreenDebugMessages", c_bool, 1),
		("bEnableOnScreenDebugMessagesDisplay", c_bool, 1),
		("bSuppressMapWarnings", c_bool, 1),
		("bCookSeparateSharedMPGameContent", c_bool, 1),
		("bDisableAILogging", c_bool, 1),
		("bUseNormalMapsForSimpleLightMaps", c_bool, 1),
		("bStartWithMatineeCapture", c_bool, 1),
		("bCompressMatineeCapture", c_bool, 1),
		("bMuteAudioWhenNotInFocus", c_bool, 1),
		("bIsPauseGFxMovieOpen", c_bool, 1),
		("bNoBuildLightingMessage", c_bool, 1),
		("bCinematicAutoSkip", c_bool, 1),
		("", c_ulong, 0),
		("MaxRMSDForCombiningMappings", c_float),
		("LightingOnlyBrightness", FLinearColor),
		("LightComplexityColors", TArray_FColor),
		("ShaderComplexityColors", TArray_FLinearColor),
		("MaxPixelShaderAdditiveComplexityCount", c_float),
		("MinTextureDensity", c_float),
		("IdealTextureDensity", c_float),
		("MaxTextureDensity", c_float),
		("MinLightMapDensity", c_float),
		("IdealLightMapDensity", c_float),
		("MaxLightMapDensity", c_float),
		("RenderLightMapDensityGrayscaleScale", c_float),
		("RenderLightMapDensityColorScale", c_float),
		("LightMapDensityVertexMappedColor", FLinearColor),
		("LightMapDensitySelectedColor", FLinearColor),
		("MinVertexDensity", c_float),
		("IdealVertexDensity", c_float),
		("MaxVertexDensity", c_float),
		("StatColorMappings", TArray_FStatColorMapping),
		("EditorBrushMaterial", POINTER(UMaterial)),
		("EditorBrushMaterialName", FString),
		("DefaultPhysMaterial", POINTER(UPhysicalMaterial)),
		("DefaultPhysMaterialName", FString),
		("ApexDamageParams", POINTER(UApexDestructibleDamageParameters)),
		("ApexDamageParamsName", FString),
		("TerrainErrorMaterial", POINTER(UMaterial)),
		("TerrainErrorMaterialName", FString),
		("TerrainMaterialMaxTextureCount", c_int),
		("OnlineSubsystemClass", POINTER(UClass)),
		("DefaultOnlineSubsystemName", FString),
		("DefaultPostProcess", POINTER(UPostProcessChain)),
		("DefaultPostProcessName", FString),
		("ThumbnailSkeletalMeshPostProcess", POINTER(UPostProcessChain)),
		("ThumbnailSkeletalMeshPostProcessName", FString),
		("ThumbnailParticleSystemPostProcess", POINTER(UPostProcessChain)),
		("ThumbnailParticleSystemPostProcessName", FString),
		("ThumbnailMaterialPostProcess", POINTER(UPostProcessChain)),
		("ThumbnailMaterialPostProcessName", FString),
		("DefaultUIScenePostProcess", POINTER(UPostProcessChain)),
		("DefaultUIScenePostProcessName", FString),
		("DefaultUICaretMaterial", POINTER(UMaterial)),
		("DefaultUICaretMaterialName", FString),
		("SceneCaptureReflectActorMaterial", POINTER(UMaterial)),
		("SceneCaptureReflectActorMaterialName", FString),
		("SceneCaptureCubeActorMaterial", POINTER(UMaterial)),
		("SceneCaptureCubeActorMaterialName", FString),
		("ScreenDoorNoiseTexture", POINTER(UTexture2D)),
		("ScreenDoorNoiseTextureName", FString),
		("ImageGrainNoiseTexture", POINTER(UTexture2D)),
		("ImageGrainNoiseTextureName", FString),
		("RandomAngleTexture", POINTER(UTexture2D)),
		("RandomAngleTextureName", FString),
		("RandomNormalTexture", POINTER(UTexture2D)),
		("RandomNormalTextureName", FString),
		("RandomMirrorDiscTexture", POINTER(UTexture2D)),
		("RandomMirrorDiscTextureName", FString),
		("WeightMapPlaceholderTexture", POINTER(UTexture)),
		("WeightMapPlaceholderTextureName", FString),
		("LightMapDensityTexture", POINTER(UTexture2D)),
		("LightMapDensityTextureName", FString),
		("LightMapDensityNormal", POINTER(UTexture2D)),
		("LightMapDensityNormalName", FString),
		("DefaultSound", POINTER(USoundNodeWave)),
		("DefaultSoundName", FString),
		("TimeBetweenPurgingPendingKillObjects", c_float),
		("Client", POINTER(UClient)),
		("GamePlayers", TArray_ULocalPlayerPtr),
		("GameViewport", POINTER(UGameViewportClient)),
		("DeferredCommands", TArray_FString),
		("TickCycles", c_int),
		("GameCycles", c_int),
		("ClientCycles", c_int),
		("MaxSmoothedFrameRate", c_float),
		("MinSmoothedFrameRate", c_float),
		("NumPawnsAllowedToBeSpawnedInAFrame", c_int),
		("RemoteControlExec", FPointer),
		("MobileMaterialEmulator", FPointer),
		("C_WorldBox", FColor),
		("C_BrushWire", FColor),
		("C_AddWire", FColor),
		("C_SubtractWire", FColor),
		("C_SemiSolidWire", FColor),
		("C_NonSolidWire", FColor),
		("C_WireBackground", FColor),
		("C_ScaleBoxHi", FColor),
		("C_VolumeCollision", FColor),
		("C_BSPCollision", FColor),
		("C_OrthoBackground", FColor),
		("C_Volume", FColor),
		("C_BrushShape", FColor),
		("StreamingDistanceFactor", c_float),
		("ScoutClassName", FString),
		("TransitionType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TransitionDescription", FString),
		("TransitionGameType", FString),
		("MeshLODRange", c_float),
		("CameraRotationThreshold", c_float),
		("CameraTranslationThreshold", c_float),
		("PrimitiveProbablyVisibleTime", c_float),
		("PercentUnoccludedRequeries", c_float),
		("MaxOcclusionPixelsFraction", c_float),
		("PhysXLevel", c_int),
		("MaxFluidNumVerts", c_int),
		("FluidSimulationTimeLimit", c_float),
		("MaxParticleResize", c_int),
		("MaxParticleResizeWarn", c_int),
		("MaxParticleVertexMemory", c_int),
		("MaxParticleSpriteCount", c_int),
		("MaxParticleSubUVCount", c_int),
		("BeginUPTryCount", c_int),
		("PendingDroppedNotes", TArray_FDropNoteInfo),
		("DynamicCoverMeshComponentName", FString),
		("NetClientTicksPerSecond", c_float),
		("MaxTrackedOcclusionIncrement", c_float),
		("TrackedOcclusionStepSize", c_float),
		("DefaultSelectedMaterialColor", FLinearColor),
		("DefaultHoveredMaterialColor", FLinearColor),
		("SelectedMaterialColor", FLinearColor),
		("UnselectedMaterialColor", FLinearColor),
		("NumberOfOnScreenDebugMessages", c_int),
		("IgnoreSimulatedFuncWarnings", TArray_FName),
		("ScreenSaverInhibitorSemaphore", c_int),
		("ScreenSaverInhibitor", FPointer),
		("HitchWatcherThreadSemaphore", c_int),
		("GlobalTranslationContext", POINTER(UTranslationContext)),
		("LoadingMovieStartTime", FDouble),
		("MatineeCaptureName", FString),
		("MatineePackageCaptureName", FString),
		("VisibleLevelsForMatineeCapture", FString),
		("MatineeCaptureFPS", c_int),
		("MatineeCaptureType", c_int),
		("BlockingMeshColor", FColor),
		("BlockingMeshOpacity", c_float),
		("CinematicAutoSkipDelay", c_float),
		("CinematicAutoSkipMaps", TArray_FString),
		("SFXVolume", c_float),
		("VoiceOverVolume", c_float),
		("BinkMovieVolumeScaleFactor", c_float),
	]

class  UEngine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USubsystem", USubsystem_Data),
		("UEngine", UEngine_Data),
	]


class  UGameEngine_Data(Structure):
	_fields_ = [
		("GPendingLevel", POINTER(UPendingLevel)),
		("bCleanupForPendingLevel", c_bool, 1),
		("bWorldWasLoadedThisTick", c_bool, 1),
		("bCheckForMovieCapture", c_bool, 1),
		("bTriggerPostLoadMap", c_bool, 1),
		("bStartedLoadMapMovie", c_bool, 1),
		("bShouldCommitPendingMapChange", c_bool, 1),
		("bClearAnimSetLinkupCachesOnLoadMap", c_bool, 1),
		("", c_ulong, 0),
		("PendingLevelPlayerControllerClassName", FString),
		("LastURL", FURL),
		("LastRemoteURL", FURL),
		("ServerActors", TArray_FString),
		("TravelURL", FString),
		("TravelType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("OnlineSubsystem", POINTER(UOnlineSubsystem)),
		("DLCEnumerator", POINTER(UDownloadableContentEnumerator)),
		("DownloadableContentEnumeratorClassName", FString),
		("DevDownloadableContentEnumeratorClassName", FString),
		("DLCManager", POINTER(UDownloadableContentManager)),
		("DownloadableContentOfferEnumeratorClassName", FString),
		("DLCOfferEnumerator", POINTER(UDownloadableContentOfferEnumerator)),
		("DownloadableContentManagerClassName", FString),
		("AdManager", POINTER(UInGameAdManager)),
		("InGameAdManagerClassName", FString),
		("LevelsToLoadForPendingMapChange", TArray_FName),
		("LoadedLevelsForPendingMapChange", TArray_ULevelPtr),
		("PendingMapChangeFailureDescription", FString),
		("MaxDeltaTime", c_float),
		("PendingLevelStreamingStatusUpdates", TArray_FLevelStreamingStatus),
		("ObjectReferencers", TArray_UObjectReferencerPtr),
		("PackagesToFullyLoad", TArray_FFullyLoadedPackagesInfo),
		("NamedNetDrivers", TArray_FNamedNetDriver),
		("AnimTags", TArray_FAnimTag),
	]

class  UGameEngine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USubsystem", USubsystem_Data),
		("UEngine", UEngine_Data),
		("UGameEngine", UGameEngine_Data),
	]


class  UInGameAdManager_Data(Structure):
	_fields_ = [
		("bShouldPauseWhileAdOpen", c_bool, 1),
		("", c_ulong, 0),
		("ClickedBannerDelegates", TArray_FScriptDelegate),
		("ClosedAdDelegates", TArray_FScriptDelegate),
		("__OnUserClickedBanner__Delegate", FScriptDelegate),
		("__OnUserClosedAdvertisement__Delegate", FScriptDelegate),
	]

class  UInGameAdManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInGameAdManager", UInGameAdManager_Data),
	]


class  UEngineBaseTypes_Data(Structure):
	_fields_ = []

class  UEngineBaseTypes(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UEngineBaseTypes", UEngineBaseTypes_Data),
	]


class  ABrush_Data(Structure):
	_fields_ = [
		("CsgOper", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BrushColor", FColor),
		("PolyFlags", c_int),
		("bColored", c_bool, 1),
		("bSolidWhenSelected", c_bool, 1),
		("bPlaceableFromClassBrowser", c_bool, 1),
		("", c_ulong, 0),
		("Brush", POINTER(UModel)),
		("BrushComponent", POINTER(UBrushComponent)),
		("SavedSelections", TArray_FGeomSelection),
	]

class  ABrush(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
	]


class  ABrushShape_Data(Structure):
	_fields_ = []

class  ABrushShape(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("ABrushShape", ABrushShape_Data),
	]


class  AVolume_Data(Structure):
	_fields_ = [
		("AssociatedActors", TArray_AActorPtr),
		("bForcePawnWalk", c_bool, 1),
		("bProcessAllActors", c_bool, 1),
		("bPawnsOnly", c_bool, 1),
		("", c_ulong, 0),
	]

class  AVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
	]


class  ABlockingVolume_Data(Structure):
	_fields_ = [
		("bBlockCamera", c_bool, 1),
		("bBlockProjectiles", c_bool, 1),
		("", c_ulong, 0),
	]

class  ABlockingVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ABlockingVolume", ABlockingVolume_Data),
	]


class  ADynamicBlockingVolume_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  ADynamicBlockingVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ABlockingVolume", ABlockingVolume_Data),
		("ADynamicBlockingVolume", ADynamicBlockingVolume_Data),
	]


class  ACullDistanceVolume_Data(Structure):
	_fields_ = [
		("CullDistances", TArray_FCullDistanceSizePair),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  ACullDistanceVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ACullDistanceVolume", ACullDistanceVolume_Data),
	]


class  ALevelGridVolume_Data(Structure):
	_fields_ = [
		("LevelGridVolumeName", FString),
		("CellShape", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Subdivisions", int * 3),
		("LoadingDistance", c_float),
		("KeepLoadedRange", c_float),
		("CellConvexElem", FKConvexElem),
	]

class  ALevelGridVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ALevelGridVolume", ALevelGridVolume_Data),
	]


class  ALevelStreamingVolume_Data(Structure):
	_fields_ = [
		("StreamingLevels", TArray_ULevelStreamingPtr),
		("bEditorPreVisOnly", c_bool, 1),
		("bDisabled", c_bool, 1),
		("bTestDistanceToVolume", c_bool, 1),
		("", c_ulong, 0),
		("StreamingUsage", c_ubyte),
		("Usage", c_ubyte),
		("CurrentVisibility", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TestVolumeDistance", c_float),
	]

class  ALevelStreamingVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ALevelStreamingVolume", ALevelStreamingVolume_Data),
	]


class  ALightmassCharacterIndirectDetailVolume_Data(Structure):
	_fields_ = []

class  ALightmassCharacterIndirectDetailVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ALightmassCharacterIndirectDetailVolume", ALightmassCharacterIndirectDetailVolume_Data),
	]


class  ALightmassImportanceVolume_Data(Structure):
	_fields_ = []

class  ALightmassImportanceVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ALightmassImportanceVolume", ALightmassImportanceVolume_Data),
	]


class  AMassiveLODOverrideVolume_Data(Structure):
	_fields_ = []

class  AMassiveLODOverrideVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AMassiveLODOverrideVolume", AMassiveLODOverrideVolume_Data),
	]


class  ANavMeshBoundsVolume_Data(Structure):
	_fields_ = []

class  ANavMeshBoundsVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ANavMeshBoundsVolume", ANavMeshBoundsVolume_Data),
	]


class  APathBlockingVolume_Data(Structure):
	_fields_ = []

class  APathBlockingVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APathBlockingVolume", APathBlockingVolume_Data),
	]


class  APhysicsVolume_Data(Structure):
	_fields_ = [
		("ZoneVelocity", FVector),
		("bVelocityAffectsWalking", c_bool, 1),
		("bPainCausing", c_bool, 1),
		("bAIShouldIgnorePain", c_bool, 1),
		("bEntryPain", c_bool, 1),
		("BACKUP_bPainCausing", c_bool, 1),
		("bDestructive", c_bool, 1),
		("bNoInventory", c_bool, 1),
		("bMoveProjectiles", c_bool, 1),
		("bBounceVelocity", c_bool, 1),
		("bNeutralZone", c_bool, 1),
		("bCrowdAgentsPlayDeathAnim", c_bool, 1),
		("bPhysicsOnContact", c_bool, 1),
		("bWaterVolume", c_bool, 1),
		("", c_ulong, 0),
		("GroundFriction", c_float),
		("TerminalVelocity", c_float),
		("DamagePerSec", c_float),
		("DamageType", POINTER(UClass)),
		("DamageTypeDefinition", POINTER(UDamageTypeDefinition)),
		("ImpactDefinition", POINTER(UImpactDefinition)),
		("Priority", c_int),
		("FluidFriction", c_float),
		("PainInterval", c_float),
		("RigidBodyDamping", c_float),
		("MaxDampingForce", c_float),
		("PainTimer", POINTER(AInfo)),
		("DamageInstigator", POINTER(AController)),
		("NextPhysicsVolume", POINTER(APhysicsVolume)),
	]

class  APhysicsVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APhysicsVolume", APhysicsVolume_Data),
	]


class  ADefaultPhysicsVolume_Data(Structure):
	_fields_ = []

class  ADefaultPhysicsVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APhysicsVolume", APhysicsVolume_Data),
		("ADefaultPhysicsVolume", ADefaultPhysicsVolume_Data),
	]


class  AGravityVolume_Data(Structure):
	_fields_ = [
		("GravityZ", c_float),
	]

class  AGravityVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APhysicsVolume", APhysicsVolume_Data),
		("AGravityVolume", AGravityVolume_Data),
	]


class  ALadderVolume_Data(Structure):
	_fields_ = [
		("WallDir", FRotator),
		("LookDir", FVector),
		("ClimbDir", FVector),
		("LadderList", POINTER(ALadder)),
		("bNoPhysicalLadder", c_bool, 1),
		("bAutoPath", c_bool, 1),
		("bAllowLadderStrafing", c_bool, 1),
		("", c_ulong, 0),
		("PendingClimber", POINTER(APawn)),
		("WallDirArrow", POINTER(UArrowComponent)),
	]

class  ALadderVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APhysicsVolume", APhysicsVolume_Data),
		("ALadderVolume", ALadderVolume_Data),
	]


class  APortalVolume_Data(Structure):
	_fields_ = [
		("Portals", TArray_APortalTeleporterPtr),
	]

class  APortalVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APortalVolume", APortalVolume_Data),
	]


class  APostProcessVolume_Data(Structure):
	_fields_ = [
		("Priority", c_float),
		("Settings", FPostProcessSettings),
		("NextLowerPriorityVolume", POINTER(APostProcessVolume)),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  APostProcessVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APostProcessVolume", APostProcessVolume_Data),
	]


class  APrecomputedVisibilityOverrideVolume_Data(Structure):
	_fields_ = [
		("OverrideVisibleActors", TArray_AActorPtr),
		("OverrideInvisibleActors", TArray_AActorPtr),
	]

class  APrecomputedVisibilityOverrideVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APrecomputedVisibilityOverrideVolume", APrecomputedVisibilityOverrideVolume_Data),
	]


class  APrecomputedVisibilityVolume_Data(Structure):
	_fields_ = []

class  APrecomputedVisibilityVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APrecomputedVisibilityVolume", APrecomputedVisibilityVolume_Data),
	]


class  AReverbVolume_Data(Structure):
	_fields_ = [
		("Priority", c_float),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
		("Settings", FReverbSettings),
		("AmbientZoneSettings", FInteriorSettings),
		("NextLowerPriorityVolume", POINTER(AReverbVolume)),
	]

class  AReverbVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AReverbVolume", AReverbVolume_Data),
	]


class  AShadowRelevanceVolume_Data(Structure):
	_fields_ = [
		("ShadowRelevanceList", TArray_FShadowRelevanceSizePair),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  AShadowRelevanceVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AShadowRelevanceVolume", AShadowRelevanceVolume_Data),
	]


class  ATriggerVolume_Data(Structure):
	_fields_ = []

class  ATriggerVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ATriggerVolume", ATriggerVolume_Data),
	]


class  ADynamicSMActor_Data(Structure):
	_fields_ = [
		("StaticMeshComponent", POINTER(UStaticMeshComponent)),
		("LightEnvironment", POINTER(UDynamicLightEnvironmentComponent)),
		("ReplicatedMesh", POINTER(UStaticMesh)),
		("ReplicatedMaterial0", POINTER(UMaterialInterface)),
		("ReplicatedMaterial1", POINTER(UMaterialInterface)),
		("bForceStaticDecals", c_bool, 1),
		("bPawnCanBaseOn", c_bool, 1),
		("bSafeBaseIfAsleep", c_bool, 1),
		("", c_ulong, 0),
		("ReplicatedMeshTranslation", FVector),
		("ReplicatedMeshRotation", FRotator),
		("ReplicatedMeshScale3D", FVector),
	]

class  ADynamicSMActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
	]


class  AInterpActor_Data(Structure):
	_fields_ = [
		("bShouldSaveForCheckpoint", c_bool, 1),
		("bMonitorMover", c_bool, 1),
		("bMonitorZVelocity", c_bool, 1),
		("bDestroyProjectilesOnEncroach", c_bool, 1),
		("bContinueOnEncroachPhysicsObject", c_bool, 1),
		("bStopOnEncroach", c_bool, 1),
		("bCrushPawnsWhenEncroaching", c_bool, 1),
		("bCrushPawnsWhenGoingDown", c_bool, 1),
		("bCrushPawnsWhenGoingUp", c_bool, 1),
		("bCrushVehiclesWhenGoingDown", c_bool, 1),
		("bCrushVehiclesWhenGoingUp", c_bool, 1),
		("bShouldShadowParentAllAttachedActors", c_bool, 1),
		("bTreatAsStaticForGBXNavMeshBuilding", c_bool, 1),
		("bIsLift", c_bool, 1),
		("", c_ulong, 0),
		("MyMarker", POINTER(ANavigationPoint)),
		("MaxZVelocity", c_float),
		("StayOpenTime", c_float),
		("OpenSound", POINTER(USoundCue)),
		("OpeningAmbientSound", POINTER(USoundCue)),
		("OpenedSound", POINTER(USoundCue)),
		("CloseSound", POINTER(USoundCue)),
		("ClosingAmbientSound", POINTER(USoundCue)),
		("ClosedSound", POINTER(USoundCue)),
		("AmbientSoundComponent", POINTER(UAudioComponent)),
		("BeforeStoppingVelocityZ", c_float),
	]

class  AInterpActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("AInterpActor", AInterpActor_Data),
	]


class  AEmitterPool_Data(Structure):
	_fields_ = [
		("PSCTemplate", POINTER(UParticleSystemComponent)),
		("PoolComponents", TArray_UParticleSystemComponentPtr),
		("ActiveComponents", TArray_UParticleSystemComponentPtr),
		("PhysXSurrogateComponent", POINTER(UParticleSystemComponent)),
		("PhysXSurrogateComponentHalfDownsampling", POINTER(UParticleSystemComponent)),
		("PhysXSurrogateComponentQuarterDownsampling", POINTER(UParticleSystemComponent)),
		("PhysXSurrogateComponentSPHFluid", POINTER(UParticleSystemComponent)),
		("MaxActiveEffects", c_int),
		("bLogPoolOverflow", c_bool, 1),
		("bLogPoolOverflowList", c_bool, 1),
		("", c_ulong, 0),
		("RelativePSCs", TArray_FEmitterBaseInfo),
		("SMC_MIC_ReductionTime", c_float),
		("SMC_MIC_CurrentReductionTime", c_float),
		("IdealStaticMeshComponents", c_int),
		("IdealMaterialInstanceConstants", c_int),
		("FreeSMComponents", TArray_UStaticMeshComponentPtr),
		("FreeMatInstConsts", TArray_UMaterialInstanceConstantPtr),
	]

class  AEmitterPool(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AEmitterPool", AEmitterPool_Data),
	]


class  AGBXNavMesh_Data(Structure):
	_fields_ = [
		("BuildVersion", c_int),
		("BuildGUID", FGuid),
		("MeshID", c_int),
		("ConnectedMeshes", TArray_FGBXConnectedNavMesh),
		("Vertices", TArray_FGBXNavMeshVertex),
		("Polys", TArray_FGBXNavMeshPoly),
		("PolyData", TArray_FGBXNavMeshPolyData),
		("PathSizes", TArray_FGBXNavMeshPathSize),
		("Obstacles", TArray_FGBXNavMeshObstacleData),
		("SpecialMovers", TArray_UGBXCrossLevelReferenceContainerPtr),
		("MeshBase", POINTER(AActor)),
		("PolyLookup", FGBXNavMeshPolyLookup),
		("CachedLocalToWorld", FMatrix),
		("CachedWorldToLocal", FMatrix),
		("CachedBaseLocation", FVector),
		("CachedBaseRotation", FRotator),
		("NextNavMesh", POINTER(AGBXNavMesh)),
		("BuildData", FPointer),
		("bShowPolyDebugText", c_bool, 1),
		("", c_ulong, 0),
		("RenderComponent", POINTER(UGBXNavMeshRenderingComponent)),
	]

class  AGBXNavMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AGBXNavMesh", AGBXNavMesh_Data),
	]


class  AHUD_Data(Structure):
	_fields_ = [
		("WhiteColor", FColor),
		("GreenColor", FColor),
		("RedColor", FColor),
		("PlayerOwner", POINTER(APlayerController)),
		("AnimDebugThis", POINTER(AActor)),
		("AnimDebugStartingPoint", FName),
		("bLostFocusPaused", c_bool, 1),
		("bShowHUD", c_bool, 1),
		("bShowScores", c_bool, 1),
		("bShowDebugInfo", c_bool, 1),
		("bShowAnimDebug", c_bool, 1),
		("bShowBadConnectionAlert", c_bool, 1),
		("bMessageBeep", c_bool, 1),
		("bShowOverlays", c_bool, 1),
		("", c_ulong, 0),
		("HudCanvasScale", c_float),
		("PostRenderedActors", TArray_AActorPtr),
		("ConsoleMessages", TArray_FConsoleMessage),
		("ConsoleColor", FColor),
		("ConsoleMessageCount", c_int),
		("ConsoleFontSize", c_int),
		("MessageFontOffset", c_int),
		("MaxHUDAreaMessageCount", c_int),
		("ConsoleMessagePosX", c_float),
		("ConsoleMessagePosY", c_float),
		("Canvas", POINTER(UCanvas)),
		("LastHUDRenderTime", c_float),
		("RenderDelta", c_float),
		("SizeX", c_float),
		("SizeY", c_float),
		("CenterX", c_float),
		("CenterY", c_float),
		("RatioX", c_float),
		("RatioY", c_float),
		("DebugDisplay", TArray_FName),
		("ActiveDebugDisplay", FName),
		("KismetTextInfo", TArray_FKismetDrawTextInfo),
	]

class  AHUD(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AHUD", AHUD_Data),
	]


class  AIDestructibleObject_Data(Structure):
	_fields_ = []

class  AIDestructibleObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AIDestructibleObject", AIDestructibleObject_Data),
	]


class  AAutoTestManager_Data(Structure):
	_fields_ = [
		("bAutomatedPerfTesting", c_bool, 1),
		("bAutoContinueToNextRound", c_bool, 1),
		("bUsingAutomatedTestingMapList", c_bool, 1),
		("bExitOnCyclesComplete", c_bool, 1),
		("bCheckingForFragmentation", c_bool, 1),
		("bCheckingForMemLeaks", c_bool, 1),
		("bDoingASentinelRun", c_bool, 1),
		("bSentinelStreamingLevelStillLoading", c_bool, 1),
		("bCanCollectStatsWhilePaused", c_bool, 1),
		("bFinishedTraversal", c_bool, 1),
		("", c_ulong, 0),
		("AutomatedPerfRemainingTime", c_int),
		("AutomatedTestingMapIndex", c_int),
		("AutomatedMapTestingList", TArray_FString),
		("AutomatedMapDLC1TestingList", TArray_FString),
		("NumAutomatedMapTestingCycles", c_int),
		("NumberOfMatchesPlayed", c_int),
		("NumMapListCyclesDone", c_int),
		("AutomatedTestingExecCommandToRunAtStartMatch", FString),
		("AutomatedMapTestingTransitionMap", FString),
		("SentinelTaskDescription", FString),
		("SentinelTaskParameter", FString),
		("SentinelTagDesc", FString),
		("SentinelPC", POINTER(APlayerController)),
		("SentinelTravelArray", TArray_FVector),
		("SentinelNavigationIdx", c_int),
		("SentinelIdx", c_int),
		("NumRotationsIncrement", c_int),
		("TravelPointsIncrement", c_int),
		("NumMinutesPerMap", c_int),
		("CommandsToRunAtEachTravelTheWorldNode", TArray_FString),
		("CommandStringToExec", FString),
		("SelectedCharacterClass", FString),
		("StationDefName", FName),
		("AutomatedTestingTravelType", FString),
		("NumOfDLCsToIncludeInRun", c_int),
	]

class  AAutoTestManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AAutoTestManager", AAutoTestManager_Data),
	]


class  ACoverGroup_Data(Structure):
	_fields_ = [
		("CoverLinkRefs", TArray_FActorReference),
		("AutoSelectRadius", c_float),
		("AutoSelectHeight", c_float),
	]

class  ACoverGroup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("ACoverGroup", ACoverGroup_Data),
	]


class  AFileWriter_Data(Structure):
	_fields_ = [
		("ArchivePtr", FPointer),
		("Filename", FString),
		("FileType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bFlushEachWrite", c_bool, 1),
		("bWantsAsyncWrites", c_bool, 1),
		("", c_ulong, 0),
	]

class  AFileWriter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFileWriter", AFileWriter_Data),
	]


class  AFileLog_Data(Structure):
	_fields_ = []

class  AFileLog(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFileWriter", AFileWriter_Data),
		("AFileLog", AFileLog_Data),
	]


class  AGameInfo_Data(Structure):
	_fields_ = [
		("bRestartLevel", c_bool, 1),
		("bPauseable", c_bool, 1),
		("bTeamGame", c_bool, 1),
		("bGameEnded", c_bool, 1),
		("bOverTime", c_bool, 1),
		("bDelayedStart", c_bool, 1),
		("bWaitingToStartMatch", c_bool, 1),
		("bChangeLevels", c_bool, 1),
		("bAlreadyChanged", c_bool, 1),
		("bAdminCanPause", c_bool, 1),
		("bGameRestarted", c_bool, 1),
		("bLevelChange", c_bool, 1),
		("bKickLiveIdlers", c_bool, 1),
		("bShutdownAIWhenIrrelevant", c_bool, 1),
		("bUsingArbitration", c_bool, 1),
		("bHasArbitratedHandshakeBegun", c_bool, 1),
		("bNeedsEndGameHandshake", c_bool, 1),
		("bIsEndGameHandshakeComplete", c_bool, 1),
		("bHasEndGameHandshakeBegun", c_bool, 1),
		("bFixedPlayerStart", c_bool, 1),
		("bUseSeamlessTravel", c_bool, 1),
		("bHasNetworkError", c_bool, 1),
		("bRequiresPushToTalk", c_bool, 1),
		("bIsStandbyCheckingEnabled", c_bool, 1),
		("bIsStandbyCheckingOn", c_bool, 1),
		("bHasStandbyCheatTriggered", c_bool, 1),
		("bNewOnlineSessionOnTravel", c_bool, 1),
		("", c_ulong, 0),
		("CauseEventCommand", FString),
		("BugLocString", FString),
		("BugRotString", FString),
		("PendingArbitrationPCs", TArray_APlayerControllerPtr),
		("ArbitrationPCs", TArray_APlayerControllerPtr),
		("ArbitrationHandshakeTimeout", c_float),
		("GameDifficulty", c_float),
		("GoreLevel", c_int),
		("GameSpeed", c_float),
		("DefaultPawnClass", POINTER(UClass)),
		("HUDType", POINTER(UClass)),
		("MaxSpectators", c_int),
		("MaxSpectatorsAllowed", c_int),
		("NumSpectators", c_int),
		("MaxPlayers", c_int),
		("MaxPlayersAllowed", c_int),
		("NumPlayers", c_int),
		("EffectiveNumPlayers", c_int),
		("NumBots", c_int),
		("NumTravellingPlayers", c_int),
		("CurrentID", c_int),
		("DefaultPlayerName", FString),
		("GameName", FString),
		("GoalScore", c_int),
		("MaxLives", c_int),
		("TimeLimit", c_int),
		("DeathMessageClass", POINTER(UClass)),
		("GameMessageClass", POINTER(UClass)),
		("BaseMutator", POINTER(AMutator)),
		("AccessControlClass", POINTER(UClass)),
		("AccessControl", POINTER(AAccessControl)),
		("BroadcastHandlerClass", POINTER(UClass)),
		("BroadcastHandler", POINTER(ABroadcastHandler)),
		("AutoTestManagerClass", POINTER(UClass)),
		("MyAutoTestManager", POINTER(AAutoTestManager)),
		("PlayerControllerClass", POINTER(UClass)),
		("PlayerReplicationInfoClass", POINTER(UClass)),
		("GameReplicationInfoClass", POINTER(UClass)),
		("GameReplicationInfo", POINTER(AGameReplicationInfo)),
		("MaxIdleTime", c_float),
		("MaxTimeMargin", c_float),
		("TimeMarginSlack", c_float),
		("MinTimeMargin", c_float),
		("InactivePRIArray", TArray_APlayerReplicationInfoPtr),
		("Pausers", TArray_FScriptDelegate),
		("OnlineSub", POINTER(UOnlineSubsystem)),
		("GameInterface", FScriptInterface),
		("OnlineStatsWriteClass", POINTER(UClass)),
		("LeaderboardId", c_int),
		("ArbitratedLeaderboardId", c_int),
		("CoverReplicatorBase", POINTER(ACoverReplicator)),
		("OnlineGameSettingsClass", POINTER(UClass)),
		("DebugBeaconActorClasses", TArray_UClassPtr),
		("ServerOptions", FString),
		("AdjustedNetSpeed", c_int),
		("LastNetSpeedUpdateTime", c_float),
		("TotalNetBandwidth", c_int),
		("MinDynamicBandwidth", c_int),
		("MaxDynamicBandwidth", c_int),
		("StandbyRxCheatTime", c_float),
		("StandbyTxCheatTime", c_float),
		("BadPingThreshold", c_int),
		("PercentMissingForRxStandby", c_float),
		("PercentMissingForTxStandby", c_float),
		("PercentForBadPing", c_float),
		("JoinInProgressStandbyWaitTime", c_float),
		("GameInfoClassAliases", TArray_FGameClassShortName),
		("DefaultGameType", FString),
		("DefaultMapPrefixes", TArray_FGameTypePrefix),
		("CustomMapPrefixes", TArray_FGameTypePrefix),
		("AnimTreePoolSize", c_int),
		("__CanUnpause__Delegate", FScriptDelegate),
	]

class  AGameInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AGameInfo", AGameInfo_Data),
	]


class  AMutator_Data(Structure):
	_fields_ = [
		("NextMutator", POINTER(AMutator)),
		("GroupNames", TArray_FString),
		("bUserAdded", c_bool, 1),
		("", c_ulong, 0),
	]

class  AMutator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AMutator", AMutator_Data),
	]


class  APotentialClimbWatcher_Data(Structure):
	_fields_ = []

class  APotentialClimbWatcher(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("APotentialClimbWatcher", APotentialClimbWatcher_Data),
	]


class  ARoute_Data(Structure):
	_fields_ = [
		("VfTable_IEditorLinkSelectionInterface", FPointer),
		("RouteType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("RouteList", TArray_FActorReference),
		("FudgeFactor", c_float),
		("RouteIndexOffset", c_int),
	]

class  ARoute(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("ARoute", ARoute_Data),
	]


class  AWindPointSource_Data(Structure):
	_fields_ = [
		("Component", POINTER(UWindPointSourceComponent)),
	]

class  AWindPointSource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AWindPointSource", AWindPointSource_Data),
	]


class  AKeypoint_Data(Structure):
	_fields_ = [
		("SpriteComp", POINTER(USpriteComponent)),
	]

class  AKeypoint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AKeypoint", AKeypoint_Data),
	]


class  ATargetPoint_Data(Structure):
	_fields_ = [
		("SpawnRefCount", c_int),
	]

class  ATargetPoint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AKeypoint", AKeypoint_Data),
		("ATargetPoint", ATargetPoint_Data),
	]


class  ALevelLandmark_Data(Structure):
	_fields_ = [
		("LandmarkName", FString),
		("LandmarkType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("AssociatedStationDefinitionName", FName),
	]

class  ALevelLandmark(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALevelLandmark", ALevelLandmark_Data),
	]


class  APersistentTransitionLandmark_Data(Structure):
	_fields_ = [
		("FromMapName", FString),
		("ToMapName", FString),
		("RequiredSublevelNames", TArray_FName),
	]

class  APersistentTransitionLandmark(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALevelLandmark", ALevelLandmark_Data),
		("APersistentTransitionLandmark", APersistentTransitionLandmark_Data),
	]


class  AMaterialInstanceActor_Data(Structure):
	_fields_ = [
		("MatInst", POINTER(UMaterialInstanceConstant)),
	]

class  AMaterialInstanceActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AMaterialInstanceActor", AMaterialInstanceActor_Data),
	]


class  AMatineeActor_Data(Structure):
	_fields_ = [
		("InterpAction", POINTER(USeqAct_Interp)),
		("bIsPlaying", c_bool, 1),
		("bReversePlayback", c_bool, 1),
		("bPaused", c_bool, 1),
		("AllAIGroupsInitialized", c_bool, 1),
		("", c_ulong, 0),
		("PlayRate", c_float),
		("Position", c_float),
		("AIGroupNames", FName * 10),
		("AIGroupPawns", POINTER(APawn) * 10),
		("AIGroupInitStage", int * 10),
		("ClientSidePositionErrorTolerance", c_float),
	]

class  AMatineeActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AMatineeActor", AMatineeActor_Data),
	]


class  ANavigationPoint_Data(Structure):
	_fields_ = [
		("bEndPoint", c_bool, 1),
		("bTransientEndPoint", c_bool, 1),
		("bHideEditorPaths", c_bool, 1),
		("bCanReach", c_bool, 1),
		("bBlocked", c_bool, 1),
		("bOneWayPath", c_bool, 1),
		("bNeverUseStrafing", c_bool, 1),
		("bAlwaysUseStrafing", c_bool, 1),
		("bForceNoStrafing", c_bool, 1),
		("bAutoBuilt", c_bool, 1),
		("bSpecialMove", c_bool, 1),
		("bNoAutoConnect", c_bool, 1),
		("bNotBased", c_bool, 1),
		("bPathsChanged", c_bool, 1),
		("bDestinationOnly", c_bool, 1),
		("bSourceOnly", c_bool, 1),
		("bSpecialForced", c_bool, 1),
		("bMustBeReachable", c_bool, 1),
		("bBlockable", c_bool, 1),
		("bFlyingPreferred", c_bool, 1),
		("bMayCausePain", c_bool, 1),
		("bAlreadyVisited", c_bool, 1),
		("bVehicleDestination", c_bool, 1),
		("bMakeSourceOnly", c_bool, 1),
		("bMustTouchToReach", c_bool, 1),
		("bCanWalkOnToReach", c_bool, 1),
		("bBuildLongPaths", c_bool, 1),
		("bBlockedForVehicles", c_bool, 1),
		("bPreferredVehiclePath", c_bool, 1),
		("bHasCrossLevelPaths", c_bool, 1),
		("bShouldSaveForCheckpoint", c_bool, 1),
		("bRequireTraceTest", c_bool, 1),
		("bIsValidStoppingPoint", c_bool, 1),
		("bReservationRequiredToStopHere", c_bool, 1),
		("bDisplayAreaReach", c_bool, 1),
		("", c_ulong, 0),
		("NavOctreeObject", FNavigationOctreeObject),
		("PathRenderingComponentClass", POINTER(UClass)),
		("PathList", TArray_UReachSpecPtr),
		("visitedWeight", c_int),
		("bestPathWeight", c_int),
		("nextNavigationPoint", POINTER(ANavigationPoint)),
		("nextOrdered", POINTER(ANavigationPoint)),
		("prevOrdered", POINTER(ANavigationPoint)),
		("previousPath", POINTER(ANavigationPoint)),
		("Cost", c_int),
		("ExtraCost", c_int),
		("TransientCost", c_int),
		("LastDetourWeight", c_float),
		("CylinderComponent", POINTER(UCylinderComponent)),
		("MaxPathSize", FCylinder),
		("NavGuid", FGuid),
		("NetworkID", c_int),
		("AnchoredPawn", POINTER(APawn)),
		("LastAnchoredPawnTime", c_float),
		("NodeSearchFlags", c_int),
		("AreaActor", POINTER(AHybridNavigationArea)),
		("AreaName", FName),
		("AreaReach", c_int),
		("AreaVerticalReach", c_int),
		("NoStoppingRadius", c_int),
		("BusyPathCostMultiplier", c_float),
	]

class  ANavigationPoint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
	]


class  ACoverLink_Data(Structure):
	_fields_ = [
		("VfTable_IIGBXNavMeshSpecialMove", FPointer),
		("GLOBAL_bUseSlotMarkers", c_bool, 1),
		("bDisabled", c_bool, 1),
		("bClaimAllSlots", c_bool, 1),
		("bAutoSort", c_bool, 1),
		("bAutoAdjust", c_bool, 1),
		("bCircular", c_bool, 1),
		("bLooped", c_bool, 1),
		("bPlayerOnly", c_bool, 1),
		("bDynamicCover", c_bool, 1),
		("bFractureOnTouch", c_bool, 1),
		("bDebug", c_bool, 1),
		("bDebug_FireLinks", c_bool, 1),
		("bDebug_ExposedLinks", c_bool, 1),
		("bDebug_CoverGen", c_bool, 1),
		("bDoAutoSlotDensityFixup", c_bool, 1),
		("", c_ulong, 0),
		("LeanTraceDist", c_float),
		("Slots", TArray_FCoverSlot),
		("DynamicLinkInfos", TArray_FDynamicLinkInfo),
		("Claims", TArray_APawnPtr),
		("InvalidateDistance", c_float),
		("MaxFireLinkDist", c_float),
		("CircularOrigin", FVector),
		("CircularRadius", c_float),
		("AlignDist", c_float),
		("AutoCoverSlotInterval", c_float),
		("StandHeight", c_float),
		("MidHeight", c_float),
		("StandingLeanOffset", FVector),
		("CrouchLeanOffset", FVector),
		("PopupOffset", FVector),
		("SlipDist", c_float),
		("TurnDist", c_float),
		("DangerScale", c_float),
		("CoverSlotMarkerClassName", FString),
		("NextCoverLink", POINTER(ACoverLink)),
		("LocationDescription", c_ubyte),
	]

class  ACoverLink(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ACoverLink", ACoverLink_Data),
	]


class  ADoorMarker_Data(Structure):
	_fields_ = [
		("MyDoor", POINTER(AInterpActor)),
		("DoorType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("DoorTrigger", POINTER(AActor)),
		("bWaitUntilCompletelyOpened", c_bool, 1),
		("bInitiallyClosed", c_bool, 1),
		("bBlockedWhenClosed", c_bool, 1),
		("bDoorOpen", c_bool, 1),
		("bTempDisabledCollision", c_bool, 1),
		("", c_ulong, 0),
	]

class  ADoorMarker(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ADoorMarker", ADoorMarker_Data),
	]


class  ADynamicAnchor_Data(Structure):
	_fields_ = [
		("CurrentUser", POINTER(AController)),
	]

class  ADynamicAnchor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ADynamicAnchor", ADynamicAnchor_Data),
	]


class  ALadder_Data(Structure):
	_fields_ = [
		("MyLadder", POINTER(ALadderVolume)),
		("LadderList", POINTER(ALadder)),
	]

class  ALadder(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ALadder", ALadder_Data),
	]


class  AAutoLadder_Data(Structure):
	_fields_ = []

class  AAutoLadder(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ALadder", ALadder_Data),
		("AAutoLadder", AAutoLadder_Data),
	]


class  ALiftCenter_Data(Structure):
	_fields_ = [
		("MyLift", POINTER(AInterpActor)),
		("MaxDist2D", c_float),
		("LiftOffset", FVector),
		("bJumpLift", c_bool, 1),
		("", c_ulong, 0),
		("CollisionHeight", c_float),
		("LiftTrigger", POINTER(ATrigger)),
	]

class  ALiftCenter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ALiftCenter", ALiftCenter_Data),
	]


class  ALiftExit_Data(Structure):
	_fields_ = [
		("MyLiftCenter", POINTER(ALiftCenter)),
		("bExitOnly", c_bool, 1),
		("", c_ulong, 0),
	]

class  ALiftExit(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ALiftExit", ALiftExit_Data),
	]


class  APathNode_Data(Structure):
	_fields_ = []

class  APathNode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APathNode", APathNode_Data),
	]


class  AVolumePathNode_Data(Structure):
	_fields_ = [
		("StartingRadius", c_float),
		("StartingHeight", c_float),
	]

class  AVolumePathNode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APathNode", APathNode_Data),
		("AVolumePathNode", AVolumePathNode_Data),
	]


class  APickupFactory_Data(Structure):
	_fields_ = [
		("bOnlyReplicateHidden", c_bool, 1),
		("bPickupHidden", c_bool, 1),
		("bPredictRespawns", c_bool, 1),
		("bIsSuperItem", c_bool, 1),
		("bRespawnPaused", c_bool, 1),
		("", c_ulong, 0),
		("InventoryType", POINTER(UClass)),
		("RespawnEffectTime", c_float),
		("MaxDesireability", c_float),
		("PickupMesh", POINTER(UPrimitiveComponent)),
		("ReplacementFactory", POINTER(APickupFactory)),
		("OriginalFactory", POINTER(APickupFactory)),
	]

class  APickupFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APickupFactory", APickupFactory_Data),
	]


class  APlayerStart_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("bPrimaryStart", c_bool, 1),
		("bBestStart", c_bool, 1),
		("", c_ulong, 0),
		("TeamIndex", c_int),
		("Score", c_int),
		("SelectionIndex", c_int),
	]

class  APlayerStart(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APlayerStart", APlayerStart_Data),
	]


class  APortalMarker_Data(Structure):
	_fields_ = [
		("MyPortal", POINTER(APortalTeleporter)),
	]

class  APortalMarker(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APortalMarker", APortalMarker_Data),
	]


class  APylon_Data(Structure):
	_fields_ = [
		("VfTable_IEditorLinkSelectionInterface", FPointer),
		("NavMeshPtr", FPointer),
		("ObstacleMesh", FPointer),
		("DynamicObstacleMesh", FPointer),
		("WorkingSetPtr", FPointer),
		("PathObjectsThatAffectThisPylon", FPointer),
		("NextPassSeedList", TArray_FVector),
		("OctreeId", FOctreeElementId),
		("OctreeIWasAddedTo", FPointer),
		("NextPylon", POINTER(APylon)),
		("ExpansionVolumes", TArray_AVolumePtr),
		("ExpansionRadius", c_float),
		("MaxExpansionRadius", c_float),
		("PathSizes", TArray_FNavMeshPathSize),
		("PylonRadiusPreview", POINTER(UDrawPylonRadiusComponent)),
		("bImportedMesh", c_bool, 1),
		("bUseExpansionSphereOverride", c_bool, 1),
		("bNeedsCostCheck", c_bool, 1),
		("bDrawEdgePolys", c_bool, 1),
		("bDrawPolyBounds", c_bool, 1),
		("bRenderInShowPaths", c_bool, 1),
		("bDrawWalkableSurface", c_bool, 1),
		("bDrawObstacleSurface", c_bool, 1),
		("bUseGBXValues", c_bool, 1),
		("bUseGBXExpansion", c_bool, 1),
		("bExpansionDoSimplification", c_bool, 1),
		("bExpansionDoThreeToTwoMerge", c_bool, 1),
		("bExpansionDoPolyMerge", c_bool, 1),
		("bExpansionDoPolyConcaveMerge", c_bool, 1),
		("bExpansionDoSquareMerge", c_bool, 1),
		("bExpansionDoSaveFixup", c_bool, 1),
		("bExpansionCullPolys", c_bool, 1),
		("bExpansionBuildObstacleMesh", c_bool, 1),
		("bExpansionCreateEdgeConnections", c_bool, 1),
		("bExpansionDoSubdivisionMerging", c_bool, 1),
		("bExpansionDoObstacleMeshSimplification", c_bool, 1),
		("bExpansionDoEdgeSmoothing", c_bool, 1),
		("bExpansionDoRawGridOnly", c_bool, 1),
		("bExpansionDoConcaveSlabsOnly", c_bool, 1),
		("bExpansionDoEdgeSimplificationEvenInConcaveSlabMode", c_bool, 1),
		("bExpansionDrawDropDownPolys", c_bool, 1),
		("bExpansionDrawPolyParents", c_bool, 1),
		("bExpansionDisableSubdivisionHeightSnapping", c_bool, 1),
		("bExpansionDisableVertMaxHeightSlopeMax", c_bool, 1),
		("bBuildThisPylon", c_bool, 1),
		("bDisabled", c_bool, 1),
		("bForceObstacleMeshCollision", c_bool, 1),
		("", c_ulong, 0),
		("ExpansionSphereCenter", FVector),
		("RenderingComp", POINTER(UNavMeshRenderingComponent)),
		("BrokenSprite", POINTER(USpriteComponent)),
		("ImposterPylons", TArray_APylonPtr),
		("OnBuild_DisableCollisionForThese", TArray_AActorPtr),
		("OnBuild_EnableCollisionForThese", TArray_AActorPtr),
		("MaxPolyHeight_Optional", c_float),
		("DebugEdgeCount", c_int),
		("IconScale", c_float),
		("GBX_PolySize", c_int),
		("EdgeCheckHeight", c_float),
		("PolyMergeThreshold", c_float),
		("OuterPylon", POINTER(APylon)),
	]

class  APylon(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APylon", APylon_Data),
	]


class  AAISwitchablePylon_Data(Structure):
	_fields_ = [
		("bOpen", c_bool, 1),
		("", c_ulong, 0),
	]

class  AAISwitchablePylon(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APylon", APylon_Data),
		("AAISwitchablePylon", AAISwitchablePylon_Data),
	]


class  ADynamicPylon_Data(Structure):
	_fields_ = [
		("bMoving", c_bool, 1),
		("", c_ulong, 0),
	]

class  ADynamicPylon(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APylon", APylon_Data),
		("ADynamicPylon", ADynamicPylon_Data),
	]


class  ATeleporter_Data(Structure):
	_fields_ = [
		("URL", FString),
		("ProductRequired", FName),
		("bChangesVelocity", c_bool, 1),
		("bChangesYaw", c_bool, 1),
		("bReversesX", c_bool, 1),
		("bReversesY", c_bool, 1),
		("bReversesZ", c_bool, 1),
		("bEnabled", c_bool, 1),
		("bCanTeleportVehicles", c_bool, 1),
		("", c_ulong, 0),
		("TargetVelocity", FVector),
		("LastFired", c_float),
	]

class  ATeleporter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ATeleporter", ATeleporter_Data),
	]


class  ANote_Data(Structure):
	_fields_ = []

class  ANote(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANote", ANote_Data),
	]


class  AProjectile_Data(Structure):
	_fields_ = [
		("Speed", c_float),
		("MaxSpeed", c_float),
		("bSwitchToZeroCollision", c_bool, 1),
		("bBlockedByInstigator", c_bool, 1),
		("bBegunPlay", c_bool, 1),
		("bRotationFollowsVelocity", c_bool, 1),
		("bIgnoreFoliageTouch", c_bool, 1),
		("", c_ulong, 0),
		("ZeroCollider", POINTER(AActor)),
		("ZeroColliderComponent", POINTER(UPrimitiveComponent)),
		("Damage", c_float),
		("DamageBaseValue", c_float),
		("DamageModifierStack", TArray_UAttributeModifierPtr),
		("DamageRadius", c_float),
		("DamageRadiusBaseValue", c_float),
		("DamageRadiusModifierStack", TArray_UAttributeModifierPtr),
		("MomentumTransfer", c_float),
		("MomentumTransferBaseValue", c_float),
		("MomentumTransferModifierStack", TArray_UAttributeModifierPtr),
		("MyDamageType", POINTER(UClass)),
		("SpawnSound", POINTER(USoundCue)),
		("ImpactSound", POINTER(USoundCue)),
		("InstigatorController", POINTER(AController)),
		("ImpactedActor", POINTER(AActor)),
		("NetCullDistanceSquared", c_float),
		("CylinderComponent", POINTER(UCylinderComponent)),
	]

class  AProjectile(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AProjectile", AProjectile_Data),
	]


class  ARigidBodyBase_Data(Structure):
	_fields_ = []

class  ARigidBodyBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
	]


class  ASceneCaptureActor_Data(Structure):
	_fields_ = [
		("SceneCapture", POINTER(USceneCaptureComponent)),
	]

class  ASceneCaptureActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASceneCaptureActor", ASceneCaptureActor_Data),
	]


class  ASceneCapture2DActor_Data(Structure):
	_fields_ = [
		("DrawFrustum", POINTER(UDrawFrustumComponent)),
	]

class  ASceneCapture2DActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASceneCaptureActor", ASceneCaptureActor_Data),
		("ASceneCapture2DActor", ASceneCapture2DActor_Data),
	]


class  ASceneCaptureCubeMapActor_Data(Structure):
	_fields_ = [
		("StaticMesh", POINTER(UStaticMeshComponent)),
		("CubeMaterialInst", POINTER(UMaterialInstanceConstant)),
	]

class  ASceneCaptureCubeMapActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASceneCaptureActor", ASceneCaptureActor_Data),
		("ASceneCaptureCubeMapActor", ASceneCaptureCubeMapActor_Data),
	]


class  ASceneCaptureReflectActor_Data(Structure):
	_fields_ = [
		("StaticMesh", POINTER(UStaticMeshComponent)),
		("ReflectMaterialInst", POINTER(UMaterialInstanceConstant)),
	]

class  ASceneCaptureReflectActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASceneCaptureActor", ASceneCaptureActor_Data),
		("ASceneCaptureReflectActor", ASceneCaptureReflectActor_Data),
	]


class  ASceneCapturePortalActor_Data(Structure):
	_fields_ = []

class  ASceneCapturePortalActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASceneCaptureActor", ASceneCaptureActor_Data),
		("ASceneCaptureReflectActor", ASceneCaptureReflectActor_Data),
		("ASceneCapturePortalActor", ASceneCapturePortalActor_Data),
	]


class  APortalTeleporter_Data(Structure):
	_fields_ = [
		("SisterPortal", POINTER(APortalTeleporter)),
		("TextureResolutionX", c_int),
		("TextureResolutionY", c_int),
		("MyMarker", POINTER(APortalMarker)),
		("bMovablePortal", c_bool, 1),
		("bAlwaysTeleportNonPawns", c_bool, 1),
		("bCanTeleportVehicles", c_bool, 1),
		("", c_ulong, 0),
	]

class  APortalTeleporter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASceneCaptureActor", ASceneCaptureActor_Data),
		("ASceneCaptureReflectActor", ASceneCaptureReflectActor_Data),
		("ASceneCapturePortalActor", ASceneCapturePortalActor_Data),
		("APortalTeleporter", APortalTeleporter_Data),
	]


class  AStaticMeshActorBase_Data(Structure):
	_fields_ = []

class  AStaticMeshActorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
	]


class  ABlockingMeshCollectionActor_Data(Structure):
	_fields_ = [
		("BlockingMeshComponents", TArray_UBlockingMeshComponentPtr),
		("MaxBlockingMeshComponents", c_int),
	]

class  ABlockingMeshCollectionActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
		("ABlockingMeshCollectionActor", ABlockingMeshCollectionActor_Data),
	]


class  AStaticMeshActor_Data(Structure):
	_fields_ = [
		("StaticMeshComponent", POINTER(UStaticMeshComponent)),
		("bDisableAutoBaseOnProcBuilding", c_bool, 1),
		("", c_ulong, 0),
	]

class  AStaticMeshActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
		("AStaticMeshActor", AStaticMeshActor_Data),
	]


class  AStaticMeshCollectionActor_Data(Structure):
	_fields_ = [
		("StaticMeshComponents", TArray_UStaticMeshComponentPtr),
		("MaxStaticMeshComponents", c_int),
	]

class  AStaticMeshCollectionActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
		("AStaticMeshCollectionActor", AStaticMeshCollectionActor_Data),
	]


class  AStaticMeshActorBasedOnExtremeContent_Data(Structure):
	_fields_ = [
		("StaticMeshComponent", POINTER(UStaticMeshComponent)),
		("ExtremeContent", TArray_FSMMaterialSetterDatum),
		("NonExtremeContent", TArray_FSMMaterialSetterDatum),
	]

class  AStaticMeshActorBasedOnExtremeContent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBasedOnExtremeContent", AStaticMeshActorBasedOnExtremeContent_Data),
	]


class  ATeleporterDestination_Data(Structure):
	_fields_ = [
		("ExitPoints", TArray_AActorPtr),
		("ExitPointsCounter", c_int),
		("IsEnabled", c_bool, 1),
		("Resurrect", c_bool, 1),
		("", c_ulong, 0),
	]

class  ATeleporterDestination(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATeleporterDestination", ATeleporterDestination_Data),
	]


class  ATrigger_Data(Structure):
	_fields_ = [
		("CylinderComponent", POINTER(UCylinderComponent)),
		("bRecentlyTriggered", c_bool, 1),
		("", c_ulong, 0),
		("AITriggerDelay", c_float),
	]

class  ATrigger(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATrigger", ATrigger_Data),
	]


class  ATrigger_PawnsOnly_Data(Structure):
	_fields_ = []

class  ATrigger_PawnsOnly(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATrigger", ATrigger_Data),
		("ATrigger_PawnsOnly", ATrigger_PawnsOnly_Data),
	]


class  UActorComponent_Data(Structure):
	_fields_ = [
		("VfTable_IIWorldBody", FPointer),
		("Scene", FPointer),
		("Owner", POINTER(AActor)),
		("bAttached", c_bool, 1),
		("bSkipChildComponentUpdate", c_bool, 1),
		("bTickInEditor", c_bool, 1),
		("bTickInGame", c_bool, 1),
		("bTickInStatusMenu", c_bool, 1),
		("bNeedsReattach", c_bool, 1),
		("bNeedsUpdateTransform", c_bool, 1),
		("", c_ulong, 0),
		("TickGroup", c_ubyte),
	]

class  UActorComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
	]


class  UAkComponent_Data(Structure):
	_fields_ = [
		("SocketName", FName),
		("bUseCustomTransform", c_bool, 1),
		("bCustomTransformChanged", c_bool, 1),
		("bShouldAllSourcesActAsOneSound", c_bool, 1),
		("bForceRecalcEnvironmentAndOcclusion", c_bool, 1),
		("bReturnToPoolWhenFinishedPlaying", c_bool, 1),
		("bNeverReturnToPoolAutomatically", c_bool, 1),
		("bCanBeOccluded", c_bool, 1),
		("bPersistAcrossWorldChanges", c_bool, 1),
		("bIsReattaching", c_bool, 1),
		("bRegistered", c_bool, 1),
		("", c_ulong, 0),
		("CustomLocations", TArray_FVector),
		("CustomRotations", TArray_FRotator),
		("LastEnvironmentalAndOcclusionUpdateTime", c_float),
		("LastSubtitleUpdateTime", c_float),
		("HeadPlayingInfoPtr", FPointer),
		("TailPlayingInfoPtr", FPointer),
		("PendingFaceFX", FPendingFaceFXInfo),
		("PendingSubtitle", FPendingSubtitleInfo),
		("SubtitlesPendingKill", TArray_FPointer),
		("CurrentObstructionLevels", c_float * 8),
		("TargetObstructionLevels", c_float * 8),
		("CurrentOcclusionLevels", c_float * 8),
		("TargetOcclusionLevels", c_float * 8),
		("SpecialOcclusionProvider", FScriptInterface),
		("KnownRTPCs", FMap_Mirror),
		("KnownSwitches", FMap_Mirror),
		("__OnAkEventCompleted__Delegate", FScriptDelegate),
		("__UpdateComponentPosition__Delegate", FScriptDelegate),
	]

class  UAkComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UAkComponent", UAkComponent_Data),
	]


class  UAudioComponent_Data(Structure):
	_fields_ = [
		("SoundCue", POINTER(USoundCue)),
		("CueFirstNode", POINTER(USoundNode)),
		("InstanceParameters", TArray_FAudioComponentParam),
		("bUseOwnerLocation", c_bool, 1),
		("bAutoPlay", c_bool, 1),
		("bAutoDestroy", c_bool, 1),
		("bStopWhenOwnerDestroyed", c_bool, 1),
		("bShouldRemainActiveIfDropped", c_bool, 1),
		("bWasOccluded", c_bool, 1),
		("bSuppressSubtitles", c_bool, 1),
		("bWasPlaying", c_bool, 1),
		("bAllowSpatialization", c_bool, 1),
		("bFinished", c_bool, 1),
		("bApplyRadioFilter", c_bool, 1),
		("bRadioFilterSelected", c_bool, 1),
		("bPreviewComponent", c_bool, 1),
		("bIgnoreForFlushing", c_bool, 1),
		("", c_ulong, 0),
		("StereoBleed", c_float),
		("LFEBleed", c_float),
		("bEQFilterApplied", c_bool, 1),
		("bAlwaysPlay", c_bool, 1),
		("bIsUISound", c_bool, 1),
		("bIsMusic", c_bool, 1),
		("bReverb", c_bool, 1),
		("bCenterChannelOnly", c_bool, 1),
		("bIsDialog", c_bool, 1),
		("bIsAmbience", c_bool, 1),
		("", c_ulong, 0),
		("WaveInstances", TArray_FPointer),
		("SoundNodeData", TArray_unsigned_char),
		("Unknown1", c_ubyte, 0x),
		("SoundNodeResetWaveMap", FMultiMap_Mirror),
		("Listener", FPointer),
		("PlaybackTime", c_float),
		("PortalVolume", POINTER(APortalVolume)),
		("Location", FVector),
		("ComponentLocation", FVector),
		("LastOwner", POINTER(AActor)),
		("SubtitlePriority", c_float),
		("FadeInStartTime", c_float),
		("FadeInStopTime", c_float),
		("FadeInTargetVolume", c_float),
		("FadeOutStartTime", c_float),
		("FadeOutStopTime", c_float),
		("FadeOutTargetVolume", c_float),
		("AdjustVolumeStartTime", c_float),
		("AdjustVolumeStopTime", c_float),
		("AdjustVolumeTargetVolume", c_float),
		("CurrAdjustVolumeTargetVolume", c_float),
		("CurrentNotifyBufferFinishedHook", POINTER(USoundNode)),
		("CurrentLocation", FVector),
		("CurrentVolume", c_float),
		("CurrentPitch", c_float),
		("CurrentHighFrequencyGain", c_float),
		("CurrentUseSpatialization", c_int),
		("CurrentNotifyOnLoop", c_int),
		("CurrentVolumeMultiplier", c_float),
		("CurrentPitchMultiplier", c_float),
		("CurrentHighFrequencyGainMultiplier", c_float),
		("CurrentVoiceCenterChannelVolume", c_float),
		("CurrentRadioFilterVolume", c_float),
		("CurrentRadioFilterVolumeThreshold", c_float),
		("LastUpdateTime", FDouble),
		("SourceInteriorVolume", c_float),
		("SourceInteriorLPF", c_float),
		("CurrentInteriorVolume", c_float),
		("CurrentInteriorLPF", c_float),
		("LastLocation", FVector),
		("LastInteriorSettings", FInteriorSettings),
		("LastReverbVolumeIndex", c_int),
		("VolumeMultiplier", c_float),
		("PitchMultiplier", c_float),
		("HighFrequencyGainMultiplier", c_float),
		("OcclusionCheckInterval", c_float),
		("LastOcclusionCheckTime", c_float),
		("PreviewSoundRadius", POINTER(UDrawSoundRadiusComponent)),
		("__OnAudioFinished__Delegate", FScriptDelegate),
		("__OnQueueSubtitles__Delegate", FScriptDelegate),
	]

class  UAudioComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UAudioComponent", UAudioComponent_Data),
	]


class  UHeightFogComponent_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
		("Height", c_float),
		("Density", c_float),
		("LightBrightness", c_float),
		("LightColor", FColor),
		("ExtinctionDistance", c_float),
		("StartDistance", c_float),
	]

class  UHeightFogComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UHeightFogComponent", UHeightFogComponent_Data),
	]


class  UPrimitiveComponent_Data(Structure):
	_fields_ = [
		("Tag", c_int),
		("Bounds", FBoxSphereBounds),
		("SceneInfo", FPointer),
		("DetachFence", c_int),
		("_LocalToWorldDeterminant", c_float),
		("Unknown1", c_ubyte, 0x),
		("_LocalToWorld", FMatrix),
		("_WorldToLocal", FMatrix),
		("_LocalToWorldScale", FVector),
		("MotionBlurInfoIndex", c_int),
		("DecalList", TArray_FPointer),
		("DecalsToReattach", TArray_UDecalComponentPtr),
		("FogVolumeComponent", POINTER(UFogVolumeDensityComponent)),
		("OverrideLightComponent", POINTER(ULightComponent)),
		("LightEnvironment", POINTER(ULightEnvironmentComponent)),
		("PreviousLightEnvironment", POINTER(ULightEnvironmentComponent)),
		("MinDrawDistance", c_float),
		("MaxDrawDistance", c_float),
		("CachedMaxDrawDistance", c_float),
		("MotionBlurInstanceScale", c_float),
		("DepthPriorityGroup", c_ubyte),
		("DetailMode", c_ubyte),
		("RBChannel", c_ubyte),
		("DynamicShadowCastRelevance", c_ubyte),
		("RBDominanceGroup", c_ubyte),
		("PreviewEnvironmentShadowing", c_ubyte),
		("ScriptRigidBodyCollisionThresholdCompiled", c_ubyte),
		("TranslucencySortPriority", c_ubyte),
		("bAllowCullDistanceVolume", c_bool, 1),
		("bAllowShadowRelevanceVolume", c_bool, 1),
		("HiddenGame", c_bool, 1),
		("HiddenEditor", c_bool, 1),
		("bOwnerNoSee", c_bool, 1),
		("bOnlyOwnerSee", c_bool, 1),
		("bOnlyPlayerOwnerSee", c_bool, 1),
		("bPlayerOwnerNoSee", c_bool, 1),
		("bIgnoreOwnerHidden", c_bool, 1),
		("bUseAsOccluder", c_bool, 1),
		("bAllowApproximateOcclusion", c_bool, 1),
		("bFirstFrameOcclusion", c_bool, 1),
		("bIgnoreNearPlaneIntersection", c_bool, 1),
		("bSelectable", c_bool, 1),
		("bForceMipStreaming", c_bool, 1),
		("bAcceptsStaticDecals", c_bool, 1),
		("bAcceptsDynamicDecals", c_bool, 1),
		("bAllowDecalAutomaticReAttach", c_bool, 1),
		("bAcceptsFoliage", c_bool, 1),
		("bInWorldForeground", c_bool, 1),
		("CastShadow", c_bool, 1),
		("bForceDirectLightMap", c_bool, 1),
		("bCastDynamicShadow", c_bool, 1),
		("bCastStaticShadow", c_bool, 1),
		("bCastOccludedShadow", c_bool, 1),
		("bSelfShadowOnly", c_bool, 1),
		("bCastHiddenShadow", c_bool, 1),
		("bCastShadowAsTwoSided", c_bool, 1),
		("bAcceptsLights", c_bool, 1),
		("bAcceptsDynamicLights", c_bool, 1),
		("bAcceptsSkyLight", c_bool, 1),
		("bUseOnePassLightingOnTranslucency", c_bool, 1),
		("bUsePrecomputedShadows", c_bool, 1),
		("bInstancedStaticRB", c_bool, 1),
		("CollideActors", c_bool, 1),
		("AlwaysCheckCollision", c_bool, 1),
		("BlockActors", c_bool, 1),
		("BlockZeroExtent", c_bool, 1),
		("BlockNonZeroExtent", c_bool, 1),
		("CanBlockCamera", c_bool, 1),
		("BlockRigidBody", c_bool, 1),
		("bBlockFootPlacement", c_bool, 1),
		("BulletListener", c_bool, 1),
		("bDisableAllRigidBody", c_bool, 1),
		("bSkipRBGeomCreation", c_bool, 1),
		("bNotifyRigidBodyCollision", c_bool, 1),
		("bFluidDrain", c_bool, 1),
		("bFluidTwoWay", c_bool, 1),
		("bIgnoreRadialImpulse", c_bool, 1),
		("bIgnoreRadialForce", c_bool, 1),
		("bIgnoreForceField", c_bool, 1),
		("bUseCompartment", c_bool, 1),
		("AlwaysLoadOnClient", c_bool, 1),
		("AlwaysLoadOnServer", c_bool, 1),
		("bPrimitiveRequiresOcclusionQuery", c_bool, 1),
		("bIgnoreHiddenActorsMembership", c_bool, 1),
		("AbsoluteTranslation", c_bool, 1),
		("AbsoluteRotation", c_bool, 1),
		("AbsoluteScale", c_bool, 1),
		("bUseOrthonormalizedLighting", c_bool, 1),
		("bBoundToGFxMovie", c_bool, 1),
		("bWasSNFiltered", c_bool, 1),
		("", c_ulong, 0),
		("OctreeNodes", TArray_int),
		("VisibilityId", c_int),
		("LightingChannels", FLightingChannelContainer),
		("RBCollideWithChannels", FRBCollisionChannelContainer),
		("PhysMaterialOverride", POINTER(UPhysicalMaterial)),
		("BodyInstance", POINTER(URB_BodyInstance)),
		("Unknown2", c_ubyte, 0x),
		("CachedParentToWorld", FMatrix),
		("CachedParentToWorldScale", FVector),
		("Translation", FVector),
		("Rotation", FRotator),
		("Scale", c_float),
		("Scale3D", FVector),
		("BoundsScale", c_float),
		("LastSubmitTime", c_float),
		("LastRenderTime", c_float),
	]

class  UPrimitiveComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
	]


class  UArrowComponent_Data(Structure):
	_fields_ = [
		("ArrowColor", FColor),
		("ArrowSize", c_float),
		("bTreatAsASprite", c_bool, 1),
		("bIsDebugBeacon", c_bool, 1),
		("", c_ulong, 0),
	]

class  UArrowComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UArrowComponent", UArrowComponent_Data),
	]


class  UBrushComponent_Data(Structure):
	_fields_ = [
		("Brush", POINTER(UModel)),
		("BrushAggGeom", FKAggregateGeom),
		("BrushPhysDesc", FPointer),
		("CachedPhysBrushData", FKCachedConvexData_Mirror),
		("CachedPhysBrushDataVersion", c_int),
		("bBlockComplexCollisionTrace", c_bool, 1),
		("", c_ulong, 0),
	]

class  UBrushComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UBrushComponent", UBrushComponent_Data),
	]


class  UCameraConeComponent_Data(Structure):
	_fields_ = []

class  UCameraConeComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UCameraConeComponent", UCameraConeComponent_Data),
	]


class  UCylinderComponent_Data(Structure):
	_fields_ = [
		("CollisionHeight", c_float),
		("CollisionRadius", c_float),
		("bDrawBoundingBox", c_bool, 1),
		("bDrawNonColliding", c_bool, 1),
		("bAlwaysRenderIfSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UCylinderComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UCylinderComponent", UCylinderComponent_Data),
	]


class  USphereComponent_Data(Structure):
	_fields_ = []

class  USphereComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UCylinderComponent", UCylinderComponent_Data),
		("USphereComponent", USphereComponent_Data),
	]


class  UDrawBoxComponent_Data(Structure):
	_fields_ = [
		("BoxColor", FColor),
		("BoxMaterial", POINTER(UMaterial)),
		("BoxExtent", FVector),
		("bDrawWireBox", c_bool, 1),
		("bDrawLitBox", c_bool, 1),
		("bDrawOnlyIfSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UDrawBoxComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawBoxComponent", UDrawBoxComponent_Data),
	]


class  UDrawCapsuleComponent_Data(Structure):
	_fields_ = [
		("CapsuleColor", FColor),
		("CapsuleMaterial", POINTER(UMaterial)),
		("CapsuleHeight", c_float),
		("CapsuleRadius", c_float),
		("bDrawWireCapsule", c_bool, 1),
		("bDrawLitCapsule", c_bool, 1),
		("bDrawOnlyIfSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UDrawCapsuleComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawCapsuleComponent", UDrawCapsuleComponent_Data),
	]


class  UDrawConeComponent_Data(Structure):
	_fields_ = [
		("ConeColor", FColor),
		("ConeRadius", c_float),
		("ConeAngle", c_float),
		("ConeSides", c_int),
	]

class  UDrawConeComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawConeComponent", UDrawConeComponent_Data),
	]


class  UDrawCylinderComponent_Data(Structure):
	_fields_ = [
		("CylinderColor", FColor),
		("CylinderMaterial", POINTER(UMaterial)),
		("CylinderRadius", c_float),
		("CylinderTopRadius", c_float),
		("CylinderHeight", c_float),
		("CylinderHeightOffset", c_float),
		("CylinderSides", c_int),
		("bDrawWireCylinder", c_bool, 1),
		("bDrawLitCylinder", c_bool, 1),
		("bDrawOnlyIfSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UDrawCylinderComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawCylinderComponent", UDrawCylinderComponent_Data),
	]


class  UDrawFrustumComponent_Data(Structure):
	_fields_ = [
		("FrustumColor", FColor),
		("FrustumAngle", c_float),
		("FrustumAspectRatio", c_float),
		("FrustumStartDist", c_float),
		("FrustumEndDist", c_float),
		("Texture", POINTER(UTexture)),
	]

class  UDrawFrustumComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawFrustumComponent", UDrawFrustumComponent_Data),
	]


class  UDrawQuadComponent_Data(Structure):
	_fields_ = [
		("Texture", POINTER(UTexture)),
		("Width", c_float),
		("Height", c_float),
	]

class  UDrawQuadComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawQuadComponent", UDrawQuadComponent_Data),
	]


class  UDrawSphereComponent_Data(Structure):
	_fields_ = [
		("SphereColor", FColor),
		("SphereMaterial", POINTER(UMaterial)),
		("SphereRadius", c_float),
		("SphereSides", c_int),
		("bDrawWireSphere", c_bool, 1),
		("bDrawLitSphere", c_bool, 1),
		("bDrawOnlyIfSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UDrawSphereComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawSphereComponent", UDrawSphereComponent_Data),
	]


class  UDrawPylonRadiusComponent_Data(Structure):
	_fields_ = []

class  UDrawPylonRadiusComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawSphereComponent", UDrawSphereComponent_Data),
		("UDrawPylonRadiusComponent", UDrawPylonRadiusComponent_Data),
	]


class  UDrawSoundRadiusComponent_Data(Structure):
	_fields_ = []

class  UDrawSoundRadiusComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawSphereComponent", UDrawSphereComponent_Data),
		("UDrawSoundRadiusComponent", UDrawSoundRadiusComponent_Data),
	]


class  UGBXNavMeshRenderingComponent_Data(Structure):
	_fields_ = [
		("bDrawPolys", c_bool, 1),
		("bDrawSplitPlanes", c_bool, 1),
		("bDrawEdgeConnections", c_bool, 1),
		("bDrawSimplificationConnections", c_bool, 1),
		("bDrawSimplifiedShapes", c_bool, 1),
		("bDrawFailedSimplificationShapes", c_bool, 1),
		("bDrawFailedTriangulationShapes", c_bool, 1),
		("bDrawBlockedEdges", c_bool, 1),
		("", c_ulong, 0),
		("MeshSpacingHullsToDraw", TArray_int),
		("NavMeshRenderingData", FPointer),
	]

class  UGBXNavMeshRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UGBXNavMeshRenderingComponent", UGBXNavMeshRenderingComponent_Data),
	]


class  ULevelGridVolumeRenderingComponent_Data(Structure):
	_fields_ = []

class  ULevelGridVolumeRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("ULevelGridVolumeRenderingComponent", ULevelGridVolumeRenderingComponent_Data),
	]


class  ULineBatchComponent_Data(Structure):
	_fields_ = [
		("FPrimitiveDrawInterfaceVfTable", FPointer),
		("FPrimitiveDrawInterfaceView", FPointer),
		("BatchedLines", TArray_FPointer),
		("BatchedPoints", TArray_FPointer),
		("DefaultLifeTime", c_float),
	]

class  ULineBatchComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("ULineBatchComponent", ULineBatchComponent_Data),
	]


class  UModelComponent_Data(Structure):
	_fields_ = [
		("Model", POINTER(UObject)),
		("ZoneIndex", c_int),
		("ComponentIndex", c_int),
		("Nodes", TArray_FPointer),
		("Elements", TArray_FPointer),
	]

class  UModelComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UModelComponent", UModelComponent_Data),
	]


class  USocketComponent_Data(Structure):
	_fields_ = [
		("SocketName", FName),
	]

class  USocketComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("USocketComponent", USocketComponent_Data),
	]


class  UHomingTargetComponent_Data(Structure):
	_fields_ = []

class  UHomingTargetComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("USocketComponent", USocketComponent_Data),
		("UHomingTargetComponent", UHomingTargetComponent_Data),
	]


class  USpriteComponent_Data(Structure):
	_fields_ = [
		("Sprite", POINTER(UTexture2D)),
		("bIsScreenSizeScaled", c_bool, 1),
		("", c_ulong, 0),
		("ScreenSize", c_float),
		("U", c_float),
		("UL", c_float),
		("V", c_float),
		("VL", c_float),
	]

class  USpriteComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("USpriteComponent", USpriteComponent_Data),
	]


class  USpriteRTTComponent_Data(Structure):
	_fields_ = [
		("SpriteRTT", POINTER(UTextureRenderTarget2D)),
	]

class  USpriteRTTComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("USpriteComponent", USpriteComponent_Data),
		("USpriteRTTComponent", USpriteRTTComponent_Data),
	]


class  URadialBlurComponent_Data(Structure):
	_fields_ = [
		("Material", POINTER(UMaterialInterface)),
		("DepthPriorityGroup", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BlurScale", c_float),
		("BlurFalloffExponent", c_float),
		("BlurOpacity", c_float),
		("MaxCullDistance", c_float),
		("DistanceFalloffExponent", c_float),
		("bRenderAsVelocity", c_bool, 1),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
		("Unknown2", c_ubyte, 0x),
		("LocalToWorld", FMatrix),
	]

class  URadialBlurComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("URadialBlurComponent", URadialBlurComponent_Data),
	]


class  USceneCaptureComponent_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("bEnablePostProcess", c_bool, 1),
		("bEnableFog", c_bool, 1),
		("bUseMainScenePostProcessSettings", c_bool, 1),
		("bSkipUpdateIfTextureUsersOccluded", c_bool, 1),
		("bSkipUpdateIfOwnerOccluded", c_bool, 1),
		("bSkipRenderingDepthPrepass", c_bool, 1),
		("", c_ulong, 0),
		("ClearColor", FColor),
		("ViewMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("SceneLOD", c_int),
		("FrameRate", c_float),
		("PostProcess", POINTER(UPostProcessChain)),
		("MaxUpdateDist", c_float),
		("MaxViewDistanceOverride", c_float),
		("MaxStreamingUpdateDist", c_float),
		("CaptureInfo", FPointer),
		("ViewState", FPointer),
		("PostProcessProxies", TArray_FPointer),
	]

class  USceneCaptureComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USceneCaptureComponent", USceneCaptureComponent_Data),
	]


class  USceneCapture2DComponent_Data(Structure):
	_fields_ = [
		("TextureTarget", POINTER(UTextureRenderTarget2D)),
		("FieldOfView", c_float),
		("NearPlane", c_float),
		("FarPlane", c_float),
		("bUpdateMatrices", c_bool, 1),
		("", c_ulong, 0),
		("Unknown1", c_ubyte, 0x),
		("ViewMatrix", FMatrix),
		("ProjMatrix", FMatrix),
	]

class  USceneCapture2DComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USceneCaptureComponent", USceneCaptureComponent_Data),
		("USceneCapture2DComponent", USceneCapture2DComponent_Data),
	]


class  USceneCapture2DHitMaskComponent_Data(Structure):
	_fields_ = [
		("TextureTarget", POINTER(UTextureRenderTarget2D)),
		("SkeletalMeshComp", POINTER(USkeletalMeshComponent)),
		("MaterialIndex", c_int),
		("ForceLOD", c_int),
		("HitMaskCullDistance", c_int),
		("FadingStartTimeSinceHit", c_float),
		("FadingPercentage", c_float),
		("FadingDurationTime", c_float),
		("FadingIntervalTime", c_float),
	]

class  USceneCapture2DHitMaskComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USceneCaptureComponent", USceneCaptureComponent_Data),
		("USceneCapture2DHitMaskComponent", USceneCapture2DHitMaskComponent_Data),
	]


class  USceneCaptureCubeMapComponent_Data(Structure):
	_fields_ = [
		("TextureTarget", POINTER(UTextureRenderTargetCube)),
		("NearPlane", c_float),
		("FarPlane", c_float),
		("WorldLocation", FVector),
	]

class  USceneCaptureCubeMapComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USceneCaptureComponent", USceneCaptureComponent_Data),
		("USceneCaptureCubeMapComponent", USceneCaptureCubeMapComponent_Data),
	]


class  USceneCapturePortalComponent_Data(Structure):
	_fields_ = [
		("TextureTarget", POINTER(UTextureRenderTarget2D)),
		("ScaleFOV", c_float),
		("ViewDestination", POINTER(AActor)),
	]

class  USceneCapturePortalComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USceneCaptureComponent", USceneCaptureComponent_Data),
		("USceneCapturePortalComponent", USceneCapturePortalComponent_Data),
	]


class  USceneCaptureReflectComponent_Data(Structure):
	_fields_ = [
		("TextureTarget", POINTER(UTextureRenderTarget2D)),
		("ScaleFOV", c_float),
	]

class  USceneCaptureReflectComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USceneCaptureComponent", USceneCaptureComponent_Data),
		("USceneCaptureReflectComponent", USceneCaptureReflectComponent_Data),
	]


class  UWindDirectionalSourceComponent_Data(Structure):
	_fields_ = [
		("SceneProxy", FPointer),
		("Strength", c_float),
		("Phase", c_float),
		("Frequency", c_float),
		("Speed", c_float),
	]

class  UWindDirectionalSourceComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UWindDirectionalSourceComponent", UWindDirectionalSourceComponent_Data),
	]


class  UWindPointSourceComponent_Data(Structure):
	_fields_ = [
		("PreviewRadiusComponent", POINTER(UDrawSphereComponent)),
		("Radius", c_float),
	]

class  UWindPointSourceComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UWindDirectionalSourceComponent", UWindDirectionalSourceComponent_Data),
		("UWindPointSourceComponent", UWindPointSourceComponent_Data),
	]


class  UActorFactory_Data(Structure):
	_fields_ = [
		("GameplayActorClass", POINTER(UClass)),
		("MenuName", FString),
		("MenuPriority", c_int),
		("AlternateMenuPriority", c_int),
		("NewActorClass", POINTER(UClass)),
		("bPlaceable", c_bool, 1),
		("bShowInEditorQuickMenu", c_bool, 1),
		("bUseCustomPropertyEditor", c_bool, 1),
		("", c_ulong, 0),
		("SpecificGameName", FString),
		("CustomPropertyEditorDelegateClassName", FString),
		("CustomPropertyEditorDelegateInstance", POINTER(UActorFactoryCustomPropertyEditorDelegate)),
		("CustomPropertyEditorDelegateTargetClass", POINTER(UClass)),
	]

class  UActorFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
	]


class  UActorFactoryActor_Data(Structure):
	_fields_ = [
		("ActorClass", POINTER(UClass)),
	]

class  UActorFactoryActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryActor", UActorFactoryActor_Data),
	]


class  UActorFactoryAI_Data(Structure):
	_fields_ = [
		("ControllerClass", POINTER(UClass)),
		("PawnClass", POINTER(UClass)),
		("PawnName", FString),
		("bGiveDefaultInventory", c_bool, 1),
		("", c_ulong, 0),
		("InventoryList", TArray_UClassPtr),
		("TeamIndex", c_int),
	]

class  UActorFactoryAI(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryAI", UActorFactoryAI_Data),
	]


class  UActorFactoryApexDestructible_Data(Structure):
	_fields_ = [
		("bStartAwake", c_bool, 1),
		("", c_ulong, 0),
		("RBChannel", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CollideWithChannels", FRBCollisionChannelContainer),
		("DestructibleAsset", POINTER(UApexDestructibleAsset)),
	]

class  UActorFactoryApexDestructible(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryApexDestructible", UActorFactoryApexDestructible_Data),
	]


class  UActorFactoryArchetype_Data(Structure):
	_fields_ = [
		("ArchetypeActor", POINTER(AActor)),
	]

class  UActorFactoryArchetype(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryArchetype", UActorFactoryArchetype_Data),
	]


class  UActorFactoryCoverLink_Data(Structure):
	_fields_ = []

class  UActorFactoryCoverLink(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryCoverLink", UActorFactoryCoverLink_Data),
	]


class  UActorFactoryDominantDirectionalLight_Data(Structure):
	_fields_ = []

class  UActorFactoryDominantDirectionalLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDominantDirectionalLight", UActorFactoryDominantDirectionalLight_Data),
	]


class  UActorFactoryDominantDirectionalLightMovable_Data(Structure):
	_fields_ = []

class  UActorFactoryDominantDirectionalLightMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDominantDirectionalLightMovable", UActorFactoryDominantDirectionalLightMovable_Data),
	]


class  UActorFactoryDynamicSM_Data(Structure):
	_fields_ = [
		("StaticMesh", POINTER(UStaticMesh)),
		("DrawScale3D", FVector),
		("bNoEncroachCheck", c_bool, 1),
		("bNotifyRigidBodyCollision", c_bool, 1),
		("bBlockRigidBody", c_bool, 1),
		("bUseCompartment", c_bool, 1),
		("bCastDynamicShadow", c_bool, 1),
		("", c_ulong, 0),
		("CollisionType", c_ubyte),
	]

class  UActorFactoryDynamicSM(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDynamicSM", UActorFactoryDynamicSM_Data),
	]


class  UActorFactoryMover_Data(Structure):
	_fields_ = []

class  UActorFactoryMover(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDynamicSM", UActorFactoryDynamicSM_Data),
		("UActorFactoryMover", UActorFactoryMover_Data),
	]


class  UActorFactoryRigidBody_Data(Structure):
	_fields_ = [
		("bStartAwake", c_bool, 1),
		("bDamageAppliesImpulse", c_bool, 1),
		("bLocalSpaceInitialVelocity", c_bool, 1),
		("bEnableStayUprightSpring", c_bool, 1),
		("", c_ulong, 0),
		("InitialVelocity", FVector),
		("AdditionalVelocity", POINTER(UDistributionVector)),
		("InitialAngularVelocity", POINTER(UDistributionVector)),
		("RBChannel", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("StayUprightTorqueFactor", c_float),
		("StayUprightMaxTorque", c_float),
	]

class  UActorFactoryRigidBody(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDynamicSM", UActorFactoryDynamicSM_Data),
		("UActorFactoryRigidBody", UActorFactoryRigidBody_Data),
	]


class  UActorFactoryEmitter_Data(Structure):
	_fields_ = [
		("ParticleSystem", POINTER(UParticleSystem)),
	]

class  UActorFactoryEmitter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryEmitter", UActorFactoryEmitter_Data),
	]


class  UActorFactoryLensFlare_Data(Structure):
	_fields_ = [
		("LensFlareObject", POINTER(ULensFlare)),
	]

class  UActorFactoryLensFlare(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryLensFlare", UActorFactoryLensFlare_Data),
	]


class  UActorFactoryLight_Data(Structure):
	_fields_ = []

class  UActorFactoryLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryLight", UActorFactoryLight_Data),
	]


class  UActorFactoryPathNode_Data(Structure):
	_fields_ = []

class  UActorFactoryPathNode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryPathNode", UActorFactoryPathNode_Data),
	]


class  UActorFactoryPhysicsAsset_Data(Structure):
	_fields_ = [
		("PhysicsAsset", POINTER(UPhysicsAsset)),
		("SkeletalMesh", POINTER(USkeletalMesh)),
		("bStartAwake", c_bool, 1),
		("bDamageAppliesImpulse", c_bool, 1),
		("bNotifyRigidBodyCollision", c_bool, 1),
		("bUseCompartment", c_bool, 1),
		("bCastDynamicShadow", c_bool, 1),
		("", c_ulong, 0),
		("InitialVelocity", FVector),
		("DrawScale3D", FVector),
	]

class  UActorFactoryPhysicsAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryPhysicsAsset", UActorFactoryPhysicsAsset_Data),
	]


class  UActorFactoryPlayerStart_Data(Structure):
	_fields_ = []

class  UActorFactoryPlayerStart(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryPlayerStart", UActorFactoryPlayerStart_Data),
	]


class  UActorFactoryPylon_Data(Structure):
	_fields_ = []

class  UActorFactoryPylon(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryPylon", UActorFactoryPylon_Data),
	]


class  UActorFactorySkeletalMesh_Data(Structure):
	_fields_ = [
		("SkeletalMesh", POINTER(USkeletalMesh)),
		("AnimSet", POINTER(UAnimSet)),
		("AnimSequenceName", FName),
	]

class  UActorFactorySkeletalMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactorySkeletalMesh", UActorFactorySkeletalMesh_Data),
	]


class  UActorFactoryStaticMesh_Data(Structure):
	_fields_ = [
		("StaticMesh", POINTER(UStaticMesh)),
		("DrawScale3D", FVector),
	]

class  UActorFactoryStaticMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryStaticMesh", UActorFactoryStaticMesh_Data),
	]


class  UActorFactoryTrigger_Data(Structure):
	_fields_ = []

class  UActorFactoryTrigger(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryTrigger", UActorFactoryTrigger_Data),
	]


class  UActorFactoryVehicle_Data(Structure):
	_fields_ = [
		("VehicleClass", POINTER(UClass)),
	]

class  UActorFactoryVehicle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryVehicle", UActorFactoryVehicle_Data),
	]


class  UActorFactoryCustomPropertyEditorDelegate_Data(Structure):
	_fields_ = []

class  UActorFactoryCustomPropertyEditorDelegate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactoryCustomPropertyEditorDelegate", UActorFactoryCustomPropertyEditorDelegate_Data),
	]


class  UAkAudioDevice_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UAkAudioDevice(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USubsystem", USubsystem_Data),
		("UAkAudioDevice", UAkAudioDevice_Data),
	]


class  UAkBaseSoundObject_Data(Structure):
	_fields_ = []

class  UAkBaseSoundObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkBaseSoundObject", UAkBaseSoundObject_Data),
	]


class  USoundCue_Data(Structure):
	_fields_ = [
		("SoundClass", FName),
		("SoundClassName", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("FirstNode", POINTER(USoundNode)),
		("Unknown2", c_ubyte, 0x),
		("MaxAudibleDistance", c_float),
		("VolumeMultiplier", c_float),
		("PitchMultiplier", c_float),
		("Duration", c_float),
		("DesignerComment", FString),
		("FaceFXAnimSetRef", POINTER(UFaceFXAnimSet)),
		("FaceFXGroupName", FString),
		("FaceFXAnimName", FString),
		("MaxConcurrentPlayCount", c_int),
		("CurrentPlayCount", c_int),
		("SoundGroup", FName),
		("Priority", c_int),
		("SpatializationPercent", c_int),
	]

class  USoundCue(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkBaseSoundObject", UAkBaseSoundObject_Data),
		("USoundCue", USoundCue_Data),
	]


class  UAkObject_Data(Structure):
	_fields_ = [
		("ShortId", c_int),
	]

class  UAkObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
	]


class  UAkBank_Data(Structure):
	_fields_ = [
		("AutoLoad", c_bool, 1),
		("GenerateDefinition", c_bool, 1),
		("", c_ulong, 0),
		("NumAsyncLoaders", c_int),
	]

class  UAkBank(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkBank", UAkBank_Data),
	]


class  UAkDialogueEvent_Data(Structure):
	_fields_ = [
		("RequiredBank", POINTER(UAkBank)),
		("Arguments", TArray_FDialogueArgument),
		("FaceFXAnimSet", POINTER(UFaceFXAnimSet)),
	]

class  UAkDialogueEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkDialogueEvent", UAkDialogueEvent_Data),
	]


class  UAkEffect_Data(Structure):
	_fields_ = [
		("EffectName", FString),
		("bCanBeEnvironmental", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAkEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkEffect", UAkEffect_Data),
	]


class  UAkEvent_Data(Structure):
	_fields_ = [
		("RequiredBank", POINTER(UAkBank)),
		("FaceFXAnimSet", POINTER(UFaceFXAnimSet)),
		("EnvironmentalEffectUpdateFrequency", c_float),
		("bCanBeOccluded", c_bool, 1),
		("bForceImmediateEnvOccRecalc", c_bool, 1),
		("bVoice", c_bool, 1),
		("bInCookedMap", c_bool, 1),
		("bInOnDemandPackage", c_bool, 1),
		("bIsSimpleEvent", c_bool, 1),
		("bReliable", c_bool, 1),
		("bWantDistanceRTPC", c_bool, 1),
		("bWantSpeedRTPC", c_bool, 1),
		("bWantApproachSpeedRTPC", c_bool, 1),
		("", c_ulong, 0),
		("MaxAttenuationRadius", c_float),
	]

class  UAkEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkEvent", UAkEvent_Data),
	]


class  UAkRtpc_Data(Structure):
	_fields_ = [
		("MinRange", c_float),
		("MaxRange", c_float),
	]

class  UAkRtpc(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkRtpc", UAkRtpc_Data),
	]


class  UAkState_Data(Structure):
	_fields_ = [
		("StateGroup", POINTER(UAkStateGroup)),
		("bIsGroupNone", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAkState(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkState", UAkState_Data),
	]


class  UAkStateGroup_Data(Structure):
	_fields_ = []

class  UAkStateGroup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkStateGroup", UAkStateGroup_Data),
	]


class  UAkSwitch_Data(Structure):
	_fields_ = [
		("SwitchGroup", POINTER(UAkSwitchGroup)),
	]

class  UAkSwitch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkSwitch", UAkSwitch_Data),
	]


class  UAkSwitchGroup_Data(Structure):
	_fields_ = []

class  UAkSwitchGroup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkSwitchGroup", UAkSwitchGroup_Data),
	]


class  UAkTrigger_Data(Structure):
	_fields_ = []

class  UAkTrigger(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAkObject", UAkObject_Data),
		("UAkTrigger", UAkTrigger_Data),
	]


class  UBookMark_Data(Structure):
	_fields_ = [
		("Location", FVector),
		("Rotation", FRotator),
		("HiddenLevels", TArray_FString),
	]

class  UBookMark(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBookMark", UBookMark_Data),
	]


class  UBookMark2D_Data(Structure):
	_fields_ = [
		("Zoom2D", c_float),
		("Location", FIntPoint),
	]

class  UBookMark2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBookMark2D", UBookMark2D_Data),
	]


class  UKismetBookMark_Data(Structure):
	_fields_ = [
		("BookMarkSequencePathName", FString),
	]

class  UKismetBookMark(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBookMark2D", UBookMark2D_Data),
		("UKismetBookMark", UKismetBookMark_Data),
	]


class  UCanvas_Data(Structure):
	_fields_ = [
		("Font", POINTER(UFont)),
		("OrgX", c_float),
		("OrgY", c_float),
		("ClipX", c_float),
		("ClipY", c_float),
		("CurX", c_float),
		("CurY", c_float),
		("CurZ", c_float),
		("CurYL", c_float),
		("DrawColor", FColor),
		("bCenter", c_bool, 1),
		("bNoSmooth", c_bool, 1),
		("", c_ulong, 0),
		("SizeX", c_int),
		("SizeY", c_int),
		("Canvas", FPointer),
		("SceneView", FPointer),
		("Unknown1", c_ubyte, 0x),
		("ColorModulate", FPlane),
		("DefaultTexture", POINTER(UTexture2D)),
		("BGColor", FColor),
	]

class  UCanvas(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCanvas", UCanvas_Data),
	]


class  UChannel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UChannel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UChannel", UChannel_Data),
	]


class  UActorChannel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UActorChannel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UChannel", UChannel_Data),
		("UActorChannel", UActorChannel_Data),
	]


class  UControlChannel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UControlChannel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UChannel", UChannel_Data),
		("UControlChannel", UControlChannel_Data),
	]


class  UFileChannel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UFileChannel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UChannel", UChannel_Data),
		("UFileChannel", UFileChannel_Data),
	]


class  UVoiceChannel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UVoiceChannel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UChannel", UChannel_Data),
		("UVoiceChannel", UVoiceChannel_Data),
	]


class  AController_Data(Structure):
	_fields_ = [
		("VfTable_IIResourcePoolProvider", FPointer),
		("VfTable_IInterface_NavigationHandle", FPointer),
		("Pawn", POINTER(APawn)),
		("PlayerReplicationInfo", POINTER(APlayerReplicationInfo)),
		("PlayerNum", c_int),
		("NextController", POINTER(AController)),
		("bIsPlayer", c_bool, 1),
		("bIsHumanPlayer", c_bool, 1),
		("bShowControllerInfo", c_bool, 1),
		("bGodMode", c_bool, 1),
		("bNonCheatGodMode", c_bool, 1),
		("bDontTargetMode", c_bool, 1),
		("bSoaking", c_bool, 1),
		("bSlowerZAcquire", c_bool, 1),
		("bNotifyPostLanded", c_bool, 1),
		("bNotifyApex", c_bool, 1),
		("bOverrideSearchStart", c_bool, 1),
		("bAdvancedTactics", c_bool, 1),
		("bCanDoSpecial", c_bool, 1),
		("bAdjusting", c_bool, 1),
		("bPreparingMove", c_bool, 1),
		("bForceStrafe", c_bool, 1),
		("bPauseNavigationUpdate", c_bool, 1),
		("bLOSflag", c_bool, 1),
		("bSkipExtraLOSChecks", c_bool, 1),
		("bNotifyFallingHitWall", c_bool, 1),
		("bEarlyOutOfSighTestsForSameType", c_bool, 1),
		("bPreciseDestination", c_bool, 1),
		("bSeeFriendly", c_bool, 1),
		("bUsingPathLanes", c_bool, 1),
		("", c_ulong, 0),
		("PrevRotation", FRotator),
		("bFire", c_ubyte),
		("bAltFire", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MinHitWall", c_float),
		("NavigationHandleClass", POINTER(UClass)),
		("NavigationHandle", POINTER(UNavigationHandle)),
		("OverrideSearchStart", FVector),
		("MoveTimer", c_float),
		("MoveTarget", POINTER(AActor)),
		("DestinationPosition", FBasedPosition),
		("FocalPosition", FBasedPosition),
		("Focus", POINTER(AActor)),
		("GoalList", POINTER(AActor) * 4),
		("AdjustPosition", FBasedPosition),
		("StartSpot", POINTER(AActor)),
		("RouteCache", TArray_ANavigationPointPtr),
		("CurrentPath", POINTER(UReachSpec)),
		("NextRoutePath", POINTER(UReachSpec)),
		("CurrentPathDir", FVector),
		("RouteGoal", POINTER(AActor)),
		("RouteDist", c_float),
		("LastRouteFind", c_float),
		("PendingMover", POINTER(AInterpActor)),
		("FailedMoveTarget", POINTER(AActor)),
		("MoveFailureCount", c_int),
		("GroundPitchTime", c_float),
		("ViewX", FVector),
		("ViewY", FVector),
		("ViewZ", FVector),
		("ShotTarget", POINTER(APawn)),
		("LastFailedReach", POINTER(AActor)),
		("FailedReachTime", c_float),
		("FailedReachLocation", FVector),
		("SightCounter", c_float),
		("SightCounterInterval", c_float),
		("InUseNodeCostMultiplier", c_float),
		("HighJumpNodeCostModifier", c_int),
		("MaxMoveTowardPawnTargetTime", c_float),
		("Enemy", POINTER(APawn)),
		("VisiblePortals", TArray_FVisiblePortalInfo),
		("LaneOffset", c_float),
		("OldBasedRotation", FRotator),
		("NavMeshPath_SearchExtent_Modifier", FVector),
		("ResourcePoolManager", POINTER(AResourcePoolManager)),
		("AccuracyPool", FResourcePoolReference),
		("OffHandAccuracyPool", FResourcePoolReference),
		("CharacterClass", POINTER(UCharacterClassDefinition)),
		("InstigatedBulletDamageModifier", c_float),
		("InstigatedBulletDamageModifierBaseValue", c_float),
		("InstigatedBulletDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedMeleeDamageModifier", c_float),
		("InstigatedMeleeDamageModifierBaseValue", c_float),
		("InstigatedMeleeDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedGrenadeDamageModifier", c_float),
		("InstigatedGrenadeDamageModifierBaseValue", c_float),
		("InstigatedGrenadeDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedRocketDamageModifier", c_float),
		("InstigatedRocketDamageModifierBaseValue", c_float),
		("InstigatedRocketDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedStatusEffectDamageModifier", c_float),
		("InstigatedStatusEffectDamageModifierBaseValue", c_float),
		("InstigatedStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedSkillDamageModifier", c_float),
		("InstigatedSkillDamageModifierBaseValue", c_float),
		("InstigatedSkillDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedStatusEffectStatusChanceModifier", c_float),
		("InstigatedStatusEffectStatusChanceModifierBaseValue", c_float),
		("InstigatedStatusEffectStatusChanceModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedIncendiaryStatusChanceModifier", c_float),
		("InstigatedIncendiaryStatusChanceModifierBaseValue", c_float),
		("InstigatedIncendiaryStatusChanceModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedShockStatusChanceModifier", c_float),
		("InstigatedShockStatusChanceModifierBaseValue", c_float),
		("InstigatedShockStatusChanceModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedCorrosiveStatusChanceModifier", c_float),
		("InstigatedCorrosiveStatusChanceModifierBaseValue", c_float),
		("InstigatedCorrosiveStatusChanceModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedAmpStatusChanceModifier", c_float),
		("InstigatedAmpStatusChanceModifierBaseValue", c_float),
		("InstigatedAmpStatusChanceModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedStatusEffectStatusDamageModifier", c_float),
		("InstigatedStatusEffectStatusDamageModifierBaseValue", c_float),
		("InstigatedStatusEffectStatusDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedIncendiaryStatusDamageModifier", c_float),
		("InstigatedIncendiaryStatusDamageModifierBaseValue", c_float),
		("InstigatedIncendiaryStatusDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedShockStatusDamageModifier", c_float),
		("InstigatedShockStatusDamageModifierBaseValue", c_float),
		("InstigatedShockStatusDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedCorrosiveStatusDamageModifier", c_float),
		("InstigatedCorrosiveStatusDamageModifierBaseValue", c_float),
		("InstigatedCorrosiveStatusDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedAmpStatusDamageModifier", c_float),
		("InstigatedAmpStatusDamageModifierBaseValue", c_float),
		("InstigatedAmpStatusDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedBulletDamageModifier", c_float),
		("ReceivedBulletDamageModifierBaseValue", c_float),
		("ReceivedBulletDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedAmplifyDamageModifier", c_float),
		("ReceivedAmplifyDamageModifierBaseValue", c_float),
		("ReceivedAmplifyDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedMeleeDamageModifier", c_float),
		("ReceivedMeleeDamageModifierBaseValue", c_float),
		("ReceivedMeleeDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedGrenadeDamageModifier", c_float),
		("ReceivedGrenadeDamageModifierBaseValue", c_float),
		("ReceivedGrenadeDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedRocketDamageModifier", c_float),
		("ReceivedRocketDamageModifierBaseValue", c_float),
		("ReceivedRocketDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedStatusEffectDamageModifier", c_float),
		("ReceivedStatusEffectDamageModifierBaseValue", c_float),
		("ReceivedStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedSkillDamageModifier", c_float),
		("ReceivedSkillDamageModifierBaseValue", c_float),
		("ReceivedSkillDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedIncindiaryDamageModifier", c_float),
		("InstigatedIncindiaryDamageModifierBaseValue", c_float),
		("InstigatedIncindiaryDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedShockDamageModifier", c_float),
		("InstigatedShockDamageModifierBaseValue", c_float),
		("InstigatedShockDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedExplosiveDamageModifier", c_float),
		("InstigatedExplosiveDamageModifierBaseValue", c_float),
		("InstigatedExplosiveDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedCorrosiveDamageModifier", c_float),
		("InstigatedCorrosiveDamageModifierBaseValue", c_float),
		("InstigatedCorrosiveDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedImpactDamageModifier", c_float),
		("InstigatedImpactDamageModifierBaseValue", c_float),
		("InstigatedImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedAmpDamageModifier", c_float),
		("InstigatedAmpDamageModifierBaseValue", c_float),
		("InstigatedAmpDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedBulletDamageAmmoTheftAmount", c_int),
		("InstigatedBulletDamageAmmoTheftAmountBaseValue", c_int),
		("InstigatedBulletDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedMeleeDamageAmmoTheftAmount", c_int),
		("InstigatedMeleeDamageAmmoTheftAmountBaseValue", c_int),
		("InstigatedMeleeDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedGrenadeDamageAmmoTheftAmount", c_int),
		("InstigatedGrenadeDamageAmmoTheftAmountBaseValue", c_int),
		("InstigatedGrenadeDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedRocketDamageAmmoTheftAmount", c_int),
		("InstigatedRocketDamageAmmoTheftAmountBaseValue", c_int),
		("InstigatedRocketDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("InstigatedStatusEffectDamageAmmoTheftAmount", c_int),
		("InstigatedStatusEffectDamageAmmoTheftAmountBaseValue", c_int),
		("InstigatedStatusEffectDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedBulletDamageAmmoTheftAmount", c_int),
		("ReceivedBulletDamageAmmoTheftAmountBaseValue", c_int),
		("ReceivedBulletDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedMeleeDamageAmmoTheftAmount", c_int),
		("ReceivedMeleeDamageAmmoTheftAmountBaseValue", c_int),
		("ReceivedMeleeDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedGrenadeDamageAmmoTheftAmount", c_int),
		("ReceivedGrenadeDamageAmmoTheftAmountBaseValue", c_int),
		("ReceivedGrenadeDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedRocketDamageAmmoTheftAmount", c_int),
		("ReceivedRocketDamageAmmoTheftAmountBaseValue", c_int),
		("ReceivedRocketDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
		("ReceivedStatusEffectDamageAmmoTheftAmount", c_int),
		("ReceivedStatusEffectDamageAmmoTheftAmountBaseValue", c_int),
		("ReceivedStatusEffectDamageAmmoTheftAmountModifierStack", TArray_UAttributeModifierPtr),
	]

class  AController(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AController", AController_Data),
	]


class  APlayerController_Data(Structure):
	_fields_ = [
		("Player", POINTER(UPlayer)),
		("PlayerCamera", POINTER(ACamera)),
		("CameraClass", POINTER(UClass)),
		("bFrozen", c_bool, 1),
		("bPressedJump", c_bool, 1),
		("bDoubleJump", c_bool, 1),
		("bUpdatePosition", c_bool, 1),
		("bUpdating", c_bool, 1),
		("bNeverSwitchOnPickup", c_bool, 1),
		("bCheatFlying", c_bool, 1),
		("bCameraPositionLocked", c_bool, 1),
		("bShortConnectTimeOut", c_bool, 1),
		("bPendingDestroy", c_bool, 1),
		("bWasSpeedHack", c_bool, 1),
		("bWasSaturated", c_bool, 1),
		("bAimingHelp", c_bool, 1),
		("bCameraCut", c_bool, 1),
		("bClientSimulatingViewTarget", c_bool, 1),
		("bForegroundFOV", c_bool, 1),
		("bHasVoiceHandshakeCompleted", c_bool, 1),
		("bCinematicMode", c_bool, 1),
		("bCinematicSplitScreen", c_bool, 1),
		("bKismetEnabledCinematicMode", c_bool, 1),
		("bInteractiveMode", c_bool, 1),
		("bCinemaDisableInputMove", c_bool, 1),
		("bCinemaDisableInputLook", c_bool, 1),
		("bCinemaDisableInputButton", c_bool, 1),
		("bCinematicModeHidePlayer", c_bool, 1),
		("bIgnoreNetworkMessages", c_bool, 1),
		("bReplicateAllPawns", c_bool, 1),
		("bIsUsingStreamingVolumes", c_bool, 1),
		("bIsExternalUIOpen", c_bool, 1),
		("bIsControllerConnected", c_bool, 1),
		("bCheckSoundOcclusion", c_bool, 1),
		("bDebugCameraAnims", c_bool, 1),
		("bFreeCamera", c_bool, 1),
		("bBlockCameraAnimsFromOverridingPostProcess", c_bool, 1),
		("bLogHearSoundOverflow", c_bool, 1),
		("bCheckRelevancyThroughPortals", c_bool, 1),
		("bDebugClientAdjustPosition", c_bool, 1),
		("bIsInHolding", c_bool, 1),
		("bOverrideOnlineProfileName", c_bool, 1),
		("bEnableAnalogMovement", c_bool, 1),
		("bStatusMenuOpen", c_bool, 1),
		("bUsingVendingMachine", c_bool, 1),
		("bUsingVehicleSpawnStation", c_bool, 1),
		("bUsingFastTravelStation", c_bool, 1),
		("bWantsCensoredContent", c_bool, 1),
		("", c_ulong, 0),
		("MaxResponseTime", c_float),
		("WaitDelay", c_float),
		("AcknowledgedPawn", POINTER(APawn)),
		("DoubleClickDir", c_ubyte),
		("LastAckedAnalogPct", c_ubyte),
		("bIgnoreMoveInput", c_ubyte),
		("bIgnoreLookInput", c_ubyte),
		("bIgnoreButtonInput", c_ubyte),
		("bRun", c_ubyte),
		("bDuck", c_ubyte),
		("NetPlayerIndex", c_ubyte),
		("ViewTarget", POINTER(AActor)),
		("RealViewTarget", POINTER(APlayerReplicationInfo)),
		("ControllingDirTrackInst", POINTER(UInterpTrackInstDirector)),
		("FOVAngle", c_float),
		("DesiredFOV", c_float),
		("DesiredFOVBaseValue", c_float),
		("DesiredFOVModifierStack", TArray_UAttributeModifierPtr),
		("DefaultFOV", c_float),
		("LODDistanceFactor", c_float),
		("ForegroundFOV", c_float),
		("TargetViewRotation", FRotator),
		("TargetEyeHeight", c_float),
		("BlendedTargetViewRotation", FRotator),
		("myHUD", POINTER(AHUD)),
		("SavedMoveClass", POINTER(UClass)),
		("SavedMoves", POINTER(USavedMove)),
		("FreeMoves", POINTER(USavedMove)),
		("PendingMove", POINTER(USavedMove)),
		("LastAckedAccel", FVector),
		("CurrentTimeStamp", c_float),
		("LastUpdateTime", c_float),
		("ServerTimeStamp", c_float),
		("TimeMargin", c_float),
		("ClientUpdateTime", c_float),
		("MaxTimeMargin", c_float),
		("LastActiveTime", c_float),
		("ClientCap", c_int),
		("DynamicPingThreshold", c_float),
		("LastPingUpdate", c_float),
		("LastSpeedHackLog", c_float),
		("PendingAdjustment", FClientAdjustment),
		("GroundPitch", c_int),
		("CheatManager", POINTER(UCheatManager)),
		("CheatClass", POINTER(UClass)),
		("PlayerInput", POINTER(UPlayerInput)),
		("InputClass", POINTER(UClass)),
		("FailedPathStart", FVector),
		("CylinderComponent", POINTER(UCylinderComponent)),
		("ForceFeedbackManagerClassName", FString),
		("ForceFeedbackManager", POINTER(UForceFeedbackManager)),
		("CurrentWaveform", POINTER(UForceFeedbackWaveform)),
		("Interactions", TArray_UInteractionPtr),
		("VoiceMuteList", TArray_FUniqueNetId),
		("GameplayVoiceMuteList", TArray_FUniqueNetId),
		("VoicePacketFilter", TArray_FUniqueNetId),
		("ConnectedPeers", TArray_FConnectedPeerInfo),
		("BestNextHostPeers", TArray_FUniqueNetId),
		("MigratedSearchToJoin", POINTER(UOnlineGameSearch)),
		("OnlineSub", POINTER(UOnlineSubsystem)),
		("VoiceInterface", FScriptInterface),
		("OnlinePlayerData", POINTER(UUIDataStore_OnlinePlayerData)),
		("StringAliasMap", POINTER(UUIDataStore_StringAliasMap)),
		("InteractDistance", c_float),
		("DelayedJoinSessionName", FName),
		("LastPresenceStatusUpdateString", FString),
		("LastLocationStatusUpdateString", FString),
		("InputRequests", TArray_FInputMatchRequest),
		("LastBroadcastTime", c_float),
		("LastBroadcastString", FString * 4),
		("PendingMapChangeLevelNames", TArray_FName),
		("MyCoverReplicator", POINTER(ACoverReplicator)),
		("DebugTextList", TArray_FDebugTextInfo),
		("SpectatorCameraSpeed", c_float),
		("PendingSwapConnection", POINTER(UNetConnection)),
		("MinRespawnDelay", c_float),
		("MaxConcurrentHearSounds", c_int),
		("HearSoundActiveComponents", TArray_UAudioComponentPtr),
		("HearSoundPoolComponents", TArray_UAudioComponentPtr),
		("LastSpectatorStateSynchTime", c_float),
		("HoldingDest", FVector),
		("HoldingRotation", FRotator),
		("HoldingDestActor", POINTER(AActor)),
		("LoadingMovieLoadedLevelNames", TArray_FName),
		("__OnMissingPeersUnregistered__Delegate", FScriptDelegate),
		("__CanUnpause__Delegate", FScriptDelegate),
		("__InputMatchDelegate__Delegate", FScriptDelegate),
	]

class  APlayerController(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AController", AController_Data),
		("APlayerController", APlayerController_Data),
	]


class  UCheatManager_Data(Structure):
	_fields_ = [
		("DebugCameraControllerRef", POINTER(ADebugCameraController)),
		("DebugCameraControllerClass", POINTER(UClass)),
		("ViewingFrom", FString),
		("OwnCamera", FString),
	]

class  UCheatManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCheatManager", UCheatManager_Data),
	]


class  UClient_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("MinDesiredFrameRate", c_float),
		("DisplayGamma", c_float),
		("InitialButtonRepeatDelay", c_float),
		("ButtonRepeatDelay", c_float),
	]

class  UClient(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UClient", UClient_Data),
	]


class  UClipPadEntry_Data(Structure):
	_fields_ = [
		("Title", FString),
		("Text", FString),
	]

class  UClipPadEntry(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UClipPadEntry", UClipPadEntry_Data),
	]


class  UCodecMovie_Data(Structure):
	_fields_ = [
		("PlaybackDuration", c_float),
	]

class  UCodecMovie(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCodecMovie", UCodecMovie_Data),
	]


class  UCodecMovieBink_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UCodecMovieBink(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCodecMovie", UCodecMovie_Data),
		("UCodecMovieBink", UCodecMovieBink_Data),
	]


class  UCodecMovieFallback_Data(Structure):
	_fields_ = [
		("CurrentTime", c_float),
	]

class  UCodecMovieFallback(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCodecMovie", UCodecMovie_Data),
		("UCodecMovieFallback", UCodecMovieFallback_Data),
	]


class  UCurveEdPresetCurve_Data(Structure):
	_fields_ = [
		("CurveName", FString),
		("Points", TArray_FPresetGeneratedPoint),
	]

class  UCurveEdPresetCurve(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCurveEdPresetCurve", UCurveEdPresetCurve_Data),
	]


class  UCustomPropertyItemHandler_Data(Structure):
	_fields_ = []

class  UCustomPropertyItemHandler(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UCustomPropertyItemHandler", UCustomPropertyItemHandler_Data),
	]


class  UDamageAdjuster_Data(Structure):
	_fields_ = []

class  UDamageAdjuster(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageAdjuster", UDamageAdjuster_Data),
	]


class  UDamagePipeline_Data(Structure):
	_fields_ = [
		("bInUse", c_bool, 1),
		("bCanHitFriendly", c_bool, 1),
		("bOvercharged", c_bool, 1),
		("", c_ulong, 0),
		("DamageTypeDef", POINTER(UDamageTypeDefinition)),
		("ImpactDefinition", POINTER(UImpactDefinition)),
		("DirectHitObject", POINTER(UObject)),
		("PenetrationCount", c_int),
		("DamageSummary", FDamageEventSummary),
		("BarrelSourceTime", c_float),
		("PlantSourceTime", c_float),
	]

class  UDamagePipeline(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamagePipeline", UDamagePipeline_Data),
	]


class  UDamageType_Data(Structure):
	_fields_ = [
		("bArmorStops", c_bool, 1),
		("bCausedByWorld", c_bool, 1),
		("bExtraMomentumZ", c_bool, 1),
		("bCausesFracture", c_bool, 1),
		("bRadialDamageVelChange", c_bool, 1),
		("", c_ulong, 0),
		("KDamageImpulse", c_float),
		("KDeathVel", c_float),
		("KDeathUpKick", c_float),
		("RadialDamageImpulse", c_float),
		("VehicleDamageScaling", c_float),
		("VehicleMomentumScaling", c_float),
		("DamagedFFWaveform", POINTER(UForceFeedbackWaveform)),
		("KilledFFWaveform", POINTER(UForceFeedbackWaveform)),
		("FracturedMeshDamage", c_float),
	]

class  UDamageType(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageType", UDamageType_Data),
	]


class  UKillZDamageType_Data(Structure):
	_fields_ = []

class  UKillZDamageType(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageType", UDamageType_Data),
		("UKillZDamageType", UKillZDamageType_Data),
	]


class  UDistributionFloatConstant_Data(Structure):
	_fields_ = [
		("Constant", c_float),
	]

class  UDistributionFloatConstant(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatConstant", UDistributionFloatConstant_Data),
	]


class  UDistributionFloatParameterBase_Data(Structure):
	_fields_ = [
		("ParameterName", FName),
		("MinInput", c_float),
		("MaxInput", c_float),
		("MinOutput", c_float),
		("MaxOutput", c_float),
		("ParamMode", c_ubyte),
	]

class  UDistributionFloatParameterBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatConstant", UDistributionFloatConstant_Data),
		("UDistributionFloatParameterBase", UDistributionFloatParameterBase_Data),
	]


class  UDistributionFloatConstantCurve_Data(Structure):
	_fields_ = [
		("ConstantCurve", FInterpCurveFloat),
	]

class  UDistributionFloatConstantCurve(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatConstantCurve", UDistributionFloatConstantCurve_Data),
	]


class  UDistributionFloatUniform_Data(Structure):
	_fields_ = [
		("Min", c_float),
		("Max", c_float),
	]

class  UDistributionFloatUniform(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatUniform", UDistributionFloatUniform_Data),
	]


class  UDistributionFloatUniformCurve_Data(Structure):
	_fields_ = [
		("ConstantCurve", FInterpCurveVector2D),
	]

class  UDistributionFloatUniformCurve(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatUniformCurve", UDistributionFloatUniformCurve_Data),
	]


class  UDistributionVectorConstant_Data(Structure):
	_fields_ = [
		("Constant", FVector),
		("bLockAxes", c_bool, 1),
		("", c_ulong, 0),
		("LockedAxes", c_ubyte),
	]

class  UDistributionVectorConstant(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionVector", UDistributionVector_Data),
		("UDistributionVectorConstant", UDistributionVectorConstant_Data),
	]


class  UDistributionVectorParameterBase_Data(Structure):
	_fields_ = [
		("ParameterName", FName),
		("MinInput", FVector),
		("MaxInput", FVector),
		("MinOutput", FVector),
		("MaxOutput", FVector),
		("ParamModes", c_ubyte * 3),
	]

class  UDistributionVectorParameterBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionVector", UDistributionVector_Data),
		("UDistributionVectorConstant", UDistributionVectorConstant_Data),
		("UDistributionVectorParameterBase", UDistributionVectorParameterBase_Data),
	]


class  UDistributionVectorConstantCurve_Data(Structure):
	_fields_ = [
		("ConstantCurve", FInterpCurveVector),
		("bLockAxes", c_bool, 1),
		("", c_ulong, 0),
		("LockedAxes", c_ubyte),
	]

class  UDistributionVectorConstantCurve(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionVector", UDistributionVector_Data),
		("UDistributionVectorConstantCurve", UDistributionVectorConstantCurve_Data),
	]


class  UDistributionVectorUniform_Data(Structure):
	_fields_ = [
		("Max", FVector),
		("Min", FVector),
		("bLockAxes", c_bool, 1),
		("bUseExtremes", c_bool, 1),
		("", c_ulong, 0),
		("LockedAxes", c_ubyte),
		("MirrorFlags", c_ubyte * 3),
	]

class  UDistributionVectorUniform(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionVector", UDistributionVector_Data),
		("UDistributionVectorUniform", UDistributionVectorUniform_Data),
	]


class  UDistributionVectorUniformCurve_Data(Structure):
	_fields_ = [
		("ConstantCurve", FInterpCurveTwoVectors),
		("bLockAxes1", c_bool, 1),
		("bLockAxes2", c_bool, 1),
		("bUseExtremes", c_bool, 1),
		("", c_ulong, 0),
		("LockedAxes", c_ubyte * 2),
		("MirrorFlags", c_ubyte * 3),
	]

class  UDistributionVectorUniformCurve(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionVector", UDistributionVector_Data),
		("UDistributionVectorUniformCurve", UDistributionVectorUniformCurve_Data),
	]


class  UDownload_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UDownload(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDownload", UDownload_Data),
	]


class  UChannelDownload_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UChannelDownload(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDownload", UDownload_Data),
		("UChannelDownload", UChannelDownload_Data),
	]


class  UEdCoordSystem_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("M", FMatrix),
		("Desc", FString),
	]

class  UEdCoordSystem(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UEdCoordSystem", UEdCoordSystem_Data),
	]


class  UEditorLinkSelectionInterface_Data(Structure):
	_fields_ = []

class  UEditorLinkSelectionInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UEditorLinkSelectionInterface", UEditorLinkSelectionInterface_Data),
	]


class  UEngineTypes_Data(Structure):
	_fields_ = []

class  UEngineTypes(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UEngineTypes", UEngineTypes_Data),
	]


class  UFacebookIntegration_Data(Structure):
	_fields_ = [
		("AppID", FString),
		("UserName", FString),
		("UserId", FString),
		("AccessToken", FString),
		("AuthorizationDelegates", TArray_FScriptDelegate),
		("FacebookRequestCompleteDelegates", TArray_FScriptDelegate),
		("WebRequestCompleteDelegates", TArray_FScriptDelegate),
		("__OnAuthorizationComplete__Delegate", FScriptDelegate),
		("__OnFacebookRequestComplete__Delegate", FScriptDelegate),
		("__OnWebRequestComplete__Delegate", FScriptDelegate),
	]

class  UFacebookIntegration(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFacebookIntegration", UFacebookIntegration_Data),
	]


class  UFaceFXAnimSet_Data(Structure):
	_fields_ = [
		("bStreamWithAudio", c_bool, 1),
		("", c_ulong, 0),
		("InternalFaceFXAnimSet", FPointer),
		("RawFaceFXAnimSetBytes", TArray_unsigned_char),
		("RawFaceFXMiniSessionBytes", TArray_unsigned_char),
		("NumLoadErrors", c_int),
	]

class  UFaceFXAnimSet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFaceFXAnimSet", UFaceFXAnimSet_Data),
	]


class  UFaceFXAsset_Data(Structure):
	_fields_ = [
		("FaceFXActor", FPointer),
		("RawFaceFXActorBytes", TArray_unsigned_char),
		("RawFaceFXSessionBytes", TArray_unsigned_char),
		("MountedFaceFXAnimSets", TArray_UFaceFXAnimSetPtr),
		("NumLoadErrors", c_int),
		("SoundNodeWaveToGroupAndAnimNameArray", TArray_FGroupAnimationAndSoundIdentifier),
	]

class  UFaceFXAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFaceFXAsset", UFaceFXAsset_Data),
	]


class  UFont_Data(Structure):
	_fields_ = [
		("Characters", TArray_FFontCharacter),
		("Textures", TArray_UTexture2DPtr),
		("Unknown1", c_ubyte, 0x),
		("IsRemapped", c_int),
		("EmScale", c_float),
		("Ascent", c_float),
		("Descent", c_float),
		("Leading", c_float),
		("Kerning", c_int),
		("ImportOptions", FFontImportOptionsData),
		("NumCharacters", c_int),
		("MaxCharHeight", TArray_int),
		("ScalingFactor", c_float),
	]

class  UFont(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFont", UFont_Data),
	]


class  UMultiFont_Data(Structure):
	_fields_ = [
		("ResolutionTestTable", TArray_float),
	]

class  UMultiFont(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFont", UFont_Data),
		("UMultiFont", UMultiFont_Data),
	]


class  UFontImportOptions_Data(Structure):
	_fields_ = [
		("Data", FFontImportOptionsData),
	]

class  UFontImportOptions(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFontImportOptions", UFontImportOptions_Data),
	]


class  UForceFeedbackManager_Data(Structure):
	_fields_ = [
		("bAllowsForceFeedback", c_bool, 1),
		("bIsPaused", c_bool, 1),
		("", c_ulong, 0),
		("FFWaveform", POINTER(UForceFeedbackWaveform)),
		("CurrentSample", c_int),
		("ElapsedTime", c_float),
		("ScaleAllWaveformsBy", c_float),
		("WaveformInstigator", POINTER(AActor)),
		("CurrentWaveformRef", c_int),
	]

class  UForceFeedbackManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UForceFeedbackManager", UForceFeedbackManager_Data),
	]


class  UForceFeedbackWaveform_Data(Structure):
	_fields_ = [
		("bIsLooping", c_bool, 1),
		("", c_ulong, 0),
		("Samples", TArray_FWaveformSample),
		("Scale", c_float),
		("WaveformFalloffStartDistance", c_float),
		("MaxWaveformDistance", c_float),
		("WaveformRef", c_int),
	]

class  UForceFeedbackWaveform(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UForceFeedbackWaveform", UForceFeedbackWaveform_Data),
	]


class  UGameplayEvents_Data(Structure):
	_fields_ = [
		("Archive", FPointer),
		("StatsFileName", FString),
		("Header", FGameplayEventsHeader),
		("CurrentSessionInfo", FGameSessionInformation),
		("PlayerList", TArray_FPlayerInformation),
		("TeamList", TArray_FTeamInformation),
		("SupportedEvents", TArray_FGameplayEventMetaData),
		("WeaponClassArray", TArray_FWeaponClassEventData),
		("DamageClassArray", TArray_FDamageClassEventData),
		("ProjectileClassArray", TArray_FProjectileClassEventData),
		("PawnClassArray", TArray_FPawnClassEventData),
		("ActorArray", TArray_FString),
		("SoundCueArray", TArray_FString),
	]

class  UGameplayEvents(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGameplayEvents", UGameplayEvents_Data),
	]


class  UGameplayEventsReader_Data(Structure):
	_fields_ = [
		("RegisteredHandlers", TArray_UGameplayEventsHandlerPtr),
	]

class  UGameplayEventsReader(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGameplayEvents", UGameplayEvents_Data),
		("UGameplayEventsReader", UGameplayEventsReader_Data),
	]


class  UGameplayEventsWriter_Data(Structure):
	_fields_ = [
		("Game", POINTER(AGameInfo)),
	]

class  UGameplayEventsWriter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGameplayEvents", UGameplayEvents_Data),
		("UGameplayEventsWriter", UGameplayEventsWriter_Data),
	]


class  UGameplayEventsHandler_Data(Structure):
	_fields_ = [
		("EventIDFilter", TArray_int),
		("GroupFilter", TArray_FGameStatGroup),
		("Reader", POINTER(UGameplayEventsReader)),
	]

class  UGameplayEventsHandler(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGameplayEventsHandler", UGameplayEventsHandler_Data),
	]


class  UGameViewportClient_Data(Structure):
	_fields_ = [
		("VfTable_FViewportClient", FPointer),
		("VfTable_FExec", FPointer),
		("Viewport", FPointer),
		("ViewportFrame", FPointer),
		("GlobalInteractions", TArray_UInteractionPtr),
		("UIControllerClass", POINTER(UClass)),
		("UIController", POINTER(UUIInteraction)),
		("ViewportConsole", POINTER(UConsole)),
		("pShowFlags", FPointer),
		("LoadingMessage", FString),
		("SavingMessage", FString),
		("ConnectingMessage", FString),
		("PausedMessage", FString),
		("PrecachingMessage", FString),
		("bShowTitleSafeZone", c_bool, 1),
		("bDisplayingUIMouseCursor", c_bool, 1),
		("bUIMouseCaptureOverride", c_bool, 1),
		("bOverrideDiffuseAndSpecular", c_bool, 1),
		("bIsPlayInEditorViewport", c_bool, 1),
		("bShowSystemMouseCursor", c_bool, 1),
		("bDisableWorldRendering", c_bool, 1),
		("bDebugNoGFxUI", c_bool, 1),
		("bUseHardwareCursorWhenWindowed", c_bool, 1),
		("", c_ulong, 0),
		("TitleSafeZone", FTitleSafeZoneArea),
		("SplitscreenInfo", TArray_FSplitscreenData),
		("DesiredSplitscreenType", c_ubyte),
		("ActiveSplitscreenType", c_ubyte),
		("Default2PSplitType", c_ubyte),
		("Default3PSplitType", c_ubyte),
		("ProgressMessage", FString * 2),
		("ProgressTimeOut", c_float),
		("ProgressFadeTime", c_float),
		("DebugProperties", TArray_FDebugDisplayProperty),
		("ScaleformInteraction", FPointer),
		("__HandleInputKey__Delegate", FScriptDelegate),
		("__HandleInputAxis__Delegate", FScriptDelegate),
		("__HandleInputChar__Delegate", FScriptDelegate),
	]

class  UGameViewportClient(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGameViewportClient", UGameViewportClient_Data),
	]


class  UGBXCrossLevelReferenceContainer_Data(Structure):
	_fields_ = [
		("CrossLevelObjectRef", POINTER(UObject)),
	]

class  UGBXCrossLevelReferenceContainer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXCrossLevelReferenceContainer", UGBXCrossLevelReferenceContainer_Data),
	]


class  UGBXDefinition_Data(Structure):
	_fields_ = []

class  UGBXDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
	]


class  UBaseHitRegionDefinition_Data(Structure):
	_fields_ = []

class  UBaseHitRegionDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UBaseHitRegionDefinition", UBaseHitRegionDefinition_Data),
	]


class  UDamageTypeDefinition_Data(Structure):
	_fields_ = []

class  UDamageTypeDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UDamageTypeDefinition", UDamageTypeDefinition_Data),
	]


class  UEngineInteractionIconDefinition_Data(Structure):
	_fields_ = []

class  UEngineInteractionIconDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UEngineInteractionIconDefinition", UEngineInteractionIconDefinition_Data),
	]


class  UPawnAllegiance_Data(Structure):
	_fields_ = [
		("DefaultOpinion", c_ubyte),
		("SelfOpinion", c_ubyte),
		("ForcedOtherOpinion", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MyOpinions", TArray_FOpinionData),
		("OtherOpinions", TArray_FOpinionData),
		("bForceAllOtherOpinions", c_bool, 1),
		("", c_ulong, 0),
		("AllegianceKilledStat", FName),
	]

class  UPawnAllegiance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UPawnAllegiance", UPawnAllegiance_Data),
	]


class  UPawnInteractionDefinition_Data(Structure):
	_fields_ = [
		("bSupportsUseEvents", c_bool, 1),
		("bSupportsUseEventsWhenDead", c_bool, 1),
		("bAimToInteract", c_bool, 1),
		("bUseInteractDistance", c_bool, 1),
		("bSupportsTouchEvents", c_bool, 1),
		("bSupportsTouchEventsWhenDead", c_bool, 1),
		("bTouchAIPawns", c_bool, 1),
		("bTouchPlayerPawns", c_bool, 1),
		("bTouchVehicles", c_bool, 1),
		("bTouchProjectiles", c_bool, 1),
		("", c_ulong, 0),
		("InteractDistance", c_float),
		("TouchRadius", c_float),
		("TouchHeight", c_float),
		("OnTouch", TArray_UBehaviorBasePtr),
		("OnUnTouch", TArray_UBehaviorBasePtr),
		("OnUse", TArray_UBehaviorBasePtr),
	]

class  UPawnInteractionDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UPawnInteractionDefinition", UPawnInteractionDefinition_Data),
	]


class  UGBXNavMeshPathModifier_Data(Structure):
	_fields_ = []

class  UGBXNavMeshPathModifier(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXNavMeshPathModifier", UGBXNavMeshPathModifier_Data),
	]


class  UGBXNavMeshPathModifier_Simplify_Data(Structure):
	_fields_ = [
		("CornerCutInterval", c_float),
	]

class  UGBXNavMeshPathModifier_Simplify(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXNavMeshPathModifier", UGBXNavMeshPathModifier_Data),
		("UGBXNavMeshPathModifier_Simplify", UGBXNavMeshPathModifier_Simplify_Data),
	]


class  UGBXNavMeshPathModifier_SmoothTurns_Data(Structure):
	_fields_ = [
		("TooSharpThreshold", c_float),
		("MaxAdjustThreshold", c_float),
		("CornerLengthModifier", c_float),
		("TestInterval", c_float),
	]

class  UGBXNavMeshPathModifier_SmoothTurns(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXNavMeshPathModifier", UGBXNavMeshPathModifier_Data),
		("UGBXNavMeshPathModifier_SmoothTurns", UGBXNavMeshPathModifier_SmoothTurns_Data),
	]


class  UGearboxEngineGlobals_Data(Structure):
	_fields_ = [
		("TheTargetableList", POINTER(UTargetableList)),
		("AnimDebugTrack", POINTER(UTexture2D)),
		("AnimDebugCarat", POINTER(UTexture2D)),
		("SingletonInstance", POINTER(UGearboxEngineGlobals)),
		("ThePersistentDataManager", POINTER(UPersistentGameDataManager)),
		("PlayerOwnedComponents", TArray_FPlayerOwnedComponent),
		("DynamicShadowDirection", FVector),
		("WholeSceneDynamicShadowRadius", c_float),
		("AkCallBackGetRTPCs", TArray_FAkCallBackGetRTPC),
		("__OnDlgFinished__Delegate", FScriptDelegate),
	]

class  UGearboxEngineGlobals(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGearboxEngineGlobals", UGearboxEngineGlobals_Data),
	]


class  UGenericParamListStatEntry_Data(Structure):
	_fields_ = [
		("StatEvent", FPointer),
		("Writer", POINTER(UGameplayEventsWriter)),
	]

class  UGenericParamListStatEntry(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGenericParamListStatEntry", UGenericParamListStatEntry_Data),
	]


class  UGuidCache_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UGuidCache(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGuidCache", UGuidCache_Data),
	]


class  UIAnimBehavior_Data(Structure):
	_fields_ = []

class  UIAnimBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIAnimBehavior", UIAnimBehavior_Data),
	]


class  UIAttributeSlotEffectProvider_Data(Structure):
	_fields_ = []

class  UIAttributeSlotEffectProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIAttributeSlotEffectProvider", UIAttributeSlotEffectProvider_Data),
	]


class  UIBalancedActor_Data(Structure):
	_fields_ = []

class  UIBalancedActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIBalancedActor", UIBalancedActor_Data),
	]


class  UIBodyCompositionInstance_Data(Structure):
	_fields_ = []

class  UIBodyCompositionInstance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIBodyCompositionInstance", UIBodyCompositionInstance_Data),
	]


class  UIBodyInfoProvider_Data(Structure):
	_fields_ = []

class  UIBodyInfoProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIBodyInfoProvider", UIBodyInfoProvider_Data),
	]


class  UIDamageCauser_Data(Structure):
	_fields_ = []

class  UIDamageCauser(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIDamageCauser", UIDamageCauser_Data),
	]


class  UIDialogBox_Data(Structure):
	_fields_ = []

class  UIDialogBox(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIDialogBox", UIDialogBox_Data),
	]


class  UIFaceFXActor_Data(Structure):
	_fields_ = []

class  UIFaceFXActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIFaceFXActor", UIFaceFXActor_Data),
	]


class  UIGBXNavMeshBuildEvents_Data(Structure):
	_fields_ = []

class  UIGBXNavMeshBuildEvents(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIGBXNavMeshBuildEvents", UIGBXNavMeshBuildEvents_Data),
	]


class  UIGBXNavMeshSeed_Data(Structure):
	_fields_ = []

class  UIGBXNavMeshSeed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIGBXNavMeshSeed", UIGBXNavMeshSeed_Data),
	]


class  UIGBXNavMeshSpecialMove_Data(Structure):
	_fields_ = []

class  UIGBXNavMeshSpecialMove(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIGBXNavMeshSpecialMove", UIGBXNavMeshSpecialMove_Data),
	]


class  UIKilledBehavior_Data(Structure):
	_fields_ = []

class  UIKilledBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIKilledBehavior", UIKilledBehavior_Data),
	]


class  UIniLocPatcher_Data(Structure):
	_fields_ = [
		("Files", TArray_FIniLocFileEntry),
		("TitleFileInterface", FScriptInterface),
		("__OnReadTitleFileComplete__Delegate", FScriptDelegate),
	]

class  UIniLocPatcher(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UIniLocPatcher", UIniLocPatcher_Data),
	]


class  UInterface_NavigationHandle_Data(Structure):
	_fields_ = []

class  UInterface_NavigationHandle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UInterface_NavigationHandle", UInterface_NavigationHandle_Data),
	]


class  UInterface_Speaker_Data(Structure):
	_fields_ = []

class  UInterface_Speaker(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UInterface_Speaker", UInterface_Speaker_Data),
	]


class  UInterpCurveEdSetup_Data(Structure):
	_fields_ = [
		("Tabs", TArray_FCurveEdTab),
		("ActiveTab", c_int),
	]

class  UInterpCurveEdSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpCurveEdSetup", UInterpCurveEdSetup_Data),
	]


class  UInterpTrack_Data(Structure):
	_fields_ = [
		("VfTable_FInterpEdInputInterface", FPointer),
		("CurveEdVTable", FPointer),
		("SubTracks", TArray_UInterpTrackPtr),
		("TrackInstClass", POINTER(UClass)),
		("ActiveCondition", c_ubyte),
		("TrackPlayDirection", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TrackTitle", FString),
		("bOnePerGroup", c_bool, 1),
		("bDirGroupOnly", c_bool, 1),
		("bDisableTrack", c_bool, 1),
		("bIsAnimControlTrack", c_bool, 1),
		("bSubTrackOnly", c_bool, 1),
		("bVisible", c_bool, 1),
		("bIsSelected", c_bool, 1),
		("bIsRecording", c_bool, 1),
		("bIsCollapsed", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrack(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
	]


class  UIResourcePoolProvider_Data(Structure):
	_fields_ = []

class  UIResourcePoolProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIResourcePoolProvider", UIResourcePoolProvider_Data),
	]


class  UISpawnActor_Data(Structure):
	_fields_ = []

class  UISpawnActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UISpawnActor", UISpawnActor_Data),
	]


class  UISpecialOcclusionProvider_Data(Structure):
	_fields_ = []

class  UISpecialOcclusionProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UISpecialOcclusionProvider", UISpecialOcclusionProvider_Data),
	]


class  UITargetable_Data(Structure):
	_fields_ = []

class  UITargetable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UITargetable", UITargetable_Data),
	]


class  UJsonObject_Data(Structure):
	_fields_ = [
		("ValueMap", FMap_Mirror),
		("ObjectMap", FMap_Mirror),
		("ValueArray", TArray_FString),
		("ObjectArray", TArray_UJsonObjectPtr),
	]

class  UJsonObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UJsonObject", UJsonObject_Data),
	]


class  UKMeshProps_Data(Structure):
	_fields_ = [
		("COMNudge", FVector),
		("AggGeom", FKAggregateGeom),
	]

class  UKMeshProps(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UKMeshProps", UKMeshProps_Data),
	]


class  ULevelBase_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  ULevelBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelBase", ULevelBase_Data),
	]


class  ULevel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("LightmapTotalSize", c_float),
		("ShadowmapTotalSize", c_float),
		("Unknown2", c_ubyte, 0x),
	]

class  ULevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelBase", ULevelBase_Data),
		("ULevel", ULevel_Data),
	]


class  UPendingLevel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UPendingLevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelBase", ULevelBase_Data),
		("UPendingLevel", UPendingLevel_Data),
	]


class  UDemoPlayPendingLevel_Data(Structure):
	_fields_ = []

class  UDemoPlayPendingLevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelBase", ULevelBase_Data),
		("UPendingLevel", UPendingLevel_Data),
		("UDemoPlayPendingLevel", UDemoPlayPendingLevel_Data),
	]


class  UNetPendingLevel_Data(Structure):
	_fields_ = []

class  UNetPendingLevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelBase", ULevelBase_Data),
		("UPendingLevel", UPendingLevel_Data),
		("UNetPendingLevel", UNetPendingLevel_Data),
	]


class  ULevelStreaming_Data(Structure):
	_fields_ = [
		("PackageName", FName),
		("LoadedLevel", POINTER(ULevel)),
		("Offset", FVector),
		("OldOffset", FVector),
		("bIsVisible", c_bool, 1),
		("bHasLoadRequestPending", c_bool, 1),
		("bHasUnloadRequestPending", c_bool, 1),
		("bShouldBeVisibleInEditor", c_bool, 1),
		("bShouldBeVisibleInEditorOnLoad", c_bool, 1),
		("bBoundingBoxVisible", c_bool, 1),
		("bLocked", c_bool, 1),
		("bIsFullyStatic", c_bool, 1),
		("bShouldBeLoaded", c_bool, 1),
		("bShouldBeVisible", c_bool, 1),
		("bShouldBlockOnLoad", c_bool, 1),
		("bDrawOnLevelStatusMap", c_bool, 1),
		("bIsRequestingUnloadAndRemoval", c_bool, 1),
		("", c_ulong, 0),
		("DrawColor", FColor),
		("EditorStreamingVolumes", TArray_ALevelStreamingVolumePtr),
		("MinTimeBetweenVolumeUnloadRequests", c_float),
		("LastVolumeUnloadRequestTime", c_float),
		("Keywords", TArray_FString),
		("EditorGridVolume", POINTER(ALevelGridVolume)),
		("GridPosition", int * 3),
	]

class  ULevelStreaming(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelStreaming", ULevelStreaming_Data),
	]


class  ULevelStreamingAlwaysLoaded_Data(Structure):
	_fields_ = [
		("bIsProceduralBuildingLODLevel", c_bool, 1),
		("", c_ulong, 0),
	]

class  ULevelStreamingAlwaysLoaded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelStreaming", ULevelStreaming_Data),
		("ULevelStreamingAlwaysLoaded", ULevelStreamingAlwaysLoaded_Data),
	]


class  ULevelStreamingDistance_Data(Structure):
	_fields_ = [
		("Origin", FVector),
		("MaxDistance", c_float),
	]

class  ULevelStreamingDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelStreaming", ULevelStreaming_Data),
		("ULevelStreamingDistance", ULevelStreamingDistance_Data),
	]


class  ULevelStreamingKismet_Data(Structure):
	_fields_ = []

class  ULevelStreamingKismet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelStreaming", ULevelStreaming_Data),
		("ULevelStreamingKismet", ULevelStreamingKismet_Data),
	]


class  ULevelStreamingPersistent_Data(Structure):
	_fields_ = []

class  ULevelStreamingPersistent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelStreaming", ULevelStreaming_Data),
		("ULevelStreamingPersistent", ULevelStreamingPersistent_Data),
	]


class  ULightmappedSurfaceCollection_Data(Structure):
	_fields_ = [
		("SourceModel", POINTER(UModel)),
		("Surfaces", TArray_int),
	]

class  ULightmappedSurfaceCollection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULightmappedSurfaceCollection", ULightmappedSurfaceCollection_Data),
	]


class  ULightmassPrimitiveSettingsObject_Data(Structure):
	_fields_ = [
		("LightmassSettings", FLightmassPrimitiveSettings),
	]

class  ULightmassPrimitiveSettingsObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULightmassPrimitiveSettingsObject", ULightmassPrimitiveSettingsObject_Data),
	]


class  ULine_Data(Structure):
	_fields_ = [
		("Parent", POINTER(ULineData)),
		("LineSegments", TArray_ULineSegmentPtr),
		("Verts", TArray_UVertexPtr),
		("RegionMaterial", POINTER(UMaterial)),
		("SIZoneMaterial", POINTER(UMaterial)),
		("SIRetreatMaterial", POINTER(UMaterial)),
		("SIStealthMaterial", POINTER(UMaterial)),
		("bMakeRegion", c_bool, 1),
		("bIsCircular", c_bool, 1),
		("bIsMoving", c_bool, 1),
		("", c_ulong, 0),
		("CombatZoneID", c_int),
		("CombatZoneName", FString),
		("RegionData", TArray_FVector),
	]

class  ULine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULine", ULine_Data),
	]


class  ULineData_Data(Structure):
	_fields_ = [
		("RubberBand", FVector * 2),
		("bShowRubberBand", c_bool, 1),
		("bTerrainTrace", c_bool, 1),
		("bShowOnlySelectedZone", c_bool, 1),
		("bAutoGenRedundantData", c_bool, 1),
		("bIsSelectedMap", c_bool, 1),
		("", c_ulong, 0),
		("ParentID", c_int),
		("SegmentID", c_int),
		("CurrentCombatZoneID", c_int),
		("CurrentCombatZoneName", FString),
		("VertexScale", c_float),
		("VertexScaleFactor", c_float),
		("LineSegmentScale", c_float),
		("LineSegmentScaleFactor", c_float),
		("EditorMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Lines", TArray_ULinePtr),
	]

class  ULineData(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULineData", ULineData_Data),
	]


class  ULineSegment_Data(Structure):
	_fields_ = [
		("ParentLine", POINTER(ULine)),
		("Verts", POINTER(UVertex) * 2),
		("Direction", FVector),
		("NormalLine", FVector * 2),
		("RightNormal", c_bool, 1),
		("bIsSelected", c_bool, 1),
		("bDelete", c_bool, 1),
		("", c_ulong, 0),
		("Size", c_float),
		("SegmentType", c_ubyte),
		("SegmentMaterial", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("SegmentID", c_int),
		("LineColor", FColor),
		("NormalColor", FColor),
		("SelectedColor", FColor),
		("VulnerableColor", FColor),
		("VantageColor", FColor),
		("SIColor", FColor),
		("RetreatColor", FColor),
		("StealthColor", FColor),
	]

class  ULineSegment(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULineSegment", ULineSegment_Data),
	]


class  UMapInfo_Data(Structure):
	_fields_ = []

class  UMapInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMapInfo", UMapInfo_Data),
	]


class  USurface_Data(Structure):
	_fields_ = []

class  USurface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
	]


class  UMaterialInterface_Data(Structure):
	_fields_ = [
		("ParentRefFence", FRenderCommandFence_Mirror),
		("LightmassSettings", FLightmassMaterialInterfaceSettings),
		("CustomSkinType", c_ubyte),
	]

class  UMaterialInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UMaterialInterface", UMaterialInterface_Data),
	]


class  UMaterial_Data(Structure):
	_fields_ = [
		("PhysMaterial", POINTER(UPhysicalMaterial)),
		("PhysicalMaterial", POINTER(UClass)),
		("PhysMaterialMask", POINTER(UTexture2D)),
		("PhysMaterialMaskUVChannel", c_int),
		("BlackPhysicalMaterial", POINTER(UPhysicalMaterial)),
		("WhitePhysicalMaterial", POINTER(UPhysicalMaterial)),
		("DiffuseColor", FColorMaterialInput),
		("DiffusePower", FScalarMaterialInput),
		("SpecularColor", FColorMaterialInput),
		("SpecularPower", FScalarMaterialInput),
		("Normal", FVectorMaterialInput),
		("EmissiveColor", FColorMaterialInput),
		("Opacity", FScalarMaterialInput),
		("OpacityMask", FScalarMaterialInput),
		("OpacityMaskClipValue", c_float),
		("bNeedsShadowDepthBias", c_bool, 1),
		("TwoSided", c_bool, 1),
		("TwoSidedSeparatePass", c_bool, 1),
		("bDisableDepthTest", c_bool, 1),
		("bDisableEdgeDetection", c_bool, 1),
		("bSceneTextureRenderBehindTranslucency", c_bool, 1),
		("bAllowFog", c_bool, 1),
		("bTranslucencyReceiveDominantShadowsFromStatic", c_bool, 1),
		("bTranslucencyInheritDominantShadowsFromOpaque", c_bool, 1),
		("bAllowTranslucencyDoF", c_bool, 1),
		("bUseOneLayerDistortion", c_bool, 1),
		("bUseLitTranslucencyDepthPass", c_bool, 1),
		("bUseLitTranslucencyPostRenderDepthPass", c_bool, 1),
		("bCastLitTranslucencyShadowAsMasked", c_bool, 1),
		("bUsedAsLightFunction", c_bool, 1),
		("bUsedWithFogVolumes", c_bool, 1),
		("bUsedAsSpecialEngineMaterial", c_bool, 1),
		("bUsedWithSkeletalMesh", c_bool, 1),
		("bUsedWithTerrain", c_bool, 1),
		("bUsedWithLandscape", c_bool, 1),
		("bUsedWithFracturedMeshes", c_bool, 1),
		("bUsedWithParticleSystem", c_bool, 1),
		("bUsedWithParticleSprites", c_bool, 1),
		("bUsedWithBeamTrails", c_bool, 1),
		("bUsedWithParticleSubUV", c_bool, 1),
		("bUsedWithFoliage", c_bool, 1),
		("bUsedWithSpeedTree", c_bool, 1),
		("bUsedWithStaticLighting", c_bool, 1),
		("bUsedWithLensFlare", c_bool, 1),
		("bUsedWithGammaCorrection", c_bool, 1),
		("bUsedWithInstancedMeshParticles", c_bool, 1),
		("bUsedWithFluidSurfaces", c_bool, 1),
		("bUsedWithDecals", c_bool, 1),
		("bUsedWithMaterialEffect", c_bool, 1),
		("bUsedWithMorphTargets", c_bool, 1),
		("bUsedWithRadialBlur", c_bool, 1),
		("bUsedWithInstancedMeshes", c_bool, 1),
		("bUsedWithSplineMeshes", c_bool, 1),
		("bUsedWithAPEXMeshes", c_bool, 1),
		("bUsedWithSPHFluid", c_bool, 1),
		("bUsedWithScreenDoorFade", c_bool, 1),
		("bUsedWithWires", c_bool, 1),
		("Wireframe", c_bool, 1),
		("bPerPixelCameraVector", c_bool, 1),
		("bAllowLightmapSpecular", c_bool, 1),
		("bNoDraw", c_bool, 1),
		("bFullResTransConsole", c_bool, 1),
		("bIsFallbackMaterial", c_bool, 1),
		("bUsesDistortion", c_bool, 1),
		("bIsMasked", c_bool, 1),
		("bIsPreviewMaterial", c_bool, 1),
		("", c_ulong, 0),
		("Distortion", FVector2MaterialInput),
		("BlendMode", c_ubyte),
		("LightingModel", c_ubyte),
		("ParticleDownsampling", c_ubyte),
		("D3D11TessellationMode", c_ubyte),
		("CustomLighting", FColorMaterialInput),
		("CustomSkylightDiffuse", FColorMaterialInput),
		("AnisotropicDirection", FVectorMaterialInput),
		("TwoSidedLightingMask", FScalarMaterialInput),
		("TwoSidedLightingColor", FColorMaterialInput),
		("WorldPositionOffset", FVectorMaterialInput),
		("WorldDisplacement", FVectorMaterialInput),
		("TessellationFactors", FVector2MaterialInput),
		("MaterialResources", FPointer * 2),
		("DefaultMaterialInstances", FPointer * 3),
		("EditorX", c_int),
		("EditorY", c_int),
		("EditorPitch", c_int),
		("EditorYaw", c_int),
		("Expressions", TArray_UMaterialExpressionPtr),
		("Unknown1", c_ubyte, 0x),
		("ReferencedTextures", TArray_UTexturePtr),
	]

class  UMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UMaterialInterface", UMaterialInterface_Data),
		("UMaterial", UMaterial_Data),
	]


class  UMaterialExpression_Data(Structure):
	_fields_ = [
		("bRealtimePreview", c_bool, 1),
		("bNeedToUpdatePreview", c_bool, 1),
		("bIsParameterExpression", c_bool, 1),
		("bShowOutputNameOnPin", c_bool, 1),
		("bHidePreviewWindow", c_bool, 1),
		("bUsedByStaticParameterSet", c_bool, 1),
		("", c_ulong, 0),
		("Compound", POINTER(UMaterialExpressionCompound)),
	]

class  UMaterialExpression(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
	]


class  UModel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UModel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UModel", UModel_Data),
	]


class  UMusicTrackDataStructures_Data(Structure):
	_fields_ = []

class  UMusicTrackDataStructures(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMusicTrackDataStructures", UMusicTrackDataStructures_Data),
	]


class  UNavigationMeshBase_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UNavigationMeshBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavigationMeshBase", UNavigationMeshBase_Data),
	]


class  UNetDriver_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("ConnectionTimeout", c_float),
		("InitialConnectTimeout", c_float),
		("KeepAliveTime", c_float),
		("RelevantTimeout", c_float),
		("SpawnPrioritySeconds", c_float),
		("ServerTravelPause", c_float),
		("MaxClientRate", c_int),
		("MaxInternetClientRate", c_int),
		("NetServerMaxTickRate", c_int),
		("bClampListenServerTickRate", BOOL),
		("AllowDownloads", BOOL),
		("AllowPeerConnections", BOOL),
		("AllowPeerVoice", c_bool, 1),
		("", c_ulong, 0),
		("Unknown2", c_ubyte, 0x),
		("MaxDownloadSize", c_int),
		("DownloadManagers", TArray_FString),
		("Unknown3", c_ubyte, 0x),
		("NetConnectionClassName", FString),
		("Unknown4", c_ubyte, 0x),
	]

class  UNetDriver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USubsystem", USubsystem_Data),
		("UNetDriver", UNetDriver_Data),
	]


class  UDemoRecDriver_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("DemoSpectatorClass", FString),
		("Unknown2", c_ubyte, 0x),
		("MaxRewindPoints", c_int),
		("Unknown3", c_ubyte, 0x),
		("RewindPointInterval", c_float),
		("NumRecentRewindPoints", c_int),
		("Unknown4", c_ubyte, 0x),
	]

class  UDemoRecDriver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USubsystem", USubsystem_Data),
		("UNetDriver", UNetDriver_Data),
		("UDemoRecDriver", UDemoRecDriver_Data),
	]


class  UObjectReferencer_Data(Structure):
	_fields_ = [
		("ReferencedObjects", TArray_UObjectPtr),
	]

class  UObjectReferencer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UObjectReferencer", UObjectReferencer_Data),
	]


class  UOnlineSubsystem_Data(Structure):
	_fields_ = [
		("VfTable_FTickableObject", FPointer),
		("AccountInterface", FScriptInterface),
		("PlayerInterface", FScriptInterface),
		("PlayerInterfaceEx", FScriptInterface),
		("SystemInterface", FScriptInterface),
		("GameInterface", FScriptInterface),
		("ContentInterface", FScriptInterface),
		("VoiceInterface", FScriptInterface),
		("StatsInterface", FScriptInterface),
		("NewsInterface", FScriptInterface),
		("PartyChatInterface", FScriptInterface),
		("TitleFileInterface", FScriptInterface),
		("AuthInterface", FScriptInterface),
		("NamedInterfaces", TArray_FNamedInterface),
		("NamedInterfaceDefs", TArray_FNamedInterfaceDef),
		("Sessions", TArray_FNamedSession),
		("bUseBuildIdOverride", c_bool, 1),
		("", c_ulong, 0),
		("BuildIdOverride", c_int),
		("IniLocPatcherClassName", FString),
		("Patcher", POINTER(UIniLocPatcher)),
		("AsyncMinCompletionTime", c_float),
	]

class  UOnlineSubsystem(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineSubsystem", UOnlineSubsystem_Data),
	]


class  UOnlineAuthInterfaceBaseImpl_Data(Structure):
	_fields_ = [
		("bAuthReady", c_bool, 1),
		("", c_ulong, 0),
		("ClientAuthSessions", TArray_FAuthSession),
		("ServerAuthSessions", TArray_FAuthSession),
		("PeerAuthSessions", TArray_FAuthSession),
		("LocalClientAuthSessions", TArray_FLocalAuthSession),
		("LocalServerAuthSessions", TArray_FLocalAuthSession),
		("LocalPeerAuthSessions", TArray_FLocalAuthSession),
		("__OnAuthReady__Delegate", FScriptDelegate),
		("__OnAuthRequestClient__Delegate", FScriptDelegate),
		("__OnAuthRequestServer__Delegate", FScriptDelegate),
		("__OnAuthBlobReceivedClient__Delegate", FScriptDelegate),
		("__OnAuthBlobReceivedServer__Delegate", FScriptDelegate),
		("__OnAuthCompleteClient__Delegate", FScriptDelegate),
		("__OnAuthCompleteServer__Delegate", FScriptDelegate),
		("__OnAuthKillClient__Delegate", FScriptDelegate),
		("__OnAuthRetryServer__Delegate", FScriptDelegate),
		("__OnClientConnectionClose__Delegate", FScriptDelegate),
		("__OnServerConnectionClose__Delegate", FScriptDelegate),
	]

class  UOnlineAuthInterfaceBaseImpl(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineAuthInterfaceBaseImpl", UOnlineAuthInterfaceBaseImpl_Data),
	]


class  UOnlineMatchmakingStats_Data(Structure):
	_fields_ = []

class  UOnlineMatchmakingStats(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineMatchmakingStats", UOnlineMatchmakingStats_Data),
	]


class  UOnlinePlayerStorage_Data(Structure):
	_fields_ = [
		("VersionNumber", c_int),
		("VersionSettingsId", c_int),
		("SaveCountSettingId", c_int),
		("ProfileSettings", TArray_FOnlineProfileSetting),
		("ProfileMappings", TArray_FSettingsPropertyPropertyMetaData),
		("AsyncState", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("DeviceID", c_int),
	]

class  UOnlinePlayerStorage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlinePlayerStorage", UOnlinePlayerStorage_Data),
	]


class  UOnlineProfileSettings_Data(Structure):
	_fields_ = [
		("ProfileSettingIds", TArray_int),
		("DefaultSettings", TArray_FOnlineProfileSetting),
		("DefaultConsoleSettings", TArray_FOnlineProfileSetting),
		("OwnerMappings", TArray_FIdToStringMapping),
	]

class  UOnlineProfileSettings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlinePlayerStorage", UOnlinePlayerStorage_Data),
		("UOnlineProfileSettings", UOnlineProfileSettings_Data),
	]


class  UOnlineStats_Data(Structure):
	_fields_ = [
		("ViewIdMappings", TArray_FStringIdToStringMapping),
	]

class  UOnlineStats(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineStats", UOnlineStats_Data),
	]


class  UOnlineStatsRead_Data(Structure):
	_fields_ = [
		("ViewId", c_int),
		("SortColumnId", c_int),
		("ColumnIds", TArray_int),
		("TotalRowsInView", c_int),
		("Rows", TArray_FOnlineStatsRow),
		("ColumnMappings", TArray_FColumnMetaData),
		("ViewName", FString),
		("TitleId", c_int),
	]

class  UOnlineStatsRead(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineStats", UOnlineStats_Data),
		("UOnlineStatsRead", UOnlineStatsRead_Data),
	]


class  UOnlineStatsWrite_Data(Structure):
	_fields_ = [
		("StatMappings", TArray_FStringIdToStringMapping),
		("Properties", TArray_FSettingsProperty),
		("ViewIds", TArray_int),
		("ArbitratedViewIds", TArray_int),
		("RatingId", c_int),
		("__OnStatsWriteComplete__Delegate", FScriptDelegate),
	]

class  UOnlineStatsWrite(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineStats", UOnlineStats_Data),
		("UOnlineStatsWrite", UOnlineStatsWrite_Data),
	]


class  UPackageMapLevel_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UPackageMapLevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPackageMap", UPackageMap_Data),
		("UPackageMapLevel", UPackageMapLevel_Data),
	]


class  UPackageMapSeekFree_Data(Structure):
	_fields_ = []

class  UPackageMapSeekFree(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPackageMap", UPackageMap_Data),
		("UPackageMapLevel", UPackageMapLevel_Data),
		("UPackageMapSeekFree", UPackageMapSeekFree_Data),
	]


class  UPatchScriptCommandlet_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UPatchScriptCommandlet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCommandlet", UCommandlet_Data),
		("UPatchScriptCommandlet", UPatchScriptCommandlet_Data),
	]


class  UPlayer_Data(Structure):
	_fields_ = [
		("VfTable_FExec", FPointer),
		("Actor", POINTER(APlayerController)),
		("CurrentNetSpeed", c_int),
		("ConfiguredInternetSpeed", c_int),
		("ConfiguredLanSpeed", c_int),
		("PP_DesaturationMultiplier", c_float),
		("PP_HighlightsMultiplier", c_float),
		("PP_MidTonesMultiplier", c_float),
		("PP_ShadowsMultiplier", c_float),
	]

class  UPlayer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPlayer", UPlayer_Data),
	]


class  ULocalPlayer_Data(Structure):
	_fields_ = [
		("VfTable_FObserverInterface", FPointer),
		("ControllerId", c_int),
		("ViewportClient", POINTER(UGameViewportClient)),
		("Origin", FVector2D),
		("Size", FVector2D),
		("PlayerPostProcess", POINTER(UPostProcessChain)),
		("PlayerPostProcessChains", TArray_UPostProcessChainPtr),
		("ViewState", FPointer),
		("ActorVisibilityHistory", FSynchronizedActorVisibilityHistory),
		("LastViewLocation", FVector),
		("CurrentPPInfo", FCurrentPostProcessVolumeInfo),
		("LevelPPInfo", FCurrentPostProcessVolumeInfo),
		("ActivePPOverrides", TArray_FPostProcessSettingsOverride),
		("WorldLightingOverrides", TArray_FWorldLightingOverride),
		("AspectRatioAxisConstraint", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LastMap", FString),
		("bWantToResetToMapDefaultPP", c_bool, 1),
		("bSentSplitJoin", c_bool, 1),
		("bPendingServerAuth", c_bool, 1),
		("bLobbyWasShown", c_bool, 1),
		("", c_ulong, 0),
		("TagContext", POINTER(UTranslationContext)),
		("CachedAuthInt", POINTER(UOnlineAuthInterfaceBaseImpl)),
		("ServerAuthTimestamp", c_float),
		("ServerAuthTimeout", c_int),
		("ServerAuthRetryCount", c_int),
		("MaxServerAuthRetryCount", c_int),
		("ServerAuthUID", FUniqueNetId),
		("Unknown2", c_ubyte, 0x),
		("ViewProjectionMatrix", FMatrix),
		("ViewProjMatTimestamp", c_float),
	]

class  ULocalPlayer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPlayer", UPlayer_Data),
		("ULocalPlayer", ULocalPlayer_Data),
	]


class  UNetConnection_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("Children", TArray_UChildConnectionPtr),
		("Unknown2", c_ubyte, 0x),
	]

class  UNetConnection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPlayer", UPlayer_Data),
		("UNetConnection", UNetConnection_Data),
	]


class  UChildConnection_Data(Structure):
	_fields_ = [
		("Parent", POINTER(UNetConnection)),
	]

class  UChildConnection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPlayer", UPlayer_Data),
		("UNetConnection", UNetConnection_Data),
		("UChildConnection", UChildConnection_Data),
	]


class  UDemoRecConnection_Data(Structure):
	_fields_ = []

class  UDemoRecConnection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPlayer", UPlayer_Data),
		("UNetConnection", UNetConnection_Data),
		("UDemoRecConnection", UDemoRecConnection_Data),
	]


class  UPolys_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UPolys(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPolys", UPolys_Data),
	]


class  UPostProcessChain_Data(Structure):
	_fields_ = [
		("Effects", TArray_UPostProcessEffectPtr),
	]

class  UPostProcessChain(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessChain", UPostProcessChain_Data),
	]


class  UPostProcessEffect_Data(Structure):
	_fields_ = [
		("bShowInEditor", c_bool, 1),
		("bShowInGame", c_bool, 1),
		("bUseWorldSettings", c_bool, 1),
		("bAffectsLightingOnly", c_bool, 1),
		("", c_ulong, 0),
		("EffectName", FName),
		("NodePosY", c_int),
		("NodePosX", c_int),
		("DrawWidth", c_int),
		("DrawHeight", c_int),
		("OutDrawY", c_int),
		("InDrawY", c_int),
		("SceneDPG", c_ubyte),
	]

class  UPostProcessEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
	]


class  UAccumulateAlphaEffect_Data(Structure):
	_fields_ = []

class  UAccumulateAlphaEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UAccumulateAlphaEffect", UAccumulateAlphaEffect_Data),
	]


class  UAmbientOcclusionEffect_Data(Structure):
	_fields_ = [
		("OcclusionColor", FLinearColor),
		("OcclusionPower", c_float),
		("OcclusionScale", c_float),
		("OcclusionBias", c_float),
		("MinOcclusion", c_float),
		("SSAO2", c_bool, 1),
		("bAngleBasedSSAO", c_bool, 1),
		("", c_ulong, 0),
		("OcclusionRadius", c_float),
		("OcclusionAttenuation", c_float),
		("OcclusionQuality", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("OcclusionFadeoutMinDistance", c_float),
		("OcclusionFadeoutMaxDistance", c_float),
		("HaloDistanceThreshold", c_float),
		("HaloDistanceScale", c_float),
		("HaloOcclusion", c_float),
		("EdgeDistanceThreshold", c_float),
		("EdgeDistanceScale", c_float),
		("FilterDistanceScale", c_float),
		("FilterSize", c_int),
		("HistoryConvergenceTime", c_float),
		("HistoryWeightConvergenceTime", c_float),
	]

class  UAmbientOcclusionEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UAmbientOcclusionEffect", UAmbientOcclusionEffect_Data),
	]


class  UBlurEffect_Data(Structure):
	_fields_ = [
		("BlurKernelSize", c_int),
	]

class  UBlurEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UBlurEffect", UBlurEffect_Data),
	]


class  UDOFEffect_Data(Structure):
	_fields_ = [
		("FalloffExponent", c_float),
		("BlurKernelSize", c_float),
		("MaxNearBlurAmount", c_float),
		("MinBlurAmount", c_float),
		("MaxFarBlurAmount", c_float),
		("FocusType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("FocusInnerRadius", c_float),
		("FocusDistance", c_float),
		("FocusPosition", FVector),
		("TunnelVisionScale", c_float),
		("TunnelVisionYOffset", c_float),
		("bOverrideDOFSettings", c_bool, 1),
		("", c_ulong, 0),
		("FalloffExponentOverride", c_float),
		("BlurKernelSizeOverride", c_float),
		("MaxNearBlurAmountOverride", c_float),
		("MaxFarBlurAmountOverride", c_float),
		("MinBlurAmountOverride", c_float),
		("FocusInnerRadiusOverride", c_float),
		("FocusDistanceOverride", c_float),
		("TunnelVisionScaleOverride", c_float),
		("TunnelVisionYOffsetOverride", c_float),
	]

class  UDOFEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UDOFEffect", UDOFEffect_Data),
	]


class  UDOFAndBloomEffect_Data(Structure):
	_fields_ = [
		("BloomScale", c_float),
		("BloomThreshold", c_float),
		("BloomTint", FColor),
		("BloomScreenBlendThreshold", c_float),
		("SceneMultiplier", c_float),
		("BlurBloomKernelSize", c_float),
		("bEnableReferenceDOF", c_bool, 1),
		("", c_ulong, 0),
		("DepthOfFieldType", c_ubyte),
		("DepthOfFieldQuality", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BokehTexture", POINTER(UTexture2D)),
	]

class  UDOFAndBloomEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UDOFEffect", UDOFEffect_Data),
		("UDOFAndBloomEffect", UDOFAndBloomEffect_Data),
	]


class  UDOFBloomMotionBlurEffect_Data(Structure):
	_fields_ = [
		("MaxVelocity", c_float),
		("MotionBlurAmount", c_float),
		("FullMotionBlur", c_bool, 1),
		("", c_ulong, 0),
		("CameraRotationThreshold", c_float),
		("CameraTranslationThreshold", c_float),
	]

class  UDOFBloomMotionBlurEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UDOFEffect", UDOFEffect_Data),
		("UDOFAndBloomEffect", UDOFAndBloomEffect_Data),
		("UDOFBloomMotionBlurEffect", UDOFBloomMotionBlurEffect_Data),
	]


class  UUberPostProcessEffect_Data(Structure):
	_fields_ = [
		("SceneShadows", FVector),
		("SceneHighLights", FVector),
		("SceneMidTones", FVector),
		("SceneDesaturation", c_float),
		("SceneColorize", FVector),
		("VignetteEnabled", c_bool, 1),
		("bEnableImageGrain", c_bool, 1),
		("bScaleEffectsWithViewSize", c_bool, 1),
		("bEnableHDRTonemapper", c_bool, 1),
		("", c_ulong, 0),
		("VignetteColor", FLinearColor),
		("VignetteBrightness", c_float),
		("VignetteTexture", POINTER(UTexture)),
		("TonemapperType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TonemapperRange", c_float),
		("TonemapperToeFactor", c_float),
		("TonemapperScale", c_float),
		("MotionBlurSoftEdgeKernelSize", c_float),
		("SceneImageGrainScale", c_float),
		("BloomWeightSmall", c_float),
		("BloomWeightMedium", c_float),
		("BloomWeightLarge", c_float),
		("BloomSizeScaleSmall", c_float),
		("BloomSizeScaleMedium", c_float),
		("BloomSizeScaleLarge", c_float),
		("PreviousLUTBlender", FLUTBlender),
		("SceneHDRTonemapperScale", c_float),
	]

class  UUberPostProcessEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UDOFEffect", UDOFEffect_Data),
		("UDOFAndBloomEffect", UDOFAndBloomEffect_Data),
		("UDOFBloomMotionBlurEffect", UDOFBloomMotionBlurEffect_Data),
		("UUberPostProcessEffect", UUberPostProcessEffect_Data),
	]


class  UDwTriovizImplEffect_Data(Structure):
	_fields_ = []

class  UDwTriovizImplEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UDwTriovizImplEffect", UDwTriovizImplEffect_Data),
	]


class  UFXAAEffect_Data(Structure):
	_fields_ = []

class  UFXAAEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UFXAAEffect", UFXAAEffect_Data),
	]


class  UMaterialEffect_Data(Structure):
	_fields_ = [
		("Material", POINTER(UMaterialInterface)),
	]

class  UMaterialEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UMaterialEffect", UMaterialEffect_Data),
	]


class  UMotionBlurEffect_Data(Structure):
	_fields_ = [
		("MaxVelocity", c_float),
		("MotionBlurAmount", c_float),
		("FullMotionBlur", c_bool, 1),
		("", c_ulong, 0),
		("CameraRotationThreshold", c_float),
		("CameraTranslationThreshold", c_float),
	]

class  UMotionBlurEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UMotionBlurEffect", UMotionBlurEffect_Data),
	]


class  UPrimitiveComponentFactory_Data(Structure):
	_fields_ = [
		("CollideActors", c_bool, 1),
		("BlockActors", c_bool, 1),
		("BlockZeroExtent", c_bool, 1),
		("BlockNonZeroExtent", c_bool, 1),
		("BlockRigidBody", c_bool, 1),
		("HiddenGame", c_bool, 1),
		("HiddenEditor", c_bool, 1),
		("CastShadow", c_bool, 1),
		("", c_ulong, 0),
	]

class  UPrimitiveComponentFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPrimitiveComponentFactory", UPrimitiveComponentFactory_Data),
	]


class  UMeshComponentFactory_Data(Structure):
	_fields_ = [
		("Materials", TArray_UMaterialInterfacePtr),
	]

class  UMeshComponentFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPrimitiveComponentFactory", UPrimitiveComponentFactory_Data),
		("UMeshComponentFactory", UMeshComponentFactory_Data),
	]


class  UStaticMeshComponentFactory_Data(Structure):
	_fields_ = [
		("StaticMesh", POINTER(UStaticMesh)),
	]

class  UStaticMeshComponentFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPrimitiveComponentFactory", UPrimitiveComponentFactory_Data),
		("UMeshComponentFactory", UMeshComponentFactory_Data),
		("UStaticMeshComponentFactory", UStaticMeshComponentFactory_Data),
	]


class  UReachSpec_Data(Structure):
	_fields_ = [
		("NavOctreeObject", FPointer),
		("Direction", FVector),
		("BlockedBy", POINTER(AActor)),
		("MaxLandingVelocity", c_int),
		("Distance", c_int),
		("Start", POINTER(ANavigationPoint)),
		("End", FActorReference),
		("CollisionRadius", c_int),
		("CollisionHeight", c_int),
		("reachFlags", c_int),
		("bPruned", c_ubyte),
		("PathColorIndex", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bAddToNavigationOctree", c_bool, 1),
		("bCanCutCorners", c_bool, 1),
		("bCheckForObstructions", c_bool, 1),
		("bSkipPrune", c_bool, 1),
		("bDisabled", c_bool, 1),
		("bRequiresSpecialMovement", c_bool, 1),
		("", c_ulong, 0),
	]

class  UReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
	]


class  UAdvancedReachSpec_Data(Structure):
	_fields_ = []

class  UAdvancedReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UAdvancedReachSpec", UAdvancedReachSpec_Data),
	]


class  UCeilingReachSpec_Data(Structure):
	_fields_ = []

class  UCeilingReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UCeilingReachSpec", UCeilingReachSpec_Data),
	]


class  UForcedReachSpec_Data(Structure):
	_fields_ = []

class  UForcedReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
	]


class  UCoverSlipReachSpec_Data(Structure):
	_fields_ = [
		("SpecDirection", c_ubyte),
	]

class  UCoverSlipReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
		("UCoverSlipReachSpec", UCoverSlipReachSpec_Data),
	]


class  UFloorToCeilingReachSpec_Data(Structure):
	_fields_ = []

class  UFloorToCeilingReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
		("UFloorToCeilingReachSpec", UFloorToCeilingReachSpec_Data),
	]


class  UMantleReachSpec_Data(Structure):
	_fields_ = [
		("bClimbUp", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMantleReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
		("UMantleReachSpec", UMantleReachSpec_Data),
	]


class  USlotToSlotReachSpec_Data(Structure):
	_fields_ = [
		("SpecDirection", c_ubyte),
	]

class  USlotToSlotReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
		("USlotToSlotReachSpec", USlotToSlotReachSpec_Data),
	]


class  USwatTurnReachSpec_Data(Structure):
	_fields_ = [
		("SpecDirection", c_ubyte),
	]

class  USwatTurnReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
		("USwatTurnReachSpec", USwatTurnReachSpec_Data),
	]


class  UWallTransReachSpec_Data(Structure):
	_fields_ = []

class  UWallTransReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UForcedReachSpec", UForcedReachSpec_Data),
		("UWallTransReachSpec", UWallTransReachSpec_Data),
	]


class  ULadderReachSpec_Data(Structure):
	_fields_ = []

class  ULadderReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("ULadderReachSpec", ULadderReachSpec_Data),
	]


class  UProscribedReachSpec_Data(Structure):
	_fields_ = []

class  UProscribedReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UProscribedReachSpec", UProscribedReachSpec_Data),
	]


class  UTeleportReachSpec_Data(Structure):
	_fields_ = []

class  UTeleportReachSpec(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UReachSpec", UReachSpec_Data),
		("UTeleportReachSpec", UTeleportReachSpec_Data),
	]


class  USavedMove_Data(Structure):
	_fields_ = [
		("NextMove", POINTER(USavedMove)),
		("TimeStamp", c_float),
		("Delta", c_float),
		("bRun", c_bool, 1),
		("bDuck", c_bool, 1),
		("bPressedJump", c_bool, 1),
		("bDoubleJump", c_bool, 1),
		("bPreciseDestination", c_bool, 1),
		("bForceRMVelocity", c_bool, 1),
		("bForceMaxAccel", c_bool, 1),
		("bRootMotionFromInterpCurve", c_bool, 1),
		("", c_ulong, 0),
		("DoubleClickMove", c_ubyte),
		("SavedPhysics", c_ubyte),
		("AnalogPct", c_ubyte),
		("RootMotionMode", c_ubyte),
		("StartLocation", FVector),
		("StartRelativeLocation", FVector),
		("StartVelocity", FVector),
		("StartFloor", FVector),
		("SavedLocation", FVector),
		("SavedVelocity", FVector),
		("SavedRelativeLocation", FVector),
		("RMVelocity", FVector),
		("Acceleration", FVector),
		("Rotation", FRotator),
		("StartBase", POINTER(AActor)),
		("EndBase", POINTER(AActor)),
		("CustomTimeDilation", c_float),
		("AccelDotThreshold", c_float),
		("RootMotionInterpCurrentTime", c_float),
		("RootMotionInterpCurveLastValue", FVector),
	]

class  USavedMove(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USavedMove", USavedMove_Data),
	]


class  USaveGameSummary_Data(Structure):
	_fields_ = [
		("BaseLevel", FName),
		("Description", FString),
	]

class  USaveGameSummary(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USaveGameSummary", USaveGameSummary_Data),
	]


class  USelection_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  USelection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USelection", USelection_Data),
	]


class  UServerCommandlet_Data(Structure):
	_fields_ = []

class  UServerCommandlet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCommandlet", UCommandlet_Data),
		("UServerCommandlet", UServerCommandlet_Data),
	]


class  USettings_Data(Structure):
	_fields_ = [
		("LocalizedSettings", TArray_FLocalizedStringSetting),
		("Properties", TArray_FSettingsProperty),
		("LocalizedSettingsMappings", TArray_FLocalizedStringSettingMetaData),
		("PropertyMappings", TArray_FSettingsPropertyPropertyMetaData),
	]

class  USettings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USettings", USettings_Data),
	]


class  UOnlineGameSearch_Data(Structure):
	_fields_ = [
		("MaxSearchResults", c_int),
		("Query", FLocalizedStringSetting),
		("bIsLanQuery", c_bool, 1),
		("bUsesArbitration", c_bool, 1),
		("bIsSearchInProgress", c_bool, 1),
		("", c_ulong, 0),
		("GameSettingsClass", POINTER(UClass)),
		("Results", TArray_FOnlineGameSearchResult),
		("ManualSkillOverride", FOverrideSkill),
		("NamedProperties", TArray_FNamedObjectProperty),
		("FilterQuery", FOnlineGameSearchQuery),
		("AdditionalSearchCriteria", FString),
		("PingBucketSize", c_int),
		("NumPingProbes", c_int),
		("MaxPingBytes", c_int),
		("NumSearchUsers", c_int),
	]

class  UOnlineGameSearch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USettings", USettings_Data),
		("UOnlineGameSearch", UOnlineGameSearch_Data),
	]


class  UOnlineGameSettings_Data(Structure):
	_fields_ = [
		("NumPublicConnections", c_int),
		("NumPrivateConnections", c_int),
		("NumOpenPublicConnections", c_int),
		("NumOpenPrivateConnections", c_int),
		("ServerNonce", FQWord),
		("bShouldAdvertise", c_bool, 1),
		("bIsLanMatch", c_bool, 1),
		("bUsesStats", c_bool, 1),
		("bAllowJoinInProgress", c_bool, 1),
		("bAllowInvites", c_bool, 1),
		("bUsesPresence", c_bool, 1),
		("bAllowJoinViaPresence", c_bool, 1),
		("bAllowJoinViaPresenceFriendsOnly", c_bool, 1),
		("bUsesArbitration", c_bool, 1),
		("bAntiCheatProtected", c_bool, 1),
		("bWasFromInvite", c_bool, 1),
		("bIsDedicated", c_bool, 1),
		("bHasSkillUpdateInProgress", c_bool, 1),
		("bShouldShrinkArbitratedSessions", c_bool, 1),
		("", c_ulong, 0),
		("OwningPlayerName", FString),
		("OwningPlayerId", FUniqueNetId),
		("PingInMs", c_int),
		("MatchQuality", c_float),
		("GameState", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BuildUniqueId", c_int),
		("BuildUniqueString", FString),
	]

class  UOnlineGameSettings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USettings", USettings_Data),
		("UOnlineGameSettings", UOnlineGameSettings_Data),
	]


class  UShaderCache_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UShaderCache(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UShaderCache", UShaderCache_Data),
	]


class  UShadowMap1D_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UShadowMap1D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UShadowMap1D", UShadowMap1D_Data),
	]


class  UShadowMap2D_Data(Structure):
	_fields_ = [
		("Texture", POINTER(UShadowMapTexture2D)),
		("CoordinateScale", FVector2D),
		("CoordinateBias", FVector2D),
		("LightGuid", FGuid),
		("bIsShadowFactorTexture", c_bool, 1),
		("", c_ulong, 0),
		("Component", POINTER(UInstancedStaticMeshComponent)),
		("InstanceIndex", c_int),
	]

class  UShadowMap2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UShadowMap2D", UShadowMap2D_Data),
	]


class  USmokeTestCommandlet_Data(Structure):
	_fields_ = []

class  USmokeTestCommandlet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCommandlet", UCommandlet_Data),
		("USmokeTestCommandlet", USmokeTestCommandlet_Data),
	]


class  USnapshotInterface_Data(Structure):
	_fields_ = [
		("bEnableInMultiplayer", c_bool, 1),
		("bTracked", c_bool, 1),
		("", c_ulong, 0),
	]

class  USnapshotInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USnapshotInterface", USnapshotInterface_Data),
	]


class  USpeechRecognition_Data(Structure):
	_fields_ = [
		("Language", FString),
		("ConfidenceThreshhold", c_float),
		("Vocabularies", TArray_FRecogVocabulary),
		("VoiceData", TArray_unsigned_char),
		("WorkingVoiceData", TArray_unsigned_char),
		("UserData", TArray_unsigned_char),
		("InstanceData", FRecogUserData * 4),
		("bDirty", c_bool, 1),
		("bInitialised", c_bool, 1),
		("", c_ulong, 0),
		("FnxVoiceData", FPointer),
	]

class  USpeechRecognition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USpeechRecognition", USpeechRecognition_Data),
	]


class  UStaticMesh_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("LODInfo", TArray_FStaticMeshLODInfo),
		("LODDistanceRatio", c_float),
		("LODMaxRange", c_float),
		("LightMapResolution", c_int),
		("LightMapCoordinateIndex", c_int),
		("Unknown2", c_ubyte, 0x),
		("BodySetup", POINTER(URB_BodySetup)),
		("Unknown3", c_ubyte, 0x),
		("UseSimpleLineCollision", BOOL),
		("UseSimpleBoxCollision", BOOL),
		("UseSimpleRigidBodyCollision", BOOL),
		("ForceComplexRigidBodyCollisionPhysX", BOOL),
		("UseFullPrecisionUVs", BOOL),
		("bUsedForInstancing", c_bool, 1),
		("", c_ulong, 0),
		("DynamicShadowCastRelevance", c_ubyte),
		("Unknown4", c_ubyte, 0x),
		("bCanBecomeDynamic", c_bool, 1),
		("", c_ulong, 0),
		("StreamingDistanceMultiplier", c_float),
		("Unknown5", c_ubyte, 0x),
	]

class  UStaticMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UStaticMesh", UStaticMesh_Data),
	]


class  URB_BodySetup_Data(Structure):
	_fields_ = [
		("SleepFamily", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BoneName", FName),
		("bFixed", c_bool, 1),
		("bNoCollision", c_bool, 1),
		("bBlockZeroExtent", c_bool, 1),
		("bBlockNonZeroExtent", c_bool, 1),
		("bEnableContinuousCollisionDetection", c_bool, 1),
		("bAlwaysFullAnimWeight", c_bool, 1),
		("bConsiderForBounds", c_bool, 1),
		("", c_ulong, 0),
		("PhysMaterial", POINTER(UPhysicalMaterial)),
		("MassScale", c_float),
		("CollisionGeom", TArray_FPointer),
		("CollisionGeomScale3D", TArray_FVector),
		("PreCachedPhysScale", TArray_FVector),
		("PreCachedPhysData", TArray_FKCachedConvexData),
		("PreCachedPhysDataVersion", c_int),
	]

class  URB_BodySetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UKMeshProps", UKMeshProps_Data),
		("URB_BodySetup", URB_BodySetup_Data),
	]


class  UTexture_Data(Structure):
	_fields_ = [
		("SRGB", c_bool, 1),
		("RGBE", c_bool, 1),
		("bIsSourceArtUncompressed", c_bool, 1),
		("CompressionNoAlpha", c_bool, 1),
		("CompressionNone", c_bool, 1),
		("CompressionNoMipmaps", c_bool, 1),
		("CompressionFullDynamicRange", c_bool, 1),
		("DeferCompression", c_bool, 1),
		("NeverStream", c_bool, 1),
		("bDitherMipMapAlpha", c_bool, 1),
		("bPreserveBorderR", c_bool, 1),
		("bPreserveBorderG", c_bool, 1),
		("bPreserveBorderB", c_bool, 1),
		("bPreserveBorderA", c_bool, 1),
		("bNoTiling", c_bool, 1),
		("bForcePVRTC4", c_bool, 1),
		("bAsyncResourceReleaseHasBeenStarted", c_bool, 1),
		("bUseCinematicMipLevels", c_bool, 1),
		("", c_ulong, 0),
		("CompressionSettings", c_ubyte),
		("Filter", c_ubyte),
		("LODGroup", c_ubyte),
		("MipGenSettings", c_ubyte),
		("LODBias", c_int),
		("CachedCombinedLODBias", c_int),
		("NumCinematicMipLevels", c_int),
		("Resource", FPointer),
		("InternalFormatLODBias", c_int),
	]

class  UTexture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
	]


class  UTexture2D_Data(Structure):
	_fields_ = [
		("Mips", FIndirectArray_Mirror),
		("SizeX", c_int),
		("SizeY", c_int),
		("OriginalSizeX", c_int),
		("OriginalSizeY", c_int),
		("Format", c_ubyte),
		("AddressX", c_ubyte),
		("AddressY", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bIsStreamable", c_bool, 1),
		("bHasCancelationPending", c_bool, 1),
		("bHasBeenLoadedFromPersistentArchive", c_bool, 1),
		("bForceMiplevelsToBeResident", c_bool, 1),
		("bGlobalForceMipLevelsToBeResident", c_bool, 1),
		("bIsCompositingSource", c_bool, 1),
		("bGoreTexture", c_bool, 1),
		("", c_ulong, 0),
		("ForceMipLevelsToBeResidentTimestamp", c_float),
		("TextureFileCacheName", FName),
		("RequestedMips", c_int),
		("ResidentMips", c_int),
		("PendingMipChangeRequestStatus", FThreadSafeCounter),
		("SystemMemoryData", TArray_unsigned_char),
		("StreamableTexturesLink", FTextureLinkedListMirror),
		("StreamingIndex", c_int),
		("MipTailBaseIdx", c_int),
		("ResourceMem", FPointer),
		("FirstResourceMemMip", c_int),
		("Timer", c_float),
	]

class  UTexture2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2D", UTexture2D_Data),
	]


class  ULightMapTexture2D_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  ULightMapTexture2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2D", UTexture2D_Data),
		("ULightMapTexture2D", ULightMapTexture2D_Data),
	]


class  UShadowMapTexture2D_Data(Structure):
	_fields_ = [
		("ShadowmapFlags", c_int),
	]

class  UShadowMapTexture2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2D", UTexture2D_Data),
		("UShadowMapTexture2D", UShadowMapTexture2D_Data),
	]


class  UTranslationContext_Data(Structure):
	_fields_ = [
		("TranslatorTags", TArray_UTranslatorTagPtr),
	]

class  UTranslationContext(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UTranslationContext", UTranslationContext_Data),
	]


class  UTranslatorTag_Data(Structure):
	_fields_ = [
		("Tag", FName),
	]

class  UTranslatorTag(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UTranslatorTag", UTranslatorTag_Data),
	]


class  UStringsTag_Data(Structure):
	_fields_ = []

class  UStringsTag(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UTranslatorTag", UTranslatorTag_Data),
		("UStringsTag", UStringsTag_Data),
	]


class  UUIRoot_Data(Structure):
	_fields_ = [
		("BadCapsLocContexts", TArray_FString),
	]

class  UUIRoot(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
	]


class  UInteraction_Data(Structure):
	_fields_ = [
		("__OnReceivedNativeInputKey__Delegate", FScriptDelegate),
		("__OnReceivedNativeInputAxis__Delegate", FScriptDelegate),
		("__OnReceivedNativeInputChar__Delegate", FScriptDelegate),
		("__OnInitialize__Delegate", FScriptDelegate),
	]

class  UInteraction(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
	]


class  UUIInteraction_Data(Structure):
	_fields_ = [
		("VfTable_FExec", FPointer),
		("VfTable_FGlobalDataStoreClientManager", FPointer),
		("VfTable_FCallbackEventDevice", FPointer),
		("UIManager", POINTER(UUIManager)),
		("UIManagerClass", POINTER(UClass)),
		("SceneClientClass", POINTER(UClass)),
		("SceneClient", POINTER(UGameUISceneClient)),
		("SupportedDoubleClickKeys", TArray_FName),
		("DataStoreManager", POINTER(UDataStoreClient)),
		("bProcessInput", int * 4),
		("UIJoystickDeadZone", c_float),
		("UIAxisMultiplier", c_float),
		("AxisRepeatDelay", c_float),
		("MouseButtonRepeatDelay", c_float),
		("DoubleClickTriggerSeconds", c_float),
		("DoubleClickPixelTolerance", c_int),
		("MouseButtonRepeatInfo", FUIKeyRepeatData),
		("ConfiguredAxisEmulationDefinitions", TArray_FUIAxisEmulationDefinition),
		("Unknown1", c_ubyte, 0x),
		("AxisInputEmulation", FUIAxisEmulationData * 4),
	]

class  UUIInteraction(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
		("UUIInteraction", UUIInteraction_Data),
	]


class  UUIManager_Data(Structure):
	_fields_ = []

class  UUIManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIManager", UUIManager_Data),
	]


class  UVertex_Data(Structure):
	_fields_ = [
		("ParentLine", POINTER(ULine)),
		("Position", FVector),
		("Material", POINTER(UMaterial)),
		("Material_Selected", POINTER(UMaterial)),
		("bIsSelected", c_bool, 1),
		("", c_ulong, 0),
		("cColor", FColor),
	]

class  UVertex(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UVertex", UVertex_Data),
	]


class  UWaveFormBase_Data(Structure):
	_fields_ = [
		("TheWaveForm", POINTER(UForceFeedbackWaveform)),
	]

class  UWaveFormBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UWaveFormBase", UWaveFormBase_Data),
	]


class  UWorld_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
	]

class  UWorld(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UWorld", UWorld_Data),
	]


class  AEnvironmentVolume_Data(Structure):
	_fields_ = [
		("VfTable_IInterface_NavMeshPathObstacle", FPointer),
		("VfTable_IInterface_NavMeshPathObject", FPointer),
		("bSplitNavMesh", c_bool, 1),
		("", c_ulong, 0),
	]

class  AEnvironmentVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AEnvironmentVolume", AEnvironmentVolume_Data),
	]


class  ATestSplittingVolume_Data(Structure):
	_fields_ = [
		("VfTable_IInterface_NavMeshPathObject", FPointer),
	]

class  ATestSplittingVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ATestSplittingVolume", ATestSplittingVolume_Data),
	]


class  AAIController_Data(Structure):
	_fields_ = [
		("bAdjustFromWalls", c_bool, 1),
		("bReverseScriptedRoute", c_bool, 1),
		("", c_ulong, 0),
		("Skill", c_float),
		("ScriptedMoveTarget", POINTER(AActor)),
		("ScriptedRoute", POINTER(ARoute)),
		("ScriptedRouteIndex", c_int),
		("ScriptedFocus", POINTER(AActor)),
	]

class  AAIController(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AController", AController_Data),
		("AAIController", AAIController_Data),
	]


class  APathTargetPoint_Data(Structure):
	_fields_ = []

class  APathTargetPoint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AKeypoint", AKeypoint_Data),
		("APathTargetPoint", APathTargetPoint_Data),
	]


class  ANavMeshObstacle_Data(Structure):
	_fields_ = [
		("VfTable_IInterface_NavMeshPathObstacle", FPointer),
		("bEnabled", c_bool, 1),
		("bPreserveInternalGeo", c_bool, 1),
		("", c_ulong, 0),
	]

class  ANavMeshObstacle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavMeshObstacle", ANavMeshObstacle_Data),
	]


class  APylonSeed_Data(Structure):
	_fields_ = [
		("VfTable_IInterface_NavMeshPathObject", FPointer),
		("VfTable_IIGBXNavMeshSeed", FPointer),
	]

class  APylonSeed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APylonSeed", APylonSeed_Data),
	]


class  ABlockingMeshActor_Data(Structure):
	_fields_ = [
		("VfTable_IIGBXNavMeshObstacle", FPointer),
		("BlockingMeshComponent", POINTER(UBlockingMeshComponent)),
		("BlockingMeshMaterial", POINTER(UMaterialInterface)),
		("bBlockNavMesh", c_bool, 1),
		("", c_ulong, 0),
		("MatInstantConstant", POINTER(UMaterialInstanceConstant)),
		("MatInstantConstantNew", POINTER(UMaterialInstanceConstant)),
	]

class  ABlockingMeshActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
		("ABlockingMeshActor", ABlockingMeshActor_Data),
	]


class  ABlockingMeshReplicatedActor_Data(Structure):
	_fields_ = [
		("bIsEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  ABlockingMeshReplicatedActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
		("ABlockingMeshActor", ABlockingMeshActor_Data),
		("ABlockingMeshReplicatedActor", ABlockingMeshReplicatedActor_Data),
	]


class  UCoverGroupRenderingComponent_Data(Structure):
	_fields_ = []

class  UCoverGroupRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UCoverGroupRenderingComponent", UCoverGroupRenderingComponent_Data),
	]


class  UMeshComponent_Data(Structure):
	_fields_ = [
		("Materials", TArray_UMaterialInterfacePtr),
	]

class  UMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
	]


class  UStaticMeshComponent_Data(Structure):
	_fields_ = [
		("StaticMesh", POINTER(UStaticMesh)),
		("OverriddenLODMaxRange", c_float),
		("StreamingDistanceMultiplier", c_float),
		("bUseSubDivisions", c_bool, 1),
		("bForceStaticDecals", c_bool, 1),
		("bCanHighlightSelectedSections", c_bool, 1),
		("bNeverBecomeDynamic", c_bool, 1),
		("bIgnoreInstanceForTextureStreaming", c_bool, 1),
		("bOverrideLightMapRes", c_bool, 1),
		("bIgnoredByFXCoordinator", c_bool, 1),
		("BlockRigidBodyPhysX", c_bool, 1),
		("", c_ulong, 0),
		("IrrelevantLights", TArray_FGuid),
		("LODData", TArray_FStaticMeshComponentLODInfo),
		("ViewZeroOffset", c_ubyte),
		("ViewOneOffset", c_ubyte),
		("ForcedLodModel", c_ubyte),
		("PreviousLODLevel", c_ubyte),
	]

class  UStaticMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UStaticMeshComponent", UStaticMeshComponent_Data),
	]


class  UCoverMeshComponent_Data(Structure):
	_fields_ = [
		("Meshes", TArray_FCoverMeshes),
		("LocationOffset", FVector),
		("AutoAdjustOn", POINTER(UStaticMesh)),
		("AutoAdjustOff", POINTER(UStaticMesh)),
		("Disabled", POINTER(UStaticMesh)),
		("bShowWhenNotSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UCoverMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UStaticMeshComponent", UStaticMeshComponent_Data),
		("UCoverMeshComponent", UCoverMeshComponent_Data),
	]


class  UNavMeshRenderingComponent_Data(Structure):
	_fields_ = []

class  UNavMeshRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UNavMeshRenderingComponent", UNavMeshRenderingComponent_Data),
	]


class  UPathRenderingComponent_Data(Structure):
	_fields_ = []

class  UPathRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UPathRenderingComponent", UPathRenderingComponent_Data),
	]


class  URouteRenderingComponent_Data(Structure):
	_fields_ = []

class  URouteRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("URouteRenderingComponent", URouteRenderingComponent_Data),
	]


class  UAutoNavMeshPathObstacleUnregister_Data(Structure):
	_fields_ = [
		("PathObstacleRef", FScriptInterface),
	]

class  UAutoNavMeshPathObstacleUnregister(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAutoNavMeshPathObstacleUnregister", UAutoNavMeshPathObstacleUnregister_Data),
	]


class  UGBXNavMeshPathFinder_Data(Structure):
	_fields_ = [
		("PathModifiers", TArray_UGBXNavMeshPathModifierPtr),
	]

class  UGBXNavMeshPathFinder(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXNavMeshPathFinder", UGBXNavMeshPathFinder_Data),
	]


class  UIGBXNavMeshObstacle_Data(Structure):
	_fields_ = []

class  UIGBXNavMeshObstacle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIGBXNavMeshObstacle", UIGBXNavMeshObstacle_Data),
	]


class  UInterface_NavMeshPathObject_Data(Structure):
	_fields_ = []

class  UInterface_NavMeshPathObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UInterface_NavMeshPathObject", UInterface_NavMeshPathObject_Data),
	]


class  UInterface_NavMeshPathSwitch_Data(Structure):
	_fields_ = []

class  UInterface_NavMeshPathSwitch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UInterface_NavMeshPathObject", UInterface_NavMeshPathObject_Data),
		("UInterface_NavMeshPathSwitch", UInterface_NavMeshPathSwitch_Data),
	]


class  UInterface_NavMeshPathObstacle_Data(Structure):
	_fields_ = []

class  UInterface_NavMeshPathObstacle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UInterface_NavMeshPathObstacle", UInterface_NavMeshPathObstacle_Data),
	]


class  UNavigationHandle_Data(Structure):
	_fields_ = [
		("AnchorPylon", POINTER(APylon)),
		("AnchorPoly", FPointer),
		("PathCache", FPathStore),
		("BestUnfinishedPathPoint", FPointer),
		("CurrentEdge", FPointer),
		("SubGoal_DestPoly", FPointer),
		("FinalDestination", FBasedPosition),
		("bSkipRouteCacheUpdates", c_bool, 1),
		("bUseORforEvaluateGoal", c_bool, 1),
		("bDebugConstraintsAndGoalEvals", c_bool, 1),
		("bUltraVerbosePathDebugging", c_bool, 1),
		("bDebug_Breadcrumbs", c_bool, 1),
		("", c_ulong, 0),
		("PathConstraintList", POINTER(UNavMeshPathConstraint)),
		("PathGoalList", POINTER(UNavMeshPathGoalEvaluator)),
		("CachedPathParams", FNavMeshPathParams),
		("LastPathError", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LastPathFailTime", c_float),
		("Breadcrumbs", FVector * 10),
		("BreadCrumbMostRecentIdx", c_int),
		("BreadCrumbDistanceInterval", c_float),
	]

class  UNavigationHandle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavigationHandle", UNavigationHandle_Data),
	]


class  UNavMeshGoal_Filter_Data(Structure):
	_fields_ = [
		("bShowDebug", c_bool, 1),
		("", c_ulong, 0),
		("NumNodesThrownOut", c_int),
		("NumNodesProcessed", c_int),
	]

class  UNavMeshGoal_Filter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshGoal_Filter", UNavMeshGoal_Filter_Data),
	]


class  UNavMeshGoalFilter_MinPathDistance_Data(Structure):
	_fields_ = [
		("MinDistancePathShouldBe", c_int),
	]

class  UNavMeshGoalFilter_MinPathDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshGoal_Filter", UNavMeshGoal_Filter_Data),
		("UNavMeshGoalFilter_MinPathDistance", UNavMeshGoalFilter_MinPathDistance_Data),
	]


class  UNavMeshGoalFilter_NotNearOtherAI_Data(Structure):
	_fields_ = [
		("DistanceToCheck", c_float),
	]

class  UNavMeshGoalFilter_NotNearOtherAI(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshGoal_Filter", UNavMeshGoal_Filter_Data),
		("UNavMeshGoalFilter_NotNearOtherAI", UNavMeshGoalFilter_NotNearOtherAI_Data),
	]


class  UNavMeshGoalFilter_OutOfViewFrom_Data(Structure):
	_fields_ = [
		("GoalPoly", FPointer),
		("OutOfViewLocation", FVector),
	]

class  UNavMeshGoalFilter_OutOfViewFrom(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshGoal_Filter", UNavMeshGoal_Filter_Data),
		("UNavMeshGoalFilter_OutOfViewFrom", UNavMeshGoalFilter_OutOfViewFrom_Data),
	]


class  UNavMeshGoalFilter_OutSideOfDotProductWedge_Data(Structure):
	_fields_ = [
		("Location", FVector),
		("Rotation", FVector),
		("Epsilon", c_float),
	]

class  UNavMeshGoalFilter_OutSideOfDotProductWedge(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshGoal_Filter", UNavMeshGoal_Filter_Data),
		("UNavMeshGoalFilter_OutSideOfDotProductWedge", UNavMeshGoalFilter_OutSideOfDotProductWedge_Data),
	]


class  UNavMeshGoalFilter_PolyEncompassesAI_Data(Structure):
	_fields_ = [
		("OverrideExtentToCheck", FVector),
	]

class  UNavMeshGoalFilter_PolyEncompassesAI(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshGoal_Filter", UNavMeshGoal_Filter_Data),
		("UNavMeshGoalFilter_PolyEncompassesAI", UNavMeshGoalFilter_PolyEncompassesAI_Data),
	]


class  UNavMeshPathConstraint_Data(Structure):
	_fields_ = [
		("NextConstraint", POINTER(UNavMeshPathConstraint)),
		("NumNodesProcessed", c_int),
		("NumThrownOutNodes", c_int),
		("AddedDirectCost", c_float),
		("AddedHeuristicCost", c_float),
	]

class  UNavMeshPathConstraint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
	]


class  UNavMeshPath_AlongLine_Data(Structure):
	_fields_ = [
		("Direction", FVector),
	]

class  UNavMeshPath_AlongLine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_AlongLine", UNavMeshPath_AlongLine_Data),
	]


class  UNavMeshPath_EnforceTwoWayEdges_Data(Structure):
	_fields_ = []

class  UNavMeshPath_EnforceTwoWayEdges(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_EnforceTwoWayEdges", UNavMeshPath_EnforceTwoWayEdges_Data),
	]


class  UNavMeshPath_MinDistBetweenSpecsOfType_Data(Structure):
	_fields_ = [
		("MinDistBetweenEdgeTypes", c_float),
		("InitLocation", FVector),
		("EdgeType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Penalty", c_float),
	]

class  UNavMeshPath_MinDistBetweenSpecsOfType(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_MinDistBetweenSpecsOfType", UNavMeshPath_MinDistBetweenSpecsOfType_Data),
	]


class  UNavMeshPath_SameCoverLink_Data(Structure):
	_fields_ = [
		("TestLink", POINTER(ACoverLink)),
	]

class  UNavMeshPath_SameCoverLink(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_SameCoverLink", UNavMeshPath_SameCoverLink_Data),
	]


class  UNavMeshPath_Toward_Data(Structure):
	_fields_ = [
		("GoalActor", POINTER(AActor)),
		("GoalPoint", FVector),
	]

class  UNavMeshPath_Toward(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_Toward", UNavMeshPath_Toward_Data),
	]


class  UNavMeshPath_WithinDistanceEnvelope_Data(Structure):
	_fields_ = [
		("MaxDistance", c_float),
		("MinDistance", c_float),
		("bSoft", c_bool, 1),
		("bOnlyThrowOutNodesThatLeaveEnvelope", c_bool, 1),
		("", c_ulong, 0),
		("SoftStartPenalty", c_float),
		("EnvelopeTestPoint", FVector),
	]

class  UNavMeshPath_WithinDistanceEnvelope(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_WithinDistanceEnvelope", UNavMeshPath_WithinDistanceEnvelope_Data),
	]


class  UNavMeshPath_WithinTraversalDist_Data(Structure):
	_fields_ = [
		("MaxTraversalDist", c_float),
		("bSoft", c_bool, 1),
		("", c_ulong, 0),
		("SoftStartPenalty", c_float),
	]

class  UNavMeshPath_WithinTraversalDist(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathConstraint", UNavMeshPathConstraint_Data),
		("UNavMeshPath_WithinTraversalDist", UNavMeshPath_WithinTraversalDist_Data),
	]


class  UNavMeshPathGoalEvaluator_Data(Structure):
	_fields_ = [
		("NextEvaluator", POINTER(UNavMeshPathGoalEvaluator)),
		("MaxPathVisits", c_int),
		("bAlwaysCallEvaluateGoal", c_bool, 1),
		("", c_ulong, 0),
		("NumNodesThrownOut", c_int),
		("NumNodesProcessed", c_int),
	]

class  UNavMeshPathGoalEvaluator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
	]


class  UNavMeshGoal_At_Data(Structure):
	_fields_ = [
		("Goal", FVector),
		("GoalDist", c_float),
		("bKeepPartial", c_bool, 1),
		("bWeightPartialByDist", c_bool, 1),
		("bGoalInSamePolyAsAnchor", c_bool, 1),
		("", c_ulong, 0),
		("PartialDistSq", c_float),
		("GoalPoly", FPointer),
		("PartialGoal", FPointer),
	]

class  UNavMeshGoal_At(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_At", UNavMeshGoal_At_Data),
	]


class  UNavMeshGoal_ClosestActorInList_Data(Structure):
	_fields_ = [
		("GoalList", TArray_FBiasedGoalActor),
		("PolyToGoalActorMap", FMultiMap_Mirror),
		("CachedAnchorPoly", FPointer),
	]

class  UNavMeshGoal_ClosestActorInList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_ClosestActorInList", UNavMeshGoal_ClosestActorInList_Data),
	]


class  UNavMeshGoal_GenericFilterContainer_Data(Structure):
	_fields_ = [
		("GoalFilters", TArray_UNavMeshGoal_FilterPtr),
		("SuccessfulGoal", FPointer),
		("MyNavigationHandle", POINTER(UNavigationHandle)),
	]

class  UNavMeshGoal_GenericFilterContainer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_GenericFilterContainer", UNavMeshGoal_GenericFilterContainer_Data),
	]


class  UNavMeshGoal_Null_Data(Structure):
	_fields_ = [
		("PartialGoal", FPointer),
	]

class  UNavMeshGoal_Null(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_Null", UNavMeshGoal_Null_Data),
	]


class  UNavMeshGoal_PolyEncompassesAI_Data(Structure):
	_fields_ = [
		("OverrideExtentToCheck", FVector),
	]

class  UNavMeshGoal_PolyEncompassesAI(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_PolyEncompassesAI", UNavMeshGoal_PolyEncompassesAI_Data),
	]


class  UNavMeshGoal_Random_Data(Structure):
	_fields_ = [
		("MinDist", c_int),
		("BestRating", c_float),
		("PartialGoal", FPointer),
	]

class  UNavMeshGoal_Random(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_Random", UNavMeshGoal_Random_Data),
	]


class  UNavMeshGoal_WithinDistanceEnvelope_Data(Structure):
	_fields_ = [
		("MaxDistance", c_float),
		("MinDistance", c_float),
		("MinTraversalDist", c_float),
		("EnvelopeTestPoint", FVector),
	]

class  UNavMeshGoal_WithinDistanceEnvelope(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UNavMeshPathGoalEvaluator", UNavMeshPathGoalEvaluator_Data),
		("UNavMeshGoal_WithinDistanceEnvelope", UNavMeshGoal_WithinDistanceEnvelope_Data),
	]


class  UPathConstraint_Data(Structure):
	_fields_ = [
		("CacheIdx", c_int),
		("NextConstraint", POINTER(UPathConstraint)),
	]

class  UPathConstraint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
	]


class  UPath_AlongLine_Data(Structure):
	_fields_ = [
		("Direction", FVector),
	]

class  UPath_AlongLine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_AlongLine", UPath_AlongLine_Data),
	]


class  UPath_AvoidInEscapableNodes_Data(Structure):
	_fields_ = [
		("Radius", c_int),
		("Height", c_int),
		("MaxFallSpeed", c_int),
		("MoveFlags", c_int),
	]

class  UPath_AvoidInEscapableNodes(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_AvoidInEscapableNodes", UPath_AvoidInEscapableNodes_Data),
	]


class  UPath_MinDistBetweenSpecsOfType_Data(Structure):
	_fields_ = [
		("MinDistBetweenSpecTypes", c_float),
		("InitLocation", FVector),
		("ReachSpecClass", POINTER(UClass)),
	]

class  UPath_MinDistBetweenSpecsOfType(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_MinDistBetweenSpecsOfType", UPath_MinDistBetweenSpecsOfType_Data),
	]


class  UPath_TowardGoal_Data(Structure):
	_fields_ = [
		("GoalActor", POINTER(AActor)),
	]

class  UPath_TowardGoal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_TowardGoal", UPath_TowardGoal_Data),
	]


class  UPath_TowardPoint_Data(Structure):
	_fields_ = [
		("GoalPoint", FVector),
	]

class  UPath_TowardPoint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_TowardPoint", UPath_TowardPoint_Data),
	]


class  UPath_WithinDistanceEnvelope_Data(Structure):
	_fields_ = [
		("MaxDistance", c_float),
		("MinDistance", c_float),
		("bSoft", c_bool, 1),
		("bOnlyThrowOutNodesThatLeaveEnvelope", c_bool, 1),
		("", c_ulong, 0),
		("SoftStartPenalty", c_float),
		("EnvelopeTestPoint", FVector),
	]

class  UPath_WithinDistanceEnvelope(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_WithinDistanceEnvelope", UPath_WithinDistanceEnvelope_Data),
	]


class  UPath_WithinTraversalDist_Data(Structure):
	_fields_ = [
		("MaxTraversalDist", c_float),
		("bSoft", c_bool, 1),
		("", c_ulong, 0),
		("SoftStartPenalty", c_float),
	]

class  UPath_WithinTraversalDist(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathConstraint", UPathConstraint_Data),
		("UPath_WithinTraversalDist", UPath_WithinTraversalDist_Data),
	]


class  UPathGoalEvaluator_Data(Structure):
	_fields_ = [
		("NextEvaluator", POINTER(UPathGoalEvaluator)),
		("GeneratedGoal", POINTER(ANavigationPoint)),
		("MaxPathVisits", c_int),
		("CacheIdx", c_int),
	]

class  UPathGoalEvaluator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathGoalEvaluator", UPathGoalEvaluator_Data),
	]


class  UGoal_AtActor_Data(Structure):
	_fields_ = [
		("GoalActor", POINTER(AActor)),
		("GoalDist", c_float),
		("bKeepPartial", c_bool, 1),
		("", c_ulong, 0),
	]

class  UGoal_AtActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathGoalEvaluator", UPathGoalEvaluator_Data),
		("UGoal_AtActor", UGoal_AtActor_Data),
	]


class  UGoal_Null_Data(Structure):
	_fields_ = []

class  UGoal_Null(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPathGoalEvaluator", UPathGoalEvaluator_Data),
		("UGoal_Null", UGoal_Null_Data),
	]


class  ASkeletalMeshActor_Data(Structure):
	_fields_ = [
		("VfTable_IIFaceFXActor", FPointer),
		("bDamageAppliesImpulse", c_bool, 1),
		("bShouldDoAnimNotifies", c_bool, 1),
		("FaceFXSpeechPending", c_bool, 1),
		("bForceSaveInCheckpoint", c_bool, 1),
		("bCollideActors_OldValue", c_bool, 1),
		("bShouldShadowParentAllAttachedActors", c_bool, 1),
		("", c_ulong, 0),
		("SkeletalMeshComponent", POINTER(USkeletalMeshComponent)),
		("LightEnvironment", POINTER(ULightEnvironmentComponent)),
		("FacialAudioComp", POINTER(UAudioComponent)),
		("ReplicatedMesh", POINTER(USkeletalMesh)),
		("ReplicatedMaterial0", POINTER(UMaterialInterface)),
		("ReplicatedMaterial1", POINTER(UMaterialInterface)),
		("ControlTargets", TArray_FSkelMeshActorControlTarget),
		("InterpGroupList", TArray_UInterpGroupPtr),
		("SavedAnimSeqName", FName),
		("SavedCurrentTime", c_float),
	]

class  ASkeletalMeshActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
	]


class  ASkeletalMeshActorBasedOnExtremeContent_Data(Structure):
	_fields_ = [
		("ExtremeContent", TArray_FSkelMaterialSetterDatum),
		("NonExtremeContent", TArray_FSkelMaterialSetterDatum),
	]

class  ASkeletalMeshActorBasedOnExtremeContent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
		("ASkeletalMeshActorBasedOnExtremeContent", ASkeletalMeshActorBasedOnExtremeContent_Data),
	]


class  ASkeletalMeshActorSpawnable_Data(Structure):
	_fields_ = []

class  ASkeletalMeshActorSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
		("ASkeletalMeshActorSpawnable", ASkeletalMeshActorSpawnable_Data),
	]


class  ASkeletalMeshCinematicActor_Data(Structure):
	_fields_ = []

class  ASkeletalMeshCinematicActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
		("ASkeletalMeshCinematicActor", ASkeletalMeshCinematicActor_Data),
	]


class  ASkeletalMeshActorMAT_Data(Structure):
	_fields_ = [
		("SlotNodes", TArray_UAnimNodeSlotPtr),
	]

class  ASkeletalMeshActorMAT(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
		("ASkeletalMeshCinematicActor", ASkeletalMeshCinematicActor_Data),
		("ASkeletalMeshActorMAT", ASkeletalMeshActorMAT_Data),
	]


class  UHeadTrackingComponent_Data(Structure):
	_fields_ = [
		("TrackControllerName", TArray_FName),
		("LookAtActorRadius", c_float),
		("bDisableBeyondLimit", c_bool, 1),
		("", c_ulong, 0),
		("MaxLookAtTime", c_float),
		("MinLookAtTime", c_float),
		("MaxInterestTime", c_float),
		("ActorClassesToLookAt", TArray_UClassPtr),
		("TargetBoneNames", TArray_FName),
		("Unknown1", c_ubyte, 0x),
		("SkeletalMeshComp", POINTER(USkeletalMeshComponent)),
		("TrackControls", TArray_USkelControlLookAtPtr),
		("RootMeshLocation", FVector),
		("RootMeshRotation", FRotator),
	]

class  UHeadTrackingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UHeadTrackingComponent", UHeadTrackingComponent_Data),
	]


class  UAnimationCompressionAlgorithm_Data(Structure):
	_fields_ = [
		("Description", FString),
		("bNeedsSkeleton", c_bool, 1),
		("", c_ulong, 0),
		("TranslationCompressionChoice", c_ubyte),
		("RotationCompressionChoice", c_ubyte),
	]

class  UAnimationCompressionAlgorithm(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
	]


class  UAnimationCompressionAlgorithm_Automatic_Data(Structure):
	_fields_ = [
		("MaxEndEffectorError", c_float),
		("bTryFixedBitwiseCompression", c_bool, 1),
		("bTryPerTrackBitwiseCompression", c_bool, 1),
		("bTryLinearKeyRemovalCompression", c_bool, 1),
		("bTryIntervalKeyRemoval", c_bool, 1),
		("bRunCurrentDefaultCompressor", c_bool, 1),
		("bAutoReplaceIfExistingErrorTooGreat", c_bool, 1),
		("bRaiseMaxErrorToExisting", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimationCompressionAlgorithm_Automatic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_Automatic", UAnimationCompressionAlgorithm_Automatic_Data),
	]


class  UAnimationCompressionAlgorithm_BitwiseCompressOnly_Data(Structure):
	_fields_ = []

class  UAnimationCompressionAlgorithm_BitwiseCompressOnly(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_BitwiseCompressOnly", UAnimationCompressionAlgorithm_BitwiseCompressOnly_Data),
	]


class  UAnimationCompressionAlgorithm_GBXCustom_Data(Structure):
	_fields_ = [
		("MinKeys", c_int),
		("bStartAtSecondKey", c_bool, 1),
		("bKeepLastKey", c_bool, 1),
		("", c_ulong, 0),
		("MaxPosDiff", c_float),
		("MaxAngleDiff", c_float),
	]

class  UAnimationCompressionAlgorithm_GBXCustom(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_GBXCustom", UAnimationCompressionAlgorithm_GBXCustom_Data),
	]


class  UAnimationCompressionAlgorithm_LeastDestructive_Data(Structure):
	_fields_ = []

class  UAnimationCompressionAlgorithm_LeastDestructive(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_LeastDestructive", UAnimationCompressionAlgorithm_LeastDestructive_Data),
	]


class  UAnimationCompressionAlgorithm_RemoveEverySecondKey_Data(Structure):
	_fields_ = [
		("MinKeys", c_int),
		("bStartAtSecondKey", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimationCompressionAlgorithm_RemoveEverySecondKey(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_RemoveEverySecondKey", UAnimationCompressionAlgorithm_RemoveEverySecondKey_Data),
	]


class  UAnimationCompressionAlgorithm_RemoveLinearKeys_Data(Structure):
	_fields_ = [
		("MaxPosDiff", c_float),
		("MaxAngleDiff", c_float),
		("MaxEffectorDiff", c_float),
		("MinEffectorDiff", c_float),
		("EffectorDiffSocket", c_float),
		("ParentKeyScale", c_float),
		("bRetarget", c_bool, 1),
		("bActuallyFilterLinearKeys", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimationCompressionAlgorithm_RemoveLinearKeys(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_RemoveLinearKeys", UAnimationCompressionAlgorithm_RemoveLinearKeys_Data),
	]


class  UAnimationCompressionAlgorithm_PerTrackCompression_Data(Structure):
	_fields_ = [
		("MaxZeroingThreshold", c_float),
		("MaxPosDiffBitwise", c_float),
		("MaxAngleDiffBitwise", c_float),
		("AllowedRotationFormats", TArray_unsigned_char),
		("AllowedTranslationFormats", TArray_unsigned_char),
		("bResampleAnimation", c_bool, 1),
		("bUseAdaptiveError", c_bool, 1),
		("bUseOverrideForEndEffectors", c_bool, 1),
		("bUseAdaptiveError2", c_bool, 1),
		("", c_ulong, 0),
		("ResampledFramerate", c_float),
		("MinKeysForResampling", c_int),
		("TrackHeightBias", c_int),
		("ParentingDivisor", c_float),
		("ParentingDivisorExponent", c_float),
		("RotationErrorSourceRatio", c_float),
		("TranslationErrorSourceRatio", c_float),
		("MaxErrorPerTrackRatio", c_float),
		("PerturbationProbeSize", c_float),
		("PerReductionCachedData", FPointer),
	]

class  UAnimationCompressionAlgorithm_PerTrackCompression(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_RemoveLinearKeys", UAnimationCompressionAlgorithm_RemoveLinearKeys_Data),
		("UAnimationCompressionAlgorithm_PerTrackCompression", UAnimationCompressionAlgorithm_PerTrackCompression_Data),
	]


class  UAnimationCompressionAlgorithm_RemoveTrivialKeys_Data(Structure):
	_fields_ = [
		("MaxPosDiff", c_float),
		("MaxAngleDiff", c_float),
	]

class  UAnimationCompressionAlgorithm_RemoveTrivialKeys(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_RemoveTrivialKeys", UAnimationCompressionAlgorithm_RemoveTrivialKeys_Data),
	]


class  UAnimationCompressionAlgorithm_RevertToRaw_Data(Structure):
	_fields_ = []

class  UAnimationCompressionAlgorithm_RevertToRaw(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimationCompressionAlgorithm", UAnimationCompressionAlgorithm_Data),
		("UAnimationCompressionAlgorithm_RevertToRaw", UAnimationCompressionAlgorithm_RevertToRaw_Data),
	]


class  UAnimMetaData_Data(Structure):
	_fields_ = []

class  UAnimMetaData(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimMetaData", UAnimMetaData_Data),
	]


class  UAnimMetaData_SkelControl_Data(Structure):
	_fields_ = [
		("SkelControlNameList", TArray_FName),
		("bFullControlOverController", c_bool, 1),
		("", c_ulong, 0),
		("SkelControlName", FName),
	]

class  UAnimMetaData_SkelControl(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimMetaData", UAnimMetaData_Data),
		("UAnimMetaData_SkelControl", UAnimMetaData_SkelControl_Data),
	]


class  UAnimMetaData_SkelControlKeyFrame_Data(Structure):
	_fields_ = [
		("KeyFrames", TArray_FTimeModifier),
	]

class  UAnimMetaData_SkelControlKeyFrame(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimMetaData", UAnimMetaData_Data),
		("UAnimMetaData_SkelControl", UAnimMetaData_SkelControl_Data),
		("UAnimMetaData_SkelControlKeyFrame", UAnimMetaData_SkelControlKeyFrame_Data),
	]


class  UAnimNotify_Data(Structure):
	_fields_ = []

class  UAnimNotify(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
	]


class  UAnimNotify_AkEvent_Data(Structure):
	_fields_ = [
		("AkEvent", POINTER(UAkEvent)),
		("bFollowActor", c_bool, 1),
		("", c_ulong, 0),
		("BoneName", FName),
	]

class  UAnimNotify_AkEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_AkEvent", UAnimNotify_AkEvent_Data),
	]


class  UAnimNotify_CameraEffect_Data(Structure):
	_fields_ = [
		("CameraLensEffect", POINTER(UClass)),
	]

class  UAnimNotify_CameraEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_CameraEffect", UAnimNotify_CameraEffect_Data),
	]


class  UAnimNotify_ClothingMaxDistanceScale_Data(Structure):
	_fields_ = [
		("StartScale", c_float),
		("EndScale", c_float),
		("ScaleMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Duration", c_float),
	]

class  UAnimNotify_ClothingMaxDistanceScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_ClothingMaxDistanceScale", UAnimNotify_ClothingMaxDistanceScale_Data),
	]


class  UAnimNotify_Footstep_Data(Structure):
	_fields_ = [
		("FootDown", c_int),
		("bFirstPerson", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNotify_Footstep(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Footstep", UAnimNotify_Footstep_Data),
	]


class  UAnimNotify_ForceField_Data(Structure):
	_fields_ = [
		("ForceFieldComponent", POINTER(UNxForceFieldComponent)),
		("bAttach", c_bool, 1),
		("", c_ulong, 0),
		("SocketName", FName),
		("BoneName", FName),
	]

class  UAnimNotify_ForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_ForceField", UAnimNotify_ForceField_Data),
	]


class  UAnimNotify_Kismet_Data(Structure):
	_fields_ = [
		("NotifyName", FName),
	]

class  UAnimNotify_Kismet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Kismet", UAnimNotify_Kismet_Data),
	]


class  UAnimNotify_PlayParticleEffect_Data(Structure):
	_fields_ = [
		("PSTemplate", POINTER(UParticleSystem)),
		("bIsExtremeContent", c_bool, 1),
		("bAttach", c_bool, 1),
		("bPreview", c_bool, 1),
		("bSkipIfOwnerIsHidden", c_bool, 1),
		("bOwnerNoSee", c_bool, 1),
		("bOnlyOwnerSee", c_bool, 1),
		("", c_ulong, 0),
		("PSNonExtremeContentTemplate", POINTER(UParticleSystem)),
		("SocketName", FName),
		("BoneName", FName),
		("BoneSocketModuleActorName", FName),
	]

class  UAnimNotify_PlayParticleEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_PlayParticleEffect", UAnimNotify_PlayParticleEffect_Data),
	]


class  UAnimNotify_Rumble_Data(Structure):
	_fields_ = [
		("PredefinedWaveForm", POINTER(UClass)),
		("WaveForm", POINTER(UForceFeedbackWaveform)),
		("bCheckForBasedPlayer", c_bool, 1),
		("", c_ulong, 0),
		("EffectRadius", c_float),
	]

class  UAnimNotify_Rumble(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Rumble", UAnimNotify_Rumble_Data),
	]


class  UAnimNotify_Script_Data(Structure):
	_fields_ = [
		("NotifyName", FName),
		("NotifyTickName", FName),
		("NotifyEndName", FName),
	]

class  UAnimNotify_Script(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Script", UAnimNotify_Script_Data),
	]


class  UAnimNotify_Scripted_Data(Structure):
	_fields_ = []

class  UAnimNotify_Scripted(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Scripted", UAnimNotify_Scripted_Data),
	]


class  UAnimNotify_PawnMaterialParam_Data(Structure):
	_fields_ = [
		("ScalarParameterInterpArray", TArray_FScalarParameterInterpStruct),
	]

class  UAnimNotify_PawnMaterialParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Scripted", UAnimNotify_Scripted_Data),
		("UAnimNotify_PawnMaterialParam", UAnimNotify_PawnMaterialParam_Data),
	]


class  UAnimNotify_ViewShake_Data(Structure):
	_fields_ = [
		("Duration", c_float),
		("RotAmplitude", FVector),
		("RotFrequency", FVector),
		("LocAmplitude", FVector),
		("LocFrequency", FVector),
		("FOVAmplitude", c_float),
		("FOVFrequency", c_float),
		("bDoControllerVibration", c_bool, 1),
		("bUseBoneLocation", c_bool, 1),
		("", c_ulong, 0),
		("ShakeRadius", c_float),
		("BoneName", FName),
		("ShakeParams", POINTER(UCameraShake)),
	]

class  UAnimNotify_ViewShake(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Scripted", UAnimNotify_Scripted_Data),
		("UAnimNotify_ViewShake", UAnimNotify_ViewShake_Data),
	]


class  UAnimNotify_Sound_Data(Structure):
	_fields_ = [
		("SoundCue", POINTER(USoundCue)),
		("bFollowActor", c_bool, 1),
		("bIgnoreIfActorHidden", c_bool, 1),
		("", c_ulong, 0),
		("BoneName", FName),
		("PercentToPlay", c_float),
		("VolumeMultiplier", c_float),
		("PitchMultiplier", c_float),
	]

class  UAnimNotify_Sound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Sound", UAnimNotify_Sound_Data),
	]


class  UAnimNotify_SoundSpatial_Data(Structure):
	_fields_ = [
		("SoundCueFirstPerson", POINTER(USoundCue)),
		("SoundCueThirdPerson", POINTER(USoundCue)),
		("bFollowActor", c_bool, 1),
		("", c_ulong, 0),
		("BoneName", FName),
	]

class  UAnimNotify_SoundSpatial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_SoundSpatial", UAnimNotify_SoundSpatial_Data),
	]


class  UAnimNotify_Trails_Data(Structure):
	_fields_ = [
		("PSTemplate", POINTER(UParticleSystem)),
		("bIsExtremeContent", c_bool, 1),
		("bPreview", c_bool, 1),
		("bSkipIfOwnerIsHidden", c_bool, 1),
		("bOwnerNoSee", c_bool, 1),
		("bOnlyOwnerSee", c_bool, 1),
		("bResampleRequired", c_bool, 1),
		("", c_ulong, 0),
		("FirstEdgeSocketName", FName),
		("ControlPointSocketName", FName),
		("SecondEdgeSocketName", FName),
		("LastStartTime", c_float),
		("EndTime", c_float),
		("SampleTimeStep", c_float),
		("TrailSampleData", TArray_FTrailSamplePoint),
		("SamplesPerSecond", c_float),
		("TrailSampledData", TArray_FTrailSample),
		("CurrentTime", c_float),
		("TimeStep", c_float),
		("AnimNodeSeq", POINTER(UAnimNodeSequence)),
	]

class  UAnimNotify_Trails(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Trails", UAnimNotify_Trails_Data),
	]


class  UAnimObject_Data(Structure):
	_fields_ = [
		("SkelComponent", POINTER(USkeletalMeshComponent)),
	]

class  UAnimObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
	]


class  UAnimNode_Data(Structure):
	_fields_ = [
		("bRelevant", c_bool, 1),
		("bJustBecameRelevant", c_bool, 1),
		("bTickDuringPausedAnims", c_bool, 1),
		("bEditorOnly", c_bool, 1),
		("bDisableCaching", c_bool, 1),
		("bCallScriptEventOnInit", c_bool, 1),
		("bCallScriptEventOnBecomeRelevant", c_bool, 1),
		("bCallScriptEventOnCeaseRelevant", c_bool, 1),
		("", c_ulong, 0),
		("NodeTickTag", c_int),
		("NodeInitTag", c_int),
		("TickArrayIndex", c_int),
		("NodeCachedAtomsTag", c_int),
		("NodeTotalWeight", c_float),
		("ParentNodes", TArray_UAnimNodeBlendBasePtr),
		("NodeName", FName),
		("CachedBoneAtoms", TArray_FBoneAtom),
		("CachedNumDesiredBones", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CachedRootMotionDelta", FBoneAtom),
		("bCachedHasRootMotion", c_int),
		("CachedCurveKeys", TArray_FCurveKey),
		("SearchTag", c_int),
	]

class  UAnimNode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
	]


class  UAnimNodeBlendBase_Data(Structure):
	_fields_ = [
		("Children", TArray_FAnimBlendChild),
		("bFixNumChildren", c_bool, 1),
		("", c_ulong, 0),
		("BlendType", c_ubyte),
	]

class  UAnimNodeBlendBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
	]


class  UAnimNode_MultiBlendPerBone_Data(Structure):
	_fields_ = [
		("PawnOwner", POINTER(APawn)),
		("MaskList", TArray_FPerBoneMaskInfo),
		("RotationBlendType", c_ubyte),
	]

class  UAnimNode_MultiBlendPerBone(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNode_MultiBlendPerBone", UAnimNode_MultiBlendPerBone_Data),
	]


class  UAnimNodeAimOffset_Data(Structure):
	_fields_ = [
		("Aim", FVector2D),
		("AngleOffset", FVector2D),
		("bForceAimDir", c_bool, 1),
		("bBakeFromAnimations", c_bool, 1),
		("bPassThroughWhenNotRendered", c_bool, 1),
		("bSynchronizeNodesInEditor", c_bool, 1),
		("bBlendInLocalSpace", c_bool, 1),
		("bMoreAccurateAndMoreExpensive", c_bool, 1),
		("", c_ulong, 0),
		("PassThroughAtOrAboveLOD", c_int),
		("ForcedAimDir", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("RequiredBones", TArray_unsigned_char),
		("AimCpntIndexLUT", TArray_unsigned_char),
		("TemplateNode", POINTER(UAnimNodeAimOffset)),
		("Profiles", TArray_FAimOffsetProfile),
		("CurrentProfileIndex", c_int),
	]

class  UAnimNodeAimOffset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeAimOffset", UAnimNodeAimOffset_Data),
	]


class  UAnimNodeBlend_Data(Structure):
	_fields_ = [
		("Child2Weight", c_float),
		("Child2WeightTarget", c_float),
		("BlendTimeToGo", c_float),
		("bSkipBlendWhenNotRendered", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeBlend(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlend", UAnimNodeBlend_Data),
	]


class  UAnimNodeAdditiveBlending_Data(Structure):
	_fields_ = [
		("bPassThroughWhenNotRendered", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeAdditiveBlending(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlend", UAnimNodeBlend_Data),
		("UAnimNodeAdditiveBlending", UAnimNodeAdditiveBlending_Data),
	]


class  UAnimNodeBlendPerBone_Data(Structure):
	_fields_ = [
		("bForceLocalSpaceBlend", c_bool, 1),
		("", c_ulong, 0),
		("BranchStartBoneName", TArray_FName),
		("Child2PerBoneWeight", TArray_float),
		("LocalToCompReqBones", TArray_unsigned_char),
	]

class  UAnimNodeBlendPerBone(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlend", UAnimNodeBlend_Data),
		("UAnimNodeBlendPerBone", UAnimNodeBlendPerBone_Data),
	]


class  UAnimNodeCrossfader_Data(Structure):
	_fields_ = [
		("DefaultAnimSeqName", FName),
		("bDontBlendOutOneShot", c_bool, 1),
		("", c_ulong, 0),
		("PendingBlendOutTimeOneShot", c_float),
	]

class  UAnimNodeCrossfader(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlend", UAnimNodeBlend_Data),
		("UAnimNodeCrossfader", UAnimNodeCrossfader_Data),
	]


class  UAnimNodePlayCustomAnim_Data(Structure):
	_fields_ = [
		("bIsPlayingCustomAnim", c_bool, 1),
		("", c_ulong, 0),
		("CustomPendingBlendOutTime", c_float),
	]

class  UAnimNodePlayCustomAnim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlend", UAnimNodeBlend_Data),
		("UAnimNodePlayCustomAnim", UAnimNodePlayCustomAnim_Data),
	]


class  UAnimNodeBlendDirectional_Data(Structure):
	_fields_ = [
		("DirDegreesPerSecond", c_float),
		("DirAngle", c_float),
		("SingleAnimAtOrAboveLOD", c_int),
		("RotationOffset", FRotator),
		("bUseAcceleration", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeBlendDirectional(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendDirectional", UAnimNodeBlendDirectional_Data),
	]


class  UAnimNodeBlendList_Data(Structure):
	_fields_ = [
		("TargetWeight", TArray_float),
		("BlendTimeToGo", c_float),
		("ActiveChildIndex", c_int),
		("bPlayActiveChild", c_bool, 1),
		("bForceChildFullWeightWhenBecomingRelevant", c_bool, 1),
		("bSkipBlendWhenNotRendered", c_bool, 1),
		("", c_ulong, 0),
		("SliderPosition", c_float),
	]

class  UAnimNodeBlendList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
	]


class  UAnimNodeBlendByBase_Data(Structure):
	_fields_ = [
		("Type", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ActorTag", FName),
		("ActorClass", POINTER(UClass)),
		("BlendTime", c_float),
		("CachedBase", POINTER(AActor)),
	]

class  UAnimNodeBlendByBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
		("UAnimNodeBlendByBase", UAnimNodeBlendByBase_Data),
	]


class  UAnimNodeBlendByPhysics_Data(Structure):
	_fields_ = [
		("DelayBeforeStartingBlend", c_float),
		("WaitingToDoBlend", FFlag),
	]

class  UAnimNodeBlendByPhysics(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
		("UAnimNodeBlendByPhysics", UAnimNodeBlendByPhysics_Data),
	]


class  UAnimNodeBlendByPosture_Data(Structure):
	_fields_ = [
		("bZeroPostSprintBlendWhenFiring", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeBlendByPosture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
		("UAnimNodeBlendByPosture", UAnimNodeBlendByPosture_Data),
	]


class  UAnimNodeBlendByProperty_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
		("bUseOwnersBase", c_bool, 1),
		("bForceUpdate", c_bool, 1),
		("bUseSpecificBlendTimes", c_bool, 1),
		("bSynchronizeNodesInEditor", c_bool, 1),
		("", c_ulong, 0),
		("CachedPropertyName", FName),
		("CachedFloatProperty", FPointer),
		("CachedBoolProperty", FPointer),
		("CachedByteProperty", FPointer),
		("CachedOwner", POINTER(AActor)),
		("BlendTime", c_float),
		("FloatPropMin", c_float),
		("FloatPropMax", c_float),
		("BlendToChild1Time", c_float),
		("BlendToChild2Time", c_float),
	]

class  UAnimNodeBlendByProperty(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
		("UAnimNodeBlendByProperty", UAnimNodeBlendByProperty_Data),
	]


class  UAnimNodeBlendBySpeed_Data(Structure):
	_fields_ = [
		("Speed", c_float),
		("LastChannel", c_int),
		("BlendUpTime", c_float),
		("BlendDownTime", c_float),
		("BlendDownPerc", c_float),
		("Constraints", TArray_float),
		("bUseAcceleration", c_bool, 1),
		("bUseBaseSkelComponentOwner", c_bool, 1),
		("bIgnoreZ", c_bool, 1),
		("bRestartChildrenOnBlendUpFromZero", c_bool, 1),
		("", c_ulong, 0),
		("BlendUpDelay", c_float),
		("BlendDownDelay", c_float),
		("BlendDelayRemaining", c_float),
	]

class  UAnimNodeBlendBySpeed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
		("UAnimNodeBlendBySpeed", UAnimNodeBlendBySpeed_Data),
	]


class  UAnimNodeRandom_Data(Structure):
	_fields_ = [
		("RandomInfo", TArray_FRandomAnimInfo),
		("PlayingSeqNode", POINTER(UAnimNodeSequence)),
		("PendingChildIndex", c_int),
		("bPickedPendingChildIndex", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeRandom(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendList", UAnimNodeBlendList_Data),
		("UAnimNodeRandom", UAnimNodeRandom_Data),
	]


class  UAnimNodeBlendMultiBone_Data(Structure):
	_fields_ = [
		("BlendTargetList", TArray_FChildBoneBlendInfo),
		("SourceRequiredBones", TArray_unsigned_char),
	]

class  UAnimNodeBlendMultiBone(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeBlendMultiBone", UAnimNodeBlendMultiBone_Data),
	]


class  UAnimNodeMirror_Data(Structure):
	_fields_ = [
		("bEnableMirroring", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeMirror(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeMirror", UAnimNodeMirror_Data),
	]


class  UAnimNodeScalePlayRate_Data(Structure):
	_fields_ = [
		("ScaleByValue", c_float),
	]

class  UAnimNodeScalePlayRate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeScalePlayRate", UAnimNodeScalePlayRate_Data),
	]


class  UAnimNodeScaleRateBySpeed_Data(Structure):
	_fields_ = [
		("BaseSpeed", c_float),
		("bUseBaseSkelComponentOwner", c_bool, 1),
		("", c_ulong, 0),
	]

class  UAnimNodeScaleRateBySpeed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeScalePlayRate", UAnimNodeScalePlayRate_Data),
		("UAnimNodeScaleRateBySpeed", UAnimNodeScaleRateBySpeed_Data),
	]


class  UAnimNodeSlot_Data(Structure):
	_fields_ = [
		("bIsPlayingCustomAnim", c_bool, 1),
		("bEarlyAnimEndNotify", c_bool, 1),
		("bSkipBlendWhenNotRendered", c_bool, 1),
		("bAdditiveAnimationsOverrideSource", c_bool, 1),
		("bIsBeingUsedByInterpGroup", c_bool, 1),
		("bReverseAnimSeqSearchOrder", c_bool, 1),
		("", c_ulong, 0),
		("PendingBlendOutTime", c_float),
		("CustomChildIndex", c_int),
		("TargetChildIndex", c_int),
		("TargetWeight", TArray_float),
		("BlendTimeToGo", c_float),
		("SynchNode", POINTER(UAnimNodeSynch)),
	]

class  UAnimNodeSlot(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeSlot", UAnimNodeSlot_Data),
	]


class  UAnimNodeSynch_Data(Structure):
	_fields_ = [
		("Groups", TArray_FSynchGroup),
	]

class  UAnimNodeSynch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimNodeSynch", UAnimNodeSynch_Data),
	]


class  UAnimTree_Data(Structure):
	_fields_ = [
		("AnimTreeTemplate", POINTER(UAnimTree)),
		("bEnablePooling", c_bool, 1),
		("bUseSavedPose", c_bool, 1),
		("bBeingEdited", c_bool, 1),
		("bParentNodeArrayBuilt", c_bool, 1),
		("bRebuildAnimTickArray", c_bool, 1),
		("", c_ulong, 0),
		("AnimGroups", TArray_FAnimGroup),
		("PrioritizedSkelBranches", TArray_FName),
		("ComposePrePassBoneNames", TArray_FName),
		("ComposePostPassBoneNames", TArray_FName),
		("RootMorphNodes", TArray_UMorphNodeBasePtr),
		("SkelControlLists", TArray_FSkelControlListHead),
		("SavedPose", TArray_FBoneAtom),
		("AnimTickArray", TArray_UAnimNodePtr),
	]

class  UAnimTree(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeBlendBase", UAnimNodeBlendBase_Data),
		("UAnimTree", UAnimTree_Data),
	]


class  UAnimNodeSequence_Data(Structure):
	_fields_ = [
		("AnimSeqName", FName),
		("Rate", c_float),
		("bPlaying", c_bool, 1),
		("bLooping", c_bool, 1),
		("bCauseActorAnimEnd", c_bool, 1),
		("bCauseActorAnimPlay", c_bool, 1),
		("bZeroRootRotation", c_bool, 1),
		("bZeroRootTranslation", c_bool, 1),
		("bDisableWarningWhenAnimNotFound", c_bool, 1),
		("bReverseAnimSeqSearchOrder", c_bool, 1),
		("bNoNotifies", c_bool, 1),
		("bForceRefposeWhenNotPlaying", c_bool, 1),
		("bIsIssuingNotifies", c_bool, 1),
		("bForceAlwaysSlave", c_bool, 1),
		("bSynchronize", c_bool, 1),
		("bReverseSync", c_bool, 1),
		("bShowTimeLineSlider", c_bool, 1),
		("bDisableAnimNotifies", c_bool, 1),
		("bLoopCameraAnim", c_bool, 1),
		("bRandomizeCameraAnimLoopStartTime", c_bool, 1),
		("bEditorOnlyAddRefPoseToAdditiveAnimation", c_bool, 1),
		("", c_ulong, 0),
		("CurrentTime", c_float),
		("PreviousTime", c_float),
		("EndTime", c_float),
		("AnimSeq", POINTER(UAnimSequence)),
		("AnimLinkupIndex", c_int),
		("NotifyWeightThreshold", c_float),
		("SynchGroupName", FName),
		("SynchPosOffset", c_float),
		("CameraAnim", POINTER(UCameraAnim)),
		("ActiveCameraAnimInstance", POINTER(UCameraAnimInst)),
		("CameraAnimScale", c_float),
		("CameraAnimPlayRate", c_float),
		("CameraAnimBlendInTime", c_float),
		("CameraAnimBlendOutTime", c_float),
		("RootBoneOption", c_ubyte * 3),
		("RootRotationOption", c_ubyte * 3),
		("Unknown1", c_ubyte, 0x),
		("MetaDataSkelControlList", TArray_USkelControlBasePtr),
	]

class  UAnimNodeSequence(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeSequence", UAnimNodeSequence_Data),
	]


class  UAnimNodeSequenceBlendBase_Data(Structure):
	_fields_ = [
		("Anims", TArray_FAnimBlendInfo),
	]

class  UAnimNodeSequenceBlendBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeSequence", UAnimNodeSequence_Data),
		("UAnimNodeSequenceBlendBase", UAnimNodeSequenceBlendBase_Data),
	]


class  UAnimNodeSequenceBlendByAim_Data(Structure):
	_fields_ = [
		("Aim", FVector2D),
		("PreviousAim", FVector2D),
		("HorizontalRange", FVector2D),
		("VerticalRange", FVector2D),
		("AngleOffset", FVector2D),
		("AnimName_LU", FName),
		("AnimName_LC", FName),
		("AnimName_LD", FName),
		("AnimName_CU", FName),
		("AnimName_CC", FName),
		("AnimName_CD", FName),
		("AnimName_RU", FName),
		("AnimName_RC", FName),
		("AnimName_RD", FName),
	]

class  UAnimNodeSequenceBlendByAim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UAnimNode", UAnimNode_Data),
		("UAnimNodeSequence", UAnimNodeSequence_Data),
		("UAnimNodeSequenceBlendBase", UAnimNodeSequenceBlendBase_Data),
		("UAnimNodeSequenceBlendByAim", UAnimNodeSequenceBlendByAim_Data),
	]


class  UMorphNodeBase_Data(Structure):
	_fields_ = [
		("NodeName", FName),
		("bDrawSlider", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMorphNodeBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
	]


class  UMorphNodeMultiPose_Data(Structure):
	_fields_ = [
		("Targets", TArray_UMorphTargetPtr),
		("MorphNames", TArray_FName),
		("Weights", TArray_float),
	]

class  UMorphNodeMultiPose(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
		("UMorphNodeMultiPose", UMorphNodeMultiPose_Data),
	]


class  UMorphNodePose_Data(Structure):
	_fields_ = [
		("Target", POINTER(UMorphTarget)),
		("MorphName", FName),
		("Weight", c_float),
	]

class  UMorphNodePose(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
		("UMorphNodePose", UMorphNodePose_Data),
	]


class  UMorphNodeWeightBase_Data(Structure):
	_fields_ = [
		("NodeConns", TArray_FMorphNodeConn),
	]

class  UMorphNodeWeightBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
		("UMorphNodeWeightBase", UMorphNodeWeightBase_Data),
	]


class  UMorphNodeWeight_Data(Structure):
	_fields_ = [
		("NodeWeight", c_float),
	]

class  UMorphNodeWeight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
		("UMorphNodeWeightBase", UMorphNodeWeightBase_Data),
		("UMorphNodeWeight", UMorphNodeWeight_Data),
	]


class  UMorphNodeWeightByBoneAngle_Data(Structure):
	_fields_ = [
		("Angle", c_float),
		("NodeWeight", c_float),
		("BaseBoneName", FName),
		("BaseBoneAxis", c_ubyte),
		("AngleBoneAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bInvertBaseBoneAxis", c_bool, 1),
		("bInvertAngleBoneAxis", c_bool, 1),
		("bControlMaterialParameter", c_bool, 1),
		("", c_ulong, 0),
		("AngleBoneName", FName),
		("MaterialSlotId", c_int),
		("ScalarParameterName", FName),
		("MaterialInstanceConstant", POINTER(UMaterialInstanceConstant)),
		("WeightArray", TArray_FBoneAngleMorph),
	]

class  UMorphNodeWeightByBoneAngle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
		("UMorphNodeWeightBase", UMorphNodeWeightBase_Data),
		("UMorphNodeWeightByBoneAngle", UMorphNodeWeightByBoneAngle_Data),
	]


class  UMorphNodeWeightByBoneRotation_Data(Structure):
	_fields_ = [
		("Angle", c_float),
		("NodeWeight", c_float),
		("BoneName", FName),
		("BoneAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bInvertBoneAxis", c_bool, 1),
		("bControlMaterialParameter", c_bool, 1),
		("", c_ulong, 0),
		("WeightArray", TArray_FBoneAngleMorph),
		("MaterialSlotId", c_int),
		("ScalarParameterName", FName),
		("MaterialInstanceConstant", POINTER(UMaterialInstanceConstant)),
	]

class  UMorphNodeWeightByBoneRotation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("UMorphNodeBase", UMorphNodeBase_Data),
		("UMorphNodeWeightBase", UMorphNodeWeightBase_Data),
		("UMorphNodeWeightByBoneRotation", UMorphNodeWeightByBoneRotation_Data),
	]


class  USkelControlBase_Data(Structure):
	_fields_ = [
		("ControlName", FName),
		("ControlStrength", c_float),
		("BlendInTime", c_float),
		("BlendOutTime", c_float),
		("BlendType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bPostPhysicsController", c_bool, 1),
		("bSetStrengthFromAnimNode", c_bool, 1),
		("bInitializedCachedNodeList", c_bool, 1),
		("bControlledByAnimMetada", c_bool, 1),
		("bInvertMetadataWeight", c_bool, 1),
		("bPropagateSetActive", c_bool, 1),
		("bIgnoreWhenNotRendered", c_bool, 1),
		("bShouldTickInScript", c_bool, 1),
		("bShouldTickOwner", c_bool, 1),
		("bEnableEaseInOut", c_bool, 1),
		("", c_ulong, 0),
		("StrengthTarget", c_float),
		("BlendTimeToGo", c_float),
		("StrengthAnimNodeNameList", TArray_FName),
		("CachedNodeList", TArray_UAnimNodePtr),
		("AnimMetadataWeight", c_float),
		("AnimMetaDataUpdateTag", c_int),
		("BoneScale", c_float),
		("ControlTickTag", c_int),
		("IgnoreAtOrAboveLOD", c_int),
		("NextControl", POINTER(USkelControlBase)),
		("ControlPosX", c_int),
		("ControlPosY", c_int),
	]

class  USkelControlBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
	]


class  USkelControl_CCD_IK_Data(Structure):
	_fields_ = [
		("EffectorLocation", FVector),
		("EffectorLocationSpace", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("EffectorSpaceBoneName", FName),
		("EffectorTranslationFromBone", FVector),
		("NumBones", c_int),
		("MaxPerBoneIterations", c_int),
		("IterationsCount", c_int),
		("Precision", c_float),
		("bStartFromTail", c_bool, 1),
		("bNoTurnOptimization", c_bool, 1),
		("", c_ulong, 0),
		("AngleConstraint", TArray_float),
		("MaxAngleSteps", c_float),
	]

class  USkelControl_CCD_IK(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControl_CCD_IK", USkelControl_CCD_IK_Data),
	]


class  USkelControl_Multiply_Data(Structure):
	_fields_ = [
		("Multiplier", c_float),
	]

class  USkelControl_Multiply(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControl_Multiply", USkelControl_Multiply_Data),
	]


class  USkelControl_TwistBone_Data(Structure):
	_fields_ = [
		("SourceBoneName", FName),
		("TwistAngleScale", c_float),
	]

class  USkelControl_TwistBone(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControl_TwistBone", USkelControl_TwistBone_Data),
	]


class  USkelControlLimb_Data(Structure):
	_fields_ = [
		("EffectorLocation", FVector),
		("EffectorRotation", FRotator),
		("EffectorLocationSpace", c_ubyte),
		("JointTargetLocationSpace", c_ubyte),
		("JointOffsetSpace", c_ubyte),
		("BoneAxis", c_ubyte),
		("JointAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("EffectorSpaceBoneName", FName),
		("JointTargetLocation", FVector),
		("JointTargetSpaceBoneName", FName),
		("JointOffset", FVector),
		("JointOffsetBoneName", FName),
		("bInvertBoneAxis", c_bool, 1),
		("bInvertJointAxis", c_bool, 1),
		("bRotateJoint", c_bool, 1),
		("bMaintainEffectorRelRot", c_bool, 1),
		("bTakeRotationFromEffectorSpace", c_bool, 1),
		("bAllowStretching", c_bool, 1),
		("SupportGearboxTwistBones", c_bool, 1),
		("bTakeRotationFromEffectorRotation", c_bool, 1),
		("", c_ulong, 0),
		("StretchLimits", FVector2D),
		("StretchRollBoneName", FName),
		("CachedTwistBoneIndex", c_int),
	]

class  USkelControlLimb(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlLimb", USkelControlLimb_Data),
	]


class  USkelControlFootPlacement_Data(Structure):
	_fields_ = [
		("FootOffset", c_float),
		("FootUpAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("FootRotOffset", FRotator),
		("bInvertFootUpAxis", c_bool, 1),
		("bOrientFootToGround", c_bool, 1),
		("bOnlyEnableForUpAdjustment", c_bool, 1),
		("", c_ulong, 0),
		("MaxUpAdjustment", c_float),
		("MaxDownAdjustment", c_float),
		("MaxFootOrientAdjust", c_float),
	]

class  USkelControlFootPlacement(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlLimb", USkelControlLimb_Data),
		("USkelControlFootPlacement", USkelControlFootPlacement_Data),
	]


class  USkelControlLookAt_Data(Structure):
	_fields_ = [
		("TargetLocation", FVector),
		("TargetLocationSpace", c_ubyte),
		("LookAtAxis", c_ubyte),
		("UpAxis", c_ubyte),
		("AllowRotationSpace", c_ubyte),
		("TargetSpaceBoneName", FName),
		("bInvertLookAtAxis", c_bool, 1),
		("bDefineUpAxis", c_bool, 1),
		("bInvertUpAxis", c_bool, 1),
		("bEnableLimit", c_bool, 1),
		("bLimitBasedOnRefPose", c_bool, 1),
		("bDisableBeyondLimit", c_bool, 1),
		("bNotifyBeyondLimit", c_bool, 1),
		("bShowLimit", c_bool, 1),
		("bAllowRotationX", c_bool, 1),
		("bAllowRotationY", c_bool, 1),
		("bAllowRotationZ", c_bool, 1),
		("", c_ulong, 0),
		("TargetLocationInterpSpeed", c_float),
		("DesiredTargetLocation", FVector),
		("ActorSpaceLookAtTarget", FVector),
		("MaxAngle", c_float),
		("OuterMaxAngle", c_float),
		("DeadZoneAngle", c_float),
		("RotationAngleRangeX", FVector2D),
		("RotationAngleRangeY", FVector2D),
		("RotationAngleRangeZ", FVector2D),
		("AllowRotationOtherBoneName", FName),
		("LookAtAlpha", c_float),
		("LookAtAlphaTarget", c_float),
		("LookAtAlphaBlendTimeToGo", c_float),
		("LimitLookDir", FVector),
		("BaseLookDir", FVector),
		("BaseBonePos", FVector),
		("LastCalcTime", c_float),
		("ControlBoneIndex", c_int),
	]

class  USkelControlLookAt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlLookAt", USkelControlLookAt_Data),
	]


class  USkelControlSingleBone_Data(Structure):
	_fields_ = [
		("bApplyTranslation", c_bool, 1),
		("bApplyRotation", c_bool, 1),
		("bAddTranslation", c_bool, 1),
		("bAddRotation", c_bool, 1),
		("bRemoveMeshRotation", c_bool, 1),
		("", c_ulong, 0),
		("BoneTranslation", FVector),
		("BoneTranslationSpace", c_ubyte),
		("BoneRotationSpace", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TranslationSpaceBoneName", FName),
		("BoneRotation", FRotator),
		("RotationSpaceBoneName", FName),
	]

class  USkelControlSingleBone(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlSingleBone", USkelControlSingleBone_Data),
	]


class  USkelControlHandlebars_Data(Structure):
	_fields_ = [
		("WheelRollAxis", c_ubyte),
		("HandlebarRotateAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("WheelBoneName", FName),
		("bInvertRotation", c_bool, 1),
		("", c_ulong, 0),
		("SteerWheelBoneIndex", c_int),
	]

class  USkelControlHandlebars(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlSingleBone", USkelControlSingleBone_Data),
		("USkelControlHandlebars", USkelControlHandlebars_Data),
	]


class  USkelControlWheel_Data(Structure):
	_fields_ = [
		("WheelDisplacement", c_float),
		("WheelMaxRenderDisplacement", c_float),
		("WheelRoll", c_float),
		("WheelRollAxis", c_ubyte),
		("WheelSteeringAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("WheelSteering", c_float),
		("bInvertWheelRoll", c_bool, 1),
		("bInvertWheelSteering", c_bool, 1),
		("", c_ulong, 0),
	]

class  USkelControlWheel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlSingleBone", USkelControlSingleBone_Data),
		("USkelControlWheel", USkelControlWheel_Data),
	]


class  USkelControlSpline_Data(Structure):
	_fields_ = [
		("SplineLength", c_int),
		("SplineBoneAxis", c_ubyte),
		("BoneRotMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bInvertSplineBoneAxis", c_bool, 1),
		("", c_ulong, 0),
		("EndSplineTension", c_float),
		("StartSplineTension", c_float),
	]

class  USkelControlSpline(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlSpline", USkelControlSpline_Data),
	]


class  USkelControlTrail_Data(Structure):
	_fields_ = [
		("ChainLength", c_int),
		("ChainBoneAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bInvertChainBoneAxis", c_bool, 1),
		("bLimitStretch", c_bool, 1),
		("bActorSpaceFakeVel", c_bool, 1),
		("bHadValidStrength", c_bool, 1),
		("", c_ulong, 0),
		("TrailRelaxation", c_float),
		("StretchLimit", c_float),
		("FakeVelocity", FVector),
		("ThisTimstep", c_float),
		("TrailBoneLocations", TArray_FVector),
		("Unknown2", c_ubyte, 0x),
		("OldLocalToWorld", FMatrix),
	]

class  USkelControlTrail(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimObject", UAnimObject_Data),
		("USkelControlBase", USkelControlBase_Data),
		("USkelControlTrail", USkelControlTrail_Data),
	]


class  UAnimSequence_Data(Structure):
	_fields_ = [
		("SequenceName", FName),
		("Notifies", TArray_FAnimNotifyEvent),
		("MetaData", TArray_UAnimMetaDataPtr),
		("BoneControlModifiers", TArray_FSkelControlModifier),
		("SequenceLength", c_float),
		("NumFrames", c_int),
		("RateScale", c_float),
		("bNoLoopingInterpolation", c_bool, 1),
		("bIsAdditive", c_bool, 1),
		("bAdditiveBuiltLooping", c_bool, 1),
		("bDoNotOverrideCompression", c_bool, 1),
		("bHasBeenUsed", c_bool, 1),
		("", c_ulong, 0),
		("RawAnimData", TArray_FRawAnimSequenceTrack),
		("RawAnimationData", TArray_FRawAnimSequenceTrack),
		("TranslationData", TArray_FTranslationTrack),
		("RotationData", TArray_FRotationTrack),
		("CurveData", TArray_FCurveTrack),
		("TranslationCompressionFormat", c_ubyte),
		("RotationCompressionFormat", c_ubyte),
		("KeyEncodingFormat", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CompressedTrackOffsets", TArray_int),
		("CompressedByteStream", TArray_unsigned_char),
		("TranslationCodec", FPointer),
		("RotationCodec", FPointer),
		("AdditiveRefPose", TArray_FBoneAtom),
		("AdditiveBasePose", TArray_FRawAnimSequenceTrack),
		("EncodingPkgVersion", c_int),
		("UseScore", c_float),
		("DeltaTrackCache", TArray_FDeltaTrackInfo),
	]

class  UAnimSequence(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimSequence", UAnimSequence_Data),
	]


class  UAnimSet_Data(Structure):
	_fields_ = [
		("bAnimRotationOnly", c_bool, 1),
		("", c_ulong, 0),
		("TrackBoneNames", TArray_FName),
		("Sequences", TArray_UAnimSequencePtr),
		("Unknown1", c_ubyte, 0x),
		("LinkupCache", TArray_FAnimSetMeshLinkup),
		("Unknown2", c_ubyte, 0x),
		("BoneUseAnimTranslation", TArray_unsigned_char),
		("ForceUseMeshTranslation", TArray_unsigned_char),
		("UseTranslationBoneNames", TArray_FName),
		("ForceMeshTranslationBoneNames", TArray_FName),
		("PreviewSkelMeshName", FName),
		("BestRatioSkelMeshName", FName),
	]

class  UAnimSet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimSet", UAnimSet_Data),
	]


class  UMorphTarget_Data(Structure):
	_fields_ = [
		("MorphLODModels", TArray_int),
		("MaterialSlotId", c_int),
		("ScalarParameterName", FName),
	]

class  UMorphTarget(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMorphTarget", UMorphTarget_Data),
	]


class  UMorphTargetSet_Data(Structure):
	_fields_ = [
		("Targets", TArray_UMorphTargetPtr),
		("BaseSkelMesh", POINTER(USkeletalMesh)),
		("RawWedgePointIndices", FArray_Mirror),
	]

class  UMorphTargetSet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMorphTargetSet", UMorphTargetSet_Data),
	]


class  UMorphWeightSequence_Data(Structure):
	_fields_ = []

class  UMorphWeightSequence(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMorphWeightSequence", UMorphWeightSequence_Data),
	]


class  ADecalActorBase_Data(Structure):
	_fields_ = [
		("Decal", POINTER(UDecalComponent)),
	]

class  ADecalActorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADecalActorBase", ADecalActorBase_Data),
	]


class  ADecalActor_Data(Structure):
	_fields_ = []

class  ADecalActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADecalActorBase", ADecalActorBase_Data),
		("ADecalActor", ADecalActor_Data),
	]


class  ADecalActorMovable_Data(Structure):
	_fields_ = []

class  ADecalActorMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADecalActorBase", ADecalActorBase_Data),
		("ADecalActorMovable", ADecalActorMovable_Data),
	]


class  ADecalManager_Data(Structure):
	_fields_ = [
		("DecalTemplate", POINTER(UDecalComponent)),
		("PoolDecals", TArray_UDecalComponentPtr),
		("MaxActiveDecals", c_int),
		("MaxActiveDecalsLow", c_int),
		("MaxActiveDecalsHigh", c_int),
		("MaxActiveDecalsSplitScreen", c_int),
		("DecalLifeSpan", c_float),
		("DecalDepthBias", c_float),
		("DecalBlendRange", FVector2D),
		("MaxFadingDecals", c_int),
		("FadingLifeSpan", c_float),
		("FadeParameterName", FName),
		("ActiveDecals", TArray_FActiveDecalInfo),
		("FadingDecals", TArray_FActiveDecalInfo),
	]

class  ADecalManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADecalManager", ADecalManager_Data),
	]


class  UDecalComponent_Data(Structure):
	_fields_ = [
		("DecalMaterial", POINTER(UMaterialInterface)),
		("Width", c_float),
		("Height", c_float),
		("TileX", c_float),
		("TileY", c_float),
		("OffsetX", c_float),
		("OffsetY", c_float),
		("DecalRotation", c_float),
		("FieldOfView", c_float),
		("NearPlane", c_float),
		("FarPlane", c_float),
		("Location", FVector),
		("Orientation", FRotator),
		("HitLocation", FVector),
		("HitNormal", FVector),
		("HitTangent", FVector),
		("HitBinormal", FVector),
		("bNoClip", c_bool, 1),
		("bStaticDecal", c_bool, 1),
		("bProjectOnBackfaces", c_bool, 1),
		("bProjectOnHidden", c_bool, 1),
		("bProjectOnBSP", c_bool, 1),
		("bProjectOnStaticMeshes", c_bool, 1),
		("bProjectOnSkeletalMeshes", c_bool, 1),
		("bProjectOnTerrain", c_bool, 1),
		("bFlipBackfaceDirection", c_bool, 1),
		("bMovableDecal", c_bool, 1),
		("bHasBeenAttached", c_bool, 1),
		("bDecalMaterialSetAtRunTime", c_bool, 1),
		("", c_ulong, 0),
		("HitComponent", POINTER(UPrimitiveComponent)),
		("HitBone", FName),
		("HitNodeIndex", c_int),
		("HitLevelIndex", c_int),
		("FracturedStaticMeshComponentIndex", c_int),
		("HitNodeIndices", TArray_int),
		("DecalReceivers", TArray_FDecalReceiver),
		("StaticReceivers", TArray_FPointer),
		("ReleaseResourcesFence", FPointer),
		("Planes", TArray_FPlane),
		("DepthBias", c_float),
		("SlopeScaleDepthBias", c_float),
		("SortOrder", c_int),
		("BackfaceAngle", c_float),
		("BlendRange", FVector2D),
		("StreamingDistanceMultiplier", c_float),
		("DecalTransform", c_ubyte),
		("FilterMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Filter", TArray_AActorPtr),
		("ReceiverImages", TArray_UPrimitiveComponentPtr),
		("ParentRelativeLocation", FVector),
		("ParentRelativeOrientation", FRotator),
		("Unknown2", c_ubyte, 0x),
		("ParentRelLocRotMatrix", FMatrix),
	]

class  UDecalComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDecalComponent", UDecalComponent_Data),
	]


class  UActorFactoryDecal_Data(Structure):
	_fields_ = [
		("DecalMaterial", POINTER(UMaterialInterface)),
	]

class  UActorFactoryDecal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDecal", UActorFactoryDecal_Data),
	]


class  UActorFactoryDecalMovable_Data(Structure):
	_fields_ = []

class  UActorFactoryDecalMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryDecal", UActorFactoryDecal_Data),
		("UActorFactoryDecalMovable", UActorFactoryDecalMovable_Data),
	]


class  UDecalMaterial_Data(Structure):
	_fields_ = []

class  UDecalMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UMaterialInterface", UMaterialInterface_Data),
		("UMaterial", UMaterial_Data),
		("UDecalMaterial", UDecalMaterial_Data),
	]


class  AFogVolumeDensityInfo_Data(Structure):
	_fields_ = [
		("DensityComponent", POINTER(UFogVolumeDensityComponent)),
		("AutomaticMeshComponent", POINTER(UStaticMeshComponent)),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  AFogVolumeDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFogVolumeDensityInfo", AFogVolumeDensityInfo_Data),
	]


class  AFogVolumeConeDensityInfo_Data(Structure):
	_fields_ = []

class  AFogVolumeConeDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFogVolumeDensityInfo", AFogVolumeDensityInfo_Data),
		("AFogVolumeConeDensityInfo", AFogVolumeConeDensityInfo_Data),
	]


class  AFogVolumeConstantDensityInfo_Data(Structure):
	_fields_ = []

class  AFogVolumeConstantDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFogVolumeDensityInfo", AFogVolumeDensityInfo_Data),
		("AFogVolumeConstantDensityInfo", AFogVolumeConstantDensityInfo_Data),
	]


class  AFogVolumeLinearHalfspaceDensityInfo_Data(Structure):
	_fields_ = []

class  AFogVolumeLinearHalfspaceDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFogVolumeDensityInfo", AFogVolumeDensityInfo_Data),
		("AFogVolumeLinearHalfspaceDensityInfo", AFogVolumeLinearHalfspaceDensityInfo_Data),
	]


class  AFogVolumeSphericalDensityInfo_Data(Structure):
	_fields_ = []

class  AFogVolumeSphericalDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AFogVolumeDensityInfo", AFogVolumeDensityInfo_Data),
		("AFogVolumeSphericalDensityInfo", AFogVolumeSphericalDensityInfo_Data),
	]


class  UExponentialHeightFogComponent_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
		("FogHeight", c_float),
		("FogDensity", c_float),
		("FogHeightFalloff", c_float),
		("FogMaxOpacity", c_float),
		("StartDistance", c_float),
		("LightTerminatorAngle", c_float),
		("OppositeLightBrightness", c_float),
		("OppositeLightColor", FColor),
		("LightInscatteringBrightness", c_float),
		("LightInscatteringColor", FColor),
	]

class  UExponentialHeightFogComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UExponentialHeightFogComponent", UExponentialHeightFogComponent_Data),
	]


class  UFogVolumeDensityComponent_Data(Structure):
	_fields_ = [
		("FogMaterial", POINTER(UMaterialInterface)),
		("DefaultFogVolumeMaterial", POINTER(UMaterialInterface)),
		("bEnabled", c_bool, 1),
		("bAffectsTranslucency", c_bool, 1),
		("bOnlyAffectsTranslucency", c_bool, 1),
		("", c_ulong, 0),
		("SimpleLightColor", FLinearColor),
		("ApproxFogLightColor", FLinearColor),
		("StartDistance", c_float),
		("MaxDistance", c_float),
		("FogVolumeActors", TArray_AActorPtr),
	]

class  UFogVolumeDensityComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UFogVolumeDensityComponent", UFogVolumeDensityComponent_Data),
	]


class  UFogVolumeConeDensityComponent_Data(Structure):
	_fields_ = [
		("MaxDensity", c_float),
		("ConeVertex", FVector),
		("ConeRadius", c_float),
		("ConeAxis", FVector),
		("ConeMaxAngle", c_float),
		("PreviewCone", POINTER(UDrawLightConeComponent)),
	]

class  UFogVolumeConeDensityComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UFogVolumeDensityComponent", UFogVolumeDensityComponent_Data),
		("UFogVolumeConeDensityComponent", UFogVolumeConeDensityComponent_Data),
	]


class  UFogVolumeConstantDensityComponent_Data(Structure):
	_fields_ = [
		("Density", c_float),
	]

class  UFogVolumeConstantDensityComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UFogVolumeDensityComponent", UFogVolumeDensityComponent_Data),
		("UFogVolumeConstantDensityComponent", UFogVolumeConstantDensityComponent_Data),
	]


class  UFogVolumeLinearHalfspaceDensityComponent_Data(Structure):
	_fields_ = [
		("PlaneDistanceFactor", c_float),
		("HalfspacePlane", FPlane),
	]

class  UFogVolumeLinearHalfspaceDensityComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UFogVolumeDensityComponent", UFogVolumeDensityComponent_Data),
		("UFogVolumeLinearHalfspaceDensityComponent", UFogVolumeLinearHalfspaceDensityComponent_Data),
	]


class  UFogVolumeSphericalDensityComponent_Data(Structure):
	_fields_ = [
		("MaxDensity", c_float),
		("SphereCenter", FVector),
		("SphereRadius", c_float),
		("PreviewSphereRadius", POINTER(UDrawLightRadiusComponent)),
	]

class  UFogVolumeSphericalDensityComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UFogVolumeDensityComponent", UFogVolumeDensityComponent_Data),
		("UFogVolumeSphericalDensityComponent", UFogVolumeSphericalDensityComponent_Data),
	]


class  UActorFactoryFogVolumeConstantDensityInfo_Data(Structure):
	_fields_ = [
		("SelectedMaterial", POINTER(UMaterialInterface)),
		("bNothingSelected", c_bool, 1),
		("", c_ulong, 0),
	]

class  UActorFactoryFogVolumeConstantDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryFogVolumeConstantDensityInfo", UActorFactoryFogVolumeConstantDensityInfo_Data),
	]


class  UActorFactoryFogVolumeLinearHalfspaceDensityInfo_Data(Structure):
	_fields_ = []

class  UActorFactoryFogVolumeLinearHalfspaceDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryFogVolumeConstantDensityInfo", UActorFactoryFogVolumeConstantDensityInfo_Data),
		("UActorFactoryFogVolumeLinearHalfspaceDensityInfo", UActorFactoryFogVolumeLinearHalfspaceDensityInfo_Data),
	]


class  UActorFactoryFogVolumeSphericalDensityInfo_Data(Structure):
	_fields_ = []

class  UActorFactoryFogVolumeSphericalDensityInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryFogVolumeConstantDensityInfo", UActorFactoryFogVolumeConstantDensityInfo_Data),
		("UActorFactoryFogVolumeSphericalDensityInfo", UActorFactoryFogVolumeSphericalDensityInfo_Data),
	]


class  AApexDestructibleActor_Data(Structure):
	_fields_ = [
		("LightEnvironment", POINTER(UDynamicLightEnvironmentComponent)),
		("bFractureMaterialOverride", c_bool, 1),
		("", c_ulong, 0),
		("FractureMaterials", TArray_UFractureMaterialPtr),
		("StaticDestructibleComponent", POINTER(UApexStaticDestructibleComponent)),
		("VisibilityFactors", TArray_unsigned_char),
		("FractureSounds", TArray_USoundCuePtr),
		("FractureParticleEffects", TArray_UParticleSystemPtr),
		("ModifyHealthParams", F_ModifyHealthParams),
	]

class  AApexDestructibleActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AApexDestructibleActor", AApexDestructibleActor_Data),
	]


class  UApexComponentBase_Data(Structure):
	_fields_ = [
		("ComponentBaseResources", FPointer),
		("ReleaseResourcesFence", FRenderCommandFence_Mirror),
		("Asset", POINTER(UApexAsset)),
		("WireframeColor", FColor),
		("bAssetChanged", c_bool, 1),
		("", c_ulong, 0),
	]

class  UApexComponentBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UApexComponentBase", UApexComponentBase_Data),
	]


class  UApexDynamicComponent_Data(Structure):
	_fields_ = [
		("ComponentDynamicResources", FPointer),
	]

class  UApexDynamicComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UApexComponentBase", UApexComponentBase_Data),
		("UApexDynamicComponent", UApexDynamicComponent_Data),
	]


class  UApexStaticComponent_Data(Structure):
	_fields_ = []

class  UApexStaticComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UApexComponentBase", UApexComponentBase_Data),
		("UApexStaticComponent", UApexStaticComponent_Data),
	]


class  UApexStaticDestructibleComponent_Data(Structure):
	_fields_ = [
		("SleepEnergyThreshold", c_float),
		("SleepDamping", c_float),
		("ApexDestructibleActor", FPointer),
		("ApexDestructiblePreview", FPointer),
		("bIsThumbnailComponent", c_bool, 1),
		("", c_ulong, 0),
	]

class  UApexStaticDestructibleComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UApexComponentBase", UApexComponentBase_Data),
		("UApexStaticComponent", UApexStaticComponent_Data),
		("UApexStaticDestructibleComponent", UApexStaticDestructibleComponent_Data),
	]


class  UBlockingMeshComponent_Data(Structure):
	_fields_ = [
		("bBlockPlayers", c_bool, 1),
		("bBlockVehicles", c_bool, 1),
		("bBlockRocketsAndGrenades", c_bool, 1),
		("bBlockBullets", c_bool, 1),
		("bBlockTossedItems", c_bool, 1),
		("bBlockEnemyPawns", c_bool, 1),
		("bBlockFriendlyPawns", c_bool, 1),
		("bBlockPlayerVehicles", c_bool, 1),
		("bBlockEnemyVehicles", c_bool, 1),
		("bIsDisabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  UBlockingMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UStaticMeshComponent", UStaticMeshComponent_Data),
		("UBlockingMeshComponent", UBlockingMeshComponent_Data),
	]


class  UInstancedStaticMeshComponent_Data(Structure):
	_fields_ = [
		("PerInstanceData", TArray_FInstancedStaticMeshInstanceData),
		("PerInstanceSMData", TArray_FInstancedStaticMeshInstanceData),
		("NumPendingLightmaps", c_int),
		("ComponentJoinKey", c_int),
		("CachedMappings", TArray_FInstancedStaticMeshMappingInfo),
		("InstancingRandomSeed", c_int),
	]

class  UInstancedStaticMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UStaticMeshComponent", UStaticMeshComponent_Data),
		("UInstancedStaticMeshComponent", UInstancedStaticMeshComponent_Data),
	]


class  USplineMeshComponent_Data(Structure):
	_fields_ = [
		("SplineParams", FSplineMeshParams),
		("SplineXDir", FVector),
		("bSmoothInterpRollScale", c_bool, 1),
		("", c_ulong, 0),
	]

class  USplineMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UStaticMeshComponent", UStaticMeshComponent_Data),
		("USplineMeshComponent", USplineMeshComponent_Data),
	]


class  UApexAsset_Data(Structure):
	_fields_ = [
		("OriginalApexName", FString),
		("ApexComponents", TArray_UApexComponentBasePtr),
	]

class  UApexAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UApexAsset", UApexAsset_Data),
	]


class  UApexClothingAsset_Data(Structure):
	_fields_ = [
		("MApexAsset", FPointer),
		("ApexClothingLibrary", POINTER(UApexGenericAsset)),
		("bUseHardwareCloth", c_bool, 1),
		("bFallbackSkinning", c_bool, 1),
		("bSlowStart", c_bool, 1),
		("bRecomputeNormals", c_bool, 1),
		("bResetAfterTeleport", c_bool, 1),
		("", c_ulong, 0),
		("UVChannelForTangentUpdate", c_int),
		("MaxDistanceBlendTime", c_float),
		("ContinuousRotationThreshold", c_float),
		("ContinuousDistanceThreshold", c_float),
		("LodWeightsMaxDistance", c_float),
		("LodWeightsDistanceWeight", c_float),
		("LodWeightsBias", c_float),
		("LodWeightsBenefitsBias", c_float),
	]

class  UApexClothingAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UApexAsset", UApexAsset_Data),
		("UApexClothingAsset", UApexClothingAsset_Data),
	]


class  UApexDestructibleAsset_Data(Structure):
	_fields_ = [
		("MApexAsset", FPointer),
		("Materials", TArray_UMaterialInterfacePtr),
		("FractureMaterials", TArray_UFractureMaterialPtr),
		("DefaultPhysMaterial", POINTER(UPhysicalMaterial)),
		("MDestructibleThumbnailComponent", FPointer),
		("bHasUniqueAssetMaterialNames", c_bool, 1),
		("bDynamic", c_bool, 1),
		("", c_ulong, 0),
		("CrumbleEmitterName", FString),
		("DustEmitterName", FString),
		("DestructibleParameters", FNxDestructibleParameters),
	]

class  UApexDestructibleAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UApexAsset", UApexAsset_Data),
		("UApexDestructibleAsset", UApexDestructibleAsset_Data),
	]


class  UApexGenericAsset_Data(Structure):
	_fields_ = [
		("MApexAsset", FPointer),
	]

class  UApexGenericAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UApexAsset", UApexAsset_Data),
		("UApexGenericAsset", UApexGenericAsset_Data),
	]


class  UInterpFilter_Data(Structure):
	_fields_ = [
		("Caption", FString),
	]

class  UInterpFilter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpFilter", UInterpFilter_Data),
	]


class  UInterpFilter_Classes_Data(Structure):
	_fields_ = []

class  UInterpFilter_Classes(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpFilter", UInterpFilter_Data),
		("UInterpFilter_Classes", UInterpFilter_Classes_Data),
	]


class  UInterpFilter_Custom_Data(Structure):
	_fields_ = []

class  UInterpFilter_Custom(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpFilter", UInterpFilter_Data),
		("UInterpFilter_Custom", UInterpFilter_Custom_Data),
	]


class  UInterpGroup_Data(Structure):
	_fields_ = [
		("VfTable_FInterpEdInputInterface", FPointer),
		("InterpTracks", TArray_UInterpTrackPtr),
		("GroupName", FName),
		("GroupColor", FColor),
		("GroupAnimSets", TArray_UAnimSetPtr),
		("bCollapsed", c_bool, 1),
		("bVisible", c_bool, 1),
		("bIsFolder", c_bool, 1),
		("bIsParented", c_bool, 1),
		("bIsSelected", c_bool, 1),
		("bRunTracksWhenSkippingToLastFrame", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpGroup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpGroup", UInterpGroup_Data),
	]


class  UInterpGroupAI_Data(Structure):
	_fields_ = [
		("StageMarkGroup", FName),
		("SnapToRootBoneLocationWhenFinished", c_bool, 1),
		("bNoEncroachmentCheck", c_bool, 1),
		("bDisableWorldCollision", c_bool, 1),
		("bIgnoreLegacyHeightAdjust", c_bool, 1),
		("bRecreatePreviewPawn", c_bool, 1),
		("bRefreshStageMarkGroup", c_bool, 1),
		("bEnableAIWhenAllAnimsFinished", c_bool, 1),
		("bUseStageMarkerForInitialLocation", c_bool, 1),
		("bPutInDemiGod", c_bool, 1),
		("", c_ulong, 0),
		("Alignment", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("AlignmentLerpTime", c_float),
	]

class  UInterpGroupAI(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpGroup", UInterpGroup_Data),
		("UInterpGroupAI", UInterpGroupAI_Data),
	]


class  UInterpGroupDirector_Data(Structure):
	_fields_ = [
		("AttachedGroupName", FName),
	]

class  UInterpGroupDirector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpGroup", UInterpGroup_Data),
		("UInterpGroupDirector", UInterpGroupDirector_Data),
	]


class  UInterpGroupInst_Data(Structure):
	_fields_ = [
		("Group", POINTER(UInterpGroup)),
		("GroupActor", POINTER(AActor)),
		("TrackInst", TArray_UInterpTrackInstPtr),
		("bWasNetworkRefreshed", c_bool, 1),
		("bDeleteIfNoGroupActor", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpGroupInst(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpGroupInst", UInterpGroupInst_Data),
	]


class  UInterpGroupInstAI_Data(Structure):
	_fields_ = [
		("AIGroup", POINTER(UInterpGroupAI)),
		("SavedPhysics", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bSavedNoEncroachCheck", c_bool, 1),
		("bSavedCollideActors", c_bool, 1),
		("bSavedBlockActors", c_bool, 1),
		("", c_ulong, 0),
		("StageMarkActor", POINTER(AActor)),
	]

class  UInterpGroupInstAI(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpGroupInst", UInterpGroupInst_Data),
		("UInterpGroupInstAI", UInterpGroupInstAI_Data),
	]


class  UInterpGroupInstDirector_Data(Structure):
	_fields_ = []

class  UInterpGroupInstDirector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpGroupInst", UInterpGroupInst_Data),
		("UInterpGroupInstDirector", UInterpGroupInstDirector_Data),
	]


class  UInterpTrackBoolProp_Data(Structure):
	_fields_ = [
		("BoolTrack", TArray_FBoolTrackKey),
		("PropertyName", FName),
	]

class  UInterpTrackBoolProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackBoolProp", UInterpTrackBoolProp_Data),
	]


class  UInterpTrackComment_Data(Structure):
	_fields_ = [
		("CommentTrack", TArray_FCommentTrackKey),
		("bOutputCommentsToScreen", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackComment(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackComment", UInterpTrackComment_Data),
	]


class  UInterpTrackDirector_Data(Structure):
	_fields_ = [
		("CutTrack", TArray_FDirectorTrackCut),
		("bSimulateCameraCutsOnClients", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackDirector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackDirector", UInterpTrackDirector_Data),
	]


class  UInterpTrackEvent_Data(Structure):
	_fields_ = [
		("EventTrack", TArray_FEventTrackKey),
		("bFireEventsWhenForwards", c_bool, 1),
		("bFireEventsWhenBackwards", c_bool, 1),
		("bFireEventsWhenJumpingForwards", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackEvent", UInterpTrackEvent_Data),
	]


class  UInterpTrackFaceFX_Data(Structure):
	_fields_ = [
		("FaceFXAnimSets", TArray_UFaceFXAnimSetPtr),
		("FaceFXSeqs", TArray_FFaceFXTrackKey),
		("CachedActorFXAsset", POINTER(UFaceFXAsset)),
		("FaceFXSoundCueKeys", TArray_FFaceFXSoundCueKey),
	]

class  UInterpTrackFaceFX(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFaceFX", UInterpTrackFaceFX_Data),
	]


class  UInterpTrackFloatBase_Data(Structure):
	_fields_ = [
		("FloatTrack", FInterpCurveFloat),
		("CurveTension", c_float),
	]

class  UInterpTrackFloatBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
	]


class  UInterpTrackAnimControl_Data(Structure):
	_fields_ = [
		("AnimSets", TArray_UAnimSetPtr),
		("SlotName", FName),
		("AnimSeqs", TArray_FAnimControlTrackKey),
		("bEnableRootMotion", c_bool, 1),
		("bSkipAnimNotifiers", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackAnimControl(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackAnimControl", UInterpTrackAnimControl_Data),
	]


class  UInterpTrackFade_Data(Structure):
	_fields_ = [
		("bPersistFade", c_bool, 1),
		("", c_ulong, 0),
		("FadeColor", FColor),
	]

class  UInterpTrackFade(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackFade", UInterpTrackFade_Data),
	]


class  UInterpTrackFloatMaterialParam_Data(Structure):
	_fields_ = [
		("Materials", TArray_FMaterialReferenceList),
		("Material", POINTER(UMaterialInterface)),
		("ParamName", FName),
		("bNeedsMaterialRefsUpdate", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackFloatMaterialParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackFloatMaterialParam", UInterpTrackFloatMaterialParam_Data),
	]


class  UInterpTrackFloatParticleParam_Data(Structure):
	_fields_ = [
		("ParamName", FName),
	]

class  UInterpTrackFloatParticleParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackFloatParticleParam", UInterpTrackFloatParticleParam_Data),
	]


class  UInterpTrackFloatProp_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
	]

class  UInterpTrackFloatProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackFloatProp", UInterpTrackFloatProp_Data),
	]


class  UInterpTrackMorphWeight_Data(Structure):
	_fields_ = [
		("MorphNodeName", FName),
	]

class  UInterpTrackMorphWeight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackMorphWeight", UInterpTrackMorphWeight_Data),
	]


class  UInterpTrackMoveAxis_Data(Structure):
	_fields_ = [
		("MoveAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LookupTrack", FInterpLookupTrack),
	]

class  UInterpTrackMoveAxis(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackMoveAxis", UInterpTrackMoveAxis_Data),
	]


class  UInterpTrackSkelControlScale_Data(Structure):
	_fields_ = [
		("SkelControlName", FName),
	]

class  UInterpTrackSkelControlScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackSkelControlScale", UInterpTrackSkelControlScale_Data),
	]


class  UInterpTrackSkelControlStrength_Data(Structure):
	_fields_ = [
		("SkelControlName", FName),
	]

class  UInterpTrackSkelControlStrength(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackSkelControlStrength", UInterpTrackSkelControlStrength_Data),
	]


class  UInterpTrackSlomo_Data(Structure):
	_fields_ = []

class  UInterpTrackSlomo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackFloatBase", UInterpTrackFloatBase_Data),
		("UInterpTrackSlomo", UInterpTrackSlomo_Data),
	]


class  UInterpTrackHeadTracking_Data(Structure):
	_fields_ = [
		("HeadTrackingTrack", TArray_FHeadTrackingKey),
		("TrackControllerName", TArray_FName),
		("LookAtActorRadius", c_float),
		("bDisableBeyondLimit", c_bool, 1),
		("bLookAtPawns", c_bool, 1),
		("", c_ulong, 0),
		("MaxLookAtTime", c_float),
		("MinLookAtTime", c_float),
		("MaxInterestTime", c_float),
		("ActorClassesToLookAt", TArray_UClassPtr),
		("TargetBoneNames", TArray_FName),
	]

class  UInterpTrackHeadTracking(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackHeadTracking", UInterpTrackHeadTracking_Data),
	]


class  UInterpTrackLinearColorBase_Data(Structure):
	_fields_ = [
		("LinearColorTrack", FInterpCurveLinearColor),
		("CurveTension", c_float),
	]

class  UInterpTrackLinearColorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackLinearColorBase", UInterpTrackLinearColorBase_Data),
	]


class  UInterpTrackLinearColorProp_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
	]

class  UInterpTrackLinearColorProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackLinearColorBase", UInterpTrackLinearColorBase_Data),
		("UInterpTrackLinearColorProp", UInterpTrackLinearColorProp_Data),
	]


class  UInterpTrackMove_Data(Structure):
	_fields_ = [
		("PosTrack", FInterpCurveVector),
		("EulerTrack", FInterpCurveVector),
		("LookupTrack", FInterpLookupTrack),
		("LookAtGroupName", FName),
		("LinCurveTension", c_float),
		("AngCurveTension", c_float),
		("bUseQuatInterpolation", c_bool, 1),
		("bShowArrowAtKeys", c_bool, 1),
		("bDisableMovement", c_bool, 1),
		("bShowTranslationOnCurveEd", c_bool, 1),
		("bShowRotationOnCurveEd", c_bool, 1),
		("bHide3DTrack", c_bool, 1),
		("", c_ulong, 0),
		("MoveFrame", c_ubyte),
		("RotMode", c_ubyte),
	]

class  UInterpTrackMove(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackMove", UInterpTrackMove_Data),
	]


class  UInterpTrackParticleReplay_Data(Structure):
	_fields_ = [
		("TrackKeys", TArray_FParticleReplayTrackKey),
		("bIsCapturingReplay", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackParticleReplay(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackParticleReplay", UInterpTrackParticleReplay_Data),
	]


class  UInterpTrackTeleport_Data(Structure):
	_fields_ = [
		("TeleportKeys", TArray_FTeleportKeyData),
	]

class  UInterpTrackTeleport(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackTeleport", UInterpTrackTeleport_Data),
	]


class  UInterpTrackToggle_Data(Structure):
	_fields_ = [
		("ToggleTrack", TArray_FToggleTrackKey),
		("bActivateSystemEachUpdate", c_bool, 1),
		("bActivateWithJustAttachedFlag", c_bool, 1),
		("bFireEventsWhenForwards", c_bool, 1),
		("bFireEventsWhenBackwards", c_bool, 1),
		("bFireEventsWhenJumpingForwards", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackToggle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackToggle", UInterpTrackToggle_Data),
	]


class  UInterpTrackVectorBase_Data(Structure):
	_fields_ = [
		("VectorTrack", FInterpCurveVector),
		("CurveTension", c_float),
	]

class  UInterpTrackVectorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
	]


class  UInterpTrackAudioMaster_Data(Structure):
	_fields_ = []

class  UInterpTrackAudioMaster(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
		("UInterpTrackAudioMaster", UInterpTrackAudioMaster_Data),
	]


class  UInterpTrackColorProp_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
	]

class  UInterpTrackColorProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
		("UInterpTrackColorProp", UInterpTrackColorProp_Data),
	]


class  UInterpTrackColorScale_Data(Structure):
	_fields_ = []

class  UInterpTrackColorScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
		("UInterpTrackColorScale", UInterpTrackColorScale_Data),
	]


class  UInterpTrackSound_Data(Structure):
	_fields_ = [
		("Sounds", TArray_FSoundTrackKey),
		("bPlayOnReverse", c_bool, 1),
		("bContinueSoundOnMatineeEnd", c_bool, 1),
		("bSuppressSubtitles", c_bool, 1),
		("bTreatAsDialogue", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackSound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
		("UInterpTrackSound", UInterpTrackSound_Data),
	]


class  UInterpTrackVectorMaterialParam_Data(Structure):
	_fields_ = [
		("Materials", TArray_FMaterialReferenceList),
		("Material", POINTER(UMaterialInterface)),
		("ParamName", FName),
		("bNeedsMaterialRefsUpdate", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackVectorMaterialParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
		("UInterpTrackVectorMaterialParam", UInterpTrackVectorMaterialParam_Data),
	]


class  UInterpTrackVectorProp_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
	]

class  UInterpTrackVectorProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVectorBase", UInterpTrackVectorBase_Data),
		("UInterpTrackVectorProp", UInterpTrackVectorProp_Data),
	]


class  UInterpTrackVisibility_Data(Structure):
	_fields_ = [
		("VisibilityTrack", TArray_FVisibilityTrackKey),
		("bFireEventsWhenForwards", c_bool, 1),
		("bFireEventsWhenBackwards", c_bool, 1),
		("bFireEventsWhenJumpingForwards", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackVisibility(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrack", UInterpTrack_Data),
		("UInterpTrackVisibility", UInterpTrackVisibility_Data),
	]


class  UInterpTrackInst_Data(Structure):
	_fields_ = []

class  UInterpTrackInst(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
	]


class  UInterpTrackInstAnimControl_Data(Structure):
	_fields_ = [
		("LastUpdatePosition", c_float),
		("ResetLocation", FVector),
		("ResetRotation", FRotator),
		("bLastAnimFinished", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackInstAnimControl(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstAnimControl", UInterpTrackInstAnimControl_Data),
	]


class  UInterpTrackInstAudioMaster_Data(Structure):
	_fields_ = []

class  UInterpTrackInstAudioMaster(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstAudioMaster", UInterpTrackInstAudioMaster_Data),
	]


class  UInterpTrackInstColorScale_Data(Structure):
	_fields_ = []

class  UInterpTrackInstColorScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstColorScale", UInterpTrackInstColorScale_Data),
	]


class  UInterpTrackInstComment_Data(Structure):
	_fields_ = [
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstComment(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstComment", UInterpTrackInstComment_Data),
	]


class  UInterpTrackInstDirector_Data(Structure):
	_fields_ = [
		("OldViewTarget", POINTER(AActor)),
		("OldRenderingOverrides", FRenderingPerformanceOverrides),
	]

class  UInterpTrackInstDirector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstDirector", UInterpTrackInstDirector_Data),
	]


class  UInterpTrackInstEvent_Data(Structure):
	_fields_ = [
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstEvent", UInterpTrackInstEvent_Data),
	]


class  UInterpTrackInstFaceFX_Data(Structure):
	_fields_ = [
		("bFirstUpdate", c_bool, 1),
		("", c_ulong, 0),
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstFaceFX(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstFaceFX", UInterpTrackInstFaceFX_Data),
	]


class  UInterpTrackInstFade_Data(Structure):
	_fields_ = []

class  UInterpTrackInstFade(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstFade", UInterpTrackInstFade_Data),
	]


class  UInterpTrackInstFloatMaterialParam_Data(Structure):
	_fields_ = [
		("MICInfos", TArray_FFloatMaterialParamMICData),
		("InstancedTrack", POINTER(UInterpTrackFloatMaterialParam)),
	]

class  UInterpTrackInstFloatMaterialParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstFloatMaterialParam", UInterpTrackInstFloatMaterialParam_Data),
	]


class  UInterpTrackInstFloatParticleParam_Data(Structure):
	_fields_ = [
		("ResetFloat", c_float),
	]

class  UInterpTrackInstFloatParticleParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstFloatParticleParam", UInterpTrackInstFloatParticleParam_Data),
	]


class  UInterpTrackInstHeadTracking_Data(Structure):
	_fields_ = [
		("Action", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Unknown2", c_ubyte, 0x),
		("Mesh", POINTER(USkeletalMeshComponent)),
		("TrackControls", TArray_USkelControlLookAtPtr),
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstHeadTracking(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstHeadTracking", UInterpTrackInstHeadTracking_Data),
	]


class  UInterpTrackInstMorphWeight_Data(Structure):
	_fields_ = []

class  UInterpTrackInstMorphWeight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstMorphWeight", UInterpTrackInstMorphWeight_Data),
	]


class  UInterpTrackInstMove_Data(Structure):
	_fields_ = [
		("ResetLocation", FVector),
		("ResetRotation", FRotator),
		("Unknown1", c_ubyte, 0x),
		("InitialTM", FMatrix),
		("InitialQuat", FQuat),
	]

class  UInterpTrackInstMove(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstMove", UInterpTrackInstMove_Data),
	]


class  UInterpTrackInstParticleReplay_Data(Structure):
	_fields_ = [
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstParticleReplay(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstParticleReplay", UInterpTrackInstParticleReplay_Data),
	]


class  UInterpTrackInstProperty_Data(Structure):
	_fields_ = [
		("PropertyUpdateCallback", POINTER(UFunction)),
		("PropertyOuterObjectInst", POINTER(UObject)),
	]

class  UInterpTrackInstProperty(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstProperty", UInterpTrackInstProperty_Data),
	]


class  UInterpTrackInstBoolProp_Data(Structure):
	_fields_ = [
		("BoolProp", FPointer),
		("BitMask", c_int),
		("Resetc_bool", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackInstBoolProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstProperty", UInterpTrackInstProperty_Data),
		("UInterpTrackInstBoolProp", UInterpTrackInstBoolProp_Data),
	]


class  UInterpTrackInstColorProp_Data(Structure):
	_fields_ = [
		("ColorProp", FPointer),
		("ResetColor", FColor),
	]

class  UInterpTrackInstColorProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstProperty", UInterpTrackInstProperty_Data),
		("UInterpTrackInstColorProp", UInterpTrackInstColorProp_Data),
	]


class  UInterpTrackInstFloatProp_Data(Structure):
	_fields_ = [
		("FloatProp", FPointer),
		("ResetFloat", c_float),
	]

class  UInterpTrackInstFloatProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstProperty", UInterpTrackInstProperty_Data),
		("UInterpTrackInstFloatProp", UInterpTrackInstFloatProp_Data),
	]


class  UInterpTrackInstLinearColorProp_Data(Structure):
	_fields_ = [
		("ColorProp", FPointer),
		("ResetColor", FLinearColor),
	]

class  UInterpTrackInstLinearColorProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstProperty", UInterpTrackInstProperty_Data),
		("UInterpTrackInstLinearColorProp", UInterpTrackInstLinearColorProp_Data),
	]


class  UInterpTrackInstVectorProp_Data(Structure):
	_fields_ = [
		("VectorProp", FPointer),
		("ResetVector", FVector),
	]

class  UInterpTrackInstVectorProp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstProperty", UInterpTrackInstProperty_Data),
		("UInterpTrackInstVectorProp", UInterpTrackInstVectorProp_Data),
	]


class  UInterpTrackInstSkelControlScale_Data(Structure):
	_fields_ = []

class  UInterpTrackInstSkelControlScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstSkelControlScale", UInterpTrackInstSkelControlScale_Data),
	]


class  UInterpTrackInstSkelControlStrength_Data(Structure):
	_fields_ = [
		("bSavedControlledByAnimMetaData", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackInstSkelControlStrength(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstSkelControlStrength", UInterpTrackInstSkelControlStrength_Data),
	]


class  UInterpTrackInstSlomo_Data(Structure):
	_fields_ = [
		("OldTimeDilation", c_float),
	]

class  UInterpTrackInstSlomo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstSlomo", UInterpTrackInstSlomo_Data),
	]


class  UInterpTrackInstSound_Data(Structure):
	_fields_ = [
		("LastUpdatePosition", c_float),
		("PlayAudioComp", POINTER(UAudioComponent)),
	]

class  UInterpTrackInstSound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstSound", UInterpTrackInstSound_Data),
	]


class  UInterpTrackInstTeleport_Data(Structure):
	_fields_ = [
		("ResetLocation", FVector),
		("ResetRotation", FRotator),
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstTeleport(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstTeleport", UInterpTrackInstTeleport_Data),
	]


class  UInterpTrackInstToggle_Data(Structure):
	_fields_ = [
		("Action", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LastUpdatePosition", c_float),
		("bSavedActiveState", c_bool, 1),
		("", c_ulong, 0),
	]

class  UInterpTrackInstToggle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstToggle", UInterpTrackInstToggle_Data),
	]


class  UInterpTrackInstVectorMaterialParam_Data(Structure):
	_fields_ = [
		("MICInfos", TArray_FVectorMaterialParamMICData),
		("InstancedTrack", POINTER(UInterpTrackVectorMaterialParam)),
	]

class  UInterpTrackInstVectorMaterialParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstVectorMaterialParam", UInterpTrackInstVectorMaterialParam_Data),
	]


class  UInterpTrackInstVisibility_Data(Structure):
	_fields_ = [
		("Action", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LastUpdatePosition", c_float),
	]

class  UInterpTrackInstVisibility(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterpTrackInst", UInterpTrackInst_Data),
		("UInterpTrackInstVisibility", UInterpTrackInstVisibility_Data),
	]


class  UMaterialExpressionAbs_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionAbs(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionAbs", UMaterialExpressionAbs_Data),
	]


class  UMaterialExpressionAdd_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionAdd(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionAdd", UMaterialExpressionAdd_Data),
	]


class  UMaterialExpressionAppendVector_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionAppendVector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionAppendVector", UMaterialExpressionAppendVector_Data),
	]


class  UMaterialExpressionArcCosine_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionArcCosine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionArcCosine", UMaterialExpressionArcCosine_Data),
	]


class  UMaterialExpressionArcSine_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionArcSine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionArcSine", UMaterialExpressionArcSine_Data),
	]


class  UMaterialExpressionArcTangent_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionArcTangent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionArcTangent", UMaterialExpressionArcTangent_Data),
	]


class  UMaterialExpressionArcTangent2_Data(Structure):
	_fields_ = [
		("InputX", FExpressionInput),
		("InputY", FExpressionInput),
	]

class  UMaterialExpressionArcTangent2(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionArcTangent2", UMaterialExpressionArcTangent2_Data),
	]


class  UMaterialExpressionBlendModeBase_Data(Structure):
	_fields_ = [
		("Base", FExpressionInput),
		("Blend", FExpressionInput),
	]

class  UMaterialExpressionBlendModeBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
	]


class  UMaterialExpressionzColorBurn_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzColorBurn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzColorBurn", UMaterialExpressionzColorBurn_Data),
	]


class  UMaterialExpressionzColorDodge_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzColorDodge(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzColorDodge", UMaterialExpressionzColorDodge_Data),
	]


class  UMaterialExpressionzExclusion_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzExclusion(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzExclusion", UMaterialExpressionzExclusion_Data),
	]


class  UMaterialExpressionzHardLight_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzHardLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzHardLight", UMaterialExpressionzHardLight_Data),
	]


class  UMaterialExpressionzLinearBurn_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzLinearBurn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzLinearBurn", UMaterialExpressionzLinearBurn_Data),
	]


class  UMaterialExpressionzLinearLight_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzLinearLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzLinearLight", UMaterialExpressionzLinearLight_Data),
	]


class  UMaterialExpressionzOverlay_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzOverlay(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzOverlay", UMaterialExpressionzOverlay_Data),
	]


class  UMaterialExpressionzPinLight_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzPinLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzPinLight", UMaterialExpressionzPinLight_Data),
	]


class  UMaterialExpressionzScreen_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzScreen(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzScreen", UMaterialExpressionzScreen_Data),
	]


class  UMaterialExpressionzSoftLight_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzSoftLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzSoftLight", UMaterialExpressionzSoftLight_Data),
	]


class  UMaterialExpressionzVividLight_Data(Structure):
	_fields_ = []

class  UMaterialExpressionzVividLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBlendModeBase", UMaterialExpressionBlendModeBase_Data),
		("UMaterialExpressionzVividLight", UMaterialExpressionzVividLight_Data),
	]


class  UMaterialExpressionBumpOffset_Data(Structure):
	_fields_ = [
		("Coordinate", FExpressionInput),
		("Height", FExpressionInput),
		("HeightRatio", c_float),
		("ReferencePlane", c_float),
	]

class  UMaterialExpressionBumpOffset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBumpOffset", UMaterialExpressionBumpOffset_Data),
	]


class  UMaterialExpressionBumpOffsetEx_Data(Structure):
	_fields_ = [
		("Coordinate", FExpressionInput),
		("Height", FExpressionInput),
		("HeightRatio", FExpressionInput),
		("ReferencePlane", FExpressionInput),
	]

class  UMaterialExpressionBumpOffsetEx(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBumpOffsetEx", UMaterialExpressionBumpOffsetEx_Data),
	]


class  UMaterialExpressionBumpOffsetSloped_Data(Structure):
	_fields_ = [
		("Coordinate", FExpressionInput),
		("NormalTexture", POINTER(UTexture2D)),
		("HeightTexture", POINTER(UTexture2D)),
		("HeightRatio", c_float),
		("ReferencePlane", c_float),
		("Iterations", c_int),
	]

class  UMaterialExpressionBumpOffsetSloped(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionBumpOffsetSloped", UMaterialExpressionBumpOffsetSloped_Data),
	]


class  UMaterialExpressionCameraVector_Data(Structure):
	_fields_ = []

class  UMaterialExpressionCameraVector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCameraVector", UMaterialExpressionCameraVector_Data),
	]


class  UMaterialExpressionCameraWorldPosition_Data(Structure):
	_fields_ = []

class  UMaterialExpressionCameraWorldPosition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCameraWorldPosition", UMaterialExpressionCameraWorldPosition_Data),
	]


class  UMaterialExpressionCeil_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionCeil(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCeil", UMaterialExpressionCeil_Data),
	]


class  UMaterialExpressionClamp_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("Min", FExpressionInput),
		("Max", FExpressionInput),
	]

class  UMaterialExpressionClamp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionClamp", UMaterialExpressionClamp_Data),
	]


class  UMaterialExpressionComment_Data(Structure):
	_fields_ = [
		("PosX", c_int),
		("PosY", c_int),
		("SizeX", c_int),
		("SizeY", c_int),
		("Text", FString),
	]

class  UMaterialExpressionComment(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionComment", UMaterialExpressionComment_Data),
	]


class  UMaterialExpressionComponentMask_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("R", c_bool, 1),
		("G", c_bool, 1),
		("B", c_bool, 1),
		("A", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionComponentMask(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionComponentMask", UMaterialExpressionComponentMask_Data),
	]


class  UMaterialExpressionCompound_Data(Structure):
	_fields_ = [
		("MaterialExpressions", TArray_UMaterialExpressionPtr),
		("Caption", FString),
		("bExpanded", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionCompound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCompound", UMaterialExpressionCompound_Data),
	]


class  UMaterialExpressionConstant_Data(Structure):
	_fields_ = [
		("R", c_float),
	]

class  UMaterialExpressionConstant(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionConstant", UMaterialExpressionConstant_Data),
	]


class  UMaterialExpressionConstant2Vector_Data(Structure):
	_fields_ = [
		("R", c_float),
		("G", c_float),
	]

class  UMaterialExpressionConstant2Vector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionConstant2Vector", UMaterialExpressionConstant2Vector_Data),
	]


class  UMaterialExpressionConstant3Vector_Data(Structure):
	_fields_ = [
		("R", c_float),
		("G", c_float),
		("B", c_float),
	]

class  UMaterialExpressionConstant3Vector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionConstant3Vector", UMaterialExpressionConstant3Vector_Data),
	]


class  UMaterialExpressionConstant4Vector_Data(Structure):
	_fields_ = [
		("R", c_float),
		("G", c_float),
		("B", c_float),
		("A", c_float),
	]

class  UMaterialExpressionConstant4Vector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionConstant4Vector", UMaterialExpressionConstant4Vector_Data),
	]


class  UMaterialExpressionConstantBiasScale_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("Bias", c_float),
		("Scale", c_float),
	]

class  UMaterialExpressionConstantBiasScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionConstantBiasScale", UMaterialExpressionConstantBiasScale_Data),
	]


class  UMaterialExpressionConstantClamp_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("Min", c_float),
		("Max", c_float),
	]

class  UMaterialExpressionConstantClamp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionConstantClamp", UMaterialExpressionConstantClamp_Data),
	]


class  UMaterialExpressionCosine_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("Period", c_float),
	]

class  UMaterialExpressionCosine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCosine", UMaterialExpressionCosine_Data),
	]


class  UMaterialExpressionCrossProduct_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionCrossProduct(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCrossProduct", UMaterialExpressionCrossProduct_Data),
	]


class  UMaterialExpressionCustom_Data(Structure):
	_fields_ = [
		("Code", FString),
		("OutputType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Description", FString),
		("Inputs", TArray_FCustomInput),
	]

class  UMaterialExpressionCustom(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCustom", UMaterialExpressionCustom_Data),
	]


class  UMaterialExpressionCustomTexture_Data(Structure):
	_fields_ = [
		("Texture", POINTER(UTexture)),
	]

class  UMaterialExpressionCustomTexture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionCustomTexture", UMaterialExpressionCustomTexture_Data),
	]


class  UMaterialExpressionDdx_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionDdx(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDdx", UMaterialExpressionDdx_Data),
	]


class  UMaterialExpressionDdy_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionDdy(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDdy", UMaterialExpressionDdy_Data),
	]


class  UMaterialExpressionDegrees_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionDegrees(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDegrees", UMaterialExpressionDegrees_Data),
	]


class  UMaterialExpressionDepthBiasedAlpha_Data(Structure):
	_fields_ = [
		("bNormalize", c_bool, 1),
		("", c_ulong, 0),
		("BiasScale", c_float),
		("Alpha", FExpressionInput),
		("Bias", FExpressionInput),
	]

class  UMaterialExpressionDepthBiasedAlpha(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDepthBiasedAlpha", UMaterialExpressionDepthBiasedAlpha_Data),
	]


class  UMaterialExpressionDepthBiasedBlend_Data(Structure):
	_fields_ = [
		("bNormalize", c_bool, 1),
		("", c_ulong, 0),
		("BiasScale", c_float),
		("RGB", FExpressionInput),
		("Alpha", FExpressionInput),
		("Bias", FExpressionInput),
	]

class  UMaterialExpressionDepthBiasedBlend(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDepthBiasedBlend", UMaterialExpressionDepthBiasedBlend_Data),
	]


class  UMaterialExpressionDepthOfFieldFunction_Data(Structure):
	_fields_ = [
		("FunctionValue", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Depth", FExpressionInput),
	]

class  UMaterialExpressionDepthOfFieldFunction(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDepthOfFieldFunction", UMaterialExpressionDepthOfFieldFunction_Data),
	]


class  UMaterialExpressionDeriveNormalZ_Data(Structure):
	_fields_ = [
		("InXY", FExpressionInput),
	]

class  UMaterialExpressionDeriveNormalZ(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDeriveNormalZ", UMaterialExpressionDeriveNormalZ_Data),
	]


class  UMaterialExpressionDesaturation_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("Percent", FExpressionInput),
		("LuminanceFactors", FLinearColor),
	]

class  UMaterialExpressionDesaturation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDesaturation", UMaterialExpressionDesaturation_Data),
	]


class  UMaterialExpressionDestColor_Data(Structure):
	_fields_ = []

class  UMaterialExpressionDestColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDestColor", UMaterialExpressionDestColor_Data),
	]


class  UMaterialExpressionDestDepth_Data(Structure):
	_fields_ = [
		("bNormalize", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionDestDepth(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDestDepth", UMaterialExpressionDestDepth_Data),
	]


class  UMaterialExpressionDistance_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDistance", UMaterialExpressionDistance_Data),
	]


class  UMaterialExpressionDivide_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionDivide(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDivide", UMaterialExpressionDivide_Data),
	]


class  UMaterialExpressionDominantSkyLight_Data(Structure):
	_fields_ = [
		("bUseTimeOfDay", c_bool, 1),
		("", c_ulong, 0),
		("TimeOfDayMax", c_float),
		("TimeOfDayMin", c_float),
	]

class  UMaterialExpressionDominantSkyLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDominantSkyLight", UMaterialExpressionDominantSkyLight_Data),
	]


class  UMaterialExpressionDotProduct_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionDotProduct(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDotProduct", UMaterialExpressionDotProduct_Data),
	]


class  UMaterialExpressionDynamicParameter_Data(Structure):
	_fields_ = [
		("ParamNames", TArray_FString),
	]

class  UMaterialExpressionDynamicParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDynamicParameter", UMaterialExpressionDynamicParameter_Data),
	]


class  UMaterialExpressionMeshEmitterDynamicParameter_Data(Structure):
	_fields_ = []

class  UMaterialExpressionMeshEmitterDynamicParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionDynamicParameter", UMaterialExpressionDynamicParameter_Data),
		("UMaterialExpressionMeshEmitterDynamicParameter", UMaterialExpressionMeshEmitterDynamicParameter_Data),
	]


class  UMaterialExpressionExp_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionExp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionExp", UMaterialExpressionExp_Data),
	]


class  UMaterialExpressionExp2_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionExp2(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionExp2", UMaterialExpressionExp2_Data),
	]


class  UMaterialExpressionFloor_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionFloor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFloor", UMaterialExpressionFloor_Data),
	]


class  UMaterialExpressionFluidNormal_Data(Structure):
	_fields_ = [
		("Coordinates", FExpressionInput),
	]

class  UMaterialExpressionFluidNormal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFluidNormal", UMaterialExpressionFluidNormal_Data),
	]


class  UMaterialExpressionFmod_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionFmod(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFmod", UMaterialExpressionFmod_Data),
	]


class  UMaterialExpressionFoliageImpulseDirection_Data(Structure):
	_fields_ = []

class  UMaterialExpressionFoliageImpulseDirection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFoliageImpulseDirection", UMaterialExpressionFoliageImpulseDirection_Data),
	]


class  UMaterialExpressionFoliageNormalizedRotationAxisAndAngle_Data(Structure):
	_fields_ = []

class  UMaterialExpressionFoliageNormalizedRotationAxisAndAngle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFoliageNormalizedRotationAxisAndAngle", UMaterialExpressionFoliageNormalizedRotationAxisAndAngle_Data),
	]


class  UMaterialExpressionFontSample_Data(Structure):
	_fields_ = [
		("Font", POINTER(UFont)),
		("FontTexturePage", c_int),
	]

class  UMaterialExpressionFontSample(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFontSample", UMaterialExpressionFontSample_Data),
	]


class  UMaterialExpressionFontSampleParameter_Data(Structure):
	_fields_ = [
		("ParameterName", FName),
		("ExpressionGUID", FGuid),
	]

class  UMaterialExpressionFontSampleParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFontSample", UMaterialExpressionFontSample_Data),
		("UMaterialExpressionFontSampleParameter", UMaterialExpressionFontSampleParameter_Data),
	]


class  UMaterialExpressionFrac_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionFrac(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFrac", UMaterialExpressionFrac_Data),
	]


class  UMaterialExpressionFresnel_Data(Structure):
	_fields_ = [
		("Exponent", c_float),
		("Normal", FExpressionInput),
	]

class  UMaterialExpressionFresnel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionFresnel", UMaterialExpressionFresnel_Data),
	]


class  UMaterialExpressionGradient_Data(Structure):
	_fields_ = [
		("Coordinates", FExpressionInput),
		("GradientStyle", c_ubyte),
		("AddressX", c_ubyte),
		("AddressY", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ForegroundColor", FLinearColor),
		("BackgroundColor", FLinearColor),
		("ForegroundOffset", FVector2D),
		("BackgroundOffset", FVector2D),
		("bReverse", c_bool, 1),
		("bSmoothInOut", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionGradient(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionGradient", UMaterialExpressionGradient_Data),
	]


class  UMaterialExpressionIf_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
		("AGreaterThanB", FExpressionInput),
		("AEqualsB", FExpressionInput),
		("ALessThanB", FExpressionInput),
	]

class  UMaterialExpressionIf(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionIf", UMaterialExpressionIf_Data),
	]


class  UMaterialExpressionLength_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionLength(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLength", UMaterialExpressionLength_Data),
	]


class  UMaterialExpressionLensFlareIntensity_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLensFlareIntensity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLensFlareIntensity", UMaterialExpressionLensFlareIntensity_Data),
	]


class  UMaterialExpressionLensFlareOcclusion_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLensFlareOcclusion(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLensFlareOcclusion", UMaterialExpressionLensFlareOcclusion_Data),
	]


class  UMaterialExpressionLensFlareRadialDistance_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLensFlareRadialDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLensFlareRadialDistance", UMaterialExpressionLensFlareRadialDistance_Data),
	]


class  UMaterialExpressionLensFlareRayDistance_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLensFlareRayDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLensFlareRayDistance", UMaterialExpressionLensFlareRayDistance_Data),
	]


class  UMaterialExpressionLensFlareSourceDistance_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLensFlareSourceDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLensFlareSourceDistance", UMaterialExpressionLensFlareSourceDistance_Data),
	]


class  UMaterialExpressionLightmapUVs_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLightmapUVs(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLightmapUVs", UMaterialExpressionLightmapUVs_Data),
	]


class  UMaterialExpressionLightmassReplace_Data(Structure):
	_fields_ = [
		("Realtime", FExpressionInput),
		("Lightmass", FExpressionInput),
	]

class  UMaterialExpressionLightmassReplace(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLightmassReplace", UMaterialExpressionLightmassReplace_Data),
	]


class  UMaterialExpressionLightVector_Data(Structure):
	_fields_ = []

class  UMaterialExpressionLightVector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLightVector", UMaterialExpressionLightVector_Data),
	]


class  UMaterialExpressionLinearInterpolate_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
		("Alpha", FExpressionInput),
	]

class  UMaterialExpressionLinearInterpolate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLinearInterpolate", UMaterialExpressionLinearInterpolate_Data),
	]


class  UMaterialExpressionLog_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionLog(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLog", UMaterialExpressionLog_Data),
	]


class  UMaterialExpressionLog10_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionLog10(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLog10", UMaterialExpressionLog10_Data),
	]


class  UMaterialExpressionLog2_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionLog2(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionLog2", UMaterialExpressionLog2_Data),
	]


class  UMaterialExpressionMax_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionMax(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionMax", UMaterialExpressionMax_Data),
	]


class  UMaterialExpressionMeshEmitterVertexColor_Data(Structure):
	_fields_ = []

class  UMaterialExpressionMeshEmitterVertexColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionMeshEmitterVertexColor", UMaterialExpressionMeshEmitterVertexColor_Data),
	]


class  UMaterialExpressionMin_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionMin(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionMin", UMaterialExpressionMin_Data),
	]


class  UMaterialExpressionMultiply_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionMultiply(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionMultiply", UMaterialExpressionMultiply_Data),
	]


class  UMaterialExpressionMultiplyAndAdd_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
		("WeightB", FExpressionInput),
	]

class  UMaterialExpressionMultiplyAndAdd(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionMultiplyAndAdd", UMaterialExpressionMultiplyAndAdd_Data),
	]


class  UMaterialExpressionNormalize_Data(Structure):
	_fields_ = [
		("VectorInput", FExpressionInput),
	]

class  UMaterialExpressionNormalize(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionNormalize", UMaterialExpressionNormalize_Data),
	]


class  UMaterialExpressionObjectOrientation_Data(Structure):
	_fields_ = []

class  UMaterialExpressionObjectOrientation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionObjectOrientation", UMaterialExpressionObjectOrientation_Data),
	]


class  UMaterialExpressionObjectRadius_Data(Structure):
	_fields_ = []

class  UMaterialExpressionObjectRadius(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionObjectRadius", UMaterialExpressionObjectRadius_Data),
	]


class  UMaterialExpressionObjectWorldPosition_Data(Structure):
	_fields_ = []

class  UMaterialExpressionObjectWorldPosition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionObjectWorldPosition", UMaterialExpressionObjectWorldPosition_Data),
	]


class  UMaterialExpressionOcclusionPercentage_Data(Structure):
	_fields_ = []

class  UMaterialExpressionOcclusionPercentage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionOcclusionPercentage", UMaterialExpressionOcclusionPercentage_Data),
	]


class  UMaterialExpressionOneMinus_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionOneMinus(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionOneMinus", UMaterialExpressionOneMinus_Data),
	]


class  UMaterialExpressionPanner_Data(Structure):
	_fields_ = [
		("Coordinate", FExpressionInput),
		("Time", FExpressionInput),
		("SpeedX", c_float),
		("SpeedY", c_float),
	]

class  UMaterialExpressionPanner(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionPanner", UMaterialExpressionPanner_Data),
	]


class  UMaterialExpressionParameter_Data(Structure):
	_fields_ = [
		("ParameterName", FName),
		("ExpressionGUID", FGuid),
	]

class  UMaterialExpressionParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionParameter", UMaterialExpressionParameter_Data),
	]


class  UMaterialExpressionScalarParameter_Data(Structure):
	_fields_ = [
		("DefaultValue", c_float),
	]

class  UMaterialExpressionScalarParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionParameter", UMaterialExpressionParameter_Data),
		("UMaterialExpressionScalarParameter", UMaterialExpressionScalarParameter_Data),
	]


class  UMaterialExpressionStaticComponentMaskParameter_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("DefaultR", c_bool, 1),
		("DefaultG", c_bool, 1),
		("DefaultB", c_bool, 1),
		("DefaultA", c_bool, 1),
		("", c_ulong, 0),
		("InstanceOverride", FPointer),
	]

class  UMaterialExpressionStaticComponentMaskParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionParameter", UMaterialExpressionParameter_Data),
		("UMaterialExpressionStaticComponentMaskParameter", UMaterialExpressionStaticComponentMaskParameter_Data),
	]


class  UMaterialExpressionStaticSwitchParameter_Data(Structure):
	_fields_ = [
		("DefaultValue", c_bool, 1),
		("ExtendedCaptionDisplay", c_bool, 1),
		("", c_ulong, 0),
		("A", FExpressionInput),
		("B", FExpressionInput),
		("InstanceOverride", FPointer),
	]

class  UMaterialExpressionStaticSwitchParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionParameter", UMaterialExpressionParameter_Data),
		("UMaterialExpressionStaticSwitchParameter", UMaterialExpressionStaticSwitchParameter_Data),
	]


class  UMaterialExpressionVectorParameter_Data(Structure):
	_fields_ = [
		("DefaultValue", FLinearColor),
	]

class  UMaterialExpressionVectorParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionParameter", UMaterialExpressionParameter_Data),
		("UMaterialExpressionVectorParameter", UMaterialExpressionVectorParameter_Data),
	]


class  UMaterialExpressionParticleMacroUV_Data(Structure):
	_fields_ = [
		("bUseViewSpace", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionParticleMacroUV(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionParticleMacroUV", UMaterialExpressionParticleMacroUV_Data),
	]


class  UMaterialExpressionPerInstanceRandom_Data(Structure):
	_fields_ = []

class  UMaterialExpressionPerInstanceRandom(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionPerInstanceRandom", UMaterialExpressionPerInstanceRandom_Data),
	]


class  UMaterialExpressionPixelDepth_Data(Structure):
	_fields_ = [
		("bNormalize", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionPixelDepth(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionPixelDepth", UMaterialExpressionPixelDepth_Data),
	]


class  UMaterialExpressionPower_Data(Structure):
	_fields_ = [
		("Base", FExpressionInput),
		("Exponent", FExpressionInput),
	]

class  UMaterialExpressionPower(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionPower", UMaterialExpressionPower_Data),
	]


class  UMaterialExpressionRadians_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionRadians(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionRadians", UMaterialExpressionRadians_Data),
	]


class  UMaterialExpressionRecipSquareRoot_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionRecipSquareRoot(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionRecipSquareRoot", UMaterialExpressionRecipSquareRoot_Data),
	]


class  UMaterialExpressionReflectionVector_Data(Structure):
	_fields_ = []

class  UMaterialExpressionReflectionVector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionReflectionVector", UMaterialExpressionReflectionVector_Data),
	]


class  UMaterialExpressionRotate3D_Data(Structure):
	_fields_ = [
		("Vec", FExpressionInput),
		("MatrixForward", FExpressionInput),
		("MatrixRight", FExpressionInput),
		("MatrixUp", FExpressionInput),
		("bTranspose", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionRotate3D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionRotate3D", UMaterialExpressionRotate3D_Data),
	]


class  UMaterialExpressionRotateAboutAxis_Data(Structure):
	_fields_ = [
		("NormalizedRotationAxisAndAngle", FExpressionInput),
		("PositionOnAxis", FExpressionInput),
		("Position", FExpressionInput),
	]

class  UMaterialExpressionRotateAboutAxis(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionRotateAboutAxis", UMaterialExpressionRotateAboutAxis_Data),
	]


class  UMaterialExpressionRotator_Data(Structure):
	_fields_ = [
		("Coordinate", FExpressionInput),
		("Time", FExpressionInput),
		("CenterX", c_float),
		("CenterY", c_float),
		("Speed", c_float),
	]

class  UMaterialExpressionRotator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionRotator", UMaterialExpressionRotator_Data),
	]


class  UMaterialExpressionSaturate_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionSaturate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSaturate", UMaterialExpressionSaturate_Data),
	]


class  UMaterialExpressionSceneDepth_Data(Structure):
	_fields_ = [
		("Coordinates", FExpressionInput),
		("bNormalize", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionSceneDepth(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSceneDepth", UMaterialExpressionSceneDepth_Data),
	]


class  UMaterialExpressionSceneTexture_Data(Structure):
	_fields_ = [
		("Coordinates", FExpressionInput),
		("SceneTextureType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ScreenAlign", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionSceneTexture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSceneTexture", UMaterialExpressionSceneTexture_Data),
	]


class  UMaterialExpressionScreenPosition_Data(Structure):
	_fields_ = [
		("ScreenAlign", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionScreenPosition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionScreenPosition", UMaterialExpressionScreenPosition_Data),
	]


class  UMaterialExpressionSine_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("Period", c_float),
	]

class  UMaterialExpressionSine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSine", UMaterialExpressionSine_Data),
	]


class  UMaterialExpressionSphereMask_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
		("Radius", FExpressionInput),
		("Hardness", FExpressionInput),
		("AttenuationRadius", c_float),
		("HardnessPercent", c_float),
	]

class  UMaterialExpressionSphereMask(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSphereMask", UMaterialExpressionSphereMask_Data),
	]


class  UMaterialExpressionSPHFluidNormal_Data(Structure):
	_fields_ = [
		("DefaultTexture", POINTER(UTexture)),
	]

class  UMaterialExpressionSPHFluidNormal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSPHFluidNormal", UMaterialExpressionSPHFluidNormal_Data),
	]


class  UMaterialExpressionSPHFluidThickness_Data(Structure):
	_fields_ = [
		("DefaultTexture", POINTER(UTexture)),
	]

class  UMaterialExpressionSPHFluidThickness(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSPHFluidThickness", UMaterialExpressionSPHFluidThickness_Data),
	]


class  UMaterialExpressionSPHFluidVertexColor_Data(Structure):
	_fields_ = [
		("DefaultTexture", POINTER(UTexture)),
	]

class  UMaterialExpressionSPHFluidVertexColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSPHFluidVertexColor", UMaterialExpressionSPHFluidVertexColor_Data),
	]


class  UMaterialExpressionSquareRoot_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionSquareRoot(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSquareRoot", UMaterialExpressionSquareRoot_Data),
	]


class  UMaterialExpressionSteepParallaxOffset_Data(Structure):
	_fields_ = [
		("ParallaxTexture", POINTER(UTexture2D)),
		("NumSteps", c_int),
		("bSmoothAndUnlit", c_bool, 1),
		("", c_ulong, 0),
		("HeightScaleInput", FExpressionInput),
	]

class  UMaterialExpressionSteepParallaxOffset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSteepParallaxOffset", UMaterialExpressionSteepParallaxOffset_Data),
	]


class  UMaterialExpressionSubtract_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
	]

class  UMaterialExpressionSubtract(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSubtract", UMaterialExpressionSubtract_Data),
	]


class  UMaterialExpressionSwizzle_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("SwizzleMask", FString),
	]

class  UMaterialExpressionSwizzle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionSwizzle", UMaterialExpressionSwizzle_Data),
	]


class  UMaterialExpressionTangent_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
	]

class  UMaterialExpressionTangent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTangent", UMaterialExpressionTangent_Data),
	]


class  UMaterialExpressionTerrainLayerCoords_Data(Structure):
	_fields_ = [
		("MappingType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MappingScale", c_float),
		("MappingRotation", c_float),
		("MappingPanU", c_float),
		("MappingPanV", c_float),
	]

class  UMaterialExpressionTerrainLayerCoords(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTerrainLayerCoords", UMaterialExpressionTerrainLayerCoords_Data),
	]


class  UMaterialExpressionTerrainLayerWeight_Data(Structure):
	_fields_ = [
		("InstanceOverride", FPointer),
		("Base", FExpressionInput),
		("Layer", FExpressionInput),
		("ParameterName", FName),
		("PreviewWeight", c_float),
		("ExpressionGUID", FGuid),
	]

class  UMaterialExpressionTerrainLayerWeight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTerrainLayerWeight", UMaterialExpressionTerrainLayerWeight_Data),
	]


class  UMaterialExpressionTerrainTextureCoordinate_Data(Structure):
	_fields_ = [
		("WeightMap", c_bool, 1),
		("", c_ulong, 0),
		("LayerIndex", c_int),
		("LayerProjection", c_ubyte),
	]

class  UMaterialExpressionTerrainTextureCoordinate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTerrainTextureCoordinate", UMaterialExpressionTerrainTextureCoordinate_Data),
	]


class  UMaterialExpressionTextureCoordinate_Data(Structure):
	_fields_ = [
		("CoordinateIndex", c_int),
		("UTiling", c_float),
		("VTiling", c_float),
		("UnMirrorU", c_bool, 1),
		("UnMirrorV", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionTextureCoordinate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureCoordinate", UMaterialExpressionTextureCoordinate_Data),
	]


class  UMaterialExpressionTextureDimensions_Data(Structure):
	_fields_ = [
		("Texture", POINTER(UTexture)),
	]

class  UMaterialExpressionTextureDimensions(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureDimensions", UMaterialExpressionTextureDimensions_Data),
	]


class  UMaterialExpressionTextureSample_Data(Structure):
	_fields_ = [
		("Texture", POINTER(UTexture)),
		("Coordinates", FExpressionInput),
	]

class  UMaterialExpressionTextureSample(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
	]


class  UMaterialExpressionDepthBiasBlend_Data(Structure):
	_fields_ = [
		("bNormalize", c_bool, 1),
		("", c_ulong, 0),
		("BiasScale", c_float),
		("Bias", FExpressionInput),
	]

class  UMaterialExpressionDepthBiasBlend(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionDepthBiasBlend", UMaterialExpressionDepthBiasBlend_Data),
	]


class  UMaterialExpressionFlipBookSample_Data(Structure):
	_fields_ = []

class  UMaterialExpressionFlipBookSample(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionFlipBookSample", UMaterialExpressionFlipBookSample_Data),
	]


class  UMaterialExpressionMeshSubUV_Data(Structure):
	_fields_ = []

class  UMaterialExpressionMeshSubUV(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionMeshSubUV", UMaterialExpressionMeshSubUV_Data),
	]


class  UMaterialExpressionMeshSubUVBlend_Data(Structure):
	_fields_ = []

class  UMaterialExpressionMeshSubUVBlend(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionMeshSubUV", UMaterialExpressionMeshSubUV_Data),
		("UMaterialExpressionMeshSubUVBlend", UMaterialExpressionMeshSubUVBlend_Data),
	]


class  UMaterialExpressionParticleSubUV_Data(Structure):
	_fields_ = []

class  UMaterialExpressionParticleSubUV(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionParticleSubUV", UMaterialExpressionParticleSubUV_Data),
	]


class  UMaterialExpressionTextureSampleParameter_Data(Structure):
	_fields_ = [
		("ParameterName", FName),
		("ExpressionGUID", FGuid),
	]

class  UMaterialExpressionTextureSampleParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
	]


class  UMaterialExpressionTextureSampleParameter2D_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTextureSampleParameter2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameter2D", UMaterialExpressionTextureSampleParameter2D_Data),
	]


class  UMaterialExpressionAntialiasedTextureMask_Data(Structure):
	_fields_ = [
		("Threshold", c_float),
		("Channel", c_ubyte),
	]

class  UMaterialExpressionAntialiasedTextureMask(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameter2D", UMaterialExpressionTextureSampleParameter2D_Data),
		("UMaterialExpressionAntialiasedTextureMask", UMaterialExpressionAntialiasedTextureMask_Data),
	]


class  UMaterialExpressionTextureSampleParameterMeshSubUV_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTextureSampleParameterMeshSubUV(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameter2D", UMaterialExpressionTextureSampleParameter2D_Data),
		("UMaterialExpressionTextureSampleParameterMeshSubUV", UMaterialExpressionTextureSampleParameterMeshSubUV_Data),
	]


class  UMaterialExpressionTextureSampleParameterMeshSubUVBlend_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTextureSampleParameterMeshSubUVBlend(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameter2D", UMaterialExpressionTextureSampleParameter2D_Data),
		("UMaterialExpressionTextureSampleParameterMeshSubUV", UMaterialExpressionTextureSampleParameterMeshSubUV_Data),
		("UMaterialExpressionTextureSampleParameterMeshSubUVBlend", UMaterialExpressionTextureSampleParameterMeshSubUVBlend_Data),
	]


class  UMaterialExpressionTextureSampleParameterSubUV_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTextureSampleParameterSubUV(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameter2D", UMaterialExpressionTextureSampleParameter2D_Data),
		("UMaterialExpressionTextureSampleParameterSubUV", UMaterialExpressionTextureSampleParameterSubUV_Data),
	]


class  UMaterialExpressionTextureSampleParameterCube_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTextureSampleParameterCube(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameterCube", UMaterialExpressionTextureSampleParameterCube_Data),
	]


class  UMaterialExpressionTextureSampleParameterMovie_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTextureSampleParameterMovie(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameterMovie", UMaterialExpressionTextureSampleParameterMovie_Data),
	]


class  UMaterialExpressionTextureSampleParameterNormal_Data(Structure):
	_fields_ = [
		("InstanceOverride", FPointer),
	]

class  UMaterialExpressionTextureSampleParameterNormal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSample", UMaterialExpressionTextureSample_Data),
		("UMaterialExpressionTextureSampleParameter", UMaterialExpressionTextureSampleParameter_Data),
		("UMaterialExpressionTextureSampleParameterNormal", UMaterialExpressionTextureSampleParameterNormal_Data),
	]


class  UMaterialExpressionTextureSplat_Data(Structure):
	_fields_ = [
		("BackdropTexture", POINTER(UTexture)),
		("OverlayTexture", POINTER(UTexture)),
		("UVs", FExpressionInput),
		("Offset", FExpressionInput),
		("Scale", FExpressionInput),
	]

class  UMaterialExpressionTextureSplat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTextureSplat", UMaterialExpressionTextureSplat_Data),
	]


class  UMaterialExpressionTime_Data(Structure):
	_fields_ = [
		("bIgnorePause", c_bool, 1),
		("", c_ulong, 0),
	]

class  UMaterialExpressionTime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTime", UMaterialExpressionTime_Data),
	]


class  UMaterialExpressionTransform_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("TransformSourceType", c_ubyte),
		("TransformType", c_ubyte),
	]

class  UMaterialExpressionTransform(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTransform", UMaterialExpressionTransform_Data),
	]


class  UMaterialExpressionTransformPosition_Data(Structure):
	_fields_ = [
		("Input", FExpressionInput),
		("TransformType", c_ubyte),
	]

class  UMaterialExpressionTransformPosition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTransformPosition", UMaterialExpressionTransformPosition_Data),
	]


class  UMaterialExpressionTwoSidedSign_Data(Structure):
	_fields_ = []

class  UMaterialExpressionTwoSidedSign(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionTwoSidedSign", UMaterialExpressionTwoSidedSign_Data),
	]


class  UMaterialExpressionVectorIf_Data(Structure):
	_fields_ = [
		("A", FExpressionInput),
		("B", FExpressionInput),
		("IfTrue", FExpressionInput),
		("IfFalse", FExpressionInput),
		("CompareFunc", c_ubyte),
	]

class  UMaterialExpressionVectorIf(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionVectorIf", UMaterialExpressionVectorIf_Data),
	]


class  UMaterialExpressionVertexColor_Data(Structure):
	_fields_ = []

class  UMaterialExpressionVertexColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionVertexColor", UMaterialExpressionVertexColor_Data),
	]


class  UMaterialExpressionWindDirectionAndSpeed_Data(Structure):
	_fields_ = []

class  UMaterialExpressionWindDirectionAndSpeed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionWindDirectionAndSpeed", UMaterialExpressionWindDirectionAndSpeed_Data),
	]


class  UMaterialExpressionWorldAmbientColor_Data(Structure):
	_fields_ = []

class  UMaterialExpressionWorldAmbientColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionWorldAmbientColor", UMaterialExpressionWorldAmbientColor_Data),
	]


class  UMaterialExpressionWorldLightColor_Data(Structure):
	_fields_ = []

class  UMaterialExpressionWorldLightColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionWorldLightColor", UMaterialExpressionWorldLightColor_Data),
	]


class  UMaterialExpressionWorldNormal_Data(Structure):
	_fields_ = []

class  UMaterialExpressionWorldNormal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionWorldNormal", UMaterialExpressionWorldNormal_Data),
	]


class  UMaterialExpressionWorldPosition_Data(Structure):
	_fields_ = []

class  UMaterialExpressionWorldPosition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UMaterialExpression", UMaterialExpression_Data),
		("UMaterialExpressionWorldPosition", UMaterialExpressionWorldPosition_Data),
	]


class  UMaterialInstance_Data(Structure):
	_fields_ = [
		("PhysMaterial", POINTER(UPhysicalMaterial)),
		("Parent", POINTER(UMaterialInterface)),
		("PhysMaterialMask", POINTER(UTexture2D)),
		("PhysMaterialMaskUVChannel", c_int),
		("BlackPhysicalMaterial", POINTER(UPhysicalMaterial)),
		("WhitePhysicalMaterial", POINTER(UPhysicalMaterial)),
		("bHasStaticPermutationResource", c_bool, 1),
		("bStaticPermutationDirty", c_bool, 1),
		("ReentrantFlag", c_bool, 1),
		("bNeedsMaterialFlattening", c_bool, 1),
		("", c_ulong, 0),
		("StaticParameters", FPointer * 2),
		("StaticPermutationResources", FPointer * 2),
		("Resources", FPointer * 3),
		("ReferencedTextures", TArray_UTexturePtr),
		("ParentLightingGuid", FGuid),
	]

class  UMaterialInstance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UMaterialInterface", UMaterialInterface_Data),
		("UMaterialInstance", UMaterialInstance_Data),
	]


class  UMaterialInstanceConstant_Data(Structure):
	_fields_ = [
		("FontParameterValues", TArray_FFontParameterValue),
		("ScalarParameterValues", TArray_FScalarParameterValue),
		("TextureParameterValues", TArray_FTextureParameterValue),
		("VectorParameterValues", TArray_FVectorParameterValue),
	]

class  UMaterialInstanceConstant(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UMaterialInterface", UMaterialInterface_Data),
		("UMaterialInstance", UMaterialInstance_Data),
		("UMaterialInstanceConstant", UMaterialInstanceConstant_Data),
	]


class  UMaterialInstanceTimeVarying_Data(Structure):
	_fields_ = [
		("bAutoActivateAll", c_bool, 1),
		("", c_ulong, 0),
		("Duration", c_float),
		("FontParameterValues", TArray_FFontParameterValueOverTime),
		("ScalarParameterValues", TArray_FScalarParameterValueOverTime),
		("TextureParameterValues", TArray_FTextureParameterValueOverTime),
		("VectorParameterValues", TArray_FVectorParameterValueOverTime),
	]

class  UMaterialInstanceTimeVarying(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UMaterialInterface", UMaterialInterface_Data),
		("UMaterialInstance", UMaterialInstance_Data),
		("UMaterialInstanceTimeVarying", UMaterialInstanceTimeVarying_Data),
	]


class  AEmitter_Data(Structure):
	_fields_ = [
		("ParticleSystemComponent", POINTER(UParticleSystemComponent)),
		("LightEnvironment", POINTER(UDynamicLightEnvironmentComponent)),
		("bDestroyOnSystemFinish", c_bool, 1),
		("bPostUpdateTickGroup", c_bool, 1),
		("bAudioEnabled", c_bool, 1),
		("bCurrentlyActive", c_bool, 1),
		("", c_ulong, 0),
	]

class  AEmitter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AEmitter", AEmitter_Data),
	]


class  AEmitterCameraLensEffectBase_Data(Structure):
	_fields_ = [
		("PS_CameraEffect", POINTER(UParticleSystem)),
		("PS_CameraEffectNonExtremeContent", POINTER(UParticleSystem)),
		("BaseFOV", c_float),
		("DistFromCamera", c_float),
		("bAllowMultipleInstances", c_bool, 1),
		("", c_ulong, 0),
		("EmittersToTreatAsSame", TArray_UClassPtr),
		("BaseCamera", POINTER(ACamera)),
	]

class  AEmitterCameraLensEffectBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AEmitter", AEmitter_Data),
		("AEmitterCameraLensEffectBase", AEmitterCameraLensEffectBase_Data),
	]


class  AParticleEventManager_Data(Structure):
	_fields_ = []

class  AParticleEventManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AParticleEventManager", AParticleEventManager_Data),
	]


class  UParticleSystemComponent_Data(Structure):
	_fields_ = [
		("Template", POINTER(UParticleSystem)),
		("LightEnvironmentClass", POINTER(UClass)),
		("LightEnvironmentSharedInstigator", POINTER(AActor)),
		("MaxLightEnvironmentPooledReuses", c_int),
		("EmitterInstances", TArray_FPointer),
		("SMComponents", TArray_UStaticMeshComponentPtr),
		("SMMaterialInterfaces", TArray_UMaterialInterfacePtr),
		("SkelMeshComponents", TArray_USkeletalMeshComponentPtr),
		("ViewMBInfoArray", TArray_FViewParticleEmitterInstanceMotionBlurInfo),
		("bFullResolution", c_bool, 1),
		("bAutoActivate", c_bool, 1),
		("bWasCompleted", c_bool, 1),
		("bSuppressSpawning", c_bool, 1),
		("bWasDeactivated", c_bool, 1),
		("bResetOnDetach", c_bool, 1),
		("bUpdateOnDedicatedServer", c_bool, 1),
		("bJustAttached", c_bool, 1),
		("bIsActive", c_bool, 1),
		("bHasBeenActivated", c_bool, 1),
		("bWarmingUp", c_bool, 1),
		("bIsCachedInPool", c_bool, 1),
		("bCanBeReclaimedByPool", c_bool, 1),
		("bOverrideLODMethod", c_bool, 1),
		("bSkipUpdateDynamicDataDuringTick", c_bool, 1),
		("bSkipBoundsUpdate", c_bool, 1),
		("bUpdateComponentInTick", c_bool, 1),
		("bDeferredBeamUpdate", c_bool, 1),
		("bIgnoreCollision", c_bool, 1),
		("bForcedInActive", c_bool, 1),
		("bIsWarmingUp", c_bool, 1),
		("bIsViewRelevanceDirty", c_bool, 1),
		("bRecacheViewRelevance", c_bool, 1),
		("bLODUpdatePending", c_bool, 1),
		("bSkipSpawnCountCheck", c_bool, 1),
		("AudioEnabled", c_bool, 1),
		("bStartEventPlayed", c_bool, 1),
		("bCheckForKillWhileIdle", c_bool, 1),
		("", c_ulong, 0),
		("InstanceParameters", TArray_FParticleSysParam),
		("OldPosition", FVector),
		("PartSysVelocity", FVector),
		("WarmupTime", c_float),
		("LODLevel", c_int),
		("SecondsBeforeInactive", c_float),
		("TimeSinceLastForceUpdateTransform", c_float),
		("MaxTimeBeforeForceUpdateTransform", c_float),
		("AccumTickTime", c_float),
		("LODMethod", c_ubyte),
		("ReplayState", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CachedViewRelevanceFlags", TArray_FMaterialViewRelevance),
		("ReplayClips", TArray_UParticleSystemReplayPtr),
		("ReplayClipIDNumber", c_int),
		("ReplayFrameIndex", c_int),
		("AccumLODDistanceCheckTime", c_float),
		("SpawnEvents", TArray_FParticleEventSpawnData),
		("DeathEvents", TArray_FParticleEventDeathData),
		("CollisionEvents", TArray_FParticleEventCollideData),
		("TraceEvents", TArray_FParticleEventTraceData),
		("KismetEvents", TArray_FParticleEventKismetData),
		("ReleaseResourcesFence", FPointer),
		("CustomTimeDilation", c_float),
		("EmitterDelay", c_float),
		("AudioEventDelay", c_float),
		("LoopingAkPlayingInfo", FAkPlayingInfo),
		("__OnSystemFinished__Delegate", FScriptDelegate),
	]

class  UParticleSystemComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UParticleSystemComponent", UParticleSystemComponent_Data),
	]


class  UDistributionFloatParticleParameter_Data(Structure):
	_fields_ = []

class  UDistributionFloatParticleParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatConstant", UDistributionFloatConstant_Data),
		("UDistributionFloatParameterBase", UDistributionFloatParameterBase_Data),
		("UDistributionFloatParticleParameter", UDistributionFloatParticleParameter_Data),
	]


class  UDistributionVectorParticleParameter_Data(Structure):
	_fields_ = []

class  UDistributionVectorParticleParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionVector", UDistributionVector_Data),
		("UDistributionVectorConstant", UDistributionVectorConstant_Data),
		("UDistributionVectorParameterBase", UDistributionVectorParameterBase_Data),
		("UDistributionVectorParticleParameter", UDistributionVectorParticleParameter_Data),
	]


class  UParticleEmitter_Data(Structure):
	_fields_ = [
		("EmitterName", FName),
		("SubUVDataOffset", c_int),
		("EmitterRenderMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LODLevels", TArray_UParticleLODLevelPtr),
		("ConvertedModules", c_bool, 1),
		("bCollapsed", c_bool, 1),
		("bIsSoloing", c_bool, 1),
		("bCookedOut", c_bool, 1),
		("", c_ulong, 0),
		("PeakActiveParticles", c_int),
		("InitialAllocationCount", c_int),
		("MediumDetailSpawnRateScale", c_float),
	]

class  UParticleEmitter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleEmitter", UParticleEmitter_Data),
	]


class  UParticleSpriteEmitter_Data(Structure):
	_fields_ = []

class  UParticleSpriteEmitter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleEmitter", UParticleEmitter_Data),
		("UParticleSpriteEmitter", UParticleSpriteEmitter_Data),
	]


class  UParticleLODLevel_Data(Structure):
	_fields_ = [
		("Level", c_int),
		("bEnabled", c_bool, 1),
		("ConvertedModules", c_bool, 1),
		("", c_ulong, 0),
		("RequiredModule", POINTER(UParticleModuleRequired)),
		("Modules", TArray_UParticleModulePtr),
		("TypeDataModule", POINTER(UParticleModule)),
		("SpawnModule", POINTER(UParticleModuleSpawn)),
		("EventGenerator", POINTER(UParticleModuleEventGenerator)),
		("SpawningModules", TArray_UParticleModuleSpawnBasePtr),
		("SpawnModules", TArray_UParticleModulePtr),
		("UpdateModules", TArray_UParticleModulePtr),
		("OrbitModules", TArray_UParticleModuleOrbitPtr),
		("EventReceiverModules", TArray_UParticleModuleEventReceiverBasePtr),
		("PeakActiveParticles", c_int),
	]

class  UParticleLODLevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleLODLevel", UParticleLODLevel_Data),
	]


class  UParticleModule_Data(Structure):
	_fields_ = [
		("bSpawnModule", c_bool, 1),
		("bUpdateModule", c_bool, 1),
		("bFinalUpdateModule", c_bool, 1),
		("bCurvesAsColor", c_bool, 1),
		("b3DDrawMode", c_bool, 1),
		("bSupported3DDrawMode", c_bool, 1),
		("bEnabled", c_bool, 1),
		("bEditable", c_bool, 1),
		("LODDuplicate", c_bool, 1),
		("bSupportsRandomSeed", c_bool, 1),
		("bRequiresLoopingNotification", c_bool, 1),
		("", c_ulong, 0),
		("LODValidity", c_ubyte),
	]

class  UParticleModule(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
	]


class  UParticleModuleAccelerationBase_Data(Structure):
	_fields_ = [
		("bAlwaysInWorldSpace", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleAccelerationBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAccelerationBase", UParticleModuleAccelerationBase_Data),
	]


class  UParticleModuleAcceleration_Data(Structure):
	_fields_ = [
		("Acceleration", FRawDistributionVector),
		("bApplyOwnerScale", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleAcceleration(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAccelerationBase", UParticleModuleAccelerationBase_Data),
		("UParticleModuleAcceleration", UParticleModuleAcceleration_Data),
	]


class  UParticleModuleAccelerationOverLifetime_Data(Structure):
	_fields_ = [
		("AccelOverLife", FRawDistributionVector),
	]

class  UParticleModuleAccelerationOverLifetime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAccelerationBase", UParticleModuleAccelerationBase_Data),
		("UParticleModuleAccelerationOverLifetime", UParticleModuleAccelerationOverLifetime_Data),
	]


class  UParticleModuleAttractorBase_Data(Structure):
	_fields_ = []

class  UParticleModuleAttractorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAttractorBase", UParticleModuleAttractorBase_Data),
	]


class  UParticleModuleAttractorLine_Data(Structure):
	_fields_ = [
		("EndPoint0", FVector),
		("EndPoint1", FVector),
		("Range", FRawDistributionFloat),
		("Strength", FRawDistributionFloat),
	]

class  UParticleModuleAttractorLine(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAttractorBase", UParticleModuleAttractorBase_Data),
		("UParticleModuleAttractorLine", UParticleModuleAttractorLine_Data),
	]


class  UParticleModuleAttractorParticle_Data(Structure):
	_fields_ = [
		("EmitterName", FName),
		("Range", FRawDistributionFloat),
		("bStrengthByDistance", c_bool, 1),
		("bAffectBaseVelocity", c_bool, 1),
		("bRenewSource", c_bool, 1),
		("bInheritSourceVel", c_bool, 1),
		("", c_ulong, 0),
		("Strength", FRawDistributionFloat),
		("SelectionMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LastSelIndex", c_int),
	]

class  UParticleModuleAttractorParticle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAttractorBase", UParticleModuleAttractorBase_Data),
		("UParticleModuleAttractorParticle", UParticleModuleAttractorParticle_Data),
	]


class  UParticleModuleAttractorPoint_Data(Structure):
	_fields_ = [
		("Position", FRawDistributionVector),
		("Range", FRawDistributionFloat),
		("Strength", FRawDistributionFloat),
		("StrengthByDistance", c_bool, 1),
		("bAffectBaseVelocity", c_bool, 1),
		("bOverrideVelocity", c_bool, 1),
		("bUseWorldSpacePosition", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleAttractorPoint(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleAttractorBase", UParticleModuleAttractorBase_Data),
		("UParticleModuleAttractorPoint", UParticleModuleAttractorPoint_Data),
	]


class  UParticleModuleBeamBase_Data(Structure):
	_fields_ = []

class  UParticleModuleBeamBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleBeamBase", UParticleModuleBeamBase_Data),
	]


class  UParticleModuleBeamModifier_Data(Structure):
	_fields_ = [
		("ModifierType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("PositionOptions", FBeamModifierOptions),
		("Position", FRawDistributionVector),
		("TangentOptions", FBeamModifierOptions),
		("Tangent", FRawDistributionVector),
		("bAbsoluteTangent", c_bool, 1),
		("", c_ulong, 0),
		("StrengthOptions", FBeamModifierOptions),
		("Strength", FRawDistributionFloat),
	]

class  UParticleModuleBeamModifier(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleBeamBase", UParticleModuleBeamBase_Data),
		("UParticleModuleBeamModifier", UParticleModuleBeamModifier_Data),
	]


class  UParticleModuleBeamNoise_Data(Structure):
	_fields_ = [
		("bLowFreq_Enabled", c_bool, 1),
		("bNRScaleEmitterTime", c_bool, 1),
		("bSmooth", c_bool, 1),
		("bNoiseLock", c_bool, 1),
		("bOscillate", c_bool, 1),
		("bUseNoiseTangents", c_bool, 1),
		("bTargetNoise", c_bool, 1),
		("bApplyNoiseScale", c_bool, 1),
		("", c_ulong, 0),
		("Frequency", c_int),
		("Frequency_LowRange", c_int),
		("NoiseRange", FRawDistributionVector),
		("NoiseRangeScale", FRawDistributionFloat),
		("NoiseSpeed", FRawDistributionVector),
		("NoiseLockRadius", c_float),
		("NoiseLockTime", c_float),
		("NoiseTension", c_float),
		("NoiseTangentStrength", FRawDistributionFloat),
		("NoiseTessellation", c_int),
		("FrequencyDistance", c_float),
		("NoiseScale", FRawDistributionFloat),
	]

class  UParticleModuleBeamNoise(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleBeamBase", UParticleModuleBeamBase_Data),
		("UParticleModuleBeamNoise", UParticleModuleBeamNoise_Data),
	]


class  UParticleModuleBeamSource_Data(Structure):
	_fields_ = [
		("SourceMethod", c_ubyte),
		("SourceTangentMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("SourceName", FName),
		("bSourceAbsolute", c_bool, 1),
		("bLockSource", c_bool, 1),
		("bLockSourceTangent", c_bool, 1),
		("bLockSourceStength", c_bool, 1),
		("", c_ulong, 0),
		("Source", FRawDistributionVector),
		("SourceTangent", FRawDistributionVector),
		("SourceStrength", FRawDistributionFloat),
	]

class  UParticleModuleBeamSource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleBeamBase", UParticleModuleBeamBase_Data),
		("UParticleModuleBeamSource", UParticleModuleBeamSource_Data),
	]


class  UParticleModuleBeamTarget_Data(Structure):
	_fields_ = [
		("TargetMethod", c_ubyte),
		("TargetTangentMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TargetName", FName),
		("Target", FRawDistributionVector),
		("bTargetAbsolute", c_bool, 1),
		("bLockTarget", c_bool, 1),
		("bLockTargetTangent", c_bool, 1),
		("bLockTargetStength", c_bool, 1),
		("", c_ulong, 0),
		("TargetTangent", FRawDistributionVector),
		("TargetStrength", FRawDistributionFloat),
		("LockRadius", c_float),
	]

class  UParticleModuleBeamTarget(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleBeamBase", UParticleModuleBeamBase_Data),
		("UParticleModuleBeamTarget", UParticleModuleBeamTarget_Data),
	]


class  UParticleModuleBeamTrace_Data(Structure):
	_fields_ = [
		("TraceExtent", FVector),
		("TraceRotation", FRotator),
		("TraceMaxDistance", c_float),
		("UpdateDelay", c_float),
		("MaxTraceEvents", c_int),
		("bTraceWorld", c_bool, 1),
		("bTraceActors", c_bool, 1),
		("bTraceBlockers", c_bool, 1),
		("bTraceMaterials", c_bool, 1),
		("bTraceProjectiles", c_bool, 1),
		("bTracePhysicsVolumes", c_bool, 1),
		("bTraceComplexCollision", c_bool, 1),
		("", c_ulong, 0),
		("LastDistance", c_float),
		("LastUpdateTime", c_float),
	]

class  UParticleModuleBeamTrace(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleBeamBase", UParticleModuleBeamBase_Data),
		("UParticleModuleBeamTarget", UParticleModuleBeamTarget_Data),
		("UParticleModuleBeamTrace", UParticleModuleBeamTrace_Data),
	]


class  UParticleModuleCameraBase_Data(Structure):
	_fields_ = []

class  UParticleModuleCameraBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleCameraBase", UParticleModuleCameraBase_Data),
	]


class  UParticleModuleCameraOffset_Data(Structure):
	_fields_ = [
		("CameraOffset", FRawDistributionFloat),
		("bSpawnTimeOnly", c_bool, 1),
		("", c_ulong, 0),
		("UpdateMethod", c_ubyte),
	]

class  UParticleModuleCameraOffset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleCameraBase", UParticleModuleCameraBase_Data),
		("UParticleModuleCameraOffset", UParticleModuleCameraOffset_Data),
	]


class  UParticleModuleCollisionBase_Data(Structure):
	_fields_ = []

class  UParticleModuleCollisionBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleCollisionBase", UParticleModuleCollisionBase_Data),
	]


class  UParticleModuleCollision_Data(Structure):
	_fields_ = [
		("DampingFactor", FRawDistributionVector),
		("DampingFactorRotation", FRawDistributionVector),
		("MaxCollisions", FRawDistributionFloat),
		("CollisionCompletionOption", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bApplyPhysics", c_bool, 1),
		("bPawnsDoNotDecrementCount", c_bool, 1),
		("bOnlyVerticalNormalsDecrementCount", c_bool, 1),
		("bDropDetail", c_bool, 1),
		("bCollideOnlyIfVisible", c_bool, 1),
		("", c_ulong, 0),
		("ParticleMass", FRawDistributionFloat),
		("DirScalar", c_float),
		("VerticalFudgeFactor", c_float),
		("DelayAmount", FRawDistributionFloat),
		("MaxCollisionDistance", c_float),
	]

class  UParticleModuleCollision(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleCollisionBase", UParticleModuleCollisionBase_Data),
		("UParticleModuleCollision", UParticleModuleCollision_Data),
	]


class  UParticleModuleCollisionActor_Data(Structure):
	_fields_ = [
		("ActorsToCollideWith", TArray_FName),
		("bCheckPawnCollisions", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleCollisionActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleCollisionBase", UParticleModuleCollisionBase_Data),
		("UParticleModuleCollision", UParticleModuleCollision_Data),
		("UParticleModuleCollisionActor", UParticleModuleCollisionActor_Data),
	]


class  UParticleModuleColorBase_Data(Structure):
	_fields_ = []

class  UParticleModuleColorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
	]


class  UParticleModuleColor_Data(Structure):
	_fields_ = [
		("StartColor", FRawDistributionVector),
		("StartAlpha", FRawDistributionFloat),
		("bClampAlpha", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleColor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
		("UParticleModuleColor", UParticleModuleColor_Data),
	]


class  UParticleModuleColor_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleColor_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
		("UParticleModuleColor", UParticleModuleColor_Data),
		("UParticleModuleColor_Seeded", UParticleModuleColor_Seeded_Data),
	]


class  UParticleModuleColorByParameter_Data(Structure):
	_fields_ = [
		("ColorParam", FName),
		("DefaultColor", FColor),
	]

class  UParticleModuleColorByParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
		("UParticleModuleColorByParameter", UParticleModuleColorByParameter_Data),
	]


class  UParticleModuleColorOverLife_Data(Structure):
	_fields_ = [
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
		("bClampAlpha", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleColorOverLife(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
		("UParticleModuleColorOverLife", UParticleModuleColorOverLife_Data),
	]


class  UParticleModuleColorScaleOverDensity_Data(Structure):
	_fields_ = [
		("ColorScaleOverDensity", FRawDistributionVector),
		("AlphaScaleOverDensity", FRawDistributionFloat),
	]

class  UParticleModuleColorScaleOverDensity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
		("UParticleModuleColorScaleOverDensity", UParticleModuleColorScaleOverDensity_Data),
	]


class  UParticleModuleColorScaleOverLife_Data(Structure):
	_fields_ = [
		("ColorScaleOverLife", FRawDistributionVector),
		("AlphaScaleOverLife", FRawDistributionFloat),
		("bEmitterTime", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleColorScaleOverLife(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleColorBase", UParticleModuleColorBase_Data),
		("UParticleModuleColorScaleOverLife", UParticleModuleColorScaleOverLife_Data),
	]


class  UParticleModuleEventBase_Data(Structure):
	_fields_ = []

class  UParticleModuleEventBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleEventBase", UParticleModuleEventBase_Data),
	]


class  UParticleModuleEventGenerator_Data(Structure):
	_fields_ = [
		("Events", TArray_FParticleEvent_GenerateInfo),
	]

class  UParticleModuleEventGenerator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleEventBase", UParticleModuleEventBase_Data),
		("UParticleModuleEventGenerator", UParticleModuleEventGenerator_Data),
	]


class  UParticleModuleEventGeneratorDecal_Data(Structure):
	_fields_ = [
		("DecalMaterials", TArray_UMaterialInterfacePtr),
		("DecalWidth", c_float),
		("DecalHeight", c_float),
		("SizeVariance", c_float),
		("DecalThickness", c_float),
		("DecalLifeSpan", c_float),
		("DecalDepthBias", c_float),
		("DecalBlendRange", FVector2D),
		("bNoClip", c_bool, 1),
		("bProjectOnTerrain", c_bool, 1),
		("bProjectOnSkeletalMeshes", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleEventGeneratorDecal(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleEventBase", UParticleModuleEventBase_Data),
		("UParticleModuleEventGenerator", UParticleModuleEventGenerator_Data),
		("UParticleModuleEventGeneratorDecal", UParticleModuleEventGeneratorDecal_Data),
	]


class  UParticleModuleEventReceiverBase_Data(Structure):
	_fields_ = [
		("EventGeneratorType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("EventName", FName),
	]

class  UParticleModuleEventReceiverBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleEventBase", UParticleModuleEventBase_Data),
		("UParticleModuleEventReceiverBase", UParticleModuleEventReceiverBase_Data),
	]


class  UParticleModuleEventReceiverKillParticles_Data(Structure):
	_fields_ = [
		("bStopSpawning", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleEventReceiverKillParticles(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleEventBase", UParticleModuleEventBase_Data),
		("UParticleModuleEventReceiverBase", UParticleModuleEventReceiverBase_Data),
		("UParticleModuleEventReceiverKillParticles", UParticleModuleEventReceiverKillParticles_Data),
	]


class  UParticleModuleEventReceiverSpawn_Data(Structure):
	_fields_ = [
		("SpawnCount", FRawDistributionFloat),
		("bUseParticleTime", c_bool, 1),
		("bUsePSysLocation", c_bool, 1),
		("bInheritVelocity", c_bool, 1),
		("bInheritRotation", c_bool, 1),
		("", c_ulong, 0),
		("InheritVelocityScale", FRawDistributionVector),
	]

class  UParticleModuleEventReceiverSpawn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleEventBase", UParticleModuleEventBase_Data),
		("UParticleModuleEventReceiverBase", UParticleModuleEventReceiverBase_Data),
		("UParticleModuleEventReceiverSpawn", UParticleModuleEventReceiverSpawn_Data),
	]


class  UParticleModuleForceFieldBase_Data(Structure):
	_fields_ = [
		("ForceField", POINTER(UNxForceFieldComponent)),
	]

class  UParticleModuleForceFieldBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleForceFieldBase", UParticleModuleForceFieldBase_Data),
	]


class  UParticleModuleKillBase_Data(Structure):
	_fields_ = []

class  UParticleModuleKillBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleKillBase", UParticleModuleKillBase_Data),
	]


class  UParticleModuleKillBox_Data(Structure):
	_fields_ = [
		("LowerLeftCorner", FRawDistributionVector),
		("UpperRightCorner", FRawDistributionVector),
		("bAbsolute", c_bool, 1),
		("bKillInside", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleKillBox(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleKillBase", UParticleModuleKillBase_Data),
		("UParticleModuleKillBox", UParticleModuleKillBox_Data),
	]


class  UParticleModuleKillHeight_Data(Structure):
	_fields_ = [
		("Height", FRawDistributionFloat),
		("bAbsolute", c_bool, 1),
		("bFloor", c_bool, 1),
		("bApplyPSysScale", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleKillHeight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleKillBase", UParticleModuleKillBase_Data),
		("UParticleModuleKillHeight", UParticleModuleKillHeight_Data),
	]


class  UParticleModuleLifetimeBase_Data(Structure):
	_fields_ = []

class  UParticleModuleLifetimeBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLifetimeBase", UParticleModuleLifetimeBase_Data),
	]


class  UParticleModuleLifetime_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
	]

class  UParticleModuleLifetime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLifetimeBase", UParticleModuleLifetimeBase_Data),
		("UParticleModuleLifetime", UParticleModuleLifetime_Data),
	]


class  UParticleModuleLifetime_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleLifetime_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLifetimeBase", UParticleModuleLifetimeBase_Data),
		("UParticleModuleLifetime", UParticleModuleLifetime_Data),
		("UParticleModuleLifetime_Seeded", UParticleModuleLifetime_Seeded_Data),
	]


class  UParticleModuleLocationBase_Data(Structure):
	_fields_ = []

class  UParticleModuleLocationBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
	]


class  UParticleModuleLocation_Data(Structure):
	_fields_ = [
		("StartLocation", FRawDistributionVector),
	]

class  UParticleModuleLocation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocation", UParticleModuleLocation_Data),
	]


class  UParticleModuleLocation_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleLocation_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocation", UParticleModuleLocation_Data),
		("UParticleModuleLocation_Seeded", UParticleModuleLocation_Seeded_Data),
	]


class  UParticleModuleLocationBoneSocket_Data(Structure):
	_fields_ = [
		("SourceType", c_ubyte),
		("SelectionMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("UniversalOffset", FVector),
		("SourceLocations", TArray_FLocationBoneSocketInfo),
		("bUpdatePositionEachFrame", c_bool, 1),
		("bOrientMeshEmitters", c_bool, 1),
		("", c_ulong, 0),
		("SkelMeshActorParamName", FName),
	]

class  UParticleModuleLocationBoneSocket(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationBoneSocket", UParticleModuleLocationBoneSocket_Data),
	]


class  UParticleModuleLocationDirect_Data(Structure):
	_fields_ = [
		("Location", FRawDistributionVector),
		("LocationOffset", FRawDistributionVector),
		("ScaleFactor", FRawDistributionVector),
		("Direction", FRawDistributionVector),
	]

class  UParticleModuleLocationDirect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationDirect", UParticleModuleLocationDirect_Data),
	]


class  UParticleModuleLocationEmitter_Data(Structure):
	_fields_ = [
		("EmitterName", FName),
		("SelectionMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("InheritSourceVelocity", c_bool, 1),
		("bInheritSourceRotation", c_bool, 1),
		("", c_ulong, 0),
		("InheritSourceVelocityScale", c_float),
		("InheritSourceRotationScale", c_float),
	]

class  UParticleModuleLocationEmitter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationEmitter", UParticleModuleLocationEmitter_Data),
	]


class  UParticleModuleLocationEmitterDirect_Data(Structure):
	_fields_ = [
		("EmitterName", FName),
	]

class  UParticleModuleLocationEmitterDirect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationEmitterDirect", UParticleModuleLocationEmitterDirect_Data),
	]


class  UParticleModuleLocationPrimitiveBase_Data(Structure):
	_fields_ = [
		("Positive_X", c_bool, 1),
		("Positive_Y", c_bool, 1),
		("Positive_Z", c_bool, 1),
		("Negative_X", c_bool, 1),
		("Negative_Y", c_bool, 1),
		("Negative_Z", c_bool, 1),
		("SurfaceOnly", c_bool, 1),
		("Velocity", c_bool, 1),
		("", c_ulong, 0),
		("VelocityScale", FRawDistributionFloat),
		("StartLocation", FRawDistributionVector),
	]

class  UParticleModuleLocationPrimitiveBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationPrimitiveBase", UParticleModuleLocationPrimitiveBase_Data),
	]


class  UParticleModuleLocationPrimitiveCylinder_Data(Structure):
	_fields_ = [
		("RadialVelocity", c_bool, 1),
		("", c_ulong, 0),
		("StartRadius", FRawDistributionFloat),
		("StartHeight", FRawDistributionFloat),
		("HeightAxis", c_ubyte),
	]

class  UParticleModuleLocationPrimitiveCylinder(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationPrimitiveBase", UParticleModuleLocationPrimitiveBase_Data),
		("UParticleModuleLocationPrimitiveCylinder", UParticleModuleLocationPrimitiveCylinder_Data),
	]


class  UParticleModuleLocationPrimitiveCylinder_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleLocationPrimitiveCylinder_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationPrimitiveBase", UParticleModuleLocationPrimitiveBase_Data),
		("UParticleModuleLocationPrimitiveCylinder", UParticleModuleLocationPrimitiveCylinder_Data),
		("UParticleModuleLocationPrimitiveCylinder_Seeded", UParticleModuleLocationPrimitiveCylinder_Seeded_Data),
	]


class  UParticleModuleLocationPrimitiveSphere_Data(Structure):
	_fields_ = [
		("StartRadius", FRawDistributionFloat),
	]

class  UParticleModuleLocationPrimitiveSphere(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationPrimitiveBase", UParticleModuleLocationPrimitiveBase_Data),
		("UParticleModuleLocationPrimitiveSphere", UParticleModuleLocationPrimitiveSphere_Data),
	]


class  UParticleModuleLocationPrimitiveSphere_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleLocationPrimitiveSphere_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationPrimitiveBase", UParticleModuleLocationPrimitiveBase_Data),
		("UParticleModuleLocationPrimitiveSphere", UParticleModuleLocationPrimitiveSphere_Data),
		("UParticleModuleLocationPrimitiveSphere_Seeded", UParticleModuleLocationPrimitiveSphere_Seeded_Data),
	]


class  UParticleModuleLocationSkelVertSurface_Data(Structure):
	_fields_ = [
		("SourceType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("UniversalOffset", FVector),
		("bUpdatePositionEachFrame", c_bool, 1),
		("bOrientMeshEmitters", c_bool, 1),
		("bEnforceNormalCheck", c_bool, 1),
		("", c_ulong, 0),
		("SkelMeshActorParamName", FName),
		("ValidAssociatedBones", TArray_FName),
		("NormalToCompare", FVector),
		("NormalCheckToleranceDegrees", c_float),
		("NormalCheckTolerance", c_float),
		("ValidMaterialIndices", TArray_int),
	]

class  UParticleModuleLocationSkelVertSurface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleLocationSkelVertSurface", UParticleModuleLocationSkelVertSurface_Data),
	]


class  UParticleModuleSourceMovement_Data(Structure):
	_fields_ = [
		("SourceMovementScale", FRawDistributionVector),
	]

class  UParticleModuleSourceMovement(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleLocationBase", UParticleModuleLocationBase_Data),
		("UParticleModuleSourceMovement", UParticleModuleSourceMovement_Data),
	]


class  UParticleModuleMaterialBase_Data(Structure):
	_fields_ = []

class  UParticleModuleMaterialBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleMaterialBase", UParticleModuleMaterialBase_Data),
	]


class  UParticleModuleMaterialByParameter_Data(Structure):
	_fields_ = [
		("MaterialParameters", TArray_FName),
		("DefaultMaterials", TArray_UMaterialInterfacePtr),
	]

class  UParticleModuleMaterialByParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleMaterialBase", UParticleModuleMaterialBase_Data),
		("UParticleModuleMaterialByParameter", UParticleModuleMaterialByParameter_Data),
	]


class  UParticleModuleMeshMaterial_Data(Structure):
	_fields_ = [
		("MeshMaterials", TArray_UMaterialInterfacePtr),
	]

class  UParticleModuleMeshMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleMaterialBase", UParticleModuleMaterialBase_Data),
		("UParticleModuleMeshMaterial", UParticleModuleMeshMaterial_Data),
	]


class  UParticleModuleOrbitBase_Data(Structure):
	_fields_ = [
		("bUseEmitterTime", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleOrbitBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleOrbitBase", UParticleModuleOrbitBase_Data),
	]


class  UParticleModuleOrbit_Data(Structure):
	_fields_ = [
		("ChainMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("OffsetAmount", FRawDistributionVector),
		("OffsetOptions", FOrbitOptions),
		("RotationAmount", FRawDistributionVector),
		("RotationOptions", FOrbitOptions),
		("RotationRateAmount", FRawDistributionVector),
		("RotationRateOptions", FOrbitOptions),
	]

class  UParticleModuleOrbit(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleOrbitBase", UParticleModuleOrbitBase_Data),
		("UParticleModuleOrbit", UParticleModuleOrbit_Data),
	]


class  UParticleModuleOrientationBase_Data(Structure):
	_fields_ = []

class  UParticleModuleOrientationBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleOrientationBase", UParticleModuleOrientationBase_Data),
	]


class  UParticleModuleOrientationAxisLock_Data(Structure):
	_fields_ = [
		("LockAxisFlags", c_ubyte),
	]

class  UParticleModuleOrientationAxisLock(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleOrientationBase", UParticleModuleOrientationBase_Data),
		("UParticleModuleOrientationAxisLock", UParticleModuleOrientationAxisLock_Data),
	]


class  UParticleModuleParameterBase_Data(Structure):
	_fields_ = []

class  UParticleModuleParameterBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleParameterBase", UParticleModuleParameterBase_Data),
	]


class  UParticleModuleParameterDynamic_Data(Structure):
	_fields_ = [
		("DynamicParams", TArray_FEmitterDynamicParameter),
		("UpdateFlags", c_int),
		("bUsesVelocity", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleParameterDynamic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleParameterBase", UParticleModuleParameterBase_Data),
		("UParticleModuleParameterDynamic", UParticleModuleParameterDynamic_Data),
	]


class  UParticleModuleParameterDynamic_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleParameterDynamic_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleParameterBase", UParticleModuleParameterBase_Data),
		("UParticleModuleParameterDynamic", UParticleModuleParameterDynamic_Data),
		("UParticleModuleParameterDynamic_Seeded", UParticleModuleParameterDynamic_Seeded_Data),
	]


class  UParticleModuleRequired_Data(Structure):
	_fields_ = [
		("Material", POINTER(UMaterialInterface)),
		("ScreenAlignment", c_ubyte),
		("SortMode", c_ubyte),
		("ParticleBurstMethod", c_ubyte),
		("InterpolationMethod", c_ubyte),
		("EmitterNormalsMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bUseLocalSpace", c_bool, 1),
		("bKillOnDeactivate", c_bool, 1),
		("bKillOnCompleted", c_bool, 1),
		("bRequiresSorting", c_bool, 1),
		("bUseLegacyEmitterTime", c_bool, 1),
		("bEmitterDurationUseRange", c_bool, 1),
		("bDurationRecalcEachLoop", c_bool, 1),
		("bEmitterDelayUseRange", c_bool, 1),
		("bDelayFirstLoopOnly", c_bool, 1),
		("bScaleUV", c_bool, 1),
		("bDirectUV", c_bool, 1),
		("bUseMaxDrawCount", c_bool, 1),
		("", c_ulong, 0),
		("EmitterDuration", c_float),
		("EmitterDurationLow", c_float),
		("EmitterLoops", c_int),
		("SpawnRate", FRawDistributionFloat),
		("BurstList", TArray_FParticleBurst),
		("EmitterDelay", c_float),
		("EmitterDelayLow", c_float),
		("SubImages_Horizontal", c_int),
		("SubImages_Vertical", c_int),
		("RandomImageTime", c_float),
		("RandomImageChanges", c_int),
		("MaxDrawCount", c_int),
		("DownsampleThresholdScreenFraction", c_float),
		("NormalsSphereCenter", FVector),
		("NormalsCylinderDirection", FVector),
	]

class  UParticleModuleRequired(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRequired", UParticleModuleRequired_Data),
	]


class  UParticleModuleRotationBase_Data(Structure):
	_fields_ = []

class  UParticleModuleRotationBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationBase", UParticleModuleRotationBase_Data),
	]


class  UParticleModuleMeshRotation_Data(Structure):
	_fields_ = [
		("StartRotation", FRawDistributionVector),
		("bInheritParent", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleMeshRotation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationBase", UParticleModuleRotationBase_Data),
		("UParticleModuleMeshRotation", UParticleModuleMeshRotation_Data),
	]


class  UParticleModuleMeshRotation_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleMeshRotation_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationBase", UParticleModuleRotationBase_Data),
		("UParticleModuleMeshRotation", UParticleModuleMeshRotation_Data),
		("UParticleModuleMeshRotation_Seeded", UParticleModuleMeshRotation_Seeded_Data),
	]


class  UParticleModuleRotation_Data(Structure):
	_fields_ = [
		("StartRotation", FRawDistributionFloat),
	]

class  UParticleModuleRotation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationBase", UParticleModuleRotationBase_Data),
		("UParticleModuleRotation", UParticleModuleRotation_Data),
	]


class  UParticleModuleRotation_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleRotation_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationBase", UParticleModuleRotationBase_Data),
		("UParticleModuleRotation", UParticleModuleRotation_Data),
		("UParticleModuleRotation_Seeded", UParticleModuleRotation_Seeded_Data),
	]


class  UParticleModuleRotationOverLifetime_Data(Structure):
	_fields_ = [
		("RotationOverLife", FRawDistributionFloat),
		("Scale", c_bool, 1),
		("bIncrement", c_bool, 1),
		("bUseRelativeTime", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleRotationOverLifetime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationBase", UParticleModuleRotationBase_Data),
		("UParticleModuleRotationOverLifetime", UParticleModuleRotationOverLifetime_Data),
	]


class  UParticleModuleRotationRateBase_Data(Structure):
	_fields_ = []

class  UParticleModuleRotationRateBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
	]


class  UParticleModuleMeshRotationRate_Data(Structure):
	_fields_ = [
		("StartRotationRate", FRawDistributionVector),
	]

class  UParticleModuleMeshRotationRate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleMeshRotationRate", UParticleModuleMeshRotationRate_Data),
	]


class  UParticleModuleMeshRotationRate_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleMeshRotationRate_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleMeshRotationRate", UParticleModuleMeshRotationRate_Data),
		("UParticleModuleMeshRotationRate_Seeded", UParticleModuleMeshRotationRate_Seeded_Data),
	]


class  UParticleModuleMeshRotationRateMultiplyLife_Data(Structure):
	_fields_ = [
		("LifeMultiplier", FRawDistributionVector),
	]

class  UParticleModuleMeshRotationRateMultiplyLife(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleMeshRotationRateMultiplyLife", UParticleModuleMeshRotationRateMultiplyLife_Data),
	]


class  UParticleModuleMeshRotationRateOverLife_Data(Structure):
	_fields_ = [
		("RotRate", FRawDistributionVector),
		("bScaleRotRate", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleMeshRotationRateOverLife(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleMeshRotationRateOverLife", UParticleModuleMeshRotationRateOverLife_Data),
	]


class  UParticleModuleRotationRate_Data(Structure):
	_fields_ = [
		("StartRotationRate", FRawDistributionFloat),
	]

class  UParticleModuleRotationRate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleRotationRate", UParticleModuleRotationRate_Data),
	]


class  UParticleModuleRotationRate_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleRotationRate_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleRotationRate", UParticleModuleRotationRate_Data),
		("UParticleModuleRotationRate_Seeded", UParticleModuleRotationRate_Seeded_Data),
	]


class  UParticleModuleRotationRateMultiplyLife_Data(Structure):
	_fields_ = [
		("LifeMultiplier", FRawDistributionFloat),
	]

class  UParticleModuleRotationRateMultiplyLife(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleRotationRateBase", UParticleModuleRotationRateBase_Data),
		("UParticleModuleRotationRateMultiplyLife", UParticleModuleRotationRateMultiplyLife_Data),
	]


class  UParticleModuleSizeBase_Data(Structure):
	_fields_ = []

class  UParticleModuleSizeBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
	]


class  UParticleModuleSize_Data(Structure):
	_fields_ = [
		("StartSize", FRawDistributionVector),
	]

class  UParticleModuleSize(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSize", UParticleModuleSize_Data),
	]


class  UParticleModuleSize_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleSize_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSize", UParticleModuleSize_Data),
		("UParticleModuleSize_Seeded", UParticleModuleSize_Seeded_Data),
	]


class  UParticleModuleSizeMultiplyLife_Data(Structure):
	_fields_ = [
		("LifeMultiplier", FRawDistributionVector),
		("MultiplyX", c_bool, 1),
		("MultiplyY", c_bool, 1),
		("MultiplyZ", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleSizeMultiplyLife(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSizeMultiplyLife", UParticleModuleSizeMultiplyLife_Data),
	]


class  UParticleModuleSizeMultiplyVelocity_Data(Structure):
	_fields_ = [
		("VelocityMultiplier", FRawDistributionVector),
		("MultiplyX", c_bool, 1),
		("MultiplyY", c_bool, 1),
		("MultiplyZ", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleSizeMultiplyVelocity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSizeMultiplyVelocity", UParticleModuleSizeMultiplyVelocity_Data),
	]


class  UParticleModuleSizeScale_Data(Structure):
	_fields_ = [
		("SizeScale", FRawDistributionVector),
		("EnableX", c_bool, 1),
		("EnableY", c_bool, 1),
		("EnableZ", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleSizeScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSizeScale", UParticleModuleSizeScale_Data),
	]


class  UParticleModuleSizeScaleByTime_Data(Structure):
	_fields_ = [
		("SizeScaleByTime", FRawDistributionVector),
		("bEnableX", c_bool, 1),
		("bEnableY", c_bool, 1),
		("bEnableZ", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleSizeScaleByTime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSizeScaleByTime", UParticleModuleSizeScaleByTime_Data),
	]


class  UParticleModuleSizeScaleOverDensity_Data(Structure):
	_fields_ = [
		("SizeScaleOverDensity", FRawDistributionVector),
	]

class  UParticleModuleSizeScaleOverDensity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSizeBase", UParticleModuleSizeBase_Data),
		("UParticleModuleSizeScaleOverDensity", UParticleModuleSizeScaleOverDensity_Data),
	]


class  UParticleModuleSpawnBase_Data(Structure):
	_fields_ = [
		("bProcessSpawnRate", c_bool, 1),
		("bProcessBurstList", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleSpawnBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSpawnBase", UParticleModuleSpawnBase_Data),
	]


class  UParticleModuleSpawn_Data(Structure):
	_fields_ = [
		("Rate", FRawDistributionFloat),
		("RateScale", FRawDistributionFloat),
		("ParticleBurstMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BurstList", TArray_FParticleBurst),
	]

class  UParticleModuleSpawn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSpawnBase", UParticleModuleSpawnBase_Data),
		("UParticleModuleSpawn", UParticleModuleSpawn_Data),
	]


class  UParticleModuleSpawnPerUnit_Data(Structure):
	_fields_ = [
		("UnitScalar", c_float),
		("SpawnPerUnit", FRawDistributionFloat),
		("bIgnoreSpawnRateWhenMoving", c_bool, 1),
		("bIgnoreMovementAlongX", c_bool, 1),
		("bIgnoreMovementAlongY", c_bool, 1),
		("bIgnoreMovementAlongZ", c_bool, 1),
		("", c_ulong, 0),
		("MovementTolerance", c_float),
		("MaxFrameDistance", c_float),
	]

class  UParticleModuleSpawnPerUnit(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSpawnBase", UParticleModuleSpawnBase_Data),
		("UParticleModuleSpawnPerUnit", UParticleModuleSpawnPerUnit_Data),
	]


class  UParticleModuleStoreSpawnTimeBase_Data(Structure):
	_fields_ = []

class  UParticleModuleStoreSpawnTimeBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleStoreSpawnTimeBase", UParticleModuleStoreSpawnTimeBase_Data),
	]


class  UParticleModuleStoreSpawnTime_Data(Structure):
	_fields_ = []

class  UParticleModuleStoreSpawnTime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleStoreSpawnTimeBase", UParticleModuleStoreSpawnTimeBase_Data),
		("UParticleModuleStoreSpawnTime", UParticleModuleStoreSpawnTime_Data),
	]


class  UParticleModuleSubUVBase_Data(Structure):
	_fields_ = []

class  UParticleModuleSubUVBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSubUVBase", UParticleModuleSubUVBase_Data),
	]


class  UParticleModuleSubUV_Data(Structure):
	_fields_ = [
		("SubImageIndex", FRawDistributionFloat),
		("bUseRealTime", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleSubUV(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSubUVBase", UParticleModuleSubUVBase_Data),
		("UParticleModuleSubUV", UParticleModuleSubUV_Data),
	]


class  UParticleModuleSubUVMovie_Data(Structure):
	_fields_ = [
		("bUseEmitterTime", c_bool, 1),
		("", c_ulong, 0),
		("FrameRate", FRawDistributionFloat),
		("StartingFrame", c_int),
	]

class  UParticleModuleSubUVMovie(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSubUVBase", UParticleModuleSubUVBase_Data),
		("UParticleModuleSubUV", UParticleModuleSubUV_Data),
		("UParticleModuleSubUVMovie", UParticleModuleSubUVMovie_Data),
	]


class  UParticleModuleSubUVDirect_Data(Structure):
	_fields_ = [
		("SubUVPosition", FRawDistributionVector),
		("SubUVSize", FRawDistributionVector),
	]

class  UParticleModuleSubUVDirect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSubUVBase", UParticleModuleSubUVBase_Data),
		("UParticleModuleSubUVDirect", UParticleModuleSubUVDirect_Data),
	]


class  UParticleModuleSubUVSelect_Data(Structure):
	_fields_ = [
		("SubImageSelect", FRawDistributionVector),
	]

class  UParticleModuleSubUVSelect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleSubUVBase", UParticleModuleSubUVBase_Data),
		("UParticleModuleSubUVSelect", UParticleModuleSubUVSelect_Data),
	]


class  UParticleModuleTrailBase_Data(Structure):
	_fields_ = []

class  UParticleModuleTrailBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTrailBase", UParticleModuleTrailBase_Data),
	]


class  UParticleModuleTrailSource_Data(Structure):
	_fields_ = [
		("SourceMethod", c_ubyte),
		("SelectionMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("SourceName", FName),
		("SourceStrength", FRawDistributionFloat),
		("bLockSourceStength", c_bool, 1),
		("bInheritRotation", c_bool, 1),
		("", c_ulong, 0),
		("SourceOffsetCount", c_int),
		("SourceOffsetDefaults", TArray_FVector),
	]

class  UParticleModuleTrailSource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTrailBase", UParticleModuleTrailBase_Data),
		("UParticleModuleTrailSource", UParticleModuleTrailSource_Data),
	]


class  UParticleModuleTrailSpawn_Data(Structure):
	_fields_ = [
		("SpawnDistanceMap", POINTER(UDistributionFloatParticleParameter)),
		("MinSpawnVelocity", c_float),
	]

class  UParticleModuleTrailSpawn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTrailBase", UParticleModuleTrailBase_Data),
		("UParticleModuleTrailSpawn", UParticleModuleTrailSpawn_Data),
	]


class  UParticleModuleTrailTaper_Data(Structure):
	_fields_ = [
		("TaperMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TaperFactor", FRawDistributionFloat),
	]

class  UParticleModuleTrailTaper(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTrailBase", UParticleModuleTrailBase_Data),
		("UParticleModuleTrailTaper", UParticleModuleTrailTaper_Data),
	]


class  UParticleModuleTypeDataBase_Data(Structure):
	_fields_ = []

class  UParticleModuleTypeDataBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
	]


class  UParticleModuleTypeDataAnimTrail_Data(Structure):
	_fields_ = [
		("ControlEdgeName", FName),
		("SheetsPerTrail", c_int),
		("bDeadTrailsOnDeactivate", c_bool, 1),
		("bClipSourceSegement", c_bool, 1),
		("bEnablePreviousTangentRecalculation", c_bool, 1),
		("bTangentRecalculationEveryFrame", c_bool, 1),
		("bRenderGeometry", c_bool, 1),
		("bRenderSpawnPoints", c_bool, 1),
		("bRenderTangents", c_bool, 1),
		("bRenderTessellation", c_bool, 1),
		("", c_ulong, 0),
		("TilingDistance", c_float),
		("DistanceTessellationStepSize", c_float),
		("TangentTessellationScalar", c_float),
	]

class  UParticleModuleTypeDataAnimTrail(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataAnimTrail", UParticleModuleTypeDataAnimTrail_Data),
	]


class  UParticleModuleTypeDataApex_Data(Structure):
	_fields_ = [
		("ApexIOFX", POINTER(UApexGenericAsset)),
		("ApexEmitter", POINTER(UApexGenericAsset)),
	]

class  UParticleModuleTypeDataApex(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataApex", UParticleModuleTypeDataApex_Data),
	]


class  UParticleModuleTypeDataBeam_Data(Structure):
	_fields_ = [
		("BeamMethod", c_ubyte),
		("EndPointMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Distance", FRawDistributionFloat),
		("EndPoint", FRawDistributionVector),
		("TessellationFactor", c_int),
		("EmitterStrength", FRawDistributionFloat),
		("TargetStrength", FRawDistributionFloat),
		("EndPointDirection", FRawDistributionVector),
		("TextureTile", c_int),
		("RenderGeometry", c_bool, 1),
		("RenderDirectLine", c_bool, 1),
		("RenderLines", c_bool, 1),
		("RenderTessellation", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleTypeDataBeam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataBeam", UParticleModuleTypeDataBeam_Data),
	]


class  UParticleModuleTypeDataBeam2_Data(Structure):
	_fields_ = [
		("BeamMethod", c_ubyte),
		("TaperMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TextureTile", c_int),
		("TextureTileDistance", c_float),
		("Sheets", c_int),
		("MaxBeamCount", c_int),
		("Speed", c_float),
		("InterpolationPoints", c_int),
		("bAlwaysOn", c_bool, 1),
		("bSpawnPerUnitHack", c_bool, 1),
		("RenderGeometry", c_bool, 1),
		("RenderDirectLine", c_bool, 1),
		("RenderLines", c_bool, 1),
		("RenderTessellation", c_bool, 1),
		("", c_ulong, 0),
		("UpVectorStepSize", c_int),
		("BranchParentName", FName),
		("Distance", FRawDistributionFloat),
		("TaperFactor", FRawDistributionFloat),
		("TaperScale", FRawDistributionFloat),
	]

class  UParticleModuleTypeDataBeam2(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataBeam2", UParticleModuleTypeDataBeam2_Data),
	]


class  UParticleModuleTypeDataMesh_Data(Structure):
	_fields_ = [
		("Mesh", POINTER(UStaticMesh)),
		("CastShadows", c_bool, 1),
		("DoCollisions", c_bool, 1),
		("bAllowMotionBlur", c_bool, 1),
		("bOverrideMaterial", c_bool, 1),
		("bCameraFacing", c_bool, 1),
		("bApplyParticleRotationAsSpin", c_bool, 1),
		("", c_ulong, 0),
		("MeshAlignment", c_ubyte),
		("AxisLockOption", c_ubyte),
		("CameraFacingUpAxisOption", c_ubyte),
		("CameraFacingOption", c_ubyte),
		("Pitch", c_float),
		("Roll", c_float),
		("Yaw", c_float),
	]

class  UParticleModuleTypeDataMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataMesh", UParticleModuleTypeDataMesh_Data),
	]


class  UParticleModuleTypeDataMeshPhysX_Data(Structure):
	_fields_ = [
		("PhysXParSys", POINTER(UPhysXParticleSystem)),
		("PhysXRotationMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("FluidRotationCoefficient", c_float),
		("VerticalLod", FPhysXEmitterVerticalLodProperties),
		("ZOffset", c_float),
		("SuppressIfLowGore", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleTypeDataMeshPhysX(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataMesh", UParticleModuleTypeDataMesh_Data),
		("UParticleModuleTypeDataMeshPhysX", UParticleModuleTypeDataMeshPhysX_Data),
	]


class  UParticleModuleTypeDataPhysX_Data(Structure):
	_fields_ = [
		("PhysXParSys", POINTER(UPhysXParticleSystem)),
		("VerticalLod", FPhysXEmitterVerticalLodProperties),
		("SPHSmoothScreenRadius", c_float),
		("SPHSmoothDepthRadius", c_float),
		("SPHCutoffThickness", c_float),
		("SuppressIfLowGore", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleTypeDataPhysX(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataPhysX", UParticleModuleTypeDataPhysX_Data),
	]


class  UParticleModuleTypeDataRibbon_Data(Structure):
	_fields_ = [
		("MaxTessellationBetweenParticles", c_int),
		("SheetsPerTrail", c_int),
		("MaxTrailCount", c_int),
		("MaxParticleInTrailCount", c_int),
		("bDeadTrailsOnDeactivate", c_bool, 1),
		("bDeadTrailsOnSourceLoss", c_bool, 1),
		("bClipSourceSegement", c_bool, 1),
		("bEnablePreviousTangentRecalculation", c_bool, 1),
		("bTangentRecalculationEveryFrame", c_bool, 1),
		("bRenderGeometry", c_bool, 1),
		("bRenderSpawnPoints", c_bool, 1),
		("bRenderTangents", c_bool, 1),
		("bRenderTessellation", c_bool, 1),
		("bEnableTangentDiffInterpScale", c_bool, 1),
		("", c_ulong, 0),
		("RenderAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("TangentSpawningScalar", c_float),
		("TilingDistance", c_float),
		("DistanceTessellationStepSize", c_float),
		("TangentTessellationScalar", c_float),
	]

class  UParticleModuleTypeDataRibbon(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataRibbon", UParticleModuleTypeDataRibbon_Data),
	]


class  UParticleModuleTypeDataTrail_Data(Structure):
	_fields_ = [
		("RenderGeometry", c_bool, 1),
		("RenderLines", c_bool, 1),
		("RenderTessellation", c_bool, 1),
		("Tapered", c_bool, 1),
		("SpawnByDistance", c_bool, 1),
		("", c_ulong, 0),
		("TessellationFactor", c_int),
		("Tension", FRawDistributionFloat),
		("SpawnDistance", FVector),
	]

class  UParticleModuleTypeDataTrail(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataTrail", UParticleModuleTypeDataTrail_Data),
	]


class  UParticleModuleTypeDataTrail2_Data(Structure):
	_fields_ = [
		("TessellationFactor", c_int),
		("TessellationFactorDistance", c_float),
		("TessellationStrength", c_float),
		("TextureTile", c_int),
		("Sheets", c_int),
		("MaxTrailCount", c_int),
		("MaxParticleInTrailCount", c_int),
		("bClipSourceSegement", c_bool, 1),
		("bClearTangents", c_bool, 1),
		("RenderGeometry", c_bool, 1),
		("RenderDirectLine", c_bool, 1),
		("RenderLines", c_bool, 1),
		("RenderTessellation", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleTypeDataTrail2(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleTypeDataBase", UParticleModuleTypeDataBase_Data),
		("UParticleModuleTypeDataTrail2", UParticleModuleTypeDataTrail2_Data),
	]


class  UParticleModuleUberBase_Data(Structure):
	_fields_ = [
		("RequiredModules", TArray_FName),
	]

class  UParticleModuleUberBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
	]


class  UParticleModuleUberLTISIVCL_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
		("StartSize", FRawDistributionVector),
		("StartVelocity", FRawDistributionVector),
		("StartVelocityRadial", FRawDistributionFloat),
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
	]

class  UParticleModuleUberLTISIVCL(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberLTISIVCL", UParticleModuleUberLTISIVCL_Data),
	]


class  UParticleModuleUberLTISIVCLIL_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
		("StartSize", FRawDistributionVector),
		("StartVelocity", FRawDistributionVector),
		("StartVelocityRadial", FRawDistributionFloat),
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
		("StartLocation", FRawDistributionVector),
	]

class  UParticleModuleUberLTISIVCLIL(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberLTISIVCLIL", UParticleModuleUberLTISIVCLIL_Data),
	]


class  UParticleModuleUberLTISIVCLILIRSSBLIRR_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
		("StartSize", FRawDistributionVector),
		("StartVelocity", FRawDistributionVector),
		("StartVelocityRadial", FRawDistributionFloat),
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
		("StartLocation", FRawDistributionVector),
		("StartRotation", FRawDistributionFloat),
		("SizeLifeMultiplier", FRawDistributionVector),
		("SizeMultiplyX", c_bool, 1),
		("SizeMultiplyY", c_bool, 1),
		("SizeMultiplyZ", c_bool, 1),
		("", c_ulong, 0),
		("StartRotationRate", FRawDistributionFloat),
	]

class  UParticleModuleUberLTISIVCLILIRSSBLIRR(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberLTISIVCLILIRSSBLIRR", UParticleModuleUberLTISIVCLILIRSSBLIRR_Data),
	]


class  UParticleModuleUberRainDrops_Data(Structure):
	_fields_ = [
		("LifetimeMin", c_float),
		("LifetimeMax", c_float),
		("StartSizeMin", FVector),
		("StartSizeMax", FVector),
		("StartVelocityMin", FVector),
		("StartVelocityMax", FVector),
		("StartVelocityRadialMin", c_float),
		("StartVelocityRadialMax", c_float),
		("ColorOverLife", FVector),
		("AlphaOverLife", c_float),
		("bIsUsingCylinder", c_bool, 1),
		("bPositive_X", c_bool, 1),
		("bPositive_Y", c_bool, 1),
		("bPositive_Z", c_bool, 1),
		("bNegative_X", c_bool, 1),
		("bNegative_Y", c_bool, 1),
		("bNegative_Z", c_bool, 1),
		("bSurfaceOnly", c_bool, 1),
		("bVelocity", c_bool, 1),
		("bRadialVelocity", c_bool, 1),
		("", c_ulong, 0),
		("PC_VelocityScale", c_float),
		("PC_StartLocation", FVector),
		("PC_StartRadius", c_float),
		("PC_StartHeight", c_float),
		("PC_HeightAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("StartLocationMin", FVector),
		("StartLocationMax", FVector),
	]

class  UParticleModuleUberRainDrops(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberRainDrops", UParticleModuleUberRainDrops_Data),
	]


class  UParticleModuleUberRainImpacts_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
		("StartSize", FRawDistributionVector),
		("StartRotation", FRawDistributionVector),
		("bInheritParent", c_bool, 1),
		("MultiplyX", c_bool, 1),
		("MultiplyY", c_bool, 1),
		("MultiplyZ", c_bool, 1),
		("bIsUsingCylinder", c_bool, 1),
		("bPositive_X", c_bool, 1),
		("bPositive_Y", c_bool, 1),
		("bPositive_Z", c_bool, 1),
		("bNegative_X", c_bool, 1),
		("bNegative_Y", c_bool, 1),
		("bNegative_Z", c_bool, 1),
		("bSurfaceOnly", c_bool, 1),
		("bVelocity", c_bool, 1),
		("bRadialVelocity", c_bool, 1),
		("", c_ulong, 0),
		("LifeMultiplier", FRawDistributionVector),
		("PC_VelocityScale", FRawDistributionFloat),
		("PC_StartLocation", FRawDistributionVector),
		("PC_StartRadius", FRawDistributionFloat),
		("PC_StartHeight", FRawDistributionFloat),
		("PC_HeightAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
	]

class  UParticleModuleUberRainImpacts(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberRainImpacts", UParticleModuleUberRainImpacts_Data),
	]


class  UParticleModuleUberRainSplashA_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
		("StartSize", FRawDistributionVector),
		("StartRotation", FRawDistributionVector),
		("bInheritParent", c_bool, 1),
		("MultiplyX", c_bool, 1),
		("MultiplyY", c_bool, 1),
		("MultiplyZ", c_bool, 1),
		("", c_ulong, 0),
		("LifeMultiplier", FRawDistributionVector),
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
	]

class  UParticleModuleUberRainSplashA(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberRainSplashA", UParticleModuleUberRainSplashA_Data),
	]


class  UParticleModuleUberRainSplashB_Data(Structure):
	_fields_ = [
		("Lifetime", FRawDistributionFloat),
		("StartSize", FRawDistributionVector),
		("ColorOverLife", FRawDistributionVector),
		("AlphaOverLife", FRawDistributionFloat),
		("LifeMultiplier", FRawDistributionVector),
		("MultiplyX", c_bool, 1),
		("MultiplyY", c_bool, 1),
		("MultiplyZ", c_bool, 1),
		("", c_ulong, 0),
		("StartRotationRate", FRawDistributionFloat),
	]

class  UParticleModuleUberRainSplashB(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleUberBase", UParticleModuleUberBase_Data),
		("UParticleModuleUberRainSplashB", UParticleModuleUberRainSplashB_Data),
	]


class  UParticleModuleVelocityBase_Data(Structure):
	_fields_ = [
		("bInWorldSpace", c_bool, 1),
		("bApplyOwnerScale", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleVelocityBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleVelocityBase", UParticleModuleVelocityBase_Data),
	]


class  UParticleModuleVelocity_Data(Structure):
	_fields_ = [
		("StartVelocity", FRawDistributionVector),
		("StartVelocityRadial", FRawDistributionFloat),
	]

class  UParticleModuleVelocity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleVelocityBase", UParticleModuleVelocityBase_Data),
		("UParticleModuleVelocity", UParticleModuleVelocity_Data),
	]


class  UParticleModuleVelocity_Seeded_Data(Structure):
	_fields_ = [
		("RandomSeedInfo", FParticleRandomSeedInfo),
	]

class  UParticleModuleVelocity_Seeded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleVelocityBase", UParticleModuleVelocityBase_Data),
		("UParticleModuleVelocity", UParticleModuleVelocity_Data),
		("UParticleModuleVelocity_Seeded", UParticleModuleVelocity_Seeded_Data),
	]


class  UParticleModuleVelocityInheritParent_Data(Structure):
	_fields_ = [
		("Scale", FRawDistributionVector),
	]

class  UParticleModuleVelocityInheritParent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleVelocityBase", UParticleModuleVelocityBase_Data),
		("UParticleModuleVelocityInheritParent", UParticleModuleVelocityInheritParent_Data),
	]


class  UParticleModuleVelocityOverLifetime_Data(Structure):
	_fields_ = [
		("VelOverLife", FRawDistributionVector),
		("Absolute", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleModuleVelocityOverLifetime(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleVelocityBase", UParticleModuleVelocityBase_Data),
		("UParticleModuleVelocityOverLifetime", UParticleModuleVelocityOverLifetime_Data),
	]


class  UParticleModuleEventSendToGame_Data(Structure):
	_fields_ = []

class  UParticleModuleEventSendToGame(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModuleEventSendToGame", UParticleModuleEventSendToGame_Data),
	]


class  UParticleSystem_Data(Structure):
	_fields_ = [
		("SystemUpdateMode", c_ubyte),
		("LODMethod", c_ubyte),
		("OcclusionBoundsMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("UpdateTime_FPS", c_float),
		("UpdateTime_Delta", c_float),
		("WarmupTime", c_float),
		("bAggressiveWithMemory", c_bool, 1),
		("bLit", c_bool, 1),
		("bOrientZAxisTowardCamera", c_bool, 1),
		("bFullResolution", c_bool, 1),
		("bRegenerateLODDuplicate", c_bool, 1),
		("bUseFixedRelativeBoundingBox", c_bool, 1),
		("bShouldResetPeakCounts", c_bool, 1),
		("bHasPhysics", c_bool, 1),
		("bUseRealtimeThumbnail", c_bool, 1),
		("ThumbnailImageOutOfDate", c_bool, 1),
		("bSkipSpawnCountCheck", c_bool, 1),
		("bUseDelayRange", c_bool, 1),
		("bUseMobilePointSprites", c_bool, 1),
		("bLoadIfPhysXLevel0", c_bool, 1),
		("bLoadIfPhysXLevel1", c_bool, 1),
		("bLoadIfPhysXLevel2", c_bool, 1),
		("", c_ulong, 0),
		("Emitters", TArray_UParticleEmitterPtr),
		("PreviewComponent", POINTER(UParticleSystemComponent)),
		("CurveEdSetup", POINTER(UInterpCurveEdSetup)),
		("LODDistanceCheckTime", c_float),
		("LODDistances", TArray_float),
		("MaxDrawDistance", c_float),
		("LODSettings", TArray_FParticleSystemLOD),
		("FixedRelativeBoundingBox", FBox),
		("SecondsBeforeInactive", c_float),
		("Delay", c_float),
		("DelayLow", c_float),
		("MacroUVPosition", FVector),
		("MacroUVRadius", c_float),
		("CustomOcclusionBounds", FBox),
		("StartAudioEvent", POINTER(UAkEvent)),
		("StopAudioEvent", POINTER(UAkEvent)),
		("StartLoopingAudioEvent", POINTER(UAkEvent)),
		("StopLoopingAudioEvent", POINTER(UAkEvent)),
		("fAudioDelaySeconds", c_float),
		("PhysxParticleSystemRef", POINTER(UParticleSystem)),
	]

class  UParticleSystem(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleSystem", UParticleSystem_Data),
	]


class  UParticleSystemReplay_Data(Structure):
	_fields_ = [
		("ClipIDNumber", c_int),
		("Frames", TArray_FParticleSystemReplayFrame),
	]

class  UParticleSystemReplay(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleSystemReplay", UParticleSystemReplay_Data),
	]


class  UPhysXParticleSystem_Data(Structure):
	_fields_ = [
		("MaxParticles1", c_int),
		("MaxParticles2", c_int),
		("MaxParticles", c_int),
		("ParticleSpawnReserve", c_int),
		("RBChannel", c_ubyte),
		("SimulationMethod", c_ubyte),
		("PacketSizeMultiplier", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("RBCollideWithChannels", FRBCollisionChannelContainer),
		("CollisionDistance", c_float),
		("RestitutionWithStaticShapes", c_float),
		("RestitutionWithDynamicShapes", c_float),
		("FrictionWithStaticShapes", c_float),
		("FrictionWithDynamicShapes", c_float),
		("StaticFrictionWithStaticShapes", c_float),
		("StaticFrictionWithDynamicShapes", c_float),
		("bDynamicCollision", c_bool, 1),
		("bDisableGravity", c_bool, 1),
		("bStaticCollision", c_bool, 1),
		("bTwoWayCollision", c_bool, 1),
		("bDestroy", c_bool, 1),
		("bSyncFailed", c_bool, 1),
		("bIsInGame", c_bool, 1),
		("", c_ulong, 0),
		("MaxMotionDistance", c_float),
		("Damping", c_float),
		("ExternalAcceleration", FVector),
		("RestParticleDistance", c_float),
		("RestDensity", c_float),
		("KernelRadiusMultiplier", c_float),
		("Stiffness", c_float),
		("Viscosity", c_float),
		("CollisionResponseCoefficient", c_float),
		("CascadeScene", FPointer),
		("PSys", FPointer),
	]

class  UPhysXParticleSystem(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPhysXParticleSystem", UPhysXParticleSystem_Data),
	]


class  AKActor_Data(Structure):
	_fields_ = [
		("bDamageAppliesImpulse", c_bool, 1),
		("bWakeOnLevelStart", c_bool, 1),
		("bCurrentSlide", c_bool, 1),
		("bSlideActive", c_bool, 1),
		("bEnableStayUprightSpring", c_bool, 1),
		("bLimitMaxPhysicsVelocity", c_bool, 1),
		("bNeedsRBStateReplication", c_bool, 1),
		("bDisableClientSidePawnInteractions", c_bool, 1),
		("", c_ulong, 0),
		("ImpactEffectComponent", POINTER(UParticleSystemComponent)),
		("ImpactSoundComponent", POINTER(UAudioComponent)),
		("ImpactSoundComponent2", POINTER(UAudioComponent)),
		("LastImpactTime", c_float),
		("ImpactEffectInfo", FPhysEffectInfo),
		("SlideEffectComponent", POINTER(UParticleSystemComponent)),
		("SlideSoundComponent", POINTER(UAudioComponent)),
		("LastSlideTime", c_float),
		("SlideEffectInfo", FPhysEffectInfo),
		("StayUprightTorqueFactor", c_float),
		("StayUprightMaxTorque", c_float),
		("MaxPhysicsVelocity", c_float),
		("NetRelevantDistanceSquared", c_float),
		("Unknown1", c_ubyte, 0x),
		("RBState", FRigidBodyState),
		("Unknown2", c_ubyte, 0x),
		("AngErrorAccumulator", c_float),
		("ReplicatedDrawScale3D", FVector),
		("InitialLocation", FVector),
		("InitialRotation", FRotator),
	]

class  AKActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("AKActor", AKActor_Data),
	]


class  AKActorFromStatic_Data(Structure):
	_fields_ = [
		("MyStaticMeshActor", POINTER(AActor)),
		("MaxImpulseSpeed", c_float),
	]

class  AKActorFromStatic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("AKActor", AKActor_Data),
		("AKActorFromStatic", AKActorFromStatic_Data),
	]


class  AKActorSpawnable_Data(Structure):
	_fields_ = [
		("bRecycleScaleToZero", c_bool, 1),
		("bScalingToZero", c_bool, 1),
		("bNotifyRigidBodyCollision", c_bool, 1),
		("", c_ulong, 0),
	]

class  AKActorSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("AKActor", AKActor_Data),
		("AKActorSpawnable", AKActorSpawnable_Data),
	]


class  AKActorPizazz_Data(Structure):
	_fields_ = [
		("ReplicatedImpulse", FImpulseData),
	]

class  AKActorPizazz(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("AKActor", AKActor_Data),
		("AKActorSpawnable", AKActorSpawnable_Data),
		("AKActorPizazz", AKActorPizazz_Data),
	]


class  AKAsset_Data(Structure):
	_fields_ = [
		("SkeletalMeshComponent", POINTER(USkeletalMeshComponent)),
		("bDamageAppliesImpulse", c_bool, 1),
		("bWakeOnLevelStart", c_bool, 1),
		("bBlockPawns", c_bool, 1),
		("", c_ulong, 0),
		("ReplicatedMesh", POINTER(USkeletalMesh)),
		("ReplicatedPhysAsset", POINTER(UPhysicsAsset)),
	]

class  AKAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AKAsset", AKAsset_Data),
	]


class  APawn_Data(Structure):
	_fields_ = [
		("VfTable_IInterface_Speaker", FPointer),
		("VfTable_IIKilledBehavior", FPointer),
		("VfTable_IITargetable", FPointer),
		("MaxStepHeight", c_float),
		("MaxJumpHeight", c_float),
		("WalkableFloorZ", c_float),
		("LedgeCheckThreshold", c_float),
		("PartialLedgeMoveDir", FVector),
		("Controller", POINTER(AController)),
		("NextPawn", POINTER(APawn)),
		("NetRelevancyTime", c_float),
		("LastRealViewer", POINTER(APlayerController)),
		("LastViewer", POINTER(AActor)),
		("bScriptTickSpecial", c_bool, 1),
		("bUpAndOut", c_bool, 1),
		("bIsWalking", c_bool, 1),
		("bWantsToCrouch", c_bool, 1),
		("bIsCrouched", c_bool, 1),
		("bTryToUncrouch", c_bool, 1),
		("bCanCrouch", c_bool, 1),
		("bCrawler", c_bool, 1),
		("bReducedSpeed", c_bool, 1),
		("bJumpCapable", c_bool, 1),
		("bCanJump", c_bool, 1),
		("bCanWalk", c_bool, 1),
		("bCanSwim", c_bool, 1),
		("bCanFly", c_bool, 1),
		("bCanClimbLadders", c_bool, 1),
		("bCanStrafe", c_bool, 1),
		("bAvoidLedges", c_bool, 1),
		("bStopAtLedges", c_bool, 1),
		("bAllowLedgeOverhang", c_bool, 1),
		("bPartiallyOverLedge", c_bool, 1),
		("bSimulateGravity", c_bool, 1),
		("bIgnoreForces", c_bool, 1),
		("bCanWalkOffLedges", c_bool, 1),
		("bCanBeBaseForPawns", c_bool, 1),
		("bSimGravityDisabled", c_bool, 1),
		("bDirectHitWall", c_bool, 1),
		("bPushesRigidBodies", c_bool, 1),
		("bForceFloorCheck", c_bool, 1),
		("bForceKeepAnchor", c_bool, 1),
		("bIgnoreAllTraces", c_bool, 1),
		("bCanMantle", c_bool, 1),
		("bCanClimbUp", c_bool, 1),
		("bCanClimbCeilings", c_bool, 1),
		("bCanSwatTurn", c_bool, 1),
		("bCanLeap", c_bool, 1),
		("bCanCoverSlip", c_bool, 1),
		("bDisplayPathErrors", c_bool, 1),
		("bCanPickupInventory", c_bool, 1),
		("bAmbientCreature", c_bool, 1),
		("bLOSHearing", c_bool, 1),
		("bMuffledHearing", c_bool, 1),
		("bDontPossess", c_bool, 1),
		("bRollToDesired", c_bool, 1),
		("bStationary", c_bool, 1),
		("bCachedRelevant", c_bool, 1),
		("bNoWeaponFiring", c_bool, 1),
		("bModifyReachSpecCost", c_bool, 1),
		("bModifyNavPointDest", c_bool, 1),
		("bPathfindsAsVehicle", c_bool, 1),
		("bPrevBypassSimulatedClientPhysics", c_bool, 1),
		("bRunPhysicsWithNoController", c_bool, 1),
		("bForceMaxAccel", c_bool, 1),
		("bLimitFallAccel", c_bool, 1),
		("bReplicateHealthToAll", c_bool, 1),
		("bForceRMVelocity", c_bool, 1),
		("bForceRegularVelocity", c_bool, 1),
		("bPlayedDeath", c_bool, 1),
		("bDesiredRotationSet", c_bool, 1),
		("bLockDesiredRotation", c_bool, 1),
		("bUnlockWhenReached", c_bool, 1),
		("bCanBeInjured", c_bool, 1),
		("bIsInjured", c_bool, 1),
		("bSpawnInFixedPosition", c_bool, 1),
		("bIsDead", c_bool, 1),
		("bNeedsBaseTickedFirst", c_bool, 1),
		("bUsedByMatinee", c_bool, 1),
		("bRootMotionFromInterpCurve", c_bool, 1),
		("bDebugShowCameraLocation", c_bool, 1),
		("bFastAttachedMove", c_bool, 1),
		("bSnapToTarget", c_bool, 1),
		("bAutoAimTarget", c_bool, 1),
		("bUnlockPreciseDestinationWhenReached", c_bool, 1),
		("ImmuneToFallingDamage", c_bool, 1),
		("bSkipClientAdjustment", c_bool, 1),
		("", c_ulong, 0),
		("bIsSprinting", c_int),
		("bIsSprintingBaseValue", c_int),
		("bIsSprintingModifierStack", TArray_UAttributeModifierPtr),
		("WalkingPhysics", c_ubyte),
		("PathSearchType", c_ubyte),
		("RemoteViewPitch", c_ubyte),
		("RemoteViewYaw", c_ubyte),
		("NextFlashLocationIdx", c_ubyte),
		("FlashCount", c_ubyte),
		("OffHandFlashCount", c_ubyte),
		("FiringMode", c_ubyte),
		("AutoAimProfile", c_ubyte),
		("bEnableWeaponFireSkillEvent", c_ubyte),
		("bEnableWeaponFireSkillEventBaseValue", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bEnableWeaponFireSkillEventModifierStack", TArray_UAttributeModifierPtr),
		("UncrouchTime", c_float),
		("CrouchHeight", c_float),
		("CrouchRadius", c_float),
		("FullHeight", c_int),
		("NonPreferredVehiclePathMultiplier", c_float),
		("PathConstraintList", POINTER(UPathConstraint)),
		("PathGoalList", POINTER(UPathGoalEvaluator)),
		("DesiredSpeed", c_float),
		("MaxDesiredSpeed", c_float),
		("HearingThreshold", c_float),
		("HearingThresholdBaseValue", c_float),
		("HearingThresholdModifierStack", TArray_UAttributeModifierPtr),
		("Alertness", c_float),
		("SightRadius", c_float),
		("SightRadiusBaseValue", c_float),
		("SightRadiusModifierStack", TArray_UAttributeModifierPtr),
		("PeripheralVision", c_float),
		("PeripheralVisionBaseValue", c_float),
		("PeripheralVisionModifierStack", TArray_UAttributeModifierPtr),
		("AvgPhysicsTime", c_float),
		("Mass", c_float),
		("Buoyancy", c_float),
		("MeleeRange", c_float),
		("Anchor", POINTER(ANavigationPoint)),
		("AnchorItem", c_int),
		("LastAnchor", POINTER(ANavigationPoint)),
		("FindAnchorFailedTime", c_float),
		("LastValidAnchorTime", c_float),
		("DestinationOffset", c_float),
		("NextPathRadius", c_float),
		("SerpentineDir", FVector),
		("SerpentineDist", c_float),
		("SerpentineTime", c_float),
		("SpawnTime", c_float),
		("MaxPitchLimit", c_int),
		("GroundSpeed", c_float),
		("GroundSpeedBaseValue", c_float),
		("GroundSpeedModifierStack", TArray_UAttributeModifierPtr),
		("WaterSpeed", c_float),
		("AirSpeed", c_float),
		("AirSpeedBaseValue", c_float),
		("AirSpeedModifierStack", TArray_UAttributeModifierPtr),
		("LadderSpeed", c_float),
		("AccelRate", c_float),
		("AccelRateBaseValue", c_float),
		("AccelRateModifierStack", TArray_UAttributeModifierPtr),
		("JumpZ", c_float),
		("JumpZBaseValue", c_float),
		("JumpZModifierStack", TArray_UAttributeModifierPtr),
		("OutofWaterZ", c_float),
		("MaxOutOfWaterStepHeight", c_float),
		("AirControl", c_float),
		("WalkingPct", c_float),
		("MovementSpeedModifier", c_float),
		("CrouchedPct", c_float),
		("SprintingPct", c_float),
		("MaxFallSpeed", c_float),
		("TotalEncumbrance", c_float),
		("TotalEncumbranceBaseValue", c_float),
		("TotalEncumbranceModifierStack", TArray_UAttributeModifierPtr),
		("EncumbranceResistance", c_float),
		("EncumbranceResistanceBaseValue", c_float),
		("EncumbranceResistanceModifierStack", TArray_UAttributeModifierPtr),
		("AIMaxFallSpeedFactor", c_float),
		("AnalogMovePct", c_float),
		("BaseEyeHeight", c_float),
		("EyeHeight", c_float),
		("Floor", FVector),
		("SplashTime", c_float),
		("HeadVolume", POINTER(APhysicsVolume)),
		("HealthVar", c_float),
		("HealthMaxVar", c_float),
		("LastHealthVar", c_int),
		("LastHealthMaxVar", c_int),
		("HealthPool", FResourcePoolReference),
		("BreathTime", c_float),
		("UnderWaterTime", c_float),
		("LastPainTime", c_float),
		("KismetDeathDelayTime", c_float),
		("RMVelocity", FVector),
		("noise1spot", FVector),
		("noise1time", c_float),
		("noise1other", POINTER(APawn)),
		("noise1loudness", c_float),
		("noise2spot", FVector),
		("noise2time", c_float),
		("noise2other", POINTER(APawn)),
		("noise2loudness", c_float),
		("SoundDampening", c_float),
		("DamageScaling", c_float),
		("MenuName", FString),
		("ControllerClass", POINTER(UClass)),
		("PlayerReplicationInfo", POINTER(APlayerReplicationInfo)),
		("OnLadder", POINTER(ALadderVolume)),
		("LandMovementState", FName),
		("WaterMovementState", FName),
		("LastStartSpot", POINTER(APlayerStart)),
		("LastStartTime", c_float),
		("TakeHitLocation", FVector),
		("HitDamageType", POINTER(UClass)),
		("HitDamageTypeDefinition", POINTER(UDamageTypeDefinition)),
		("HitImpactDefinition", POINTER(UImpactDefinition)),
		("TearOffMomentum", FVector),
		("Mesh", POINTER(USkeletalMeshComponent)),
		("CylinderComponent", POINTER(UCylinderComponent)),
		("RBPushRadius", c_float),
		("RBPushStrength", c_float),
		("DrivenVehicle", POINTER(AVehicle)),
		("AlwaysRelevantDistanceSquared", c_float),
		("VehicleCheckRadius", c_float),
		("LastHitBy", POINTER(AController)),
		("ViewPitchMin", c_float),
		("ViewPitchMax", c_float),
		("AllowedYawError", c_int),
		("DesiredRotation", FRotator),
		("InventoryManagerClass", POINTER(UClass)),
		("InvManager", POINTER(AInventoryManager)),
		("Weapon", POINTER(AWeapon)),
		("OffHandWeapon", POINTER(AWeapon)),
		("FlashLocationWeaponID", c_int),
		("FlashLocation", FVector * 10),
		("ShotCount", c_int),
		("PreRagdollCollisionComponent", POINTER(UPrimitiveComponent)),
		("Allegiance", POINTER(UPawnAllegiance)),
		("AllegianceParent", FScriptInterface),
		("AllegianceChildren", TArray_FScriptInterface),
		("PhysicsPushBody", POINTER(URB_BodyInstance)),
		("FailedLandingCount", c_int),
		("SlotNodes", TArray_UAnimNodeSlotPtr),
		("InterpGroupList", TArray_UInterpGroupPtr),
		("FacialAudioComp", POINTER(UAudioComponent)),
		("ScalarParameterInterpArray", TArray_FScalarParameterInterpStruct),
		("RootMotionInterpCurve", FRootMotionCurve),
		("RootMotionInterpRate", c_float),
		("RootMotionInterpCurrentTime", c_float),
		("RootMotionInterpCurveLastValue", FVector),
		("MaxPreciseDestinationSpeed", c_float),
		("HorizontalPreciseDestinationThreshold", c_float),
		("VerticalPreciseDestinationThreshold", c_float),
		("NormalImpactDamageModifier", c_float),
		("NormalImpactDamageModifierBaseValue", c_float),
		("NormalImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("NormalStatusEffectDamageModifier", c_float),
		("NormalStatusEffectDamageModifierBaseValue", c_float),
		("NormalStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ExplosiveImpactDamageModifier", c_float),
		("ExplosiveImpactDamageModifierBaseValue", c_float),
		("ExplosiveImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ExplosiveStatusEffectDamageModifier", c_float),
		("ExplosiveStatusEffectDamageModifierBaseValue", c_float),
		("ExplosiveStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ShockImpactDamageModifier", c_float),
		("ShockImpactDamageModifierBaseValue", c_float),
		("ShockImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("ShockStatusEffectDamageModifier", c_float),
		("ShockStatusEffectDamageModifierBaseValue", c_float),
		("ShockStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("CorrosiveImpactDamageModifier", c_float),
		("CorrosiveImpactDamageModifierBaseValue", c_float),
		("CorrosiveImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("CorrosiveStatusEffectDamageModifier", c_float),
		("CorrosiveStatusEffectDamageModifierBaseValue", c_float),
		("CorrosiveStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("IncendiaryImpactDamageModifier", c_float),
		("IncendiaryImpactDamageModifierBaseValue", c_float),
		("IncendiaryImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("IncendiaryStatusEffectDamageModifier", c_float),
		("IncendiaryStatusEffectDamageModifierBaseValue", c_float),
		("IncendiaryStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("AmpImpactDamageModifier", c_float),
		("AmpImpactDamageModifierBaseValue", c_float),
		("AmpImpactDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("AmpStatusEffectDamageModifier", c_float),
		("AmpStatusEffectDamageModifierBaseValue", c_float),
		("AmpStatusEffectDamageModifierModifierStack", TArray_UAttributeModifierPtr),
		("RecentDamage", FRecentDamageTracker),
		("BalanceDefinitionState", FBalanceDefSpawnedActorState),
		("YawLastFrame", c_int),
		("YawPerSecond", c_float),
	]

class  APawn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APawn", APawn_Data),
	]


class  AVehicle_Data(Structure):
	_fields_ = [
		("Driver", POINTER(APawn)),
		("bDriving", c_bool, 1),
		("bDriverIsVisible", c_bool, 1),
		("bAttachDriver", c_bool, 1),
		("bTurnInPlace", c_bool, 1),
		("bSeparateTurretFocus", c_bool, 1),
		("bFollowLookDir", c_bool, 1),
		("bHasHandbrake", c_bool, 1),
		("bScriptedRise", c_bool, 1),
		("bDuckObstacles", c_bool, 1),
		("bAvoidReversing", c_bool, 1),
		("bRetryPathfindingWithDriver", c_bool, 1),
		("bIgnoreStallZ", c_bool, 1),
		("bDoExtraNetRelevancyTraces", c_bool, 1),
		("", c_ulong, 0),
		("ExitPositions", TArray_FVector),
		("ExitRadius", c_float),
		("ExitOffset", FVector),
		("Steering", c_float),
		("Throttle", c_float),
		("Rise", c_float),
		("TargetLocationAdjustment", FVector),
		("DriverDamageMult", c_float),
		("MomentumMult", c_float),
		("CrushedDamageType", POINTER(UClass)),
		("MinCrushSpeed", c_float),
		("ForceCrushPenetration", c_float),
		("StuckCount", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ThrottleTime", c_float),
		("StuckTime", c_float),
		("OldSteering", c_float),
		("OnlySteeringStartTime", c_float),
		("OldThrottle", c_float),
		("AIMoveCheckTime", c_float),
		("VehicleMovingTime", c_float),
		("TurnTime", c_float),
	]

class  AVehicle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APawn", APawn_Data),
		("AVehicle", AVehicle_Data),
	]


class  ASVehicle_Data(Structure):
	_fields_ = [
		("SimObj", POINTER(USVehicleSimBase)),
		("Wheels", TArray_USVehicleWheelPtr),
		("COMOffset", FVector),
		("InertiaTensorMultiplier", FVector),
		("bStayUpright", c_bool, 1),
		("bUseSuspensionAxis", c_bool, 1),
		("bUpdateWheelShapes", c_bool, 1),
		("bVehicleOnGround", c_bool, 1),
		("bVehicleOnWater", c_bool, 1),
		("bIsInverted", c_bool, 1),
		("bChassisTouchingGround", c_bool, 1),
		("bWasChassisTouchingGroundLastTick", c_bool, 1),
		("bCanFlip", c_bool, 1),
		("bFlipRight", c_bool, 1),
		("bIsUprighting", c_bool, 1),
		("bOutputHandbrake", c_bool, 1),
		("bHoldingDownHandbrake", c_bool, 1),
		("bAllowPhysFlying", c_bool, 1),
		("", c_ulong, 0),
		("StayUprightRollResistAngle", c_float),
		("StayUprightPitchResistAngle", c_float),
		("StayUprightStiffness", c_float),
		("StayUprightDamping", c_float),
		("StayUprightConstraintSetup", POINTER(URB_StayUprightSetup)),
		("StayUprightConstraintInstance", POINTER(URB_ConstraintInstance)),
		("HeavySuspensionShiftPercent", c_float),
		("MaxSpeed", c_float),
		("MaxAngularVelocity", c_float),
		("TimeOffGround", c_float),
		("UprightLiftStrength", c_float),
		("UprightTorqueStrength", c_float),
		("UprightTime", c_float),
		("UprightStartTime", c_float),
		("EngineSound", POINTER(UAudioComponent)),
		("SquealSound", POINTER(UAudioComponent)),
		("CollisionSound", POINTER(USoundCue)),
		("EnterVehicleSound", POINTER(USoundCue)),
		("ExitVehicleSound", POINTER(USoundCue)),
		("CollisionIntervalSecs", c_float),
		("CollisionThreshold", c_float),
		("SquealThreshold", c_float),
		("SquealLatThreshold", c_float),
		("LatAngleVolumeMult", c_float),
		("EngineStartOffsetSecs", c_float),
		("EngineStopOffsetSecs", c_float),
		("LastCollisionSoundTime", c_float),
		("OutputBrake", c_float),
		("OutputGas", c_float),
		("OutputSteering", c_float),
		("OutputRise", c_float),
		("ForwardVel", c_float),
		("NumPoweredWheels", c_int),
		("BaseOffset", FVector),
		("CamDist", c_float),
		("DriverViewPitch", c_int),
		("DriverViewYaw", c_int),
		("Unknown1", c_ubyte, 0x),
		("VState", FVehicleState),
		("Unknown2", c_ubyte, 0x),
		("AngErrorAccumulator", c_float),
		("RadialImpulseScaling", c_float),
	]

class  ASVehicle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APawn", APawn_Data),
		("AVehicle", AVehicle_Data),
		("ASVehicle", ASVehicle_Data),
	]


class  ARB_ConstraintActor_Data(Structure):
	_fields_ = [
		("ConstraintActor1", POINTER(AActor)),
		("ConstraintActor2", POINTER(AActor)),
		("ConstraintSetup", POINTER(URB_ConstraintSetup)),
		("ConstraintInstance", POINTER(URB_ConstraintInstance)),
		("bDisableCollision", c_bool, 1),
		("bUpdateActor1RefFrame", c_bool, 1),
		("bUpdateActor2RefFrame", c_bool, 1),
		("", c_ulong, 0),
		("PulleyPivotActor1", POINTER(AActor)),
		("PulleyPivotActor2", POINTER(AActor)),
	]

class  ARB_ConstraintActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_ConstraintActor", ARB_ConstraintActor_Data),
	]


class  ARB_LineImpulseActor_Data(Structure):
	_fields_ = [
		("ImpulseStrength", c_float),
		("ImpulseRange", c_float),
		("bVelChange", c_bool, 1),
		("bStopAtFirstHit", c_bool, 1),
		("bCauseFracture", c_bool, 1),
		("", c_ulong, 0),
		("Arrow", POINTER(UArrowComponent)),
		("ImpulseCount", c_ubyte),
	]

class  ARB_LineImpulseActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_LineImpulseActor", ARB_LineImpulseActor_Data),
	]


class  ARB_RadialImpulseActor_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawSphereComponent)),
		("ImpulseComponent", POINTER(URB_RadialImpulseComponent)),
		("ImpulseCount", c_ubyte),
	]

class  ARB_RadialImpulseActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_RadialImpulseActor", ARB_RadialImpulseActor_Data),
	]


class  ARB_Thruster_Data(Structure):
	_fields_ = [
		("bThrustEnabled", c_bool, 1),
		("", c_ulong, 0),
		("ThrustStrength", c_float),
	]

class  ARB_Thruster(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_Thruster", ARB_Thruster_Data),
	]


class  URB_ConstraintDrawComponent_Data(Structure):
	_fields_ = [
		("LimitMaterial", POINTER(UMaterialInterface)),
	]

class  URB_ConstraintDrawComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("URB_ConstraintDrawComponent", URB_ConstraintDrawComponent_Data),
	]


class  URB_RadialImpulseComponent_Data(Structure):
	_fields_ = [
		("ImpulseFalloff", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ImpulseStrength", c_float),
		("ImpulseRadius", c_float),
		("bVelChange", c_bool, 1),
		("bCauseFracture", c_bool, 1),
		("", c_ulong, 0),
		("PreviewSphere", POINTER(UDrawSphereComponent)),
	]

class  URB_RadialImpulseComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("URB_RadialImpulseComponent", URB_RadialImpulseComponent_Data),
	]


class  URB_Handle_Data(Structure):
	_fields_ = [
		("GrabbedComponent", POINTER(UPrimitiveComponent)),
		("GrabbedBoneName", FName),
		("SceneIndex", c_int),
		("bInHardware", c_bool, 1),
		("bRotationConstrained", c_bool, 1),
		("bInterpolating", c_bool, 1),
		("", c_ulong, 0),
		("HandleData", FPointer),
		("KinActorData", FPointer),
		("LinearDamping", c_float),
		("LinearStiffness", c_float),
		("LinearStiffnessScale3D", FVector),
		("LinearDampingScale3D", FVector),
		("AngularDamping", c_float),
		("AngularStiffness", c_float),
		("Destination", FVector),
		("StepSize", FVector),
		("Location", FVector),
	]

class  URB_Handle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("URB_Handle", URB_Handle_Data),
	]


class  URB_Spring_Data(Structure):
	_fields_ = [
		("Component1", POINTER(UPrimitiveComponent)),
		("BoneName1", FName),
		("Component2", POINTER(UPrimitiveComponent)),
		("BoneName2", FName),
		("SceneIndex", c_int),
		("bInHardware", c_bool, 1),
		("bEnableForceMassRatio", c_bool, 1),
		("", c_ulong, 0),
		("SpringData", FPointer),
		("TimeSinceActivation", c_float),
		("MinBodyMass", c_float),
		("SpringSaturateDist", c_float),
		("SpringMaxForce", c_float),
		("MaxForceMassRatio", c_float),
		("SpringMaxForceTimeScale", FInterpCurveFloat),
		("DampSaturateVel", c_float),
		("DampMaxForce", c_float),
	]

class  URB_Spring(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("URB_Spring", URB_Spring_Data),
	]


class  USVehicleSimBase_Data(Structure):
	_fields_ = [
		("WheelSuspensionStiffness", c_float),
		("WheelSuspensionDamping", c_float),
		("WheelSuspensionBias", c_float),
		("WheelLongExtremumSlip", c_float),
		("WheelLongExtremumValue", c_float),
		("WheelLongAsymptoteSlip", c_float),
		("WheelLongAsymptoteValue", c_float),
		("WheelLatExtremumSlip", c_float),
		("WheelLatExtremumValue", c_float),
		("WheelLatAsymptoteSlip", c_float),
		("WheelLatAsymptoteValue", c_float),
		("WheelInertia", c_float),
		("bWheelSpeedOverride", c_bool, 1),
		("bClampedFrictionModel", c_bool, 1),
		("bAutoDrive", c_bool, 1),
		("", c_ulong, 0),
		("AutoDriveSteer", c_float),
	]

class  USVehicleSimBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USVehicleSimBase", USVehicleSimBase_Data),
	]


class  USVehicleSimCar_Data(Structure):
	_fields_ = [
		("ChassisTorqueScale", c_float),
		("MaxSteerAngleCurve", FInterpCurveFloat),
		("SteerSpeed", c_float),
		("ReverseThrottle", c_float),
		("EngineBrakeFactor", c_float),
		("MaxBrakeTorque", c_float),
		("StopThreshold", c_float),
		("bIsDriving", c_bool, 1),
		("", c_ulong, 0),
		("ActualSteering", c_float),
		("TimeSinceThrottle", c_float),
	]

class  USVehicleSimCar(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USVehicleSimBase", USVehicleSimBase_Data),
		("USVehicleSimCar", USVehicleSimCar_Data),
	]


class  USVehicleSimTank_Data(Structure):
	_fields_ = [
		("LeftTrackVel", c_float),
		("RightTrackVel", c_float),
		("LeftTrackTorque", c_float),
		("RightTrackTorque", c_float),
		("MaxEngineTorque", c_float),
		("EngineDamping", c_float),
		("InsideTrackTorqueFactor", c_float),
		("SteeringLatStiffnessFactor", c_float),
		("TurnInPlaceThrottle", c_float),
		("TurnMaxGripReduction", c_float),
		("TurnGripScaleRate", c_float),
		("bTurnInPlaceOnSteer", c_bool, 1),
		("", c_ulong, 0),
	]

class  USVehicleSimTank(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("USVehicleSimBase", USVehicleSimBase_Data),
		("USVehicleSimCar", USVehicleSimCar_Data),
		("USVehicleSimTank", USVehicleSimTank_Data),
	]


class  UActorFactoryApexClothing_Data(Structure):
	_fields_ = [
		("ClothingAssets", TArray_UApexClothingAssetPtr),
		("ClothingRBChannel", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ClothingRBCollideWithChannels", FRBCollisionChannelContainer),
	]

class  UActorFactoryApexClothing(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactorySkeletalMesh", UActorFactorySkeletalMesh_Data),
		("UActorFactoryApexClothing", UActorFactoryApexClothing_Data),
	]


class  UApexDestructibleDamageParameters_Data(Structure):
	_fields_ = [
		("DamageMap", TArray_FDamagePair),
	]

class  UApexDestructibleDamageParameters(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UApexDestructibleDamageParameters", UApexDestructibleDamageParameters_Data),
	]


class  UFractureMaterial_Data(Structure):
	_fields_ = [
		("FractureEffect", POINTER(UParticleSystem)),
		("FractureSound", POINTER(USoundCue)),
	]

class  UFractureMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UFractureMaterial", UFractureMaterial_Data),
	]


class  UPhysicalMaterial_Data(Structure):
	_fields_ = [
		("MaterialIndex", c_int),
		("Friction", c_float),
		("Restitution", c_float),
		("bForceConeFriction", c_bool, 1),
		("bEnableAnisotropicFriction", c_bool, 1),
		("", c_ulong, 0),
		("AnisoFrictionDir", FVector),
		("FrictionV", c_float),
		("Density", c_float),
		("AngularDamping", c_float),
		("LinearDamping", c_float),
		("MagneticResponse", c_float),
		("WindResponse", c_float),
		("ImpactThreshold", c_float),
		("ImpactReFireDelay", c_float),
		("ImpactEffect", POINTER(UParticleSystem)),
		("ImpactSound", POINTER(USoundCue)),
		("ImpactDefinition", POINTER(UImpactDefinition)),
		("SlideThreshold", c_float),
		("SlideReFireDelay", c_float),
		("SlideEffect", POINTER(UParticleSystem)),
		("SlideSound", POINTER(USoundCue)),
		("SlideImpactDefinition", POINTER(UImpactDefinition)),
		("FractureSoundExplosion", POINTER(USoundCue)),
		("FractureSoundSingle", POINTER(USoundCue)),
		("Parent", POINTER(UPhysicalMaterial)),
		("PhysicalMaterialProperty", POINTER(UPhysicalMaterialPropertyBase)),
	]

class  UPhysicalMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPhysicalMaterial", UPhysicalMaterial_Data),
	]


class  UPhysicalMaterialPropertyBase_Data(Structure):
	_fields_ = []

class  UPhysicalMaterialPropertyBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPhysicalMaterialPropertyBase", UPhysicalMaterialPropertyBase_Data),
	]


class  UPhysicsAsset_Data(Structure):
	_fields_ = [
		("BodySetup", TArray_URB_BodySetupPtr),
		("BodySetupIndexMap", FMap_Mirror),
		("BoundsBodies", TArray_int),
		("ConstraintSetup", TArray_URB_ConstraintSetupPtr),
		("DefaultInstance", POINTER(UPhysicsAssetInstance)),
	]

class  UPhysicsAsset(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPhysicsAsset", UPhysicsAsset_Data),
	]


class  UPhysicsAssetInstance_Data(Structure):
	_fields_ = [
		("Owner", POINTER(AActor)),
		("RootBodyIndex", c_int),
		("Bodies", TArray_URB_BodyInstancePtr),
		("Constraints", TArray_URB_ConstraintInstancePtr),
		("CollisionDisableTable", FMap_Mirror),
		("LinearSpringScale", c_float),
		("LinearDampingScale", c_float),
		("LinearForceLimitScale", c_float),
		("AngularSpringScale", c_float),
		("AngularDampingScale", c_float),
		("AngularForceLimitScale", c_float),
		("bInitBodies", c_bool, 1),
		("", c_ulong, 0),
	]

class  UPhysicsAssetInstance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPhysicsAssetInstance", UPhysicsAssetInstance_Data),
	]


class  UPhysicsLODVerticalEmitter_Data(Structure):
	_fields_ = [
		("ParticlePercentage", c_int),
	]

class  UPhysicsLODVerticalEmitter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPhysicsLODVerticalEmitter", UPhysicsLODVerticalEmitter_Data),
	]


class  URB_BodyInstance_Data(Structure):
	_fields_ = [
		("OwnerComponent", POINTER(UPrimitiveComponent)),
		("BodyIndex", c_int),
		("Velocity", FVector),
		("PreviousVelocity", FVector),
		("SceneIndex", c_int),
		("BodyData", FPointer),
		("BoneSpring", FPointer),
		("BoneSpringKinActor", FPointer),
		("bEnableBoneSpringLinear", c_bool, 1),
		("bEnableBoneSpringAngular", c_bool, 1),
		("bDisableOnOverextension", c_bool, 1),
		("bNotifyOwnerOnOverextension", c_bool, 1),
		("bTeleportOnOverextension", c_bool, 1),
		("bUseKinActorForBoneSpring", c_bool, 1),
		("bMakeSpringToBaseCollisionComponent", c_bool, 1),
		("bOnlyCollideWithPawns", c_bool, 1),
		("bEnableCollisionResponse", c_bool, 1),
		("bPushBody", c_bool, 1),
		("bForceUnfixed", c_bool, 1),
		("bInstanceAlwaysFullAnimWeight", c_bool, 1),
		("", c_ulong, 0),
		("BoneLinearSpring", c_float),
		("BoneLinearDamping", c_float),
		("BoneAngularSpring", c_float),
		("BoneAngularDamping", c_float),
		("OverextensionThreshold", c_float),
		("CustomGravityFactor", c_float),
		("LastEffectPlayedTime", c_float),
		("PhysMaterialOverride", POINTER(UPhysicalMaterial)),
		("ContactReportForceThreshold", c_float),
		("InstanceMassScale", c_float),
		("InstanceDampingScale", c_float),
	]

class  URB_BodyInstance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_BodyInstance", URB_BodyInstance_Data),
	]


class  URB_ConstraintInstance_Data(Structure):
	_fields_ = [
		("Owner", POINTER(AActor)),
		("OwnerComponent", POINTER(UPrimitiveComponent)),
		("ConstraintIndex", c_int),
		("SceneIndex", c_int),
		("bInHardware", c_bool, 1),
		("bLinearXPositionDrive", c_bool, 1),
		("bLinearXVelocityDrive", c_bool, 1),
		("bLinearYPositionDrive", c_bool, 1),
		("bLinearYVelocityDrive", c_bool, 1),
		("bLinearZPositionDrive", c_bool, 1),
		("bLinearZVelocityDrive", c_bool, 1),
		("bSwingPositionDrive", c_bool, 1),
		("bSwingVelocityDrive", c_bool, 1),
		("bTwistPositionDrive", c_bool, 1),
		("bTwistVelocityDrive", c_bool, 1),
		("bAngularSlerpDrive", c_bool, 1),
		("bTerminated", c_bool, 1),
		("", c_ulong, 0),
		("ConstraintData", FPointer),
		("LinearPositionTarget", FVector),
		("LinearVelocityTarget", FVector),
		("LinearDriveSpring", c_float),
		("LinearDriveDamping", c_float),
		("LinearDriveForceLimit", c_float),
		("Unknown1", c_ubyte, 0x),
		("AngularPositionTarget", FQuat),
		("AngularVelocityTarget", FVector),
		("AngularDriveSpring", c_float),
		("AngularDriveDamping", c_float),
		("AngularDriveForceLimit", c_float),
		("DummyKinActor", FPointer),
	]

class  URB_ConstraintInstance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintInstance", URB_ConstraintInstance_Data),
	]


class  URB_ConstraintSetup_Data(Structure):
	_fields_ = [
		("JointName", FName),
		("ConstraintBone1", FName),
		("ConstraintBone2", FName),
		("Pos1", FVector),
		("PriAxis1", FVector),
		("SecAxis1", FVector),
		("Pos2", FVector),
		("PriAxis2", FVector),
		("SecAxis2", FVector),
		("PulleyPivot1", FVector),
		("PulleyPivot2", FVector),
		("bEnableProjection", c_bool, 1),
		("bLinearLimitSoft", c_bool, 1),
		("bLinearBreakable", c_bool, 1),
		("bSwingLimited", c_bool, 1),
		("bTwistLimited", c_bool, 1),
		("bSwingLimitSoft", c_bool, 1),
		("bTwistLimitSoft", c_bool, 1),
		("bAngularBreakable", c_bool, 1),
		("bIsPulley", c_bool, 1),
		("bMaintainMinDistance", c_bool, 1),
		("", c_ulong, 0),
		("LinearXSetup", FLinearDOFSetup),
		("LinearYSetup", FLinearDOFSetup),
		("LinearZSetup", FLinearDOFSetup),
		("LinearLimitStiffness", c_float),
		("LinearLimitDamping", c_float),
		("LinearBreakThreshold", c_float),
		("Swing1LimitAngle", c_float),
		("Swing2LimitAngle", c_float),
		("TwistLimitAngle", c_float),
		("SwingLimitStiffness", c_float),
		("SwingLimitDamping", c_float),
		("TwistLimitStiffness", c_float),
		("TwistLimitDamping", c_float),
		("AngularBreakThreshold", c_float),
		("PulleyRatio", c_float),
	]

class  URB_ConstraintSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
	]


class  URB_BSJointSetup_Data(Structure):
	_fields_ = []

class  URB_BSJointSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_BSJointSetup", URB_BSJointSetup_Data),
	]


class  URB_DistanceJointSetup_Data(Structure):
	_fields_ = []

class  URB_DistanceJointSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_DistanceJointSetup", URB_DistanceJointSetup_Data),
	]


class  URB_HingeSetup_Data(Structure):
	_fields_ = []

class  URB_HingeSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_HingeSetup", URB_HingeSetup_Data),
	]


class  URB_PrismaticSetup_Data(Structure):
	_fields_ = []

class  URB_PrismaticSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_PrismaticSetup", URB_PrismaticSetup_Data),
	]


class  URB_PulleyJointSetup_Data(Structure):
	_fields_ = []

class  URB_PulleyJointSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_PulleyJointSetup", URB_PulleyJointSetup_Data),
	]


class  URB_SkelJointSetup_Data(Structure):
	_fields_ = []

class  URB_SkelJointSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_SkelJointSetup", URB_SkelJointSetup_Data),
	]


class  URB_StayUprightSetup_Data(Structure):
	_fields_ = []

class  URB_StayUprightSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("URB_ConstraintSetup", URB_ConstraintSetup_Data),
		("URB_StayUprightSetup", URB_StayUprightSetup_Data),
	]


class  USVehicleWheel_Data(Structure):
	_fields_ = [
		("Steer", c_float),
		("MotorTorque", c_float),
		("BrakeTorque", c_float),
		("ChassisTorque", c_float),
		("bPoweredWheel", c_bool, 1),
		("bHoverWheel", c_bool, 1),
		("bNoContactWheel", c_bool, 1),
		("bCollidesVehicles", c_bool, 1),
		("bCollidesPawns", c_bool, 1),
		("bIsSquealing", c_bool, 1),
		("bWheelOnGround", c_bool, 1),
		("bForceWantsParticleComponent", c_bool, 1),
		("", c_ulong, 0),
		("SteerFactor", c_float),
		("SkelControlName", FName),
		("WheelControl", POINTER(USkelControlWheel)),
		("BoneName", FName),
		("BoneOffset", FVector),
		("WheelRadius", c_float),
		("SuspensionTravel", c_float),
		("SuspensionSpeed", c_float),
		("WheelParticleSystem", POINTER(UParticleSystem)),
		("Side", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LongSlipFactor", c_float),
		("LatSlipFactor", c_float),
		("HandbrakeLongSlipFactor", c_float),
		("HandbrakeLatSlipFactor", c_float),
		("ParkedSlipFactorLat", c_float),
		("ParkedSlipFactorLong", c_float),
		("WheelPosition", FVector),
		("SpinVel", c_float),
		("LongSlipRatio", c_float),
		("LatSlipAngle", c_float),
		("ContactNormal", FVector),
		("LongDirection", FVector),
		("LatDirection", FVector),
		("ContactForce", c_float),
		("LongImpulse", c_float),
		("LatImpulse", c_float),
		("ContactPhysMat", POINTER(UPhysicalMaterial)),
		("WaterContactZOffset", c_float),
		("DesiredSuspensionPosition", c_float),
		("SuspensionPosition", c_float),
		("CurrentRotation", c_float),
		("WheelShape", FPointer),
		("WheelMaterialIndex", c_int),
		("WheelPSCClass", POINTER(UClass)),
		("WheelParticleComp", POINTER(UParticleSystemComponent)),
		("SlipParticleParamName", FName),
	]

class  USVehicleWheel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("USVehicleWheel", USVehicleWheel_Data),
	]


class  ANxGenericForceFieldBrush_Data(Structure):
	_fields_ = [
		("ExcludeChannel", c_int),
		("CollideWithChannels", FRBCollisionChannelContainer),
		("RBChannel", c_ubyte),
		("Coordinates", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Constant", FVector),
		("PositionMultiplierX", FVector),
		("PositionMultiplierY", FVector),
		("PositionMultiplierZ", FVector),
		("PositionTarget", FVector),
		("VelocityMultiplierX", FVector),
		("VelocityMultiplierY", FVector),
		("VelocityMultiplierZ", FVector),
		("VelocityTarget", FVector),
		("Noise", FVector),
		("FalloffLinear", FVector),
		("FalloffQuadratic", FVector),
		("TorusRadius", c_float),
		("ForceField", FPointer),
		("ConvexMeshes", TArray_FPointer),
		("ExclusionShapes", TArray_FPointer),
		("ExclusionShapePoses", TArray_FPointer),
		("LinearKernel", FPointer),
	]

class  ANxGenericForceFieldBrush(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ANxGenericForceFieldBrush", ANxGenericForceFieldBrush_Data),
	]


class  ARB_ForceFieldExcludeVolume_Data(Structure):
	_fields_ = [
		("ForceFieldChannel", c_int),
	]

class  ARB_ForceFieldExcludeVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ARB_ForceFieldExcludeVolume", ARB_ForceFieldExcludeVolume_Data),
	]


class  ANxForceField_Data(Structure):
	_fields_ = [
		("ExcludeChannel", c_int),
		("bForceActive", c_bool, 1),
		("", c_ulong, 0),
		("CollideWithChannels", FRBCollisionChannelContainer),
		("RBChannel", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ForceField", FPointer),
		("ConvexMeshes", TArray_FPointer),
		("ExclusionShapes", TArray_FPointer),
		("ExclusionShapePoses", TArray_FPointer),
		("U2NRotation", FPointer),
		("SceneIndex", c_int),
	]

class  ANxForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
	]


class  ANxCylindricalForceField_Data(Structure):
	_fields_ = [
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("UseSpecialRadialForce", c_bool, 1),
		("", c_ulong, 0),
		("Kernel", FPointer),
	]

class  ANxCylindricalForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxCylindricalForceField", ANxCylindricalForceField_Data),
	]


class  ANxCylindricalForceFieldCapsule_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawCapsuleComponent)),
	]

class  ANxCylindricalForceFieldCapsule(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxCylindricalForceField", ANxCylindricalForceField_Data),
		("ANxCylindricalForceFieldCapsule", ANxCylindricalForceFieldCapsule_Data),
	]


class  ANxForceFieldGeneric_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UForceFieldShape)),
		("DrawComponent", POINTER(UActorComponent)),
		("RoughExtentX", c_float),
		("RoughExtentY", c_float),
		("RoughExtentZ", c_float),
		("Coordinates", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Constant", FVector),
		("PositionMultiplierX", FVector),
		("PositionMultiplierY", FVector),
		("PositionMultiplierZ", FVector),
		("PositionTarget", FVector),
		("VelocityMultiplierX", FVector),
		("VelocityMultiplierY", FVector),
		("VelocityMultiplierZ", FVector),
		("VelocityTarget", FVector),
		("Noise", FVector),
		("FalloffLinear", FVector),
		("FalloffQuadratic", FVector),
		("TorusRadius", c_float),
		("LinearKernel", FPointer),
	]

class  ANxForceFieldGeneric(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxForceFieldGeneric", ANxForceFieldGeneric_Data),
	]


class  ANxForceFieldRadial_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UForceFieldShape)),
		("DrawComponent", POINTER(UActorComponent)),
		("ForceStrength", c_float),
		("ForceRadius", c_float),
		("SelfRotationStrength", c_float),
		("ForceFalloff", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Kernel", FPointer),
	]

class  ANxForceFieldRadial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxForceFieldRadial", ANxForceFieldRadial_Data),
	]


class  ANxForceFieldTornado_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UForceFieldShape)),
		("DrawComponent", POINTER(UActorComponent)),
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("BSpecialRadialForceMode", c_bool, 1),
		("", c_ulong, 0),
		("SelfRotationStrength", c_float),
		("Kernel", FPointer),
	]

class  ANxForceFieldTornado(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxForceFieldTornado", ANxForceFieldTornado_Data),
	]


class  ANxGenericForceField_Data(Structure):
	_fields_ = [
		("Coordinates", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Constant", FVector),
		("PositionMultiplierX", FVector),
		("PositionMultiplierY", FVector),
		("PositionMultiplierZ", FVector),
		("PositionTarget", FVector),
		("VelocityMultiplierX", FVector),
		("VelocityMultiplierY", FVector),
		("VelocityMultiplierZ", FVector),
		("VelocityTarget", FVector),
		("Noise", FVector),
		("FalloffLinear", FVector),
		("FalloffQuadratic", FVector),
		("TorusRadius", c_float),
		("LinearKernel", FPointer),
	]

class  ANxGenericForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxGenericForceField", ANxGenericForceField_Data),
	]


class  ANxGenericForceFieldBox_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawBoxComponent)),
		("BoxExtent", FVector),
	]

class  ANxGenericForceFieldBox(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxGenericForceField", ANxGenericForceField_Data),
		("ANxGenericForceFieldBox", ANxGenericForceFieldBox_Data),
	]


class  ANxGenericForceFieldCapsule_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawCapsuleComponent)),
		("CapsuleHeight", c_float),
		("CapsuleRadius", c_float),
	]

class  ANxGenericForceFieldCapsule(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxGenericForceField", ANxGenericForceField_Data),
		("ANxGenericForceFieldCapsule", ANxGenericForceFieldCapsule_Data),
	]


class  ANxRadialForceField_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawSphereComponent)),
		("ForceStrength", c_float),
		("ForceRadius", c_float),
		("ForceFalloff", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("LinearKernel", FPointer),
	]

class  ANxRadialForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxRadialForceField", ANxRadialForceField_Data),
	]


class  ANxRadialCustomForceField_Data(Structure):
	_fields_ = [
		("SelfRotationStrength", c_float),
		("Kernel", FPointer),
	]

class  ANxRadialCustomForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxRadialForceField", ANxRadialForceField_Data),
		("ANxRadialCustomForceField", ANxRadialCustomForceField_Data),
	]


class  ANxTornadoAngularForceField_Data(Structure):
	_fields_ = [
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("BSpecialRadialForceMode", c_bool, 1),
		("", c_ulong, 0),
		("SelfRotationStrength", c_float),
		("Kernel", FPointer),
	]

class  ANxTornadoAngularForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxTornadoAngularForceField", ANxTornadoAngularForceField_Data),
	]


class  ANxTornadoAngularForceFieldCapsule_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawCapsuleComponent)),
	]

class  ANxTornadoAngularForceFieldCapsule(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxTornadoAngularForceField", ANxTornadoAngularForceField_Data),
		("ANxTornadoAngularForceFieldCapsule", ANxTornadoAngularForceFieldCapsule_Data),
	]


class  ANxTornadoForceField_Data(Structure):
	_fields_ = [
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("BSpecialRadialForceMode", c_bool, 1),
		("", c_ulong, 0),
		("Kernel", FPointer),
	]

class  ANxTornadoForceField(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxTornadoForceField", ANxTornadoForceField_Data),
	]


class  ANxTornadoForceFieldCapsule_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawCapsuleComponent)),
	]

class  ANxTornadoForceFieldCapsule(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceField", ANxForceField_Data),
		("ANxTornadoForceField", ANxTornadoForceField_Data),
		("ANxTornadoForceFieldCapsule", ANxTornadoForceFieldCapsule_Data),
	]


class  ANxForceFieldSpawnable_Data(Structure):
	_fields_ = [
		("ForceFieldComponent", POINTER(UNxForceFieldComponent)),
	]

class  ANxForceFieldSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANxForceFieldSpawnable", ANxForceFieldSpawnable_Data),
	]


class  ARB_CylindricalForceActor_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawCylinderComponent)),
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("bForceActive", c_bool, 1),
		("bForceApplyToCloth", c_bool, 1),
		("bForceApplyToFluid", c_bool, 1),
		("bForceApplyToRigidBodies", c_bool, 1),
		("bForceApplyToProjectiles", c_bool, 1),
		("", c_ulong, 0),
		("CollideWithChannels", FRBCollisionChannelContainer),
	]

class  ARB_CylindricalForceActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_CylindricalForceActor", ARB_CylindricalForceActor_Data),
	]


class  ARB_RadialForceActor_Data(Structure):
	_fields_ = [
		("RenderComponent", POINTER(UDrawSphereComponent)),
		("ForceStrength", c_float),
		("ForceRadius", c_float),
		("SwirlStrength", c_float),
		("SpinTorque", c_float),
		("ForceFalloff", c_ubyte),
		("RadialForceMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bForceActive", c_bool, 1),
		("bForceApplyToCloth", c_bool, 1),
		("bForceApplyToFluid", c_bool, 1),
		("bForceApplyToRigidBodies", c_bool, 1),
		("bForceApplyToProjectiles", c_bool, 1),
		("", c_ulong, 0),
		("CollideWithChannels", FRBCollisionChannelContainer),
	]

class  ARB_RadialForceActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_RadialForceActor", ARB_RadialForceActor_Data),
	]


class  UNxForceFieldComponent_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UForceFieldShape)),
		("DrawComponent", POINTER(UActorComponent)),
		("ExcludeChannel", c_int),
		("bForceActive", c_bool, 1),
		("bDestroyWhenInactive", c_bool, 1),
		("", c_ulong, 0),
		("CollideWithChannels", FRBCollisionChannelContainer),
		("Duration", c_float),
		("ForceField", FPointer),
		("ConvexMeshes", TArray_FPointer),
		("ExclusionShapes", TArray_FPointer),
		("ExclusionShapePoses", TArray_FPointer),
		("SceneIndex", c_int),
		("ElapsedTime", c_float),
		("RenderComponent", POINTER(UPrimitiveComponent)),
		("RBPhysScene", FPointer),
	]

class  UNxForceFieldComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UNxForceFieldComponent", UNxForceFieldComponent_Data),
	]


class  UNxForceFieldCylindricalComponent_Data(Structure):
	_fields_ = [
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("UseSpecialRadialForce", c_bool, 1),
		("", c_ulong, 0),
		("Kernel", FPointer),
	]

class  UNxForceFieldCylindricalComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UNxForceFieldComponent", UNxForceFieldComponent_Data),
		("UNxForceFieldCylindricalComponent", UNxForceFieldCylindricalComponent_Data),
	]


class  UNxForceFieldGenericComponent_Data(Structure):
	_fields_ = [
		("RoughExtentX", c_float),
		("RoughExtentY", c_float),
		("RoughExtentZ", c_float),
		("Coordinates", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Constant", FVector),
		("PositionMultiplierX", FVector),
		("PositionMultiplierY", FVector),
		("PositionMultiplierZ", FVector),
		("PositionTarget", FVector),
		("VelocityMultiplierX", FVector),
		("VelocityMultiplierY", FVector),
		("VelocityMultiplierZ", FVector),
		("VelocityTarget", FVector),
		("Noise", FVector),
		("FalloffLinear", FVector),
		("FalloffQuadratic", FVector),
		("TorusRadius", c_float),
		("Kernel", FPointer),
	]

class  UNxForceFieldGenericComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UNxForceFieldComponent", UNxForceFieldComponent_Data),
		("UNxForceFieldGenericComponent", UNxForceFieldGenericComponent_Data),
	]


class  UNxForceFieldRadialComponent_Data(Structure):
	_fields_ = [
		("ForceStrength", c_float),
		("ForceRadius", c_float),
		("SelfRotationStrength", c_float),
		("ForceFalloff", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Kernel", FPointer),
	]

class  UNxForceFieldRadialComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UNxForceFieldComponent", UNxForceFieldComponent_Data),
		("UNxForceFieldRadialComponent", UNxForceFieldRadialComponent_Data),
	]


class  UNxForceFieldTornadoComponent_Data(Structure):
	_fields_ = [
		("RadialStrength", c_float),
		("RotationalStrength", c_float),
		("LiftStrength", c_float),
		("ForceRadius", c_float),
		("ForceTopRadius", c_float),
		("LiftFalloffHeight", c_float),
		("EscapeVelocity", c_float),
		("ForceHeight", c_float),
		("HeightOffset", c_float),
		("BSpecialRadialForceMode", c_bool, 1),
		("", c_ulong, 0),
		("SelfRotationStrength", c_float),
		("Kernel", FPointer),
	]

class  UNxForceFieldTornadoComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UNxForceFieldComponent", UNxForceFieldComponent_Data),
		("UNxForceFieldTornadoComponent", UNxForceFieldTornadoComponent_Data),
	]


class  UForceFieldShape_Data(Structure):
	_fields_ = []

class  UForceFieldShape(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UForceFieldShape", UForceFieldShape_Data),
	]


class  UForceFieldShapeBox_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UDrawBoxComponent)),
	]

class  UForceFieldShapeBox(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UForceFieldShape", UForceFieldShape_Data),
		("UForceFieldShapeBox", UForceFieldShapeBox_Data),
	]


class  UForceFieldShapeCapsule_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UDrawCapsuleComponent)),
	]

class  UForceFieldShapeCapsule(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UForceFieldShape", UForceFieldShape_Data),
		("UForceFieldShapeCapsule", UForceFieldShapeCapsule_Data),
	]


class  UForceFieldShapeSphere_Data(Structure):
	_fields_ = [
		("Shape", POINTER(UDrawSphereComponent)),
	]

class  UForceFieldShapeSphere(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UForceFieldShape", UForceFieldShape_Data),
		("UForceFieldShapeSphere", UForceFieldShapeSphere_Data),
	]


class  APrefabInstance_Data(Structure):
	_fields_ = [
		("TemplatePrefab", POINTER(UPrefab)),
		("TemplateVersion", c_int),
		("Unknown1", c_ubyte, 0x),
		("SequenceInstance", POINTER(UPrefabSequence)),
		("PI_PackageVersion", c_int),
		("PI_LicenseePackageVersion", c_int),
		("PI_GamePackageVersion", c_int),
		("PI_Bytes", TArray_unsigned_char),
		("PI_CompleteObjects", TArray_UObjectPtr),
		("PI_ReferencedObjects", TArray_UObjectPtr),
		("PI_SavedNames", TArray_FString),
		("Unknown2", c_ubyte, 0x),
	]

class  APrefabInstance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APrefabInstance", APrefabInstance_Data),
	]


class  UPrefab_Data(Structure):
	_fields_ = [
		("PrefabVersion", c_int),
		("PrefabArchetypes", TArray_UObjectPtr),
		("RemovedArchetypes", TArray_UObjectPtr),
		("PrefabSequence", POINTER(UPrefabSequence)),
	]

class  UPrefab(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPrefab", UPrefab_Data),
	]


class  USequenceObject_Data(Structure):
	_fields_ = [
		("ObjInstanceVersion", c_int),
		("ParentSequence", POINTER(USequence)),
		("bDeletable", c_bool, 1),
		("bDrawFirst", c_bool, 1),
		("bDrawLast", c_bool, 1),
		("bOutputObjCommentToScreen", c_bool, 1),
		("bSuppressAutoComment", c_bool, 1),
		("bShouldPersistWhenStreamedOut", c_bool, 1),
		("", c_ulong, 0),
	]

class  USequenceObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
	]


class  USequenceOp_Data(Structure):
	_fields_ = [
		("bIsActivated", c_bool, 1),
		("bIsCurrentDebuggerOp", c_bool, 1),
		("bActive", c_bool, 1),
		("bLatentExecution", c_bool, 1),
		("bSupportsMultipleActivations", c_bool, 1),
		("bAutoActivateOutputLinks", c_bool, 1),
		("bHaveMovingVarConnector", c_bool, 1),
		("bHaveMovingInputConnector", c_bool, 1),
		("bHaveMovingOutputConnector", c_bool, 1),
		("bPendingVarConnectorRecalc", c_bool, 1),
		("bPendingInputConnectorRecalc", c_bool, 1),
		("bPendingOutputConnectorRecalc", c_bool, 1),
		("bIsBreakpointSet", c_bool, 1),
		("bIsHiddenBreakpointSet", c_bool, 1),
		("bFlipWidgetVertical", c_bool, 1),
		("", c_ulong, 0),
		("InputLinks", TArray_FSeqOpInputLink),
		("OutputLinks", TArray_FSeqOpOutputLink),
		("VariableLinks", TArray_FSeqVarLink),
		("EventLinks", TArray_FSeqEventLink),
		("PlayerIndex", c_int),
		("GamepadID", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ActivateCount", c_int),
		("SearchTag", c_int),
	]

class  USequenceOp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
	]


class  USequenceEvent_Data(Structure):
	_fields_ = [
		("DuplicateEvts", TArray_USequenceEventPtr),
		("Originator", POINTER(AActor)),
		("Instigator", POINTER(AActor)),
		("ActivationTime", c_float),
		("TriggerCount", c_int),
		("MaxTriggerCount", c_int),
		("ReTriggerDelay", c_float),
		("bEnabled", c_bool, 1),
		("bPlayerOnly", c_bool, 1),
		("bAIOnly", c_bool, 1),
		("bRegistered", c_bool, 1),
		("bClientSideOnly", c_bool, 1),
		("", c_ulong, 0),
		("Priority", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MaxWidth", c_int),
		("RequiredAllegiance", POINTER(UPawnAllegiance)),
		("CustomEnableCondition", POINTER(USequenceEventCustomEnableCondition)),
	]

class  USequenceEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
	]


class  USequenceEventCustomEnableCondition_Data(Structure):
	_fields_ = []

class  USequenceEventCustomEnableCondition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceEventCustomEnableCondition", USequenceEventCustomEnableCondition_Data),
	]


class  USequenceFrame_Data(Structure):
	_fields_ = [
		("SizeX", c_int),
		("SizeY", c_int),
		("BorderWidth", c_int),
		("bDrawBox", c_bool, 1),
		("bFilled", c_bool, 1),
		("bTileFill", c_bool, 1),
		("", c_ulong, 0),
		("BorderColor", FColor),
		("FillColor", FColor),
	]

class  USequenceFrame(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceFrame", USequenceFrame_Data),
	]


class  USavingSequenceFrame_Data(Structure):
	_fields_ = []

class  USavingSequenceFrame(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceFrame", USequenceFrame_Data),
		("USavingSequenceFrame", USavingSequenceFrame_Data),
	]


class  USequenceFrameWrapped_Data(Structure):
	_fields_ = []

class  USequenceFrameWrapped(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceFrame", USequenceFrame_Data),
		("USequenceFrameWrapped", USequenceFrameWrapped_Data),
	]


class  USeqDef_Base_Data(Structure):
	_fields_ = [
		("Definition", POINTER(UGBXDefinition)),
	]

class  USeqDef_Base(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USeqDef_Base", USeqDef_Base_Data),
	]


class  USequence_Data(Structure):
	_fields_ = [
		("LogFile", FPointer),
		("SequenceObjects", TArray_USequenceObjectPtr),
		("ActiveSequenceOps", TArray_USequenceOpPtr),
		("NestedSequences", TArray_USequencePtr),
		("UnregisteredEvents", TArray_USequenceEventPtr),
		("DelayedActivatedOps", TArray_FActivateOp),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
		("QueuedActivations", TArray_FQueuedActivationInfo),
		("DefaultViewX", c_int),
		("DefaultViewY", c_int),
		("DefaultViewZoom", c_float),
	]

class  USequence(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequence", USequence_Data),
	]


class  UPrefabSequence_Data(Structure):
	_fields_ = [
		("OwnerPrefab", POINTER(APrefabInstance)),
	]

class  UPrefabSequence(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequence", USequence_Data),
		("UPrefabSequence", UPrefabSequence_Data),
	]


class  UPrefabSequenceContainer_Data(Structure):
	_fields_ = []

class  UPrefabSequenceContainer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequence", USequence_Data),
		("UPrefabSequenceContainer", UPrefabSequenceContainer_Data),
	]


class  USequenceDefinition_Data(Structure):
	_fields_ = []

class  USequenceDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequence", USequence_Data),
		("USequenceDefinition", USequenceDefinition_Data),
	]


class  USequenceAction_Data(Structure):
	_fields_ = [
		("HandlerName", FName),
		("bCallHandler", c_bool, 1),
		("", c_ulong, 0),
		("Targets", TArray_UObjectPtr),
	]

class  USequenceAction(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
	]


class  USeqAct_ActivateRemoteEvent_Data(Structure):
	_fields_ = [
		("Instigator", POINTER(AActor)),
		("EventName", FName),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_ActivateRemoteEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ActivateRemoteEvent", USeqAct_ActivateRemoteEvent_Data),
	]


class  USeqAct_AndGate_Data(Structure):
	_fields_ = [
		("bOpen", c_bool, 1),
		("", c_ulong, 0),
		("LinkedOutputFiredStatus", TArray_BOOL),
		("LinkedOutputs", TArray_FPointer),
	]

class  USeqAct_AndGate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_AndGate", USeqAct_AndGate_Data),
	]


class  USeqAct_ApplyBehavior_Data(Structure):
	_fields_ = [
		("Behaviors", TArray_UBehaviorBasePtr),
	]

class  USeqAct_ApplyBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ApplyBehavior", USeqAct_ApplyBehavior_Data),
	]


class  USeqAct_ApplySoundNode_Data(Structure):
	_fields_ = [
		("PlaySound", POINTER(USoundCue)),
		("ApplyNode", POINTER(USoundNode)),
	]

class  USeqAct_ApplySoundNode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ApplySoundNode", USeqAct_ApplySoundNode_Data),
	]


class  USeqAct_AttachToEvent_Data(Structure):
	_fields_ = [
		("bPreferController", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_AttachToEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_AttachToEvent", USeqAct_AttachToEvent_Data),
	]


class  USeqAct_CameraFade_Data(Structure):
	_fields_ = [
		("FadeColor", FColor),
		("FadeAlpha", FVector2D),
		("FadeOpacity", c_float),
		("FadeTime", c_float),
		("bPersistFade", c_bool, 1),
		("", c_ulong, 0),
		("FadeTimeRemaining", c_float),
		("CachedPCs", TArray_APlayerControllerPtr),
	]

class  USeqAct_CameraFade(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_CameraFade", USeqAct_CameraFade_Data),
	]


class  USeqAct_CameraLookAt_Data(Structure):
	_fields_ = [
		("bAffectCamera", c_bool, 1),
		("bAlwaysFocus", c_bool, 1),
		("bAdjustCamera", c_bool, 1),
		("bTurnInPlace", c_bool, 1),
		("bIgnoreTrace", c_bool, 1),
		("bAffectHead", c_bool, 1),
		("bRotatePlayerWithCamera", c_bool, 1),
		("bToggleGodMode", c_bool, 1),
		("bLeaveCameraRotation", c_bool, 1),
		("bDisableInput", c_bool, 1),
		("bUsedTimer", c_bool, 1),
		("bCheckLineOfSight", c_bool, 1),
		("", c_ulong, 0),
		("InterpSpeedRange", FVector2D),
		("InFocusFOV", FVector2D),
		("FocusBoneName", FName),
		("TextDisplay", FString),
		("TotalTime", c_float),
		("CameraFOV", c_float),
		("RemainingTime", c_float),
	]

class  USeqAct_CameraLookAt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_CameraLookAt", USeqAct_CameraLookAt_Data),
	]


class  USeqAct_ChangeCollision_Data(Structure):
	_fields_ = [
		("bCollideActors", c_bool, 1),
		("bBlockActors", c_bool, 1),
		("bIgnoreEncroachers", c_bool, 1),
		("", c_ulong, 0),
		("CollisionType", c_ubyte),
	]

class  USeqAct_ChangeCollision(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ChangeCollision", USeqAct_ChangeCollision_Data),
	]


class  USeqAct_CommitMapChange_Data(Structure):
	_fields_ = []

class  USeqAct_CommitMapChange(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_CommitMapChange", USeqAct_CommitMapChange_Data),
	]


class  USeqAct_ConsoleCommand_Data(Structure):
	_fields_ = [
		("Command", FString),
		("Commands", TArray_FString),
	]

class  USeqAct_ConsoleCommand(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ConsoleCommand", USeqAct_ConsoleCommand_Data),
	]


class  USeqAct_ConvertToString_Data(Structure):
	_fields_ = [
		("bIncludeVarComment", c_bool, 1),
		("", c_ulong, 0),
		("VarSeparator", FString),
		("NumberOfInputs", c_int),
	]

class  USeqAct_ConvertToString(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ConvertToString", USeqAct_ConvertToString_Data),
	]


class  USeqAct_DrawText_Data(Structure):
	_fields_ = [
		("DisplayTimeSeconds", c_float),
		("bDisplayOnObject", c_bool, 1),
		("", c_ulong, 0),
		("DrawTextInfo", FKismetDrawTextInfo),
	]

class  USeqAct_DrawText(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_DrawText", USeqAct_DrawText_Data),
	]


class  USeqAct_FinishSequence_Data(Structure):
	_fields_ = [
		("OutputLabel", FString),
	]

class  USeqAct_FinishSequence(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_FinishSequence", USeqAct_FinishSequence_Data),
	]


class  USeqAct_Gate_Data(Structure):
	_fields_ = [
		("bOpen", c_bool, 1),
		("", c_ulong, 0),
		("AutoCloseCount", c_int),
		("CurrentCloseCount", c_int),
	]

class  USeqAct_Gate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Gate", USeqAct_Gate_Data),
	]


class  USeqAct_GetDistance_Data(Structure):
	_fields_ = [
		("Distance", c_float),
		("Method", c_ubyte),
	]

class  USeqAct_GetDistance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_GetDistance", USeqAct_GetDistance_Data),
	]


class  USeqAct_GetLocationAndRotation_Data(Structure):
	_fields_ = [
		("Location", FVector),
		("RotationVector", FVector),
		("Rotation", FVector),
		("SocketOrBoneName", FName),
	]

class  USeqAct_GetLocationAndRotation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_GetLocationAndRotation", USeqAct_GetLocationAndRotation_Data),
	]


class  USeqAct_GetProperty_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
	]

class  USeqAct_GetProperty(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_GetProperty", USeqAct_GetProperty_Data),
	]


class  USeqAct_GetVectorComponents_Data(Structure):
	_fields_ = [
		("InVector", FVector),
		("X", c_float),
		("Y", c_float),
		("Z", c_float),
	]

class  USeqAct_GetVectorComponents(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_GetVectorComponents", USeqAct_GetVectorComponents_Data),
	]


class  USeqAct_GetVelocity_Data(Structure):
	_fields_ = [
		("VelocityMag", c_float),
		("VelocityVect", FVector),
	]

class  USeqAct_GetVelocity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_GetVelocity", USeqAct_GetVelocity_Data),
	]


class  USeqAct_HeadTrackingControl_Data(Structure):
	_fields_ = [
		("TrackControllerName", TArray_FName),
		("LookAtActorRadius", c_float),
		("bDisableBeyondLimit", c_bool, 1),
		("bLookAtPawns", c_bool, 1),
		("", c_ulong, 0),
		("MaxLookAtTime", c_float),
		("MinLookAtTime", c_float),
		("MaxInterestTime", c_float),
		("ActorClassesToLookAt", TArray_UClassPtr),
		("TargetBoneNames", TArray_FName),
		("LookAtTargets", TArray_UObjectPtr),
		("Unknown1", c_ubyte, 0x),
	]

class  USeqAct_HeadTrackingControl(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_HeadTrackingControl", USeqAct_HeadTrackingControl_Data),
	]


class  USeqAct_IsInObjectList_Data(Structure):
	_fields_ = [
		("bCheckForAllObjects", c_bool, 1),
		("bObjectFound", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_IsInObjectList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_IsInObjectList", USeqAct_IsInObjectList_Data),
	]


class  USeqAct_Latent_Data(Structure):
	_fields_ = [
		("LatentActors", TArray_AActorPtr),
		("bAborted", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_Latent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
	]


class  USeqAct_ActorFactory_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("bIsSpawning", c_bool, 1),
		("bCheckSpawnCollision", c_bool, 1),
		("", c_ulong, 0),
		("Factory", POINTER(UActorFactory)),
		("PointSelection", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("SpawnPoints", TArray_AActorPtr),
		("SpawnLocations", TArray_FVector),
		("SpawnOrientations", TArray_FVector),
		("SpawnCount", c_int),
		("SpawnDelay", c_float),
		("LastSpawnIdx", c_int),
		("SpawnedCount", c_int),
		("RemainingDelay", c_float),
	]

class  USeqAct_ActorFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_ActorFactory", USeqAct_ActorFactory_Data),
	]


class  USeqAct_ActorFactoryEx_Data(Structure):
	_fields_ = []

class  USeqAct_ActorFactoryEx(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_ActorFactory", USeqAct_ActorFactory_Data),
		("USeqAct_ActorFactoryEx", USeqAct_ActorFactoryEx_Data),
	]


class  USeqAct_ProjectileFactory_Data(Structure):
	_fields_ = [
		("PSTemplate", POINTER(UParticleSystem)),
		("SocketName", FName),
		("BoneName", FName),
	]

class  USeqAct_ProjectileFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_ActorFactory", USeqAct_ActorFactory_Data),
		("USeqAct_ProjectileFactory", USeqAct_ProjectileFactory_Data),
	]


class  USeqAct_AIMoveToActor_Data(Structure):
	_fields_ = [
		("bInterruptable", c_bool, 1),
		("bFaceDestinationDirection", c_bool, 1),
		("bPickClosest", c_bool, 1),
		("", c_ulong, 0),
		("Destination", TArray_AActorPtr),
		("MovementSpeedModifier", c_float),
		("LookAt", POINTER(AActor)),
		("LastDestinationChoice", c_int),
	]

class  USeqAct_AIMoveToActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_AIMoveToActor", USeqAct_AIMoveToActor_Data),
	]


class  USeqAct_Delay_Data(Structure):
	_fields_ = [
		("bDelayActive", c_bool, 1),
		("bStartWillRestart", c_bool, 1),
		("", c_ulong, 0),
		("DefaultDuration", c_float),
		("Duration", c_float),
		("LastUpdateTime", c_float),
		("RemainingTime", c_float),
	]

class  USeqAct_Delay(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_Delay", USeqAct_Delay_Data),
	]


class  USeqAct_DelaySwitch_Data(Structure):
	_fields_ = [
		("LinkCount", c_int),
		("CurrentIdx", c_int),
		("SwitchDelay", c_float),
		("NextLinkTime", c_float),
	]

class  USeqAct_DelaySwitch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_DelaySwitch", USeqAct_DelaySwitch_Data),
	]


class  USeqAct_ForceGarbageCollection_Data(Structure):
	_fields_ = []

class  USeqAct_ForceGarbageCollection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_ForceGarbageCollection", USeqAct_ForceGarbageCollection_Data),
	]


class  USeqAct_Interp_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("Unknown2", c_ubyte, 0x),
		("PlayRate", c_float),
		("Position", c_float),
		("ForceStartPosition", c_float),
		("bIsPlaying", c_bool, 1),
		("bPaused", c_bool, 1),
		("bIsBeingEdited", c_bool, 1),
		("bLooping", c_bool, 1),
		("bRewindOnPlay", c_bool, 1),
		("bNoResetOnRewind", c_bool, 1),
		("bRewindIfAlreadyPlaying", c_bool, 1),
		("bReversePlayback", c_bool, 1),
		("bInterpForPathBuilding", c_bool, 1),
		("bForceStartPos", c_bool, 1),
		("bDisableRadioFilter", c_bool, 1),
		("bClientSideOnly", c_bool, 1),
		("bSkipUpdateIfNotVisible", c_bool, 1),
		("bIsSkippable", c_bool, 1),
		("bIsSkipped", c_bool, 1),
		("bShouldShowGore", c_bool, 1),
		("TestForInputActorsOnClient", c_bool, 1),
		("bFireEventsWhenJumpToLastFrame", c_bool, 1),
		("bFireCompleteEventWhenJumpToLastFrame", c_bool, 1),
		("bLastFrameEventFired", c_bool, 1),
		("bSkipNextUpdate", c_bool, 1),
		("bInitialReplication", c_bool, 1),
		("", c_ulong, 0),
		("LinkedCover", TArray_ACoverLinkPtr),
		("InterpData", POINTER(UInterpData)),
		("GroupInst", TArray_UInterpGroupInstPtr),
		("ReplicatedActorClass", POINTER(UClass)),
		("ReplicatedActor", POINTER(AMatineeActor)),
		("PreferredSplitScreenNum", c_int),
		("CameraCuts", TArray_FCameraCutInfo),
		("TerminationTime", c_float),
		("RenderingOverrides", FRenderingPerformanceOverrides),
	]

class  USeqAct_Interp(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_Interp", USeqAct_Interp_Data),
	]


class  USeqAct_LevelStreamingBase_Data(Structure):
	_fields_ = [
		("bMakeVisibleAfterLoad", c_bool, 1),
		("bShouldBlockOnLoad", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_LevelStreamingBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_LevelStreamingBase", USeqAct_LevelStreamingBase_Data),
	]


class  USeqAct_LevelStreaming_Data(Structure):
	_fields_ = [
		("Level", POINTER(ULevelStreaming)),
		("LevelName", FName),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_LevelStreaming(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_LevelStreamingBase", USeqAct_LevelStreamingBase_Data),
		("USeqAct_LevelStreaming", USeqAct_LevelStreaming_Data),
	]


class  USeqAct_MultiLevelStreaming_Data(Structure):
	_fields_ = [
		("Levels", TArray_FLevelStreamingNameCombo),
		("bUnloadAllOtherLevels", c_bool, 1),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_MultiLevelStreaming(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_LevelStreamingBase", USeqAct_LevelStreamingBase_Data),
		("USeqAct_MultiLevelStreaming", USeqAct_MultiLevelStreaming_Data),
	]


class  USeqAct_LevelVisibility_Data(Structure):
	_fields_ = [
		("Level", POINTER(ULevelStreaming)),
		("LevelName", FName),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_LevelVisibility(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_LevelVisibility", USeqAct_LevelVisibility_Data),
	]


class  USeqAct_PlaySound_Data(Structure):
	_fields_ = [
		("PlaySound", POINTER(USoundCue)),
		("ExtraDelay", c_float),
		("SoundDuration", c_float),
		("FadeInTime", c_float),
		("FadeOutTime", c_float),
		("VolumeMultiplier", c_float),
		("PitchMultiplier", c_float),
		("bSuppressSubtitles", c_bool, 1),
		("bStopped", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_PlaySound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_PlaySound", USeqAct_PlaySound_Data),
	]


class  USeqAct_PrepareMapChange_Data(Structure):
	_fields_ = [
		("MainLevelName", FName),
		("InitiallyLoadedSecondaryLevelNames", TArray_FName),
		("bIsHighPriority", c_bool, 1),
		("bTransitionToFakeEntry", c_bool, 1),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_PrepareMapChange(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_PrepareMapChange", USeqAct_PrepareMapChange_Data),
	]


class  USeqAct_SetDOFParams_Data(Structure):
	_fields_ = [
		("FalloffExponent", c_float),
		("BlurKernelSize", c_float),
		("MaxNearBlurAmount", c_float),
		("MinBlurAmount", c_float),
		("MaxFarBlurAmount", c_float),
		("FocusInnerRadius", c_float),
		("FocusDistance", c_float),
		("FocusPosition", FVector),
		("InterpolateSeconds", c_float),
		("InterpolateElapsed", c_float),
		("OldFalloffExponent", c_float),
		("OldBlurKernelSize", c_float),
		("OldMaxNearBlurAmount", c_float),
		("OldMinBlurAmount", c_float),
		("OldMaxFarBlurAmount", c_float),
		("OldFocusInnerRadius", c_float),
		("OldFocusDistance", c_float),
		("OldFocusPosition", FVector),
	]

class  USeqAct_SetDOFParams(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_SetDOFParams", USeqAct_SetDOFParams_Data),
	]


class  USeqAct_SetMotionBlurParams_Data(Structure):
	_fields_ = [
		("MotionBlurAmount", c_float),
		("InterpolateSeconds", c_float),
		("InterpolateElapsed", c_float),
		("OldMotionBlurAmount", c_float),
	]

class  USeqAct_SetMotionBlurParams(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_SetMotionBlurParams", USeqAct_SetMotionBlurParams_Data),
	]


class  USeqAct_StreamInTextures_Data(Structure):
	_fields_ = [
		("bLocationBased", c_bool, 1),
		("bStreamingActive", c_bool, 1),
		("bHasTriggeredAllLoaded", c_bool, 1),
		("", c_ulong, 0),
		("Seconds", c_float),
		("StreamingDistanceMultiplier", c_float),
		("NumWantingResourcesID", c_int),
		("StopTimestamp", c_float),
		("LocationActors", TArray_UObjectPtr),
		("ForceMaterials", TArray_UMaterialInterfacePtr),
		("CinematicTextureGroups", FTextureGroupContainer),
		("SelectedCinematicTextureGroups", c_int),
	]

class  USeqAct_StreamInTextures(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_StreamInTextures", USeqAct_StreamInTextures_Data),
	]


class  USeqAct_WaitForLevelsVisible_Data(Structure):
	_fields_ = [
		("LevelNames", TArray_FName),
		("bShouldBlockOnLoad", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_WaitForLevelsVisible(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Latent", USeqAct_Latent_Data),
		("USeqAct_WaitForLevelsVisible", USeqAct_WaitForLevelsVisible_Data),
	]


class  USeqAct_Log_Data(Structure):
	_fields_ = [
		("bOutputToScreen", c_bool, 1),
		("bIncludeObjComment", c_bool, 1),
		("", c_ulong, 0),
		("TargetDuration", c_float),
		("TargetOffset", FVector),
		("LogMessage", FString),
	]

class  USeqAct_Log(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Log", USeqAct_Log_Data),
	]


class  USeqAct_ModifyCover_Data(Structure):
	_fields_ = [
		("Slots", TArray_int),
		("ManualCoverType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bManualAdjustPlayersOnly", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_ModifyCover(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ModifyCover", USeqAct_ModifyCover_Data),
	]


class  USeqAct_ModifyHealth_Data(Structure):
	_fields_ = [
		("DamageType", POINTER(UClass)),
		("DamageTypeDefinition", POINTER(UDamageTypeDefinition)),
		("ImpactDefinition", POINTER(UImpactDefinition)),
		("Momentum", c_float),
		("Amount", c_float),
		("Radius", c_float),
		("bHeal", c_bool, 1),
		("bRadial", c_bool, 1),
		("bFalloff", c_bool, 1),
		("", c_ulong, 0),
		("Instigator", POINTER(AActor)),
	]

class  USeqAct_ModifyHealth(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ModifyHealth", USeqAct_ModifyHealth_Data),
	]


class  USeqAct_ParticleEventGenerator_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("bUseEmitterLocation", c_bool, 1),
		("", c_ulong, 0),
		("Instigator", POINTER(AActor)),
		("EventNames", TArray_FString),
		("EventTime", c_float),
		("EventLocation", FVector),
		("EventDirection", FVector),
		("EventVelocity", FVector),
		("EventNormal", FVector),
	]

class  USeqAct_ParticleEventGenerator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ParticleEventGenerator", USeqAct_ParticleEventGenerator_Data),
	]


class  USeqAct_PhysXSwitch_Data(Structure):
	_fields_ = []

class  USeqAct_PhysXSwitch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_PhysXSwitch", USeqAct_PhysXSwitch_Data),
	]


class  USeqAct_PlayCameraAnim_Data(Structure):
	_fields_ = [
		("CameraAnim", POINTER(UCameraAnim)),
		("bLoop", c_bool, 1),
		("bRandomStartTime", c_bool, 1),
		("", c_ulong, 0),
		("BlendInTime", c_float),
		("BlendOutTime", c_float),
		("Rate", c_float),
		("IntensityScale", c_float),
		("PlaySpace", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("UserDefinedSpaceActor", POINTER(AActor)),
	]

class  USeqAct_PlayCameraAnim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_PlayCameraAnim", USeqAct_PlayCameraAnim_Data),
	]


class  USeqAct_PlayFaceFXAnim_Data(Structure):
	_fields_ = [
		("FaceFXAnimSetRef", POINTER(UFaceFXAnimSet)),
		("FaceFXGroupName", FString),
		("FaceFXAnimName", FString),
		("SoundCueToPlay", POINTER(USoundCue)),
		("AkEventToPlay", POINTER(UAkEvent)),
	]

class  USeqAct_PlayFaceFXAnim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_PlayFaceFXAnim", USeqAct_PlayFaceFXAnim_Data),
	]


class  USeqAct_PlayMusicTrack_Data(Structure):
	_fields_ = [
		("MusicTrack", FMusicTrackStruct),
	]

class  USeqAct_PlayMusicTrack(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_PlayMusicTrack", USeqAct_PlayMusicTrack_Data),
	]


class  USeqAct_Possess_Data(Structure):
	_fields_ = [
		("PawnToPossess", POINTER(APawn)),
		("bKillOldPawn", c_bool, 1),
		("bTryToLeaveVehicle", c_bool, 1),
		("bBypassVehicleEntryAnimation", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_Possess(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Possess", USeqAct_Possess_Data),
	]


class  USeqAct_SetApexClothingParam_Data(Structure):
	_fields_ = [
		("bEnableApexClothingSimulation", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_SetApexClothingParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetApexClothingParam", USeqAct_SetApexClothingParam_Data),
	]


class  USeqAct_SetBlockRigidBody_Data(Structure):
	_fields_ = []

class  USeqAct_SetBlockRigidBody(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetBlockRigidBody", USeqAct_SetBlockRigidBody_Data),
	]


class  USeqAct_SetCameraTarget_Data(Structure):
	_fields_ = [
		("CameraTarget", POINTER(AActor)),
		("TransitionParams", FViewTargetTransitionParams),
	]

class  USeqAct_SetCameraTarget(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetCameraTarget", USeqAct_SetCameraTarget_Data),
	]


class  USeqAct_SetMaterial_Data(Structure):
	_fields_ = [
		("NewMaterial", POINTER(UMaterialInterface)),
		("MaterialIndex", c_int),
	]

class  USeqAct_SetMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetMaterial", USeqAct_SetMaterial_Data),
	]


class  USeqAct_SetMatInstScalarParam_Data(Structure):
	_fields_ = [
		("MatInst", POINTER(UMaterialInstanceConstant)),
		("ParamName", FName),
		("ScalarValue", c_float),
	]

class  USeqAct_SetMatInstScalarParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetMatInstScalarParam", USeqAct_SetMatInstScalarParam_Data),
	]


class  USeqAct_SetMesh_Data(Structure):
	_fields_ = [
		("NewSkeletalMesh", POINTER(USkeletalMesh)),
		("NewStaticMesh", POINTER(UStaticMesh)),
		("MeshType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bIsAllowedToMove", c_bool, 1),
		("bAllowDecalsToReattach", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_SetMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetMesh", USeqAct_SetMesh_Data),
	]


class  USeqAct_SetPhysics_Data(Structure):
	_fields_ = [
		("newPhysics", c_ubyte),
	]

class  USeqAct_SetPhysics(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetPhysics", USeqAct_SetPhysics_Data),
	]


class  USeqAct_SetRigidBodyIgnoreVehicles_Data(Structure):
	_fields_ = []

class  USeqAct_SetRigidBodyIgnoreVehicles(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetRigidBodyIgnoreVehicles", USeqAct_SetRigidBodyIgnoreVehicles_Data),
	]


class  USeqAct_SetSequenceVariable_Data(Structure):
	_fields_ = []

class  USeqAct_SetSequenceVariable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
	]


class  USeqAct_AccessObjectList_Data(Structure):
	_fields_ = [
		("OutputObject", POINTER(UObject)),
		("ObjectIndex", c_int),
	]

class  USeqAct_AccessObjectList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_AccessObjectList", USeqAct_AccessObjectList_Data),
	]


class  USeqAct_AddFloat_Data(Structure):
	_fields_ = [
		("ValueA", c_float),
		("ValueB", c_float),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_AddFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_AddFloat", USeqAct_AddFloat_Data),
	]


class  USeqAct_AddInt_Data(Structure):
	_fields_ = [
		("ValueA", c_int),
		("ValueB", c_int),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_AddInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_AddInt", USeqAct_AddInt_Data),
	]


class  USeqAct_CastToFloat_Data(Structure):
	_fields_ = [
		("Value", c_int),
		("FloatResult", c_float),
	]

class  USeqAct_CastToFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_CastToFloat", USeqAct_CastToFloat_Data),
	]


class  USeqAct_CastToInt_Data(Structure):
	_fields_ = [
		("bTruncate", c_bool, 1),
		("", c_ulong, 0),
		("Value", c_float),
		("IntResult", c_int),
	]

class  USeqAct_CastToInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_CastToInt", USeqAct_CastToInt_Data),
	]


class  USeqAct_DivideFloat_Data(Structure):
	_fields_ = [
		("ValueA", c_float),
		("ValueB", c_float),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_DivideFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_DivideFloat", USeqAct_DivideFloat_Data),
	]


class  USeqAct_DivideInt_Data(Structure):
	_fields_ = [
		("ValueA", c_int),
		("ValueB", c_int),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_DivideInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_DivideInt", USeqAct_DivideInt_Data),
	]


class  USeqAct_ModifyObjectList_Data(Structure):
	_fields_ = [
		("ListEntriesCount", c_int),
	]

class  USeqAct_ModifyObjectList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_ModifyObjectList", USeqAct_ModifyObjectList_Data),
	]


class  USeqAct_MultiplyFloat_Data(Structure):
	_fields_ = [
		("ValueA", c_float),
		("ValueB", c_float),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_MultiplyFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_MultiplyFloat", USeqAct_MultiplyFloat_Data),
	]


class  USeqAct_MultiplyInt_Data(Structure):
	_fields_ = [
		("ValueA", c_int),
		("ValueB", c_int),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_MultiplyInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_MultiplyInt", USeqAct_MultiplyInt_Data),
	]


class  USeqAct_SetBool_Data(Structure):
	_fields_ = [
		("DefaultValue", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_SetBool(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetBool", USeqAct_SetBool_Data),
	]


class  USeqAct_SetFloat_Data(Structure):
	_fields_ = [
		("Target", c_float),
		("Value", TArray_float),
	]

class  USeqAct_SetFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetFloat", USeqAct_SetFloat_Data),
	]


class  USeqAct_SetInt_Data(Structure):
	_fields_ = [
		("Target", c_int),
		("Value", TArray_int),
	]

class  USeqAct_SetInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetInt", USeqAct_SetInt_Data),
	]


class  USeqAct_SetLocation_Data(Structure):
	_fields_ = [
		("bSetLocation", c_bool, 1),
		("bSetRotation", c_bool, 1),
		("", c_ulong, 0),
		("LocationValue", FVector),
		("RotationValue", FRotator),
		("Target", POINTER(UObject)),
	]

class  USeqAct_SetLocation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetLocation", USeqAct_SetLocation_Data),
	]


class  USeqAct_SetObject_Data(Structure):
	_fields_ = [
		("DefaultValue", POINTER(UObject)),
		("Value", POINTER(UObject)),
	]

class  USeqAct_SetObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetObject", USeqAct_SetObject_Data),
	]


class  USeqAct_SetString_Data(Structure):
	_fields_ = [
		("Target", FString),
		("Value", FString),
	]

class  USeqAct_SetString(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetString", USeqAct_SetString_Data),
	]


class  USeqAct_SubtractFloat_Data(Structure):
	_fields_ = [
		("ValueA", c_float),
		("ValueB", c_float),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_SubtractFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SubtractFloat", USeqAct_SubtractFloat_Data),
	]


class  USeqAct_SubtractInt_Data(Structure):
	_fields_ = [
		("ValueA", c_int),
		("ValueB", c_int),
		("FloatResult", c_float),
		("IntResult", c_int),
	]

class  USeqAct_SubtractInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SubtractInt", USeqAct_SubtractInt_Data),
	]


class  USeqAct_SetVectorComponents_Data(Structure):
	_fields_ = [
		("OutVector", FVector),
		("X", c_float),
		("Y", c_float),
		("Z", c_float),
	]

class  USeqAct_SetVectorComponents(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetVectorComponents", USeqAct_SetVectorComponents_Data),
	]


class  USeqAct_Switch_Data(Structure):
	_fields_ = [
		("LinkCount", c_int),
		("IncrementAmount", c_int),
		("bLooping", c_bool, 1),
		("bAutoDisableLinks", c_bool, 1),
		("", c_ulong, 0),
		("Indices", TArray_int),
	]

class  USeqAct_Switch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Switch", USeqAct_Switch_Data),
	]


class  USeqAct_RandomSwitch_Data(Structure):
	_fields_ = [
		("AutoDisabledIndices", TArray_int),
	]

class  USeqAct_RandomSwitch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Switch", USeqAct_Switch_Data),
		("USeqAct_RandomSwitch", USeqAct_RandomSwitch_Data),
	]


class  USeqAct_Timer_Data(Structure):
	_fields_ = [
		("ActivationTime", c_float),
		("Time", c_float),
	]

class  USeqAct_Timer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Timer", USeqAct_Timer_Data),
	]


class  USeqAct_Toggle_Data(Structure):
	_fields_ = []

class  USeqAct_Toggle(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Toggle", USeqAct_Toggle_Data),
	]


class  USeqAct_Trace_Data(Structure):
	_fields_ = [
		("bTraceActors", c_bool, 1),
		("bTraceWorld", c_bool, 1),
		("", c_ulong, 0),
		("TraceExtent", FVector),
		("StartOffset", FVector),
		("EndOffset", FVector),
		("HitObject", POINTER(UObject)),
		("Distance", c_float),
		("HitLocation", FVector),
	]

class  USeqAct_Trace(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Trace", USeqAct_Trace_Data),
	]


class  USequenceCondition_Data(Structure):
	_fields_ = []

class  USequenceCondition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
	]


class  USeqCond_CompareBool_Data(Structure):
	_fields_ = [
		("bResult", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqCond_CompareBool(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_CompareBool", USeqCond_CompareBool_Data),
	]


class  USeqCond_CompareFloat_Data(Structure):
	_fields_ = [
		("ValueA", c_float),
		("ValueB", c_float),
	]

class  USeqCond_CompareFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_CompareFloat", USeqCond_CompareFloat_Data),
	]


class  USeqCond_CompareInt_Data(Structure):
	_fields_ = [
		("ValueA", c_int),
		("ValueB", c_int),
	]

class  USeqCond_CompareInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_CompareInt", USeqCond_CompareInt_Data),
	]


class  USeqCond_CompareObject_Data(Structure):
	_fields_ = []

class  USeqCond_CompareObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_CompareObject", USeqCond_CompareObject_Data),
	]


class  USeqCond_GetServerType_Data(Structure):
	_fields_ = []

class  USeqCond_GetServerType(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_GetServerType", USeqCond_GetServerType_Data),
	]


class  USeqCond_Increment_Data(Structure):
	_fields_ = [
		("IncrementAmount", c_int),
		("ValueA", c_int),
		("ValueB", c_int),
	]

class  USeqCond_Increment(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_Increment", USeqCond_Increment_Data),
	]


class  USeqCond_IncrementFloat_Data(Structure):
	_fields_ = [
		("IncrementAmount", c_float),
		("ValueA", c_float),
		("ValueB", c_float),
	]

class  USeqCond_IncrementFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IncrementFloat", USeqCond_IncrementFloat_Data),
	]


class  USeqCond_IsAlive_Data(Structure):
	_fields_ = []

class  USeqCond_IsAlive(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsAlive", USeqCond_IsAlive_Data),
	]


class  USeqCond_IsBenchmarking_Data(Structure):
	_fields_ = []

class  USeqCond_IsBenchmarking(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsBenchmarking", USeqCond_IsBenchmarking_Data),
	]


class  USeqCond_IsConsole_Data(Structure):
	_fields_ = []

class  USeqCond_IsConsole(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsConsole", USeqCond_IsConsole_Data),
	]


class  USeqCond_IsInCombat_Data(Structure):
	_fields_ = []

class  USeqCond_IsInCombat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsInCombat", USeqCond_IsInCombat_Data),
	]


class  USeqCond_IsLoggedIn_Data(Structure):
	_fields_ = [
		("NumNeededLoggedIn", c_int),
	]

class  USeqCond_IsLoggedIn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsLoggedIn", USeqCond_IsLoggedIn_Data),
	]


class  USeqCond_IsPIE_Data(Structure):
	_fields_ = []

class  USeqCond_IsPIE(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsPIE", USeqCond_IsPIE_Data),
	]


class  USeqCond_IsSameTeam_Data(Structure):
	_fields_ = []

class  USeqCond_IsSameTeam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_IsSameTeam", USeqCond_IsSameTeam_Data),
	]


class  USeqCond_MatureLanguage_Data(Structure):
	_fields_ = []

class  USeqCond_MatureLanguage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_MatureLanguage", USeqCond_MatureLanguage_Data),
	]


class  USeqCond_ShowGore_Data(Structure):
	_fields_ = []

class  USeqCond_ShowGore(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_ShowGore", USeqCond_ShowGore_Data),
	]


class  USeqCond_SwitchBase_Data(Structure):
	_fields_ = []

class  USeqCond_SwitchBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_SwitchBase", USeqCond_SwitchBase_Data),
	]


class  USeqCond_SwitchClass_Data(Structure):
	_fields_ = [
		("ClassArray", TArray_FSwitchClassInfo),
	]

class  USeqCond_SwitchClass(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_SwitchBase", USeqCond_SwitchBase_Data),
		("USeqCond_SwitchClass", USeqCond_SwitchClass_Data),
	]


class  USeqCond_SwitchObject_Data(Structure):
	_fields_ = [
		("SupportedValues", TArray_FSwitchObjectCase),
	]

class  USeqCond_SwitchObject(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_SwitchBase", USeqCond_SwitchBase_Data),
		("USeqCond_SwitchObject", USeqCond_SwitchObject_Data),
	]


class  USeqCond_SwitchPlatform_Data(Structure):
	_fields_ = []

class  USeqCond_SwitchPlatform(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceCondition", USequenceCondition_Data),
		("USeqCond_SwitchPlatform", USeqCond_SwitchPlatform_Data),
	]


class  USeqEvent_AISeeEnemy_Data(Structure):
	_fields_ = [
		("MaxSightDistance", c_float),
	]

class  USeqEvent_AISeeEnemy(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_AISeeEnemy", USeqEvent_AISeeEnemy_Data),
	]


class  USeqEvent_AnimNotify_Data(Structure):
	_fields_ = [
		("NotifyName", FName),
	]

class  USeqEvent_AnimNotify(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_AnimNotify", USeqEvent_AnimNotify_Data),
	]


class  USeqEvent_Console_Data(Structure):
	_fields_ = [
		("ConsoleEventName", FName),
		("EventDesc", FString),
	]

class  USeqEvent_Console(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_Console", USeqEvent_Console_Data),
	]


class  USeqEvent_ConstraintBroken_Data(Structure):
	_fields_ = []

class  USeqEvent_ConstraintBroken(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_ConstraintBroken", USeqEvent_ConstraintBroken_Data),
	]


class  USeqEvent_Destroyed_Data(Structure):
	_fields_ = []

class  USeqEvent_Destroyed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_Destroyed", USeqEvent_Destroyed_Data),
	]


class  USeqEvent_LevelLoaded_Data(Structure):
	_fields_ = []

class  USeqEvent_LevelLoaded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_LevelLoaded", USeqEvent_LevelLoaded_Data),
	]


class  USeqEvent_Mover_Data(Structure):
	_fields_ = [
		("StayOpenTime", c_float),
	]

class  USeqEvent_Mover(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_Mover", USeqEvent_Mover_Data),
	]


class  USeqEvent_ParticleEvent_Data(Structure):
	_fields_ = [
		("EventType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("EventPosition", FVector),
		("EventEmitterTime", c_float),
		("EventVelocity", FVector),
		("EventParticleTime", c_float),
		("EventNormal", FVector),
		("UseRelfectedImpactVector", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqEvent_ParticleEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_ParticleEvent", USeqEvent_ParticleEvent_Data),
	]


class  USeqEvent_ProjectileLanded_Data(Structure):
	_fields_ = [
		("MaxDistance", c_float),
	]

class  USeqEvent_ProjectileLanded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_ProjectileLanded", USeqEvent_ProjectileLanded_Data),
	]


class  USeqEvent_RemoteEvent_Data(Structure):
	_fields_ = [
		("EventName", FName),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqEvent_RemoteEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_RemoteEvent", USeqEvent_RemoteEvent_Data),
	]


class  USeqEvent_RigidBodyCollision_Data(Structure):
	_fields_ = [
		("MinCollisionVelocity", c_float),
	]

class  USeqEvent_RigidBodyCollision(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_RigidBodyCollision", USeqEvent_RigidBodyCollision_Data),
	]


class  USeqEvent_SeeDeath_Data(Structure):
	_fields_ = []

class  USeqEvent_SeeDeath(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_SeeDeath", USeqEvent_SeeDeath_Data),
	]


class  USeqEvent_SequenceActivated_Data(Structure):
	_fields_ = [
		("InputLabel", FString),
	]

class  USeqEvent_SequenceActivated(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_SequenceActivated", USeqEvent_SequenceActivated_Data),
	]


class  USeqEvent_TakeDamage_Data(Structure):
	_fields_ = [
		("MinDamageAmount", c_float),
		("DamageThreshold", c_float),
		("DamageTypes", TArray_UClassPtr),
		("DamageTypeDefinitions", TArray_UDamageTypeDefinitionPtr),
		("IgnoreDamageTypes", TArray_UClassPtr),
		("IgnoreDamageTypeDefinitions", TArray_UDamageTypeDefinitionPtr),
		("CurrentDamage", c_float),
		("bResetDamageOnToggle", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqEvent_TakeDamage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_TakeDamage", USeqEvent_TakeDamage_Data),
	]


class  USeqEvent_Touch_Data(Structure):
	_fields_ = [
		("ClassProximityTypes", TArray_UClassPtr),
		("ArchetypeFilter", TArray_AActorPtr),
		("IgnoredClassProximityTypes", TArray_UClassPtr),
		("bForceOverlapping", c_bool, 1),
		("bUseInstigator", c_bool, 1),
		("bAllowDeadPawns", c_bool, 1),
		("", c_ulong, 0),
		("TouchedList", TArray_AActorPtr),
	]

class  USeqEvent_Touch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_Touch", USeqEvent_Touch_Data),
	]


class  USeqEvent_Used_Data(Structure):
	_fields_ = [
		("bAimToInteract", c_bool, 1),
		("bUseInteractDistance", c_bool, 1),
		("", c_ulong, 0),
		("InteractDistance", c_float),
		("InteractText", FString),
		("InteractIcon", POINTER(UTexture2D)),
		("ClassProximityTypes", TArray_UClassPtr),
		("IgnoredClassProximityTypes", TArray_UClassPtr),
	]

class  USeqEvent_Used(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_Used", USeqEvent_Used_Data),
	]


class  USequenceVariable_Data(Structure):
	_fields_ = [
		("VarName", FName),
		("bLinkToAttribute", c_bool, 1),
		("", c_ulong, 0),
		("OptionalAttributeDefinition", POINTER(UAttributeDefinition)),
	]

class  USequenceVariable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
	]


class  UInterpData_Data(Structure):
	_fields_ = [
		("InterpLength", c_float),
		("PathBuildTime", c_float),
		("InterpGroups", TArray_UInterpGroupPtr),
		("CurveEdSetup", POINTER(UInterpCurveEdSetup)),
		("EdSectionStart", c_float),
		("EdSectionEnd", c_float),
		("bShouldBakeAndPrune", c_bool, 1),
		("", c_ulong, 0),
		("BakeAndPruneStatus", TArray_FAnimSetBakeAndPruneStatus),
		("CachedDirectorGroup", POINTER(UInterpGroupDirector)),
	]

class  UInterpData(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("UInterpData", UInterpData_Data),
	]


class  USeqVar_Bool_Data(Structure):
	_fields_ = [
		("bValue", c_int),
	]

class  USeqVar_Bool(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Bool", USeqVar_Bool_Data),
	]


class  USeqVar_External_Data(Structure):
	_fields_ = [
		("ExpectedType", POINTER(UClass)),
		("VariableLabel", FString),
	]

class  USeqVar_External(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_External", USeqVar_External_Data),
	]


class  USeqVar_Float_Data(Structure):
	_fields_ = [
		("FloatValue", c_float),
	]

class  USeqVar_Float(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Float", USeqVar_Float_Data),
	]


class  USeqVar_RandomFloat_Data(Structure):
	_fields_ = [
		("Min", c_float),
		("Max", c_float),
	]

class  USeqVar_RandomFloat(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Float", USeqVar_Float_Data),
		("USeqVar_RandomFloat", USeqVar_RandomFloat_Data),
	]


class  USeqVar_Int_Data(Structure):
	_fields_ = [
		("IntValue", c_int),
	]

class  USeqVar_Int(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Int", USeqVar_Int_Data),
	]


class  USeqVar_RandomInt_Data(Structure):
	_fields_ = [
		("Min", c_int),
		("Max", c_int),
	]

class  USeqVar_RandomInt(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Int", USeqVar_Int_Data),
		("USeqVar_RandomInt", USeqVar_RandomInt_Data),
	]


class  USeqVar_Named_Data(Structure):
	_fields_ = [
		("ExpectedType", POINTER(UClass)),
		("FindVarName", FName),
		("bStatusIsOk", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqVar_Named(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Named", USeqVar_Named_Data),
	]


class  USeqVar_Object_Data(Structure):
	_fields_ = [
		("ObjValue", POINTER(UObject)),
		("ActorLocation", FVector),
	]

class  USeqVar_Object(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Object", USeqVar_Object_Data),
	]


class  USeqVar_Character_Data(Structure):
	_fields_ = [
		("PawnClass", POINTER(UClass)),
	]

class  USeqVar_Character(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Object", USeqVar_Object_Data),
		("USeqVar_Character", USeqVar_Character_Data),
	]


class  USeqVar_Group_Data(Structure):
	_fields_ = [
		("GroupName", FName),
		("bCachedList", c_bool, 1),
		("", c_ulong, 0),
		("Actors", TArray_UObjectPtr),
	]

class  USeqVar_Group(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Object", USeqVar_Object_Data),
		("USeqVar_Group", USeqVar_Group_Data),
	]


class  USeqVar_ObjectList_Data(Structure):
	_fields_ = [
		("ObjList", TArray_UObjectPtr),
	]

class  USeqVar_ObjectList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Object", USeqVar_Object_Data),
		("USeqVar_ObjectList", USeqVar_ObjectList_Data),
	]


class  USeqVar_ObjectVolume_Data(Structure):
	_fields_ = [
		("LastUpdateTime", c_float),
		("ContainedObjects", TArray_UObjectPtr),
		("ExcludeClassList", TArray_UClassPtr),
		("bCollidingOnly", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqVar_ObjectVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Object", USeqVar_Object_Data),
		("USeqVar_ObjectVolume", USeqVar_ObjectVolume_Data),
	]


class  USeqVar_Player_Data(Structure):
	_fields_ = [
		("Players", TArray_UObjectPtr),
		("bAllPlayers", c_bool, 1),
		("", c_ulong, 0),
		("PlayerIdx", c_int),
	]

class  USeqVar_Player(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Object", USeqVar_Object_Data),
		("USeqVar_Player", USeqVar_Player_Data),
	]


class  USeqVar_String_Data(Structure):
	_fields_ = [
		("StrValue", FString),
	]

class  USeqVar_String(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_String", USeqVar_String_Data),
	]


class  USeqVar_Vector_Data(Structure):
	_fields_ = [
		("VectValue", FVector),
	]

class  USeqVar_Vector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Vector", USeqVar_Vector_Data),
	]


class  AAmbientSound_Data(Structure):
	_fields_ = [
		("bAutoPlay", c_bool, 1),
		("bIsPlaying", c_bool, 1),
		("", c_ulong, 0),
		("AudioComponent", POINTER(UAudioComponent)),
	]

class  AAmbientSound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AKeypoint", AKeypoint_Data),
		("AAmbientSound", AAmbientSound_Data),
	]


class  UDistributionFloatSoundParameter_Data(Structure):
	_fields_ = []

class  UDistributionFloatSoundParameter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UDistributionFloat", UDistributionFloat_Data),
		("UDistributionFloatConstant", UDistributionFloatConstant_Data),
		("UDistributionFloatParameterBase", UDistributionFloatParameterBase_Data),
		("UDistributionFloatSoundParameter", UDistributionFloatSoundParameter_Data),
	]


class  USoundNode_Data(Structure):
	_fields_ = [
		("NodeUpdateHint", c_int),
		("ChildNodes", TArray_USoundNodePtr),
	]

class  USoundNode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USoundNode", USoundNode_Data),
	]


class  USoundNodeWave_Data(Structure):
	_fields_ = [
		("CompressionQuality", c_int),
		("bForceRealTimeDecompression", c_bool, 1),
		("bLoopingSound", c_bool, 1),
		("bDynamicResource", c_bool, 1),
		("bUseTTS", c_bool, 1),
		("bProcedural", c_bool, 1),
		("bStreamable", c_bool, 1),
		("bLoopedOnPS3", c_bool, 1),
		("bMature", c_bool, 1),
		("bManualWordWrap", c_bool, 1),
		("bSingleLine", c_bool, 1),
		("", c_ulong, 0),
		("TTSSpeaker", c_ubyte),
		("DecompressionType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("SpokenText", FString),
		("Volume", c_float),
		("Pitch", c_float),
		("Duration", c_float),
		("NumChannels", c_int),
		("SampleRate", c_int),
		("RawData", FUntypedBulkData_Mirror),
		("VorbisDecompressor", FPointer),
		("RawPCMData", FPointer),
		("RawPCMDataSize", c_int),
		("CompressedPCData", FUntypedBulkData_Mirror),
		("CompressedXbox360Data", FUntypedBulkData_Mirror),
		("CompressedPS3Data", FUntypedBulkData_Mirror),
		("ResourceID", c_int),
		("ResourceSize", c_int),
		("ResourceData", FPointer),
		("Subtitles", TArray_FSubtitleCue),
		("LocalizedSubtitles", TArray_FLocalizedSubtitle),
	]

class  USoundNodeWave(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USoundNode", USoundNode_Data),
		("USoundNodeWave", USoundNodeWave_Data),
	]


class  ALandscapeProxy_Data(Structure):
	_fields_ = [
		("LandscapeComponents", TArray_ULandscapeComponentPtr),
		("CollisionComponents", TArray_ULandscapeHeightfieldCollisionComponentPtr),
		("Unknown1", c_ubyte, 0x),
		("Unknown2", c_ubyte, 0x),
		("StaticLightingResolution", c_float),
		("LandscapeActor", POINTER(ALandscape)),
		("bIsProxy", c_bool, 1),
		("", c_ulong, 0),
	]

class  ALandscapeProxy(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("ALandscapeProxy", ALandscapeProxy_Data),
	]


class  ALandscape_Data(Structure):
	_fields_ = [
		("LandscapeMaterial", POINTER(UMaterialInterface)),
		("MaxLODLevel", c_int),
		("LayerNames", TArray_FName),
		("LayerInfos", TArray_FLandscapeLayerInfo),
		("StreamingDistanceMultiplier", c_float),
		("Unknown1", c_ubyte, 0x),
		("Unknown2", c_ubyte, 0x),
		("Unknown3", c_ubyte, 0x),
		("DataInterface", FPointer),
		("ComponentSizeQuads", c_int),
		("SubsectionSizeQuads", c_int),
		("NumSubsections", c_int),
		("Proxies", FSet_Mirror),
	]

class  ALandscape(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("ALandscapeProxy", ALandscapeProxy_Data),
		("ALandscape", ALandscape_Data),
	]


class  ATerrain_Data(Structure):
	_fields_ = [
		("Heights", TArray_FTerrainHeight),
		("InfoData", TArray_FTerrainInfoData),
		("Layers", TArray_FTerrainLayer),
		("NormalMapLayer", c_int),
		("DecoLayers", TArray_FTerrainDecoLayer),
		("AlphaMaps", TArray_FAlphaMap),
		("TerrainComponents", TArray_UTerrainComponentPtr),
		("NumSectionsX", c_int),
		("NumSectionsY", c_int),
		("WeightedMaterials", TArray_ATerrain_FTerrainWeightedMaterial),
		("WeightedTextureMaps", TArray_UTerrainWeightMapTexturePtr),
		("MaxTesselationLevel", c_int),
		("WeightmapQuadAlphaThreshold", c_ubyte),
		("WeightmapTexelAlphaThreshold", c_ubyte),
		("WeightmapQuadMaxLayers", c_ubyte),
		("WeightmapTexelMaxLayers", c_ubyte),
		("WeightmapTesselationLevel", c_int),
		("PreviousWeightmapTesselationLevel", c_int),
		("CachedTerrainMaterials", FCachedTerrainMaterialArray * 2),
		("TerrainMaterialGBX", POINTER(UMaterial)),
		("TerrainMaterialResourceGBX", FPointer),
		("NumPatchesX", c_int),
		("PreviousNumPatchesX", c_int),
		("NumPatchesY", c_int),
		("PreviousNumPatchesY", c_int),
		("MaxComponentSize", c_int),
		("StaticLightingResolution", c_int),
		("bIsOverridingLightResolution", c_bool, 1),
		("bBilinearFilterLightmapGeneration", c_bool, 1),
		("bCastShadow", c_bool, 1),
		("bForceDirectLightMap", c_bool, 1),
		("bCastDynamicShadow", c_bool, 1),
		("bEnableSpecular", c_bool, 1),
		("bBlockRigidBody", c_bool, 1),
		("bAllowRigidBodyUnderneath", c_bool, 1),
		("bAcceptsDynamicLights", c_bool, 1),
		("bLocked", c_bool, 1),
		("bHeightmapLocked", c_bool, 1),
		("bUseWorldOriginTextureUVs", c_bool, 1),
		("bAllowDuplication", c_bool, 1),
		("bBlockUnreal", c_bool, 1),
		("", c_ulong, 0),
		("TerrainPhysMaterialOverride", POINTER(UPhysicalMaterial)),
		("LightingChannels", FLightingChannelContainer),
		("ReleaseResourcesFence", FPointer),
		("SelectedVertices", TArray_FSelectedTerrainVertex),
	]

class  ATerrain(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("ATerrain", ATerrain_Data),
	]


class  ULandscapeComponent_Data(Structure):
	_fields_ = [
		("SectionBaseX", c_int),
		("SectionBaseY", c_int),
		("ComponentSizeQuads", c_int),
		("SubsectionSizeQuads", c_int),
		("NumSubsections", c_int),
		("MaterialInstance", POINTER(UMaterialInstanceConstant)),
		("WeightmapLayerAllocations", TArray_FWeightmapLayerAllocationInfo),
		("WeightmapTextures", TArray_UTexture2DPtr),
		("WeightmapScaleBias", FVector4),
		("WeightmapSubsectionOffset", c_float),
		("Unknown1", c_ubyte, 0x),
		("HeightmapScaleBias", FVector4),
		("HeightmapTexture", POINTER(UTexture2D)),
		("CachedBoxSphereBounds", FBoxSphereBounds),
		("StaticLightingResolution", c_int),
		("ShadowMaps", TArray_UShadowMap2DPtr),
		("IrrelevantLights", TArray_FGuid),
		("LightMap", FLightMapRef),
		("EditToolRenderData", FPointer),
		("CollisionMipLevel", c_int),
		("PlatformData", FPointer),
		("PlatformDataSize", c_int),
	]

class  ULandscapeComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("ULandscapeComponent", ULandscapeComponent_Data),
	]


class  ULandscapeHeightfieldCollisionComponent_Data(Structure):
	_fields_ = [
		("CollisionHeightData", FUntypedBulkData_Mirror),
		("SectionBaseX", c_int),
		("SectionBaseY", c_int),
		("CollisionSizeQuads", c_int),
		("CollisionScale", c_float),
		("CollisionQuadFlags", TArray_unsigned_char),
		("PhysicalMaterials", TArray_UPhysicalMaterialPtr),
		("RBHeightfield", FPointer),
		("CachedBoxSphereBounds", FBoxSphereBounds),
	]

class  ULandscapeHeightfieldCollisionComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("ULandscapeHeightfieldCollisionComponent", ULandscapeHeightfieldCollisionComponent_Data),
	]


class  UTerrainComponent_Data(Structure):
	_fields_ = [
		("ShadowMaps", TArray_UShadowMap2DPtr),
		("IrrelevantLights", TArray_FGuid),
		("TerrainObject", FPointer),
		("TerrainRenderResources", FPointer),
		("SectionBaseX", c_int),
		("SectionBaseY", c_int),
		("SectionSizeX", c_int),
		("SectionSizeY", c_int),
		("TrueSectionSizeX", c_int),
		("TrueSectionSizeY", c_int),
		("LightMap", FPointer),
		("BatchMaterials", TArray_int),
		("FullBatch", c_int),
		("GameBVTree", FTerrainBVTree),
		("EditorBVTree", FTerrainBVTree),
		("RBHeightfield", FPointer),
	]

class  UTerrainComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UTerrainComponent", UTerrainComponent_Data),
	]


class  UTerrainWeightMapTexture_Data(Structure):
	_fields_ = []

class  UTerrainWeightMapTexture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2D", UTexture2D_Data),
		("UTerrainWeightMapTexture", UTerrainWeightMapTexture_Data),
	]


class  UTerrainLayerSetup_Data(Structure):
	_fields_ = [
		("Materials", TArray_FTerrainFilteredMaterial),
	]

class  UTerrainLayerSetup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UTerrainLayerSetup", UTerrainLayerSetup_Data),
	]


class  UTerrainMaterial_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("LocalToMapping", FMatrix),
		("MappingType", c_ubyte),
		("Unknown2", c_ubyte, 0x),
		("MappingScale", c_float),
		("MappingRotation", c_float),
		("MappingPanU", c_float),
		("MappingPanV", c_float),
		("Material", POINTER(UMaterialInterface)),
		("DisplacementMap", POINTER(UTexture2D)),
		("DisplacementScale", c_float),
		("FoliageMeshes", TArray_FTerrainFoliageMesh),
	]

class  UTerrainMaterial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UTerrainMaterial", UTerrainMaterial_Data),
	]


class  UDataStoreClient_Data(Structure):
	_fields_ = [
		("GlobalDataStoreClasses", TArray_FString),
		("GlobalDataStores", TArray_UUIDataStorePtr),
		("PlayerDataStoreClassNames", TArray_FString),
		("PlayerDataStoreClasses", TArray_UClassPtr),
		("PlayerDataStores", TArray_FPlayerDataStoreGroup),
	]

class  UDataStoreClient(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UDataStoreClient", UDataStoreClient_Data),
	]


class  UConsole_Data(Structure):
	_fields_ = [
		("ConsoleTargetPlayer", POINTER(ULocalPlayer)),
		("DefaultTexture_Black", POINTER(UTexture2D)),
		("DefaultTexture_White", POINTER(UTexture2D)),
		("ConsoleKey", FName),
		("TypeKey", FName),
		("MaxScrollbackSize", c_int),
		("Scrollback", TArray_FString),
		("SBHead", c_int),
		("SBPos", c_int),
		("HistoryTop", c_int),
		("HistoryBot", c_int),
		("HistoryCur", c_int),
		("History", FString * 16),
		("bNavigatingHistory", c_bool, 1),
		("bCaptureKeyInput", c_bool, 1),
		("bCtrl", c_bool, 1),
		("bEnableUI", c_bool, 1),
		("bAutoCompleteLocked", c_bool, 1),
		("bRequireCtrlToNavigateAutoComplete", c_bool, 1),
		("bIsRuntimeAutoCompleteUpToDate", c_bool, 1),
		("", c_ulong, 0),
		("TypedStr", FString),
		("TypedStrPos", c_int),
		("ManualAutoCompleteList", TArray_FAutoCompleteCommand),
		("AutoCompleteList", TArray_FAutoCompleteCommand),
		("AutoCompleteIndex", c_int),
		("AutoCompleteTree", FAutoCompleteNode),
		("AutoCompleteIndices", TArray_int),
	]

class  UConsole(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
		("UConsole", UConsole_Data),
	]


class  UInput_Data(Structure):
	_fields_ = [
		("Bindings", TArray_FKeyBind),
		("PressedKeys", TArray_FName),
		("CurrentEvent", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CurrentDelta", c_float),
		("CurrentDeltaTime", c_float),
		("Unknown2", c_ubyte, 0x),
		("AxisArray", TArray_FPointer),
	]

class  UInput(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
		("UInput", UInput_Data),
	]


class  UPlayerInput_Data(Structure):
	_fields_ = [
		("bUsingGamepad", c_bool, 1),
		("bInvertGamepad", c_bool, 1),
		("bInvertMouse", c_bool, 1),
		("bInvertTurn", c_bool, 1),
		("bInvertGamepadTurn", c_bool, 1),
		("bInvertGamepadMove", c_bool, 1),
		("bInvertGamepadStrafe", c_bool, 1),
		("bWasForward", c_bool, 1),
		("bWasBack", c_bool, 1),
		("bWasLeft", c_bool, 1),
		("bWasRight", c_bool, 1),
		("bEdgeForward", c_bool, 1),
		("bEdgeBack", c_bool, 1),
		("bEdgeLeft", c_bool, 1),
		("bEdgeRight", c_bool, 1),
		("bEnableMouseSmoothing", c_bool, 1),
		("bEnableFOVScaling", c_bool, 1),
		("bLockTurnUntilRelease", c_bool, 1),
		("", c_ulong, 0),
		("LastAxisKeyName", FName),
		("DoubleClickTimer", c_float),
		("DoubleClickTime", c_float),
		("MouseSensitivity", c_float),
		("aBaseX", c_float),
		("aBaseY", c_float),
		("aBaseZ", c_float),
		("aMouseX", c_float),
		("aMouseY", c_float),
		("aForward", c_float),
		("aTurn", c_float),
		("aStrafe", c_float),
		("aUp", c_float),
		("aLookUp", c_float),
		("aRightAnalogTrigger", c_float),
		("aLeftAnalogTrigger", c_float),
		("aPS3AccelX", c_float),
		("aPS3AccelY", c_float),
		("aPS3AccelZ", c_float),
		("aPS3Gyro", c_float),
		("RawJoyUp", c_float),
		("RawJoyRight", c_float),
		("RawJoyLookRight", c_float),
		("RawJoyLookUp", c_float),
		("MoveForwardSpeed", c_float),
		("MoveStrafeSpeed", c_float),
		("LookRightScale", c_float),
		("LookUpScale", c_float),
		("bStrafe", c_ubyte),
		("bXAxis", c_ubyte),
		("bYAxis", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ZeroTime", c_float * 2),
		("SmoothedMouse", c_float * 2),
		("MouseSamples", c_int),
		("MouseSamplingTotal", c_float),
		("AutoUnlockTurnTime", c_float),
	]

class  UPlayerInput(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
		("UInput", UInput_Data),
		("UPlayerInput", UPlayerInput_Data),
	]


class  UPlayerManagerInteraction_Data(Structure):
	_fields_ = []

class  UPlayerManagerInteraction(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
		("UPlayerManagerInteraction", UPlayerManagerInteraction_Data),
	]


class  UUISceneClient_Data(Structure):
	_fields_ = [
		("VfTable_FExec", FPointer),
		("RenderViewport", FPointer),
		("MousePosition", FIntPoint),
		("DataStoreManager", POINTER(UDataStoreClient)),
		("Unknown1", c_ubyte, 0x),
		("CanvasToScreen", FMatrix),
		("InvCanvasToScreen", FMatrix),
		("UIScenePostProcess", POINTER(UPostProcessChain)),
		("bEnablePostProcess", c_bool, 1),
		("", c_ulong, 0),
	]

class  UUISceneClient(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUISceneClient", UUISceneClient_Data),
	]


class  UUISoundTheme_Data(Structure):
	_fields_ = [
		("SoundEventBindings", TArray_FSoundEventMapping),
	]

class  UUISoundTheme(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUISoundTheme", UUISoundTheme_Data),
	]


class  UUIDataStoreSubscriber_Data(Structure):
	_fields_ = []

class  UUIDataStoreSubscriber(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UUIDataStoreSubscriber", UUIDataStoreSubscriber_Data),
	]


class  UUIDataStorePublisher_Data(Structure):
	_fields_ = []

class  UUIDataStorePublisher(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UUIDataStoreSubscriber", UUIDataStoreSubscriber_Data),
		("UUIDataStorePublisher", UUIDataStorePublisher_Data),
	]


class  UUIListElementCellProvider_Data(Structure):
	_fields_ = []

class  UUIListElementCellProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UUIListElementCellProvider", UUIListElementCellProvider_Data),
	]


class  UUIListElementProvider_Data(Structure):
	_fields_ = []

class  UUIListElementProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UUIListElementProvider", UUIListElementProvider_Data),
	]


class  UUIDataProvider_Data(Structure):
	_fields_ = [
		("WriteAccessType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ProviderChangedNotifies", TArray_FScriptDelegate),
		("__OnDataProviderPropertyChange__Delegate", FScriptDelegate),
	]

class  UUIDataProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
	]


class  UUIConfigProvider_Data(Structure):
	_fields_ = []

class  UUIConfigProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIConfigProvider", UUIConfigProvider_Data),
	]


class  UUIConfigFileProvider_Data(Structure):
	_fields_ = [
		("Sections", TArray_UUIConfigSectionProviderPtr),
		("ConfigFileName", FString),
	]

class  UUIConfigFileProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIConfigProvider", UUIConfigProvider_Data),
		("UUIConfigFileProvider", UUIConfigFileProvider_Data),
	]


class  UUIConfigSectionProvider_Data(Structure):
	_fields_ = [
		("SectionName", FString),
	]

class  UUIConfigSectionProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIConfigProvider", UUIConfigProvider_Data),
		("UUIConfigSectionProvider", UUIConfigSectionProvider_Data),
	]


class  UUIDataProvider_OnlinePlayerDataBase_Data(Structure):
	_fields_ = [
		("PlayerControllerId", c_int),
	]

class  UUIDataProvider_OnlinePlayerDataBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
	]


class  UUIDataProvider_OnlineFriendMessages_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementCellProvider", FPointer),
		("Messages", TArray_FOnlineFriendMessage),
		("SendingPlayerNameCol", FString),
		("bIsFriendInviteCol", FString),
		("bWasAcceptedCol", FString),
		("bWasDeniedCol", FString),
		("MessageCol", FString),
		("LastInviteFrom", FString),
	]

class  UUIDataProvider_OnlineFriendMessages(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
		("UUIDataProvider_OnlineFriendMessages", UUIDataProvider_OnlineFriendMessages_Data),
	]


class  UUIDataProvider_OnlineFriends_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementCellProvider", FPointer),
		("FriendsList", TArray_FOnlineFriend),
		("NickNameCol", FString),
		("PresenceInfoCol", FString),
		("FriendStateCol", FString),
		("bIsOnlineCol", FString),
		("bIsPlayingCol", FString),
		("bIsPlayingThisGameCol", FString),
		("bIsJoinableCol", FString),
		("bHasVoiceSupportCol", FString),
		("bHaveInvitedCol", FString),
		("bHasInvitedYouCol", FString),
		("bHaveRequestedCol", FString),
		("bHasRequestedYouCol", FString),
		("OfflineText", FString),
		("OnlineText", FString),
		("AwayText", FString),
		("BusyText", FString),
	]

class  UUIDataProvider_OnlineFriends(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
		("UUIDataProvider_OnlineFriends", UUIDataProvider_OnlineFriends_Data),
	]


class  UUIDataProvider_OnlinePartyChatList_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementCellProvider", FPointer),
		("PartyMembersList", TArray_FOnlinePartyMember),
		("NatTypes", TArray_FString),
		("NickNameCol", FString),
		("NatTypeCol", FString),
		("IsLocalCol", FString),
		("IsInPartyVoiceCol", FString),
		("IsTalkingCol", FString),
		("IsInGameSessionCol", FString),
		("IsPlayingThisGameCol", FString),
	]

class  UUIDataProvider_OnlinePartyChatList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
		("UUIDataProvider_OnlinePartyChatList", UUIDataProvider_OnlinePartyChatList_Data),
	]


class  UUIDataProvider_OnlinePlayerStorage_Data(Structure):
	_fields_ = [
		("Profile", POINTER(UOnlinePlayerStorage)),
		("ProviderName", FName),
		("bWasErrorLastRead", c_bool, 1),
		("bIsExternalUIOpen", c_bool, 1),
		("bNeedsDeferredRefresh", c_bool, 1),
		("", c_ulong, 0),
		("PlayerStorageArrayProviders", TArray_FPlayerStorageArrayProvider),
		("DeviceStorageSizeNeeded", c_int),
	]

class  UUIDataProvider_OnlinePlayerStorage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
		("UUIDataProvider_OnlinePlayerStorage", UUIDataProvider_OnlinePlayerStorage_Data),
	]


class  UUIDataProvider_OnlineProfileSettings_Data(Structure):
	_fields_ = []

class  UUIDataProvider_OnlineProfileSettings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
		("UUIDataProvider_OnlinePlayerStorage", UUIDataProvider_OnlinePlayerStorage_Data),
		("UUIDataProvider_OnlineProfileSettings", UUIDataProvider_OnlineProfileSettings_Data),
	]


class  UUIDataProvider_PlayerAchievements_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementCellProvider", FPointer),
		("Achievements", TArray_FAchievementDetails),
	]

class  UUIDataProvider_PlayerAchievements(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerDataBase", UUIDataProvider_OnlinePlayerDataBase_Data),
		("UUIDataProvider_PlayerAchievements", UUIDataProvider_PlayerAchievements_Data),
	]


class  UUIDataProvider_OnlinePlayerStorageArray_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("VfTable_IUIListElementCellProvider", FPointer),
		("PlayerStorage", POINTER(UOnlinePlayerStorage)),
		("PlayerStorageId", c_int),
		("PlayerStorageName", FName),
		("ColumnHeaderText", FString),
		("Values", TArray_FName),
	]

class  UUIDataProvider_OnlinePlayerStorageArray(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_OnlinePlayerStorageArray", UUIDataProvider_OnlinePlayerStorageArray_Data),
	]


class  UUIDataProvider_SettingsArray_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("VfTable_IUIListElementCellProvider", FPointer),
		("Settings", POINTER(USettings)),
		("SettingsId", c_int),
		("SettingsName", FName),
		("ColumnHeaderText", FString),
		("Values", TArray_FIdToStringMapping),
	]

class  UUIDataProvider_SettingsArray(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataProvider_SettingsArray", UUIDataProvider_SettingsArray_Data),
	]


class  UUIDataStore_Data(Structure):
	_fields_ = [
		("Tag", FName),
		("RefreshSubscriberNotifies", TArray_FScriptDelegate),
		("__OnDataStoreValueUpdated__Delegate", FScriptDelegate),
	]

class  UUIDataStore(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
	]


class  UUIDataStore_DynamicResource_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("ProfileProvider", POINTER(UUIDataProvider_OnlineProfileSettings)),
		("GameResourceDataStore", POINTER(UUIDataStore_GameResource)),
		("ResourceProviderDefinitions", TArray_FDynamicResourceProviderDefinition),
		("ResourceProviders", FMultiMap_Mirror),
	]

class  UUIDataStore_DynamicResource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_DynamicResource", UUIDataStore_DynamicResource_Data),
	]


class  UUIDataStore_Fonts_Data(Structure):
	_fields_ = []

class  UUIDataStore_Fonts(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Fonts", UUIDataStore_Fonts_Data),
	]


class  UUIDataStore_GameResource_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("ElementProviderTypes", TArray_FGameResourceDataProvider),
		("ListElementProviders", FMultiMap_Mirror),
	]

class  UUIDataStore_GameResource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_GameResource", UUIDataStore_GameResource_Data),
	]


class  UUIDataStore_MenuItems_Data(Structure):
	_fields_ = [
		("CurrentGameSettingsTag", FName),
		("OptionProviders", FMultiMap_Mirror),
		("DynamicProviders", TArray_UUIDataProvider_MenuItemPtr),
	]

class  UUIDataStore_MenuItems(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_GameResource", UUIDataStore_GameResource_Data),
		("UUIDataStore_MenuItems", UUIDataStore_MenuItems_Data),
	]


class  UUIDataStore_GameState_Data(Structure):
	_fields_ = [
		("__OnRefreshDataFieldValue__Delegate", FScriptDelegate),
	]

class  UUIDataStore_GameState(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_GameState", UUIDataStore_GameState_Data),
	]


class  UUIDataStore_Registry_Data(Structure):
	_fields_ = [
		("RegistryDataProvider", POINTER(UUIDynamicFieldProvider)),
	]

class  UUIDataStore_Registry(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Registry", UUIDataStore_Registry_Data),
	]


class  UUIDataStore_Remote_Data(Structure):
	_fields_ = []

class  UUIDataStore_Remote(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Remote", UUIDataStore_Remote_Data),
	]


class  UUIDataStore_OnlineGameSearch_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("VfTable_IUIListElementCellProvider", FPointer),
		("SearchResultsName", FName),
		("OnlineSub", POINTER(UOnlineSubsystem)),
		("GameInterface", FScriptInterface),
		("GameSearchCfgList", TArray_FGameSearchCfg),
		("SelectedIndex", c_int),
		("ActiveSearchIndex", c_int),
	]

class  UUIDataStore_OnlineGameSearch(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Remote", UUIDataStore_Remote_Data),
		("UUIDataStore_OnlineGameSearch", UUIDataStore_OnlineGameSearch_Data),
	]


class  UUIDataStore_OnlinePlayerData_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("FriendsProvider", POINTER(UUIDataProvider_OnlineFriends)),
		("PlayerControllerId", c_int),
		("PlayerNick", FString),
		("ProfileSettingsClassName", FString),
		("ProfileSettingsClass", POINTER(UClass)),
		("ProfileProvider", POINTER(UUIDataProvider_OnlineProfileSettings)),
		("ProfileProviderClassName", FString),
		("ProfileProviderClass", POINTER(UClass)),
		("PlayerStorageClassName", FString),
		("PlayerStorageClass", POINTER(UClass)),
		("StorageProvider", POINTER(UUIDataProvider_OnlinePlayerStorage)),
		("StorageProviderClassName", FString),
		("StorageProviderClass", POINTER(UClass)),
		("FriendMessagesProvider", POINTER(UUIDataProvider_OnlineFriendMessages)),
		("AchievementsProvider", POINTER(UUIDataProvider_PlayerAchievements)),
		("FriendsProviderClassName", FString),
		("FriendsProviderClass", POINTER(UClass)),
		("FriendMessagesProviderClassName", FString),
		("FriendMessagesProviderClass", POINTER(UClass)),
		("AchievementsProviderClassName", FString),
		("AchievementsProviderClass", POINTER(UClass)),
		("PartyChatProviderClassName", FString),
		("PartyChatProviderClass", POINTER(UClass)),
		("PartyChatProvider", POINTER(UUIDataProvider_OnlinePartyChatList)),
	]

class  UUIDataStore_OnlinePlayerData(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Remote", UUIDataStore_Remote_Data),
		("UUIDataStore_OnlinePlayerData", UUIDataStore_OnlinePlayerData_Data),
	]


class  UUIDataStore_OnlineStats_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("VfTable_IUIListElementCellProvider", FPointer),
		("StatsReadClasses", TArray_UClassPtr),
		("StatsReadName", FName),
		("PlayerNickData", FPlayerNickMetaData),
		("RankNameMetaData", FRankMetaData),
		("TotalRowsName", FName),
		("StatsReadObjects", TArray_UOnlineStatsReadPtr),
		("StatsRead", POINTER(UOnlineStatsRead)),
		("CurrentReadType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("StatsInterface", FScriptInterface),
		("PlayerInterface", FScriptInterface),
	]

class  UUIDataStore_OnlineStats(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Remote", UUIDataStore_Remote_Data),
		("UUIDataStore_OnlineStats", UUIDataStore_OnlineStats_Data),
	]


class  UUIDataStore_Settings_Data(Structure):
	_fields_ = []

class  UUIDataStore_Settings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Settings", UUIDataStore_Settings_Data),
	]


class  UUIDataStore_OnlineGameSettings_Data(Structure):
	_fields_ = [
		("GameSettingsCfgList", TArray_FGameSettingsCfg),
		("SettingsProviderClass", POINTER(UClass)),
		("SelectedIndex", c_int),
	]

class  UUIDataStore_OnlineGameSettings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_Settings", UUIDataStore_Settings_Data),
		("UUIDataStore_OnlineGameSettings", UUIDataStore_OnlineGameSettings_Data),
	]


class  UUIDataStore_StringBase_Data(Structure):
	_fields_ = []

class  UUIDataStore_StringBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_StringBase", UUIDataStore_StringBase_Data),
	]


class  UUIDataStore_InputAlias_Data(Structure):
	_fields_ = [
		("InputAliases", TArray_FUIDataStoreInputAlias),
		("Unknown1", c_ubyte, 0x),
	]

class  UUIDataStore_InputAlias(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_StringBase", UUIDataStore_StringBase_Data),
		("UUIDataStore_InputAlias", UUIDataStore_InputAlias_Data),
	]


class  UUIDataStore_StringAliasMap_Data(Structure):
	_fields_ = [
		("MenuInputMapArray", TArray_FUIMenuInputMap),
		("MenuInputSets", FMap_Mirror),
		("PlayerIndex", c_int),
	]

class  UUIDataStore_StringAliasMap(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_StringBase", UUIDataStore_StringBase_Data),
		("UUIDataStore_StringAliasMap", UUIDataStore_StringAliasMap_Data),
	]


class  UUIDataStore_Strings_Data(Structure):
	_fields_ = [
		("LocFileProviders", TArray_UUIConfigFileProviderPtr),
	]

class  UUIDataStore_Strings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDataStore", UUIDataStore_Data),
		("UUIDataStore_StringBase", UUIDataStore_StringBase_Data),
		("UUIDataStore_Strings", UUIDataStore_Strings_Data),
	]


class  UUIDynamicFieldProvider_Data(Structure):
	_fields_ = [
		("PersistentDataFields", TArray_FUIProviderScriptFieldValue),
		("RuntimeDataFields", TArray_FUIProviderScriptFieldValue),
		("PersistentCollectionData", FMap_Mirror),
		("RuntimeCollectionData", FMap_Mirror),
	]

class  UUIDynamicFieldProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIDynamicFieldProvider", UUIDynamicFieldProvider_Data),
	]


class  UUIPropertyDataProvider_Data(Structure):
	_fields_ = [
		("ComplexPropertyTypes", TArray_UClassPtr),
		("__CanSupportComplexPropertyType__Delegate", FScriptDelegate),
	]

class  UUIPropertyDataProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
	]


class  UUIDynamicDataProvider_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementCellProvider", FPointer),
		("DataClass", POINTER(UClass)),
		("DataSource", POINTER(UObject)),
	]

class  UUIDynamicDataProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIDynamicDataProvider", UUIDynamicDataProvider_Data),
	]


class  UUIDataProvider_Settings_Data(Structure):
	_fields_ = [
		("Settings", POINTER(USettings)),
		("SettingsArrayProviders", TArray_FSettingsArrayProvider),
		("bIsAListRow", c_bool, 1),
		("", c_ulong, 0),
	]

class  UUIDataProvider_Settings(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIDynamicDataProvider", UUIDynamicDataProvider_Data),
		("UUIDataProvider_Settings", UUIDataProvider_Settings_Data),
	]


class  UUIResourceDataProvider_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("VfTable_IUIListElementCellProvider", FPointer),
		("bDataBindingPropertiesOnly", c_bool, 1),
		("bSkipDuringEnumeration", c_bool, 1),
		("", c_ulong, 0),
	]

class  UUIResourceDataProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
	]


class  UUIDataProvider_MenuItem_Data(Structure):
	_fields_ = [
		("OptionType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("OptionSet", TArray_FName),
		("DataStoreMarkup", FString),
		("DescriptionMarkup", FString),
		("RequiredGameMode", FName),
		("FriendlyName", FString),
		("CustomFriendlyName", FString),
		("Description", FString),
		("bEditableCombo", c_bool, 1),
		("bNumericCombo", c_bool, 1),
		("bKeyboardOrMouseOption", c_bool, 1),
		("bOnlineOnly", c_bool, 1),
		("bOfflineOnly", c_bool, 1),
		("bSearchAllInis", c_bool, 1),
		("bRemoveOn360", c_bool, 1),
		("bRemoveOnPC", c_bool, 1),
		("bRemoveOnPS3", c_bool, 1),
		("", c_ulong, 0),
		("EditBoxMaxLength", c_int),
		("RangeData", FUIRangeData),
		("SchemaCellFields", TArray_FName),
		("IniName", FString),
	]

class  UUIDataProvider_MenuItem(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
		("UUIDataProvider_MenuItem", UUIDataProvider_MenuItem_Data),
	]


class  UUIMapSummary_Data(Structure):
	_fields_ = [
		("MapName", FString),
		("ScreenshotPathName", FString),
		("DisplayName", FString),
		("Description", FString),
	]

class  UUIMapSummary(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
		("UUIMapSummary", UUIMapSummary_Data),
	]


class  UUIResourceCombinationProvider_Data(Structure):
	_fields_ = [
		("VfTable_IUIListElementProvider", FPointer),
		("VfTable_IUIListElementCellProvider", FPointer),
		("StaticDataProvider", POINTER(UUIResourceDataProvider)),
		("ProfileProvider", POINTER(UUIDataProvider_OnlineProfileSettings)),
	]

class  UUIResourceCombinationProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIResourceCombinationProvider", UUIResourceCombinationProvider_Data),
	]


class  UGameUISceneClient_Data(Structure):
	_fields_ = [
		("LatestDeltaTime", c_float),
		("DoubleClickStartTime", FDouble),
		("DoubleClickStartPosition", FIntPoint),
		("InitialPressedKeys", FMap_Mirror),
		("bUpdateInputProcessingStatus", c_bool, 1),
		("bUpdateSceneViewportSizes", c_bool, 1),
		("bEnableDebugInput", c_bool, 1),
		("bRenderDebugInfo", c_bool, 1),
		("bCaptureUnprocessedInput", c_bool, 1),
		("", c_ulong, 0),
		("NavAliases", TArray_FName),
		("AxisInputKeys", TArray_FName),
	]

class  UGameUISceneClient(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUISceneClient", UUISceneClient_Data),
		("UGameUISceneClient", UGameUISceneClient_Data),
	]


class  UScene_Data(Structure):
	_fields_ = []

class  UScene(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UScene", UScene_Data),
	]


class  AFoliageFactory_Data(Structure):
	_fields_ = [
		("Meshes", TArray_FFoliageMesh),
		("VolumeFalloffRadius", c_float),
		("VolumeFalloffExponent", c_float),
		("SurfaceDensityUpFacing", c_float),
		("SurfaceDensityDownFacing", c_float),
		("SurfaceDensitySideFacing", c_float),
		("FacingFalloffExponent", c_float),
		("MaxInstanceCount", c_int),
	]

class  AFoliageFactory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AFoliageFactory", AFoliageFactory_Data),
	]


class  AInstancedFoliageActor_Data(Structure):
	_fields_ = [
		("FoliageMeshes", FMap_Mirror),
	]

class  AInstancedFoliageActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInstancedFoliageActor", AInstancedFoliageActor_Data),
	]


class  AInteractiveFoliageActor_Data(Structure):
	_fields_ = [
		("CylinderComponent", POINTER(UCylinderComponent)),
		("TouchingActorEntryPosition", FVector),
		("FoliageVelocity", FVector),
		("FoliageForce", FVector),
		("FoliagePosition", FVector),
		("FoliageDamageImpulseScale", c_float),
		("FoliageTouchImpulseScale", c_float),
		("FoliageStiffness", c_float),
		("FoliageStiffnessQuadratic", c_float),
		("FoliageDamping", c_float),
		("MaxDamageImpulse", c_float),
		("MaxTouchImpulse", c_float),
		("MaxForce", c_float),
		("Mass", c_float),
	]

class  AInteractiveFoliageActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AStaticMeshActorBase", AStaticMeshActorBase_Data),
		("AStaticMeshActor", AStaticMeshActor_Data),
		("AInteractiveFoliageActor", AInteractiveFoliageActor_Data),
	]


class  UFoliageComponent_Data(Structure):
	_fields_ = [
		("LitInstances", TArray_FStoredFoliageInstance),
		("StaticallyRelevantLights", TArray_FGuid),
		("StaticallyIrrelevantLights", TArray_FGuid),
		("DirectionalStaticLightingScale", c_float * 3),
		("SimpleStaticLightingScale", c_float * 3),
		("InstanceStaticMesh", POINTER(UStaticMesh)),
		("Material", POINTER(UMaterialInterface)),
		("MaxDrawRadius", c_float),
		("MinTransitionRadius", c_float),
		("MinThinningRadius", c_float),
		("MinScale", FVector),
		("MaxScale", FVector),
		("SwayScale", c_float),
	]

class  UFoliageComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UFoliageComponent", UFoliageComponent_Data),
	]


class  UInteractiveFoliageComponent_Data(Structure):
	_fields_ = [
		("FoliageSceneProxy", FPointer),
	]

class  UInteractiveFoliageComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("UStaticMeshComponent", UStaticMeshComponent_Data),
		("UInteractiveFoliageComponent", UInteractiveFoliageComponent_Data),
	]


class  UActorFactoryInteractiveFoliage_Data(Structure):
	_fields_ = []

class  UActorFactoryInteractiveFoliage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactoryStaticMesh", UActorFactoryStaticMesh_Data),
		("UActorFactoryInteractiveFoliage", UActorFactoryInteractiveFoliage_Data),
	]


class  AFluidInfluenceActor_Data(Structure):
	_fields_ = [
		("FlowDirection", POINTER(UArrowComponent)),
		("Sprite", POINTER(USpriteComponent)),
		("InfluenceComponent", POINTER(UFluidInfluenceComponent)),
		("bActive", c_bool, 1),
		("bToggled", c_bool, 1),
		("", c_ulong, 0),
	]

class  AFluidInfluenceActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AFluidInfluenceActor", AFluidInfluenceActor_Data),
	]


class  AFluidSurfaceActor_Data(Structure):
	_fields_ = [
		("FluidComponent", POINTER(UFluidSurfaceComponent)),
		("ProjectileEntryEffect", POINTER(UParticleSystem)),
	]

class  AFluidSurfaceActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AFluidSurfaceActor", AFluidSurfaceActor_Data),
	]


class  AFluidSurfaceActorMovable_Data(Structure):
	_fields_ = []

class  AFluidSurfaceActorMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AFluidSurfaceActor", AFluidSurfaceActor_Data),
		("AFluidSurfaceActorMovable", AFluidSurfaceActorMovable_Data),
	]


class  UFluidInfluenceComponent_Data(Structure):
	_fields_ = [
		("bActive", c_bool, 1),
		("RaindropFillEntireFluid", c_bool, 1),
		("bIsToggleTriggered", c_bool, 1),
		("", c_ulong, 0),
		("FluidActor", POINTER(AFluidSurfaceActor)),
		("InfluenceType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MaxDistance", c_float),
		("WaveStrength", c_float),
		("WaveFrequency", c_float),
		("WavePhase", c_float),
		("WaveRadius", c_float),
		("RaindropAreaRadius", c_float),
		("RaindropRadius", c_float),
		("RaindropStrength", c_float),
		("RaindropRate", c_float),
		("FlowSpeed", c_float),
		("FlowNumRipples", c_int),
		("FlowSideMotionRadius", c_float),
		("FlowWaveRadius", c_float),
		("FlowStrength", c_float),
		("FlowFrequency", c_float),
		("SphereOuterRadius", c_float),
		("SphereInnerRadius", c_float),
		("SphereStrength", c_float),
		("CurrentAngle", c_float),
		("CurrentTimer", c_float),
		("CurrentFluidActor", POINTER(AFluidSurfaceActor)),
	]

class  UFluidInfluenceComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UFluidInfluenceComponent", UFluidInfluenceComponent_Data),
	]


class  UFluidSurfaceComponent_Data(Structure):
	_fields_ = [
		("FluidMaterial", POINTER(UMaterialInterface)),
		("LightMapResolution", c_int),
		("EnableSimulation", c_bool, 1),
		("EnableDetail", c_bool, 1),
		("bTiling", c_bool, 1),
		("bPause", c_bool, 1),
		("bShowSimulationNormals", c_bool, 1),
		("bShowSimulationPosition", c_bool, 1),
		("bShowDetailNormals", c_bool, 1),
		("bShowDetailPosition", c_bool, 1),
		("bShowFluidSimulation", c_bool, 1),
		("bShowFluidDetail", c_bool, 1),
		("bTestRipple", c_bool, 1),
		("bTestRippleCenterOnDetail", c_bool, 1),
		("", c_ulong, 0),
		("SimulationQuadsX", c_int),
		("SimulationQuadsY", c_int),
		("GridSpacing", c_float),
		("GridSpacingLowRes", c_float),
		("TargetSimulation", POINTER(AActor)),
		("GPUTessellationFactor", c_float),
		("FluidDamping", c_float),
		("FluidTravelSpeed", c_float),
		("FluidHeightScale", c_float),
		("FluidUpdateRate", c_float),
		("ForceImpact", c_float),
		("ForceContinuous", c_float),
		("LightingContrast", c_float),
		("TargetDetail", POINTER(AActor)),
		("DeactivationDistance", c_float),
		("DetailResolution", c_int),
		("DetailSize", c_float),
		("DetailDamping", c_float),
		("DetailTravelSpeed", c_float),
		("DetailTransfer", c_float),
		("DetailHeightScale", c_float),
		("DetailUpdateRate", c_float),
		("NormalLength", c_float),
		("TestRippleSpeed", c_float),
		("TestRippleFrequency", c_float),
		("TestRippleRadius", c_float),
		("FluidWidth", c_float),
		("FluidHeight", c_float),
		("TestRippleTime", c_float),
		("TestRippleAngle", c_float),
		("DeactivationTimer", c_float),
		("ViewDistance", c_float),
		("SimulationPosition", FVector),
		("DetailPosition", FVector),
		("ClampMap", TArray_unsigned_char),
		("ShadowMaps", TArray_UShadowMap2DPtr),
		("LightMap", FLightMapRef),
		("FluidSimulation", FPointer),
	]

class  UFluidSurfaceComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UFluidSurfaceComponent", UFluidSurfaceComponent_Data),
	]


class  ALensFlareSource_Data(Structure):
	_fields_ = [
		("LensFlareComp", POINTER(ULensFlareComponent)),
		("bCurrentlyActive", c_bool, 1),
		("", c_ulong, 0),
	]

class  ALensFlareSource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALensFlareSource", ALensFlareSource_Data),
	]


class  ULensFlareComponent_Data(Structure):
	_fields_ = [
		("Template", POINTER(ULensFlare)),
		("PreviewInnerCone", POINTER(UDrawLightConeComponent)),
		("PreviewOuterCone", POINTER(UDrawLightConeComponent)),
		("PreviewRadius", POINTER(UDrawLightRadiusComponent)),
		("bAutoActivate", c_bool, 1),
		("bIsActive", c_bool, 1),
		("bHasTranslucency", c_bool, 1),
		("bHasUnlitTranslucency", c_bool, 1),
		("bHasUnlitDistortion", c_bool, 1),
		("bUsesSceneColor", c_bool, 1),
		("bHasSeparateTranslucency", c_bool, 1),
		("bUseTrueConeCalculation", c_bool, 1),
		("bVisibleForMobile", c_bool, 1),
		("", c_ulong, 0),
		("OuterCone", c_float),
		("InnerCone", c_float),
		("ConeFudgeFactor", c_float),
		("Radius", c_float),
		("MinStrength", c_float),
		("SourceColor", FLinearColor),
		("Materials", TArray_FLensFlareElementMaterials),
		("ReleaseResourcesFence", FPointer),
		("NextTraceTime", c_float),
	]

class  ULensFlareComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("ULensFlareComponent", ULensFlareComponent_Data),
	]


class  ULensFlare_Data(Structure):
	_fields_ = [
		("SourceElement", FLensFlareElement),
		("SourceMesh", POINTER(UStaticMesh)),
		("SourceDPG", c_ubyte),
		("ReflectionsDPG", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Reflections", TArray_FLensFlareElement),
		("OuterCone", c_float),
		("InnerCone", c_float),
		("ConeFudgeFactor", c_float),
		("Radius", c_float),
		("bUseTrueConeCalculation", c_bool, 1),
		("bUseFixedRelativeBoundingBox", c_bool, 1),
		("bRenderDebugLines", c_bool, 1),
		("ThumbnailImageOutOfDate", c_bool, 1),
		("", c_ulong, 0),
		("MinStrength", c_float),
		("ScreenPercentageMap", FRawDistributionFloat),
		("FixedRelativeBoundingBox", FBox),
		("CurveEdSetup", POINTER(UInterpCurveEdSetup)),
		("ReflectionCount", c_int),
		("ThumbnailAngle", FRotator),
		("ThumbnailDistance", c_float),
		("ThumbnailImage", POINTER(UTexture2D)),
	]

class  ULensFlare(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULensFlare", ULensFlare_Data),
	]


class  UTextureFlipBook_Data(Structure):
	_fields_ = [
		("VfTable_FTickableObject", FPointer),
		("TimeIntoMovie", c_float),
		("TimeSinceLastFrame", c_float),
		("HorizontalScale", c_float),
		("VerticalScale", c_float),
		("bPaused", c_bool, 1),
		("bStopped", c_bool, 1),
		("bLooping", c_bool, 1),
		("bAutoPlay", c_bool, 1),
		("", c_ulong, 0),
		("HorizontalImages", c_int),
		("VerticalImages", c_int),
		("FBMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("FrameRate", c_float),
		("FrameTime", c_float),
		("CurrentRow", c_int),
		("CurrentColumn", c_int),
		("RenderOffsetU", c_float),
		("RenderOffsetV", c_float),
		("ReleaseResourcesFence", FPointer),
	]

class  UTextureFlipBook(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2D", UTexture2D_Data),
		("UTextureFlipBook", UTextureFlipBook_Data),
	]


class  UTexture2DComposite_Data(Structure):
	_fields_ = [
		("SourceRegions", TArray_FSourceTexture2DRegion),
		("MaxTextureSize", c_int),
	]

class  UTexture2DComposite(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2DComposite", UTexture2DComposite_Data),
	]


class  UTexture2DDynamic_Data(Structure):
	_fields_ = [
		("SizeX", c_int),
		("SizeY", c_int),
		("Format", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("NumMips", c_int),
		("bIsResolveTarget", c_bool, 1),
		("", c_ulong, 0),
	]

class  UTexture2DDynamic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTexture2DDynamic", UTexture2DDynamic_Data),
	]


class  UTextureCube_Data(Structure):
	_fields_ = [
		("SizeX", c_int),
		("SizeY", c_int),
		("Format", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("NumMips", c_int),
		("bIsCubemapValid", c_bool, 1),
		("", c_ulong, 0),
		("FacePosX", POINTER(UTexture2D)),
		("FaceNegX", POINTER(UTexture2D)),
		("FacePosY", POINTER(UTexture2D)),
		("FaceNegY", POINTER(UTexture2D)),
		("FacePosZ", POINTER(UTexture2D)),
		("FaceNegZ", POINTER(UTexture2D)),
	]

class  UTextureCube(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTextureCube", UTextureCube_Data),
	]


class  UTextureMovie_Data(Structure):
	_fields_ = [
		("SizeX", c_int),
		("SizeY", c_int),
		("Format", c_ubyte),
		("AddressX", c_ubyte),
		("AddressY", c_ubyte),
		("MovieStreamSource", c_ubyte),
		("DecoderClass", POINTER(UClass)),
		("Decoder", POINTER(UCodecMovie)),
		("Paused", c_bool, 1),
		("Stopped", c_bool, 1),
		("GamePaused", c_bool, 1),
		("Looping", c_bool, 1),
		("ResetOnLastFrame", c_bool, 1),
		("AutoPlay", c_bool, 1),
		("", c_ulong, 0),
		("MovieName", FString),
		("Data", FUntypedBulkData_Mirror),
		("ReleaseCodecFence", FPointer),
	]

class  UTextureMovie(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTextureMovie", UTextureMovie_Data),
	]


class  UTextureRenderTarget_Data(Structure):
	_fields_ = [
		("bUpdateImmediate", c_bool, 1),
		("bNeedsTwoCopies", c_bool, 1),
		("bRenderOnce", c_bool, 1),
		("", c_ulong, 0),
		("TargetGamma", c_float),
	]

class  UTextureRenderTarget(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTextureRenderTarget", UTextureRenderTarget_Data),
	]


class  UTextureRenderTarget2D_Data(Structure):
	_fields_ = [
		("SizeX", c_int),
		("SizeY", c_int),
		("Format", c_ubyte),
		("AddressX", c_ubyte),
		("AddressY", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ClearColor", FLinearColor),
		("bForceLinearGamma", c_bool, 1),
		("", c_ulong, 0),
	]

class  UTextureRenderTarget2D(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTextureRenderTarget", UTextureRenderTarget_Data),
		("UTextureRenderTarget2D", UTextureRenderTarget2D_Data),
	]


class  UScriptedTexture_Data(Structure):
	_fields_ = [
		("bNeedsUpdate", c_bool, 1),
		("bSkipNextClear", c_bool, 1),
		("", c_ulong, 0),
		("__Render__Delegate", FScriptDelegate),
	]

class  UScriptedTexture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTextureRenderTarget", UTextureRenderTarget_Data),
		("UTextureRenderTarget2D", UTextureRenderTarget2D_Data),
		("UScriptedTexture", UScriptedTexture_Data),
	]


class  UTextureRenderTargetCube_Data(Structure):
	_fields_ = [
		("SizeX", c_int),
		("Format", c_ubyte),
	]

class  UTextureRenderTargetCube(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USurface", USurface_Data),
		("UTexture", UTexture_Data),
		("UTextureRenderTarget", UTextureRenderTarget_Data),
		("UTextureRenderTargetCube", UTextureRenderTargetCube_Data),
	]


class  UAudioDevice_Data(Structure):
	_fields_ = [
		("MaxChannels", c_int),
		("CommonAudioPoolSize", c_int),
		("LowPassFilterResonance", c_float),
		("WorkAroundXDKRegression", c_bool, 1),
		("bUsesVirtualVoices", c_bool, 1),
		("bGameWasTicking", c_bool, 1),
		("", c_ulong, 0),
		("MinCompressedDurationEditor", c_float),
		("MinCompressedDurationGame", c_float),
		("ChirpInSoundNodeWaveName", FString),
		("ChirpInSoundNodeWave", POINTER(USoundNodeWave)),
		("ChirpOutSoundNodeWaveName", FString),
		("ChirpOutSoundNodeWave", POINTER(USoundNodeWave)),
		("CommonAudioPool", FPointer),
		("CommonAudioPoolFreeBytes", c_int),
		("AudioComponents", TArray_UAudioComponentPtr),
		("Sources", TArray_FPointer),
		("FreeSources", TArray_FPointer),
		("Unknown1", c_ubyte, 0x),
		("Listeners", TArray_FListener),
		("CurrentTick", FQWord),
		("Unknown2", c_ubyte, 0x),
		("Unknown3", c_ubyte, 0x),
		("Unknown4", c_ubyte, 0x),
		("Unknown5", c_ubyte, 0x),
		("Unknown6", c_ubyte, 0x),
		("Effects", FPointer),
		("BaseSoundModeName", FName),
		("CurrentMode", POINTER(USoundMode)),
		("SoundModeStartTime", FDouble),
		("SoundModeFadeInStartTime", FDouble),
		("SoundModeFadeInEndTime", FDouble),
		("SoundModeEndTime", FDouble),
		("ListenerVolumeIndex", c_int),
		("ListenerInteriorSettings", FInteriorSettings),
		("InteriorStartTime", FDouble),
		("InteriorEndTime", FDouble),
		("ExteriorEndTime", FDouble),
		("InteriorLPFEndTime", FDouble),
		("ExteriorLPFEndTime", FDouble),
		("InteriorVolumeInterp", c_float),
		("InteriorLPFInterp", c_float),
		("ExteriorVolumeInterp", c_float),
		("ExteriorLPFInterp", c_float),
		("TestAudioComponent", POINTER(UAudioComponent)),
		("TextToSpeech", FPointer),
		("DebugState", c_ubyte),
		("Unknown7", c_ubyte, 0x),
		("TransientMasterVolume", c_float),
		("LastUpdateTime", c_float),
	]

class  UAudioDevice(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USubsystem", USubsystem_Data),
		("UAudioDevice", UAudioDevice_Data),
	]


class  USoundClass_Data(Structure):
	_fields_ = [
		("Properties", FSoundClassProperties),
		("ChildClassNames", TArray_FName),
		("bIsChild", c_bool, 1),
		("Unknown1", c_ubyte, 0x),
		("", c_ulong, 0),
	]

class  USoundClass(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USoundClass", USoundClass_Data),
	]


class  USoundMode_Data(Structure):
	_fields_ = [
		("bApplyEQ", c_bool, 1),
		("", c_ulong, 0),
		("EQSettings", FAudioEQEffect),
		("SoundClassEffects", TArray_FSoundClassAdjuster),
		("InitialDelay", c_float),
		("FadeInTime", c_float),
		("Duration", c_float),
		("FadeOutTime", c_float),
	]

class  USoundMode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USoundMode", USoundMode_Data),
	]


class  ADebugCameraController_Data(Structure):
	_fields_ = [
		("PrimaryKey", FName),
		("SecondaryKey", FName),
		("UnselectKey", FName),
		("bShowSelectedInfo", c_bool, 1),
		("bIsFrozenRendering", c_bool, 1),
		("", c_ulong, 0),
		("OryginalControllerRef", POINTER(APlayerController)),
		("OryginalPlayer", POINTER(UPlayer)),
		("DrawFrustum", POINTER(UDrawFrustumComponent)),
		("SelectedActor", POINTER(AActor)),
		("SelectedComponent", POINTER(UPrimitiveComponent)),
	]

class  ADebugCameraController(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AController", AController_Data),
		("APlayerController", APlayerController_Data),
		("ADebugCameraController", ADebugCameraController_Data),
	]


class  AMatineePawn_Data(Structure):
	_fields_ = []

class  AMatineePawn(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APawn", APawn_Data),
		("AMatineePawn", AMatineePawn_Data),
	]


class  AScout_Data(Structure):
	_fields_ = [
		("PathSizes", TArray_FPathSizeInfo),
		("TestJumpZ", c_float),
		("TestGroundSpeed", c_float),
		("TestMaxFallSpeed", c_float),
		("TestFallSpeed", c_float),
		("MaxLandingVelocity", c_float),
		("MinNumPlayerStarts", c_int),
		("DefaultReachSpecClass", POINTER(UClass)),
		("EdgePathColors", TArray_FColor),
		("NavMeshGen_StepSize", c_float),
		("NavMeshGen_EntityHalfHeight", c_float),
		("NavMeshGen_StartingHeightOffset", c_float),
		("NavMeshGen_MaxDropHeight", c_float),
		("NavMeshGen_MaxStepHeight", c_float),
		("NavMeshGen_VertZDeltaSnapThresh", c_float),
		("NavMeshGen_MinPolyArea", c_float),
		("NavMeshGen_BorderBackfill_CheckDist", c_float),
		("NavMeshGen_MinMergeDotAreaThreshold", c_float),
		("NavMeshGen_MinMergeDotSmallArea", c_float),
		("NavMeshGen_MinMergeDotLargeArea", c_float),
		("NavMeshGen_MaxPolyHeight", c_float),
		("NavMeshGen_HeightMergeThreshold", c_float),
		("NavMeshGen_EdgeMaxDelta", c_float),
		("NavMeshGen_MaxGroundCheckSize", c_float),
		("NavMeshGen_MinEdgeLength", c_float),
		("NavMeshGen_MinConcaveMergeDot", c_float),
		("NavMeshGen_ExpansionDoObstacleMeshSimplification", c_bool, 1),
		("bHightlightOneWayReachSpecs", c_bool, 1),
		("", c_ulong, 0),
		("MinMantleFallDist", c_float),
		("MaxMantleFallDist", c_float),
		("MinMantleLateralDist", c_float),
		("MaxMantleLateralDist", c_float),
		("MaxMantleFallTime", c_float),
	]

class  AScout(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APawn", APawn_Data),
		("AScout", AScout_Data),
	]


class  ALight_Data(Structure):
	_fields_ = [
		("LightComponent", POINTER(ULightComponent)),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  ALight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
	]


class  ADirectionalLight_Data(Structure):
	_fields_ = []

class  ADirectionalLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ADirectionalLight", ADirectionalLight_Data),
	]


class  ADirectionalLightToggleable_Data(Structure):
	_fields_ = []

class  ADirectionalLightToggleable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ADirectionalLight", ADirectionalLight_Data),
		("ADirectionalLightToggleable", ADirectionalLightToggleable_Data),
	]


class  ADominantDirectionalLight_Data(Structure):
	_fields_ = []

class  ADominantDirectionalLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ADirectionalLight", ADirectionalLight_Data),
		("ADominantDirectionalLight", ADominantDirectionalLight_Data),
	]


class  ADominantDirectionalLightMovable_Data(Structure):
	_fields_ = []

class  ADominantDirectionalLightMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ADirectionalLight", ADirectionalLight_Data),
		("ADominantDirectionalLight", ADominantDirectionalLight_Data),
		("ADominantDirectionalLightMovable", ADominantDirectionalLightMovable_Data),
	]


class  ALightShafts_Data(Structure):
	_fields_ = []

class  ALightShafts(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ALightShafts", ALightShafts_Data),
	]


class  APointLight_Data(Structure):
	_fields_ = []

class  APointLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("APointLight", APointLight_Data),
	]


class  ADominantPointLight_Data(Structure):
	_fields_ = []

class  ADominantPointLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("APointLight", APointLight_Data),
		("ADominantPointLight", ADominantPointLight_Data),
	]


class  APointLightMovable_Data(Structure):
	_fields_ = []

class  APointLightMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("APointLight", APointLight_Data),
		("APointLightMovable", APointLightMovable_Data),
	]


class  APointLightToggleable_Data(Structure):
	_fields_ = []

class  APointLightToggleable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("APointLight", APointLight_Data),
		("APointLightToggleable", APointLightToggleable_Data),
	]


class  ASkyLight_Data(Structure):
	_fields_ = []

class  ASkyLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASkyLight", ASkyLight_Data),
	]


class  ASkyLightToggleable_Data(Structure):
	_fields_ = []

class  ASkyLightToggleable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASkyLight", ASkyLight_Data),
		("ASkyLightToggleable", ASkyLightToggleable_Data),
	]


class  ASpotLight_Data(Structure):
	_fields_ = []

class  ASpotLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASpotLight", ASpotLight_Data),
	]


class  ADominantSpotLight_Data(Structure):
	_fields_ = []

class  ADominantSpotLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASpotLight", ASpotLight_Data),
		("ADominantSpotLight", ADominantSpotLight_Data),
	]


class  AGeneratedMeshAreaLight_Data(Structure):
	_fields_ = []

class  AGeneratedMeshAreaLight(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASpotLight", ASpotLight_Data),
		("AGeneratedMeshAreaLight", AGeneratedMeshAreaLight_Data),
	]


class  ASpotLightMovable_Data(Structure):
	_fields_ = []

class  ASpotLightMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASpotLight", ASpotLight_Data),
		("ASpotLightMovable", ASpotLightMovable_Data),
	]


class  ASpotLightToggleable_Data(Structure):
	_fields_ = []

class  ASpotLightToggleable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("ASpotLight", ASpotLight_Data),
		("ASpotLightToggleable", ASpotLightToggleable_Data),
	]


class  AStaticLightCollectionActor_Data(Structure):
	_fields_ = [
		("LightComponents", TArray_ULightComponentPtr),
		("MaxLightComponents", c_int),
	]

class  AStaticLightCollectionActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ALight", ALight_Data),
		("AStaticLightCollectionActor", AStaticLightCollectionActor_Data),
	]


class  ULightComponent_Data(Structure):
	_fields_ = [
		("SceneInfo", FPointer),
		("WorldToLight", FMatrix),
		("LightToWorld", FMatrix),
		("LightGuid", FGuid),
		("LightmapGuid", FGuid),
		("Brightness", c_float),
		("LightColor", FColor),
		("Function", POINTER(ULightFunction)),
		("bEnabled", c_bool, 1),
		("CastShadows", c_bool, 1),
		("CastStaticShadows", c_bool, 1),
		("CastDynamicShadows", c_bool, 1),
		("bCastCompositeShadow", c_bool, 1),
		("bAffectCompositeShadowDirection", c_bool, 1),
		("bNonModulatedSelfShadowing", c_bool, 1),
		("bSelfShadowOnly", c_bool, 1),
		("bAllowPreShadow", c_bool, 1),
		("bForceDynamicLight", c_bool, 1),
		("UseDirectLightMap", c_bool, 1),
		("bHasLightEverBeenBuiltIntoLightMap", c_bool, 1),
		("bCanAffectDynamicPrimitivesOutsideDynamicChannel", c_bool, 1),
		("bAllowProjectedShadowing", c_bool, 1),
		("bRenderLightShafts", c_bool, 1),
		("bPrecomputedLightingIsValid", c_bool, 1),
		("bExplicitlyAssignedLight", c_bool, 1),
		("bAllowCompositingIntoDLE", c_bool, 1),
		("", c_ulong, 0),
		("LightEnvironment", POINTER(ULightEnvironmentComponent)),
		("LightingChannels", FLightingChannelContainer),
		("LightAffectsClassification", c_ubyte),
		("LightShadowMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ModShadowColor", FLinearColor),
		("ModShadowFadeoutTime", c_float),
		("ModShadowFadeoutExponent", c_float),
		("LightListIndex", c_int),
		("ShadowProjectionTechnique", c_ubyte),
		("ShadowFilterQuality", c_ubyte),
		("Unknown2", c_ubyte, 0x),
		("MinShadowResolution", c_int),
		("MaxShadowResolution", c_int),
		("ShadowFadeResolution", c_int),
		("OcclusionDepthRange", c_float),
		("BloomScale", c_float),
		("BloomThreshold", c_float),
		("BloomScreenBlendThreshold", c_float),
		("BloomTint", FColor),
		("RadialBlurPercent", c_float),
		("OcclusionMaskDarkness", c_float),
	]

class  ULightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
	]


class  UDirectionalLightComponent_Data(Structure):
	_fields_ = [
		("TraceDistance", c_float),
		("WholeSceneDynamicShadowRadius", c_float),
		("NumWholeSceneDynamicShadowCascades", c_int),
		("CascadeDistributionExponent", c_float),
		("LightmassSettings", FLightmassDirectionalLightSettings),
	]

class  UDirectionalLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("UDirectionalLightComponent", UDirectionalLightComponent_Data),
	]


class  UDominantDirectionalLightComponent_Data(Structure):
	_fields_ = [
		("DominantLightmassBrightness", c_float),
		("TimeOfDayDiffuseBrightness", c_float),
		("TimeOfDayDiffuseColor", FColor),
		("TimeOfDaySpecularBrightness", c_float),
		("TimeOfDaySpecularColor", FColor),
		("Unknown1", c_ubyte, 0x),
		("DominantLightShadowInfo", FDominantShadowInfo),
		("Unknown2", c_ubyte, 0x),
		("DominantLightShadowMap", FArray_Mirror),
	]

class  UDominantDirectionalLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("UDirectionalLightComponent", UDirectionalLightComponent_Data),
		("UDominantDirectionalLightComponent", UDominantDirectionalLightComponent_Data),
	]


class  ULightShaftComponent_Data(Structure):
	_fields_ = [
		("TraceDistance", c_float),
		("LightShaftType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("Radius", c_float),
	]

class  ULightShaftComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("ULightShaftComponent", ULightShaftComponent_Data),
	]


class  UPointLightComponent_Data(Structure):
	_fields_ = [
		("ShadowRadiusMultiplier", c_float),
		("Radius", c_float),
		("FalloffExponent", c_float),
		("ShadowFalloffExponent", c_float),
		("MinShadowFalloffRadius", c_float),
		("Unknown1", c_ubyte, 0x),
		("CachedParentToWorld", FMatrix),
		("Translation", FVector),
		("Unknown2", c_ubyte, 0x),
		("ShadowPlane", FPlane),
		("PreviewLightRadius", POINTER(UDrawLightRadiusComponent)),
		("LightmassSettings", FLightmassPointLightSettings),
		("PreviewLightSourceRadius", POINTER(UDrawLightRadiusComponent)),
	]

class  UPointLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("UPointLightComponent", UPointLightComponent_Data),
	]


class  UDominantPointLightComponent_Data(Structure):
	_fields_ = []

class  UDominantPointLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("UPointLightComponent", UPointLightComponent_Data),
		("UDominantPointLightComponent", UDominantPointLightComponent_Data),
	]


class  USpotLightComponent_Data(Structure):
	_fields_ = [
		("InnerConeAngle", c_float),
		("OuterConeAngle", c_float),
		("LightShaftConeAngle", c_float),
		("PreviewInnerCone", POINTER(UDrawLightConeComponent)),
		("PreviewOuterCone", POINTER(UDrawLightConeComponent)),
		("Rotation", FRotator),
	]

class  USpotLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("UPointLightComponent", UPointLightComponent_Data),
		("USpotLightComponent", USpotLightComponent_Data),
	]


class  UDominantSpotLightComponent_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("DominantLightShadowInfo", FDominantShadowInfo),
		("Unknown2", c_ubyte, 0x),
		("DominantLightShadowMap", FArray_Mirror),
	]

class  UDominantSpotLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("UPointLightComponent", UPointLightComponent_Data),
		("USpotLightComponent", USpotLightComponent_Data),
		("UDominantSpotLightComponent", UDominantSpotLightComponent_Data),
	]


class  USkyLightComponent_Data(Structure):
	_fields_ = [
		("LowerBrightness", c_float),
		("LowerColor", FColor),
	]

class  USkyLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("USkyLightComponent", USkyLightComponent_Data),
	]


class  USphericalHarmonicLightComponent_Data(Structure):
	_fields_ = [
	
		("Unknown1", c_ubyte, 0x),
		("WorldSpaceIncidentLighting", FSHVectorRGB),
		("IndirectColor", FLinearColor),
		("IndirectDirection", FVector),
		("bRenderBeforeModShadows", c_bool, 1),
		("", c_ulong, 0),
	]

class  USphericalHarmonicLightComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightComponent", ULightComponent_Data),
		("USphericalHarmonicLightComponent", USphericalHarmonicLightComponent_Data),
	]


class  ULightEnvironmentComponent_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("bForceNonCompositeDynamicLights", c_bool, 1),
		("bAllowDynamicShadowsOnTranslucency", c_bool, 1),
		("bAllowPreShadow", c_bool, 1),
		("bTranslucencyShadowed", c_bool, 1),
		("", c_ulong, 0),
		("DominantShadowFactor", c_float),
		("AffectingDominantLight", POINTER(ULightComponent)),
		("AffectedComponents", TArray_UPrimitiveComponentPtr),
	]

class  ULightEnvironmentComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightEnvironmentComponent", ULightEnvironmentComponent_Data),
	]


class  UDynamicLightEnvironmentComponent_Data(Structure):
	_fields_ = [
		("State", FPointer),
		("InvisibleUpdateTime", c_float),
		("MinTimeBetweenFullUpdates", c_float),
		("VelocityUpdateTimeScale", c_float),
		("ShadowInterpolationSpeed", c_float),
		("NumVolumeVisibilitySamples", c_int),
		("LightingBoundsScale", c_float),
		("AmbientShadowColor", FLinearColor),
		("AmbientShadowSourceDirection", FVector),
		("AmbientGlow", FLinearColor),
		("LightDistance", c_float),
		("ShadowDistance", c_float),
		("bCastShadows", c_bool, 1),
		("bCompositeShadowsFromDynamicLights", c_bool, 1),
		("bForceCompositeAllLights", c_bool, 1),
		("bAffectedBySmallDynamicLights", c_bool, 1),
		("bUseBooleanEnvironmentShadowing", c_bool, 1),
		("bShadowFromEnvironment", c_bool, 1),
		("bDynamic", c_bool, 1),
		("bSynthesizeDirectionalLight", c_bool, 1),
		("bSynthesizeSHLight", c_bool, 1),
		("bRequiresNonLatentUpdates", c_bool, 1),
		("bTraceFromClosestBoundsPoint", c_bool, 1),
		("bIsCharacterLightEnvironment", c_bool, 1),
		("bOverrideOwnerLightingChannels", c_bool, 1),
		("bAlwaysInfluencedByDominantDirectionalLight", c_bool, 1),
		("", c_ulong, 0),
		("ModShadowFadeoutTime", c_float),
		("ModShadowFadeoutExponent", c_float),
		("MaxModulatedShadowColor", FLinearColor),
		("DominantShadowTransitionStartDistance", c_float),
		("DominantShadowTransitionEndDistance", c_float),
		("MinShadowAngle", c_float),
		("BoundsMethod", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("OverriddenBounds", FBoxSphereBounds),
		("OverriddenLightingChannels", FLightingChannelContainer),
		("OverriddenLightComponents", TArray_ULightComponentPtr),
	]

class  UDynamicLightEnvironmentComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightEnvironmentComponent", ULightEnvironmentComponent_Data),
		("UDynamicLightEnvironmentComponent", UDynamicLightEnvironmentComponent_Data),
	]


class  UParticleLightEnvironmentComponent_Data(Structure):
	_fields_ = [
		("ReferenceCount", c_int),
		("NumPooledReuses", c_int),
		("SharedInstigator", POINTER(AActor)),
		("SharedParticleSystem", POINTER(UParticleSystem)),
		("bAllowDLESharing", c_bool, 1),
		("", c_ulong, 0),
	]

class  UParticleLightEnvironmentComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("ULightEnvironmentComponent", ULightEnvironmentComponent_Data),
		("UDynamicLightEnvironmentComponent", UDynamicLightEnvironmentComponent_Data),
		("UParticleLightEnvironmentComponent", UParticleLightEnvironmentComponent_Data),
	]


class  UDrawLightConeComponent_Data(Structure):
	_fields_ = []

class  UDrawLightConeComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawConeComponent", UDrawConeComponent_Data),
		("UDrawLightConeComponent", UDrawLightConeComponent_Data),
	]


class  UDrawLightRadiusComponent_Data(Structure):
	_fields_ = []

class  UDrawLightRadiusComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UDrawSphereComponent", UDrawSphereComponent_Data),
		("UDrawLightRadiusComponent", UDrawLightRadiusComponent_Data),
	]


class  ULightFunction_Data(Structure):
	_fields_ = [
		("SourceMaterial", POINTER(UMaterialInterface)),
		("Scale", FVector),
		("DisabledBrightness", c_float),
	]

class  ULightFunction(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULightFunction", ULightFunction_Data),
	]


class  USkeletalMeshComponent_Data(Structure):
	_fields_ = [
		("VfTable_IIAnimBehavior", FPointer),
		("SkeletalMesh", POINTER(USkeletalMesh)),
		("AttachedToSkelComponent", POINTER(USkeletalMeshComponent)),
		("GestaltData", FGestaltDataContainer),
		("AnimTreeTemplate", POINTER(UAnimTree)),
		("Animations", POINTER(UAnimNode)),
		("AnimTickArray", TArray_UAnimNodePtr),
		("AnimAlwaysTickArray", TArray_UAnimNodePtr),
		("AnimTickRelevancyArray", TArray_int),
		("AnimTickWeightsArray", TArray_float),
		("SkelControlTickArray", TArray_USkelControlBasePtr),
		("PhysicsAsset", POINTER(UPhysicsAsset)),
		("PhysicsAssetInstance", POINTER(UPhysicsAssetInstance)),
		("ApexClothing", FPointer),
		("PhysicsWeight", c_float),
		("GlobalAnimRateScale", c_float),
		("StreamingDistanceMultiplier", c_float),
		("MeshObject", FPointer),
		("SpaceBases", TArray_FBoneAtom),
		("LocalAtoms", TArray_FBoneAtom),
		("CachedLocalAtoms", TArray_FBoneAtom),
		("CachedSpaceBases", TArray_FBoneAtom),
		("LowUpdateFrameRate", c_int),
		("RequiredBones", TArray_unsigned_char),
		("ComposeOrderedRequiredBones", TArray_unsigned_char),
		("ParentAnimComponent", POINTER(USkeletalMeshComponent)),
		("ParentBoneMap", TArray_int),
		("AnimSets", TArray_UAnimSetPtr),
		("TemporarySavedAnimSets", TArray_UAnimSetPtr),
		("MorphSets", TArray_UMorphTargetSetPtr),
		("ActiveMorphs", TArray_FActiveMorph),
		("ActiveCurveMorphs", TArray_FActiveMorph),
		("Unknown1", c_ubyte, 0x),
		("Attachments", TArray_FAttachment),
		("SkelControlIndex", TArray_unsigned_char),
		("PostPhysSkelControlIndex", TArray_unsigned_char),
		("ForcedLodModel", c_int),
		("MinLodModel", c_int),
		("PredictedLODLevel", c_int),
		("OldPredictedLODLevel", c_int),
		("AnimationLODDistanceFactor", c_float),
		("AnimationLODFrameRate", c_int),
		("MaxDistanceFactor", c_float),
		("bForceWireframe", c_int),
		("bForceRefpose", c_int),
		("bOldForceRefPose", c_int),
		("bNoSkeletonUpdate", c_bool, 1),
		("", c_ulong, 0),
		("bDisplayBones", c_int),
		("bShowPrePhysBones", c_int),
		("bHideSkin", c_int),
		("bForceRawOffset", c_int),
		("bIgnoreControllers", c_int),
		("bTransformFromAnimParent", c_int),
		("TickTag", c_int),
		("InitTag", c_int),
		("CachedAtomsTag", c_int),
		("bUseSingleBodyPhysics", c_int),
		("bRequiredBonesUpToDate", c_int),
		("MinDistFactorForKinematicUpdate", c_float),
		("FramesPhysicsAsleep", c_int),
		("bHasValidBodies", c_bool, 1),
		("bSkipAllUpdateWhenPhysicsAsleep", c_bool, 1),
		("bComponentUseFixedSkelBounds", c_bool, 1),
		("bUseBoundsFromParentAnimComponent", c_bool, 1),
		("bDoKinematicUpdatePostFence", c_bool, 1),
		("bConsiderAllBodiesForBounds", c_bool, 1),
		("bUpdateSkelWhenNotRendered", c_bool, 1),
		("bIgnoreControllersWhenNotRendered", c_bool, 1),
		("bTickAnimNodesWhenNotRendered", c_bool, 1),
		("bNotUpdatingKinematicDueToDistance", c_bool, 1),
		("bForceDiscardRootMotion", c_bool, 1),
		("bNotifyRootMotionProcessed", c_bool, 1),
		("bRootMotionModeChangeNotify", c_bool, 1),
		("bRootMotionExtractedNotify", c_bool, 1),
		("bProcessingRootMotion", c_bool, 1),
		("bDisableFaceFXMaterialInstanceCreation", c_bool, 1),
		("bDisableFaceFX", c_bool, 1),
		("bAnimTreeInitialised", c_bool, 1),
		("bForceMeshObjectUpdate", c_bool, 1),
		("bHasPhysicsAssetInstance", c_bool, 1),
		("bUpdateKinematicBonesFromAnimation", c_bool, 1),
		("bUpdateJointsFromAnimation", c_bool, 1),
		("bSkelCompFixed", c_bool, 1),
		("bHasHadPhysicsBlendedIn", c_bool, 1),
		("bForceUpdateAttachmentsInTick", c_bool, 1),
		("bEnableFullAnimWeightBodies", c_bool, 1),
		("bPerBoneVolumeEffects", c_bool, 1),
		("bPerBoneMotionBlur", c_bool, 1),
		("bSyncActorLocationToRootRigidBody", c_bool, 1),
		("bUseRawData", c_bool, 1),
		("bDisableWarningWhenAnimNotFound", c_bool, 1),
		("bOverrideAttachmentOwnerVisibility", c_bool, 1),
		("bNeedsToDeleteHitMask", c_bool, 1),
		("bPauseAnims", c_bool, 1),
		("bChartDistanceFactor", c_bool, 1),
		("bEnableLineCheckWithBounds", c_bool, 1),
		("bCanHighlightSelectedSections", c_bool, 1),
		("bIgnorePitchRollForRootRotation", c_bool, 1),
		("bIgnoredByFXCoordinator", c_bool, 1),
		("bSkipUpdateSkelPose", c_bool, 1),
		("bForceNonThreadedSkelUpdate", c_bool, 1),
		("bWaitingForThreadedAnimResults", c_bool, 1),
		("", c_ulong, 0),
		("LineCheckBoundsScale", FVector),
		("bEnableClothSimulation", c_bool, 1),
		("bDisableClothCollision", c_bool, 1),
		("bClothFrozen", c_bool, 1),
		("bAutoFreezeClothWhenNotRendered", c_bool, 1),
		("bResetWhenInactive", c_bool, 1),
		("bClothAwakeOnStartup", c_bool, 1),
		("bClothBaseVelClamp", c_bool, 1),
		("bClothBaseVelInterp", c_bool, 1),
		("bAttachClothVertsToBaseBody", c_bool, 1),
		("bIsClothOnStaticObject", c_bool, 1),
		("bUpdatedFixedClothVerts", c_bool, 1),
		("bClothPositionalDampening", c_bool, 1),
		("bClothWindRelativeToOwner", c_bool, 1),
		("bRecentlyRendered", c_bool, 1),
		("bCacheAnimSequenceNodes", c_bool, 1),
		("bIsGestaltAccessoryMesh", c_bool, 1),
		("bNeedsInstanceWeightUpdate", c_bool, 1),
		("bAlwaysUseInstanceWeights", c_bool, 1),
		("bUpdateComposeSkeletonPasses", c_bool, 1),
		("bValidTemporarySavedAnimSets", c_bool, 1),
		("", c_ulong, 0),
		("InstanceVertexWeightBones", TArray_FBonePair),
		("LODInfo", TArray_FSkelMeshComponentLODInfo),
		("FrozenLocalToWorldPos", FVector),
		("FrozenLocalToWorldRot", FRotator),
		("ClothExternalForce", FVector),
		("ClothWind", FVector),
		("ClothBaseVelClampRange", FVector),
		("ClothBlendWeight", c_float),
		("ClothDynamicBlendWeight", c_float),
		("ClothBlendMinDistanceFactor", c_float),
		("ClothBlendMaxDistanceFactor", c_float),
		("MinPosDampRange", FVector),
		("MaxPosDampRange", FVector),
		("MinPosDampScale", FVector),
		("MaxPosDampScale", FVector),
		("ClothSim", FPointer),
		("SceneIndex", c_int),
		("ClothMeshPosData", TArray_FVector),
		("ClothMeshNormalData", TArray_FVector),
		("ClothMeshIndexData", TArray_int),
		("NumClothMeshVerts", c_int),
		("NumClothMeshIndices", c_int),
		("ClothMeshParentData", TArray_int),
		("NumClothMeshParentIndices", c_int),
		("LastClothHitVertexId", c_int),
		("ClothMeshWeldedPosData", TArray_FVector),
		("ClothMeshWeldedNormalData", TArray_FVector),
		("ClothMeshWeldedIndexData", TArray_int),
		("ClothDirtyBufferFlag", c_int),
		("ClothRBChannel", c_ubyte),
		("Unknown2", c_ubyte, 0x),
		("ClothRBCollideWithChannels", FRBCollisionChannelContainer),
		("ClothForceScale", c_float),
		("ClothImpulseScale", c_float),
		("ClothAttachmentTearFactor", c_float),
		("bClothUseCompartment", c_bool, 1),
		("", c_ulong, 0),
		("MinDistanceForClothReset", c_float),
		("LastClothLocation", FVector),
		("ApexClothingRBChannel", c_ubyte),
		("Unknown3", c_ubyte, 0x),
		("ApexClothingRBCollideWithChannels", FRBCollisionChannelContainer),
		("ApexClothingCollisionRBChannel", c_ubyte),
		("Unknown4", c_ubyte, 0x),
		("bAutoFreezeApexClothingWhenNotRendered", c_bool, 1),
		("bLocalSpaceWind", c_bool, 1),
		("", c_ulong, 0),
		("WindVelocity", FVector),
		("WindVelocityBlendTime", c_float),
		("bSkipInitClothing", c_bool, 1),
		("", c_ulong, 0),
		("SoftBodySim", FPointer),
		("SoftBodySceneIndex", c_int),
		("bEnableSoftBodySimulation", c_bool, 1),
		("", c_ulong, 0),
		("SoftBodyTetraPosData", TArray_FVector),
		("SoftBodyTetraIndexData", TArray_int),
		("NumSoftBodyTetraVerts", c_int),
		("NumSoftBodyTetraIndices", c_int),
		("SoftBodyImpulseScale", c_float),
		("bSoftBodyFrozen", c_bool, 1),
		("bAutoFreezeSoftBodyWhenNotRendered", c_bool, 1),
		("bSoftBodyAwakeOnStartup", c_bool, 1),
		("bSoftBodyUseCompartment", c_bool, 1),
		("", c_ulong, 0),
		("SoftBodyRBChannel", c_ubyte),
		("Unknown5", c_ubyte, 0x),
		("SoftBodyRBCollideWithChannels", FRBCollisionChannelContainer),
		("SoftBodyASVPlane", FPointer),
		("LimitMaterial", POINTER(UMaterial)),
		("Unknown6", c_ubyte, 0x),
		("RootMotionDelta", FBoneAtom),
		("RootMotionVelocity", FVector),
		("RootBoneTranslation", FVector),
		("RootMotionAccelScale", FVector),
		("RootMotionMode", c_ubyte),
		("PreviousRMM", c_ubyte),
		("PendingRMM", c_ubyte),
		("OldPendingRMM", c_ubyte),
		("bRMMOneFrameDelay", c_int),
		("RootMotionRotationMode", c_ubyte),
		("AnimRotationOnly", c_ubyte),
		("Unknown7", c_ubyte, 0x),
		("bRemoveRootBoneScale", c_int),
		("bOverrideRootMotionSpace", c_bool, 1),
		("", c_ulong, 0),
		("RootMotionSpace", FRotator),
		("FaceFXBlendMode", c_ubyte),
		("Unknown8", c_ubyte, 0x),
		("FaceFXActorInstance", FPointer),
		("CachedFaceFXAudioComp", POINTER(UAudioComponent)),
		("BoneVisibilityStates", TArray_unsigned_char),
		("CachedFaceFxAkEvent", POINTER(UAkEvent)),
		("FaceFXPlayTime", c_float),
		("CachedPlayingInfo", FAkPlayingInfo),
		("PlayingFXAnimSet", POINTER(UFaceFXAnimSet)),
		("LocalToWorldBoneAtom", FBoneAtom),
		("ProgressiveDrawingFraction", c_float),
		("CustomSortAlternateIndexMode", c_ubyte),
		("ViewZeroOffset", c_ubyte),
		("ViewOneOffset", c_ubyte),
		("Unknown9", c_ubyte, 0x),
		("BlendMorphNode", POINTER(UMorphNodeWeight)),
		("MorphWeightTarget", c_float),
		("MorphWeightStart", c_float),
		("MorphBlendTime", c_float),
		("MorphBlendCurr", c_float),
	]

class  USkeletalMeshComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UMeshComponent", UMeshComponent_Data),
		("USkeletalMeshComponent", USkeletalMeshComponent_Data),
	]


class  USkeletalMesh_Data(Structure):
	_fields_ = [
		("Bounds", FBoxSphereBounds),
		("Materials", TArray_UMaterialInterfacePtr),
		("ClothingAssets", TArray_UApexClothingAssetPtr),
		("Origin", FVector),
		("RotOrigin", FRotator),
		("RefSkeleton", TArray_int),
		("SkeletalDepth", c_int),
		("Unknown1", c_ubyte, 0x),
		("LODModels", FIndirectArray_Mirror),
		("RefBasesInvMatrix", TArray_FBoneAtom),
		("ReferencePoseBounds", FBoxSphereBounds),
		("SkelMirrorTable", TArray_FBoneMirrorInfo),
		("SkelMirrorAxis", c_ubyte),
		("SkelMirrorFlipAxis", c_ubyte),
		("Unknown2", c_ubyte, 0x),
		("Sockets", TArray_USkeletalMeshSocketPtr),
		("BoneBreakNames", TArray_FString),
		("BoneBreakOptions", TArray_unsigned_char),
		("LODInfo", TArray_FSkeletalMeshLODInfo),
		("PerPolyCollisionBones", TArray_FName),
		("AddToParentPerPolyCollisionBone", TArray_FName),
		("PerPolyBoneKDOPs", TArray_int),
		("bPerPolyUseSoftWeighting", c_bool, 1),
		("bUseSimpleLineCollision", c_bool, 1),
		("bUseSimpleBoxCollision", c_bool, 1),
		("bForceCPUSkinning", c_bool, 1),
		("bUseFullPrecisionUVs", c_bool, 1),
		("", c_ulong, 0),
		("FaceFXAsset", POINTER(UFaceFXAsset)),
		("LODBiasPC", c_int),
		("LODBiasPS3", c_int),
		("LODBiasXbox360", c_int),
		("ClothMesh", TArray_FPointer),
		("ClothMeshScale", TArray_float),
		("ClothToGraphicsVertMap", TArray_int),
		("ClothMovementScale", TArray_float),
		("ClothMovementScaleGenMode", c_ubyte),
		("Unknown3", c_ubyte, 0x),
		("ClothToAnimMeshMaxDist", c_float),
		("bLimitClothToAnimMesh", c_bool, 1),
		("", c_ulong, 0),
		("ClothWeldingMap", TArray_int),
		("ClothWeldingDomain", c_int),
		("ClothWeldedIndices", TArray_int),
		("bForceNoWelding", c_bool, 1),
		("", c_ulong, 0),
		("NumFreeClothVerts", c_int),
		("ClothIndexBuffer", TArray_int),
		("ClothBones", TArray_FName),
		("ClothHierarchyLevels", c_int),
		("bEnableClothBendConstraints", c_bool, 1),
		("bEnableClothDamping", c_bool, 1),
		("bUseClothCOMDamping", c_bool, 1),
		("", c_ulong, 0),
		("ClothStretchStiffness", c_float),
		("ClothBendStiffness", c_float),
		("ClothDensity", c_float),
		("ClothThickness", c_float),
		("ClothDamping", c_float),
		("ClothIterations", c_int),
		("ClothHierarchicalIterations", c_int),
		("ClothFriction", c_float),
		("ClothRelativeGridSpacing", c_float),
		("ClothPressure", c_float),
		("ClothCollisionResponseCoefficient", c_float),
		("ClothAttachmentResponseCoefficient", c_float),
		("ClothAttachmentTearFactor", c_float),
		("ClothSleepLinearVelocity", c_float),
		("HardStretchLimitFactor", c_float),
		("bHardStretchLimit", c_bool, 1),
		("bEnableClothOrthoBendConstraints", c_bool, 1),
		("bEnableClothSelfCollision", c_bool, 1),
		("bEnableClothPressure", c_bool, 1),
		("bEnableClothTwoWayCollision", c_bool, 1),
		("", c_ulong, 0),
		("ClothSpecialBones", TArray_FClothSpecialBoneInfo),
		("bEnableClothLineChecks", c_bool, 1),
		("bClothMetal", c_bool, 1),
		("", c_ulong, 0),
		("ClothMetalImpulseThreshold", c_float),
		("ClothMetalPenetrationDepth", c_float),
		("ClothMetalMaxDeformationDistance", c_float),
		("bEnableClothTearing", c_bool, 1),
		("", c_ulong, 0),
		("ClothTearFactor", c_float),
		("ClothTearReserve", c_int),
		("bEnableValidBounds", c_bool, 1),
		("", c_ulong, 0),
		("ValidBoundsMin", FVector),
		("ValidBoundsMax", FVector),
		("ClothTornTriMap", FMap_Mirror),
		("SoftBodySurfaceToGraphicsVertMap", TArray_int),
		("SoftBodySurfaceIndices", TArray_int),
		("SoftBodyTetraVertsUnscaled", TArray_FVector),
		("SoftBodyTetraIndices", TArray_int),
		("SoftBodyTetraLinks", TArray_FSoftBodyTetraLink),
		("CachedSoftBodyMeshes", TArray_FPointer),
		("CachedSoftBodyMeshScales", TArray_float),
		("SoftBodyBones", TArray_FName),
		("SoftBodySpecialBones", TArray_FSoftBodySpecialBoneInfo),
		("SoftBodyVolumeStiffness", c_float),
		("SoftBodyStretchingStiffness", c_float),
		("SoftBodyDensity", c_float),
		("SoftBodyParticleRadius", c_float),
		("SoftBodyDamping", c_float),
		("SoftBodySolverIterations", c_int),
		("SoftBodyFriction", c_float),
		("SoftBodyRelativeGridSpacing", c_float),
		("SoftBodySleepLinearVelocity", c_float),
		("bEnableSoftBodySelfCollision", c_bool, 1),
		("", c_ulong, 0),
		("SoftBodyAttachmentResponse", c_float),
		("SoftBodyCollisionResponse", c_float),
		("SoftBodyDetailLevel", c_float),
		("SoftBodySubdivisionLevel", c_int),
		("bSoftBodyIsoSurface", c_bool, 1),
		("bEnableSoftBodyDamping", c_bool, 1),
		("bUseSoftBodyCOMDamping", c_bool, 1),
		("", c_ulong, 0),
		("SoftBodyAttachmentThreshold", c_float),
		("bEnableSoftBodyTwoWayCollision", c_bool, 1),
		("", c_ulong, 0),
		("SoftBodyAttachmentTearFactor", c_float),
		("bEnableSoftBodyLineChecks", c_bool, 1),
		("bHasVertexColors", c_bool, 1),
		("", c_ulong, 0),
		("GraphicsIndexIsCloth", TArray_BOOL),
		("CachedStreamingTextureFactors", TArray_float),
		("StreamingDistanceMultiplier", c_float),
		("ReleaseResourcesFence", c_int),
		("SkelMeshRUID", FQWord),
		("CachedRefBoneAtoms", TArray_FBoneAtom),
		("CachedAnimSetLinkupName", FName),
	]

class  USkeletalMesh(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USkeletalMesh", USkeletalMesh_Data),
	]


class  USkeletalMeshSocket_Data(Structure):
	_fields_ = [
		("SocketName", FName),
		("BoneName", FName),
		("RelativeLocation", FVector),
		("RelativeRotation", FRotator),
		("RelativeScale", FVector),
	]

class  USkeletalMeshSocket(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USkeletalMeshSocket", USkeletalMeshSocket_Data),
	]


class  ASplineActor_Data(Structure):
	_fields_ = [
		("Connections", TArray_FSplineConnection),
		("SplineActorTangent", FVector),
		("SplineColor", FColor),
		("bDisableDestination", c_bool, 1),
		("bAlreadyVisited", c_bool, 1),
		("", c_ulong, 0),
		("LinksFrom", TArray_ASplineActorPtr),
		("nextOrdered", POINTER(ASplineActor)),
		("prevOrdered", POINTER(ASplineActor)),
		("previousPath", POINTER(ASplineActor)),
		("bestPathWeight", c_int),
		("visitedWeight", c_int),
		("SplineVelocityOverTime", FInterpCurveFloat),
	]

class  ASplineActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASplineActor", ASplineActor_Data),
	]


class  ASplineLoftActor_Data(Structure):
	_fields_ = [
		("ScaleX", c_float),
		("ScaleY", c_float),
		("SplineMeshComps", TArray_USplineMeshComponentPtr),
		("DeformMesh", POINTER(UStaticMesh)),
		("DeformMeshMaterials", TArray_UMaterialInterfacePtr),
		("Roll", c_float),
		("WorldXDir", FVector),
		("Offset", FVector2D),
		("bSmoothInterpRollAndScale", c_bool, 1),
		("bAcceptsLights", c_bool, 1),
		("", c_ulong, 0),
		("MeshLightEnvironment", POINTER(UDynamicLightEnvironmentComponent)),
		("MeshMaxDrawDistance", c_float),
	]

class  ASplineLoftActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASplineActor", ASplineActor_Data),
		("ASplineLoftActor", ASplineLoftActor_Data),
	]


class  ASplineLoftActorMovable_Data(Structure):
	_fields_ = []

class  ASplineLoftActorMovable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASplineActor", ASplineActor_Data),
		("ASplineLoftActor", ASplineLoftActor_Data),
		("ASplineLoftActorMovable", ASplineLoftActorMovable_Data),
	]


class  USplineComponent_Data(Structure):
	_fields_ = [
		("SplineInfo", FInterpCurveVector),
		("SplineCurviness", c_float),
		("SplineColor", FColor),
		("SplineDrawRes", c_float),
		("SplineArrowSize", c_float),
		("bSplineDisabled", c_bool, 1),
		("", c_ulong, 0),
		("SplineReparamTable", FInterpCurveFloat),
	]

class  USplineComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("USplineComponent", USplineComponent_Data),
	]


class  AReplicationInfo_Data(Structure):
	_fields_ = []

class  AReplicationInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AReplicationInfo", AReplicationInfo_Data),
	]


class  AGameReplicationInfo_Data(Structure):
	_fields_ = [
		("VfTable_IIResourcePoolProvider", FPointer),
		("GameClass", POINTER(UClass)),
		("bStopCountDown", c_bool, 1),
		("bMatchHasBegun", c_bool, 1),
		("bMatchIsOver", c_bool, 1),
		("bAllInCinematicMode", c_bool, 1),
		("bIgnoreMoveInput", c_bool, 1),
		("bIgnoreLookInput", c_bool, 1),
		("bIgnoreButtonInput", c_bool, 1),
		("", c_ulong, 0),
		("RemainingTime", c_int),
		("ElapsedTime", c_int),
		("RemainingMinute", c_int),
		("GoalScore", c_int),
		("TimeLimit", c_int),
		("Teams", TArray_ATeamInfoPtr),
		("ServerName", FString),
		("Winner", POINTER(AActor)),
		("PRIArray", TArray_APlayerReplicationInfoPtr),
		("InactivePRIArray", TArray_APlayerReplicationInfoPtr),
		("ResourcePoolManager", POINTER(AResourcePoolManager)),
		("MusicInfo", FMusicStateInfo),
	]

class  AGameReplicationInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AReplicationInfo", AReplicationInfo_Data),
		("AGameReplicationInfo", AGameReplicationInfo_Data),
	]


class  APlayerReplicationInfo_Data(Structure):
	_fields_ = [
		("Score", c_float),
		("Deaths", c_int),
		("Ping", c_ubyte),
		("TTSSpeaker", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("NumLives", c_int),
		("PlayerName", FString),
		("PlayerNameHTML", FString),
		("OldName", FString),
		("PlayerID", c_int),
		("Team", POINTER(ATeamInfo)),
		("bAdmin", c_bool, 1),
		("bIsSpectator", c_bool, 1),
		("bOnlySpectator", c_bool, 1),
		("bWaitingPlayer", c_bool, 1),
		("bReadyToPlay", c_bool, 1),
		("bOutOfLives", c_bool, 1),
		("bBot", c_bool, 1),
		("bHasBeenWelcomed", c_bool, 1),
		("bIsInactive", c_bool, 1),
		("bFromPreviousLevel", c_bool, 1),
		("", c_ulong, 0),
		("StartTime", c_int),
		("StringSpectating", FString),
		("StringUnknown", FString),
		("Kills", c_int),
		("GameMessageClass", POINTER(UClass)),
		("ExactPing", c_float),
		("SavedNetworkAddress", FString),
		("UniqueId", FUniqueNetId),
		("SessionName", FName),
		("AutomatedTestingData", FAutomatedTestingDatum),
		("StatConnectionCounts", c_int),
		("StatPingTotals", c_int),
		("StatPingMin", c_int),
		("StatPingMax", c_int),
		("StatPKLTotal", c_int),
		("StatPKLMin", c_int),
		("StatPKLMax", c_int),
		("StatMaxInBPS", c_int),
		("StatAvgInBPS", c_int),
		("StatMaxOutBPS", c_int),
		("StatAvgOutBPS", c_int),
		("Avatar", POINTER(UTexture2D)),
	]

class  APlayerReplicationInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AReplicationInfo", AReplicationInfo_Data),
		("APlayerReplicationInfo", APlayerReplicationInfo_Data),
	]


class  ATeamInfo_Data(Structure):
	_fields_ = [
		("TeamName", FString),
		("Size", c_int),
		("Score", c_float),
		("TeamIndex", c_int),
		("TeamColor", FColor),
	]

class  ATeamInfo(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AReplicationInfo", AReplicationInfo_Data),
		("ATeamInfo", ATeamInfo_Data),
	]


class  ACamera_Data(Structure):
	_fields_ = [
		("PCOwner", POINTER(APlayerController)),
		("CameraStyle", FName),
		("DefaultFOV", c_float),
		("bLockedFOV", c_bool, 1),
		("bConstrainAspectRatio", c_bool, 1),
		("bEnableFading", c_bool, 1),
		("bForceDisableTemporalAA", c_bool, 1),
		("bEnableColorScaling", c_bool, 1),
		("bEnableColorScaleInterp", c_bool, 1),
		("bUseClientSideCameraUpdates", c_bool, 1),
		("bDebugClientSideCamera", c_bool, 1),
		("bShouldSendClientSideCameraUpdate", c_bool, 1),
		("", c_ulong, 0),
		("LockedFOV", c_float),
		("ConstrainedAspectRatio", c_float),
		("DefaultAspectRatio", c_float),
		("OffAxisYawAngle", c_float),
		("OffAxisPitchAngle", c_float),
		("FadeColor", FColor),
		("FadeAmount", c_float),
		("CamOverridePostProcessAlpha", c_float),
		("CamPostProcessSettings", FPostProcessSettings),
		("RenderingOverrides", FRenderingPerformanceOverrides),
		("ColorScale", FVector),
		("DesiredColorScale", FVector),
		("OriginalColorScale", FVector),
		("ColorScaleInterpDuration", c_float),
		("ColorScaleInterpStartTime", c_float),
		("CameraCache", FTCameraCache),
		("LastFrameCameraCache", FTCameraCache),
		("ViewTarget", FTViewTarget),
		("PendingViewTarget", FTViewTarget),
		("BlendTimeToGo", c_float),
		("BlendParams", FViewTargetTransitionParams),
		("ModifierList", TArray_UCameraModifierPtr),
		("FreeCamDistance", c_float),
		("FreeCamOffset", FVector),
		("FadeAlpha", FVector2D),
		("FadeTime", c_float),
		("FadeTimeRemaining", c_float),
		("CameraLensEffects", TArray_AEmitterCameraLensEffectBasePtr),
		("CameraShakeCamMod", POINTER(UCameraModifier_CameraShake)),
		("CameraShakeCamModClass", POINTER(UClass)),
		("AnimInstPool", POINTER(UCameraAnimInst) * 8),
		("ActiveAnims", TArray_UCameraAnimInstPtr),
		("FreeAnims", TArray_UCameraAnimInstPtr),
		("AnimCameraActor", POINTER(ADynamicCameraActor)),
	]

class  ACamera(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ACamera", ACamera_Data),
	]


class  ACameraActor_Data(Structure):
	_fields_ = [
		("bConstrainAspectRatio", c_bool, 1),
		("bCamOverridePostProcess", c_bool, 1),
		("", c_ulong, 0),
		("AspectRatio", c_float),
		("FOVAngle", c_float),
		("CamOverridePostProcessAlpha", c_float),
		("CamOverridePostProcess", FPostProcessSettings),
		("DrawFrustum", POINTER(UDrawFrustumComponent)),
		("MeshComp", POINTER(UStaticMeshComponent)),
	]

class  ACameraActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ACameraActor", ACameraActor_Data),
	]


class  ADynamicCameraActor_Data(Structure):
	_fields_ = []

class  ADynamicCameraActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ACameraActor", ACameraActor_Data),
		("ADynamicCameraActor", ADynamicCameraActor_Data),
	]


class  UCameraAnim_Data(Structure):
	_fields_ = [
		("CameraInterpGroup", POINTER(UInterpGroup)),
		("AnimLength", c_float),
		("BoundingBox", FBox),
		("BasePPSettings", FPostProcessSettings),
		("BasePPSettingsAlpha", c_float),
		("BaseFOV", c_float),
	]

class  UCameraAnim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCameraAnim", UCameraAnim_Data),
	]


class  UCameraAnimInst_Data(Structure):
	_fields_ = [
		("CamAnim", POINTER(UCameraAnim)),
		("InterpGroupInst", POINTER(UInterpGroupInst)),
		("CurTime", c_float),
		("bLooping", c_bool, 1),
		("bFinished", c_bool, 1),
		("bAutoReleaseWhenFinished", c_bool, 1),
		("bBlendingIn", c_bool, 1),
		("bBlendingOut", c_bool, 1),
		("", c_ulong, 0),
		("BlendInTime", c_float),
		("BlendOutTime", c_float),
		("CurBlendInTime", c_float),
		("CurBlendOutTime", c_float),
		("PlayRate", c_float),
		("BasePlayScale", c_float),
		("TransientScaleModifier", c_float),
		("CurrentBlendWeight", c_float),
		("RemainingTime", c_float),
		("MoveTrack", POINTER(UInterpTrackMove)),
		("MoveInst", POINTER(UInterpTrackInstMove)),
		("SourceAnimNode", POINTER(UAnimNodeSequence)),
		("PlaySpace", c_ubyte),
		("MirrorAxes", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("UserPlaySpaceMatrix", FMatrix),
		("LastPPSettings", FPostProcessSettings),
		("LastPPSettingsAlpha", c_float),
		("LastCameraLoc", FVector),
	]

class  UCameraAnimInst(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCameraAnimInst", UCameraAnimInst_Data),
	]


class  UCameraModifier_Data(Structure):
	_fields_ = [
		("bDisabled", c_bool, 1),
		("bPendingDisable", c_bool, 1),
		("bExclusive", c_bool, 1),
		("bDebug", c_bool, 1),
		("", c_ulong, 0),
		("CameraOwner", POINTER(ACamera)),
		("Priority", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("AlphaInTime", c_float),
		("AlphaOutTime", c_float),
		("Alpha", c_float),
		("TargetAlpha", c_float),
	]

class  UCameraModifier(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCameraModifier", UCameraModifier_Data),
	]


class  UCameraModifier_CameraShake_Data(Structure):
	_fields_ = [
		("ActiveShakes", TArray_FCameraShakeInstance),
		("SplitScreenShakeScale", c_float),
	]

class  UCameraModifier_CameraShake(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCameraModifier", UCameraModifier_Data),
		("UCameraModifier_CameraShake", UCameraModifier_CameraShake_Data),
	]


class  UCameraShake_Data(Structure):
	_fields_ = [
		("bSingleInstance", c_bool, 1),
		("bRandomAnimSegment", c_bool, 1),
		("", c_ulong, 0),
		("OscillationDuration", c_float),
		("OscillationBlendInTime", c_float),
		("OscillationBlendOutTime", c_float),
		("RotOscillation", FROscillator),
		("LocOscillation", FVOscillator),
		("FOVOscillation", FFOscillator),
		("Anim", POINTER(UCameraAnim)),
		("AnimPlayRate", c_float),
		("AnimScale", c_float),
		("AnimBlendInTime", c_float),
		("AnimBlendOutTime", c_float),
		("RandomAnimSegmentDuration", c_float),
	]

class  UCameraShake(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UCameraShake", UCameraShake_Data),
	]


class  AResourcePoolManager_Data(Structure):
	_fields_ = [
	
		("ResourcePools", POINTER(UResourcePool) * 16),
		("Unknown1", c_ubyte, 0x),
		("NextPoolGUID", c_ubyte),
		("Unknown2", c_ubyte, 0x),
		("ReplicatedPoolIdentities", FResourcePoolIdentityState * 16),
		("ReplicatedCurrentValues", c_float * 16),
		("ReplicatedMinValues", c_float * 16),
		("ReplicatedMaxValues", c_float * 16),
		("ReplicatedRarelyChangedState", FRarelyChangedPoolState * 16),
	]

class  AResourcePoolManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AReplicationInfo", AReplicationInfo_Data),
		("AResourcePoolManager", AResourcePoolManager_Data),
	]


class  AWorldSoundManager_Data(Structure):
	_fields_ = [
		("EventSources", TArray_FWorldEventSource),
		("UIAkComponent", POINTER(UAkComponent)),
		("bHasTicked", c_bool, 1),
		("", c_ulong, 0),
	]

class  AWorldSoundManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AWorldSoundManager", AWorldSoundManager_Data),
	]


class  UComponentLifetimeManagerComponent_Data(Structure):
	_fields_ = [
		("ManagedComponents", TArray_UActorComponentPtr),
		("ManagedComponentsLifeSpan", c_float),
	]

class  UComponentLifetimeManagerComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UComponentLifetimeManagerComponent", UComponentLifetimeManagerComponent_Data),
	]


class  UAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
	]


class  UBalancedActorAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UBalancedActorAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UBalancedActorAttributeContextResolver", UBalancedActorAttributeContextResolver_Data),
	]


class  UCharacterClassAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UCharacterClassAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UCharacterClassAttributeContextResolver", UCharacterClassAttributeContextResolver_Data),
	]


class  UControllerAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UControllerAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UControllerAttributeContextResolver", UControllerAttributeContextResolver_Data),
	]


class  UGameInfoAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UGameInfoAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UGameInfoAttributeContextResolver", UGameInfoAttributeContextResolver_Data),
	]


class  UOffHandWeaponAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UOffHandWeaponAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UOffHandWeaponAttributeContextResolver", UOffHandWeaponAttributeContextResolver_Data),
	]


class  UPawnAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UPawnAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UPawnAttributeContextResolver", UPawnAttributeContextResolver_Data),
	]


class  UResourcePoolAttributeContextResolver_Data(Structure):
	_fields_ = [
		("Resource", POINTER(UResourceDefinition)),
	]

class  UResourcePoolAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UResourcePoolAttributeContextResolver", UResourcePoolAttributeContextResolver_Data),
	]


class  UWeaponAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UWeaponAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UWeaponAttributeContextResolver", UWeaponAttributeContextResolver_Data),
	]


class  UWeaponResourcePoolAttributeContextResolver_Data(Structure):
	_fields_ = [
		("PrimaryHandResource", POINTER(UResourceDefinition)),
		("OffHandResource", POINTER(UResourceDefinition)),
	]

class  UWeaponResourcePoolAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UWeaponResourcePoolAttributeContextResolver", UWeaponResourcePoolAttributeContextResolver_Data),
	]


class  UAttributeEffect_Data(Structure):
	_fields_ = []

class  UAttributeEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeEffect", UAttributeEffect_Data),
	]


class  UAttributeExpression_Data(Structure):
	_fields_ = []

class  UAttributeExpression(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeExpression", UAttributeExpression_Data),
	]


class  UAttributeMultiContextResolver_Data(Structure):
	_fields_ = []

class  UAttributeMultiContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeMultiContextResolver", UAttributeMultiContextResolver_Data),
	]


class  UWeaponAttributeMultiContextResolver_Data(Structure):
	_fields_ = []

class  UWeaponAttributeMultiContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeMultiContextResolver", UAttributeMultiContextResolver_Data),
		("UWeaponAttributeMultiContextResolver", UWeaponAttributeMultiContextResolver_Data),
	]


class  UAttributeValueResolver_Data(Structure):
	_fields_ = []

class  UAttributeValueResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeValueResolver", UAttributeValueResolver_Data),
	]


class  UObjectPropertyAttributeValueResolver_Data(Structure):
	_fields_ = [
		("PropertyName", FName),
		("CachedProperty", POINTER(UProperty)),
	]

class  UObjectPropertyAttributeValueResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeValueResolver", UAttributeValueResolver_Data),
		("UObjectPropertyAttributeValueResolver", UObjectPropertyAttributeValueResolver_Data),
	]


class  UReadOnlyObjectPropertyAttributeValueResolver_Data(Structure):
	_fields_ = []

class  UReadOnlyObjectPropertyAttributeValueResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeValueResolver", UAttributeValueResolver_Data),
		("UObjectPropertyAttributeValueResolver", UObjectPropertyAttributeValueResolver_Data),
		("UReadOnlyObjectPropertyAttributeValueResolver", UReadOnlyObjectPropertyAttributeValueResolver_Data),
	]


class  UBehaviorBase_Data(Structure):
	_fields_ = [
		("Context", FBehaviorContextData),
	]

class  UBehaviorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
	]


class  UBehavior_Kill_Data(Structure):
	_fields_ = [
		("DeathType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("DamageType", POINTER(UDamageTypeDefinition)),
		("TargetContext", FBehaviorContextData),
	]

class  UBehavior_Kill(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_Kill", UBehavior_Kill_Data),
	]


class  UBehavior_PlaySound_Data(Structure):
	_fields_ = [
		("Sound", POINTER(UAkEvent)),
		("bReplicateSound", c_bool, 1),
		("", c_ulong, 0),
	]

class  UBehavior_PlaySound(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_PlaySound", UBehavior_PlaySound_Data),
	]


class  UBehavior_RemoteEvent_Data(Structure):
	_fields_ = [
		("EventName", FName),
		("bDebug", c_bool, 1),
		("", c_ulong, 0),
	]

class  UBehavior_RemoteEvent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_RemoteEvent", UBehavior_RemoteEvent_Data),
	]


class  UExpressionEvaluator_Data(Structure):
	_fields_ = []

class  UExpressionEvaluator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UExpressionEvaluator", UExpressionEvaluator_Data),
	]


class  UExpressionTree_Data(Structure):
	_fields_ = [
		("RootChild", POINTER(UExpressionEvaluator)),
	]

class  UExpressionTree(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UExpressionEvaluator", UExpressionEvaluator_Data),
		("UExpressionTree", UExpressionTree_Data),
	]


class  UAttributeDefinitionBase_Data(Structure):
	_fields_ = [
		("bIsSimpleAttribute", c_bool, 1),
		("", c_ulong, 0),
		("AttributeDataType", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ContextResolverChain", TArray_UAttributeContextResolverPtr),
		("ValueResolverChain", TArray_UAttributeValueResolverPtr),
	]

class  UAttributeDefinitionBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UAttributeDefinitionBase", UAttributeDefinitionBase_Data),
	]


class  UAttributeDefinition_Data(Structure):
	_fields_ = []

class  UAttributeDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UAttributeDefinitionBase", UAttributeDefinitionBase_Data),
		("UAttributeDefinition", UAttributeDefinition_Data),
	]


class  UNestedAttributeDefinition_Data(Structure):
	_fields_ = [
		("OuterContextAttributeDefinition", POINTER(UAttributeDefinition)),
		("InnerContextAttributeDefinition", POINTER(UAttributeDefinition)),
	]

class  UNestedAttributeDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UAttributeDefinitionBase", UAttributeDefinitionBase_Data),
		("UAttributeDefinition", UAttributeDefinition_Data),
		("UNestedAttributeDefinition", UNestedAttributeDefinition_Data),
	]


class  UAttributeDefinitionMultiContext_Data(Structure):
	_fields_ = [
		("MultiContextResolver", POINTER(UAttributeMultiContextResolver)),
	]

class  UAttributeDefinitionMultiContext(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UAttributeDefinitionBase", UAttributeDefinitionBase_Data),
		("UAttributeDefinitionMultiContext", UAttributeDefinitionMultiContext_Data),
	]


class  UAttributeInitializationDefinition_Data(Structure):
	_fields_ = [
		("BaseValueMode", c_ubyte),
		("RoundingMode", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("ValueFormula", FBalanceFormula),
		("ConditionalInitialization", FConditionalInitializationExpressions),
		("RandomVariance", FVariance),
		("RangeRestriction", FRange),
	]

class  UAttributeInitializationDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UAttributeInitializationDefinition", UAttributeInitializationDefinition_Data),
	]


class  UBaseBalanceDefinition_Data(Structure):
	_fields_ = []

class  UBaseBalanceDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UBaseBalanceDefinition", UBaseBalanceDefinition_Data),
	]


class  UCharacterClassDefinition_Data(Structure):
	_fields_ = [
		("GroundSpeed", c_float),
		("AirSpeed", c_float),
		("WalkingPct", c_float),
		("SprintingPct", c_float),
		("JumpZ", c_float),
		("CrouchedPct", c_float),
		("BaseEncumbranceResistance", FAttributeInitializationData),
		("MaxFallSpeed", c_float),
		("HealthPoolDefinition", POINTER(UResourcePoolDefinition)),
		("ShieldPoolDefinition", POINTER(UResourcePoolDefinition)),
		("AccuracyPoolDefinition", POINTER(UResourcePoolDefinition)),
		("OffHandAccuracyPoolDefinition", POINTER(UResourcePoolDefinition)),
		("ResourcePools", TArray_UResourcePoolDefinitionPtr),
		("bDealsLocationalDamage", c_bool, 1),
		("CanHarmSelf", c_bool, 1),
		("bAutoDisableAttractorOnDeath", c_bool, 1),
		("", c_ulong, 0),
		("BaseArmor", FAttributeInitializationData),
		("BaseNormalDamageModifiers", FDamageTypeResistance),
		("BaseExplosiveDamageModifiers", FDamageTypeResistance),
		("BaseShockDamageModifiers", FDamageTypeResistance),
		("BaseCorrosiveDamageModifiers", FDamageTypeResistance),
		("BaseIncendiaryDamageModifiers", FDamageTypeResistance),
		("BaseAmpDamageModifiers", FDamageTypeResistance),
	]

class  UCharacterClassDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UCharacterClassDefinition", UCharacterClassDefinition_Data),
	]


class  UExpressionEvaluatorDefinition_Data(Structure):
	_fields_ = [
		("Expression", POINTER(UExpressionEvaluator)),
	]

class  UExpressionEvaluatorDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UExpressionEvaluatorDefinition", UExpressionEvaluatorDefinition_Data),
	]


class  UGestaltPartMatricesCollectionDefinition_Data(Structure):
	_fields_ = [
		("Collection", TArray_FGPMCollection),
	]

class  UGestaltPartMatricesCollectionDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UGestaltPartMatricesCollectionDefinition", UGestaltPartMatricesCollectionDefinition_Data),
	]


class  UImpactDefinition_Data(Structure):
	_fields_ = []

class  UImpactDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UImpactDefinition", UImpactDefinition_Data),
	]


class  UResourceDefinition_Data(Structure):
	_fields_ = [
		("ResourceName", FString),
		("bIntegerOnlyUpdates", c_bool, 1),
		("bSerializeInSaveGame", c_bool, 1),
		("", c_ulong, 0),
		("DefaultResourcePoolClass", POINTER(UClass)),
		("DefaultResourcePoolDefinition", POINTER(UResourcePoolDefinition)),
		("ResourceContextResolver", POINTER(UAttributeContextResolver)),
	]

class  UResourceDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UResourceDefinition", UResourceDefinition_Data),
	]


class  UResourcePoolDefinition_Data(Structure):
	_fields_ = [
		("Resource", POINTER(UResourceDefinition)),
		("NetRelevancy", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("RegenerationResource", POINTER(UResourceDefinition)),
		("BaseMinValue", c_float),
		("BaseMaxValue", FAttributeInitializationData),
		("StartingValue", c_float),
		("StartWithMinValue", c_bool, 1),
		("StartWithMaxValue", c_bool, 1),
		("bUpdateCurrentValueOnExtremaChange", c_bool, 1),
		("bPulseBasedOnRegenRate", c_bool, 1),
		("bPulseWhenLow", c_bool, 1),
		("", c_ulong, 0),
		("BaseConsumptionRate", c_float),
		("BaseActiveRegenerationRate", c_float),
		("BasePassiveRegenerationRate", c_float),
		("BaseOnIdleRegenerationRate", c_float),
		("BaseOnIdleRegenerationDelay", c_float),
		("RecentImpulseTimer", c_float),
		("PercBarPulseSpeed", c_float),
		("PercPulseResourceLow", c_float),
		("OnResourceDepleted", TArray_UBehaviorBasePtr),
		("OnResourceNotDepleted", TArray_UBehaviorBasePtr),
		("OnResourceRegenerated", TArray_UBehaviorBasePtr),
		("OnResourceNotRegenerated", TArray_UBehaviorBasePtr),
		("UpgradeLevelAttribute", POINTER(UAttributeDefinition)),
		("TotalUpgradeCount", c_int),
		("MaxValueUpgrade", FAttributeInitializationData),
	]

class  UResourcePoolDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UResourcePoolDefinition", UResourcePoolDefinition_Data),
	]


class  UGestaltPartMatrices_Data(Structure):
	_fields_ = [
		("GestaltAccessoryMeshList", TArray_FGestaltAccessoryMeshEntry),
		("Matrices", TArray_FMatrix),
		("ArchetypeName", FName),
	]

class  UGestaltPartMatrices(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGestaltPartMatrices", UGestaltPartMatrices_Data),
	]


class  UICounterBehavior_Data(Structure):
	_fields_ = []

class  UICounterBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UICounterBehavior", UICounterBehavior_Data),
	]


class  UIInstanceData_Data(Structure):
	_fields_ = []

class  UIInstanceData(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIInstanceData", UIInstanceData_Data),
	]


class  UInstanceDataHelper_Data(Structure):
	_fields_ = []

class  UInstanceDataHelper(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInstanceDataHelper", UInstanceDataHelper_Data),
	]


class  UPackageReferencer_Data(Structure):
	_fields_ = [
		("PackageNames", TArray_FString),
	]

class  UPackageReferencer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPackageReferencer", UPackageReferencer_Data),
	]


class  UPersistentGameDataManager_Data(Structure):
	_fields_ = [
		("SequencesWithPersistentData", TArray_UPersistentSequenceDataPtr),
	]

class  UPersistentGameDataManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPersistentGameDataManager", UPersistentGameDataManager_Data),
	]


class  UPersistentSequenceData_Data(Structure):
	_fields_ = [
		("LevelPackageName", FName),
		("SequenceName", FName),
		("Unknown1", c_ubyte, 0x),
	]

class  UPersistentSequenceData(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPersistentSequenceData", UPersistentSequenceData_Data),
	]


class  UResourcePool_Data(Structure):
	_fields_ = [
		("Definition", POINTER(UResourcePoolDefinition)),
		("PoolGUID", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("MinValue", c_float),
		("MinValueBaseValue", c_float),
		("MinValueModifierStack", TArray_UAttributeModifierPtr),
		("MaxValue", c_float),
		("MaxValueBaseValue", c_float),
		("MaxValueModifierStack", TArray_UAttributeModifierPtr),
		("CurrentValue", c_float),
		("ConsumptionRate", c_float),
		("ConsumptionRateBaseValue", c_float),
		("ConsumptionRateModifierStack", TArray_UAttributeModifierPtr),
		("ActiveRegenerationRate", c_float),
		("ActiveRegenerationRateBaseValue", c_float),
		("ActiveRegenerationRateModifierStack", TArray_UAttributeModifierPtr),
		("OnIdleRegenerationRate", c_float),
		("OnIdleRegenerationRateBaseValue", c_float),
		("OnIdleRegenerationRateModifierStack", TArray_UAttributeModifierPtr),
		("OnIdleRegenerationDelay", c_float),
		("OnIdleRegenerationDelayBaseValue", c_float),
		("OnIdleRegenerationDelayModifierStack", TArray_UAttributeModifierPtr),
		("PassiveRegenerationRate", c_float),
		("PassiveRegenerationRateBaseValue", c_float),
		("PassiveRegenerationRateModifierStack", TArray_UAttributeModifierPtr),
		("LastMinValue", c_float),
		("LastMaxValue", c_float),
		("LastCurrentValue", c_float),
		("PoolIdleDelayStartTime", c_float),
		("RateRemainder", c_float),
		("RecentImpulseCount", c_int),
		("RegenerationDisabled", c_int),
		("RegenerationDisabledBaseValue", c_int),
		("RegenerationDisabledModifierStack", TArray_UAttributeModifierPtr),
		("ResetRecentImpulseCountTime", c_float),
		("bIsAuthoritative", c_bool, 1),
		("bIsBeingInitialized", c_bool, 1),
		("bHasPoolBeenFullSinceLastBeingDepleted", c_bool, 1),
		("bDisallowReinitialization", c_bool, 1),
		("bHideHUDDisplay", c_bool, 1),
		("bCreatedAndNotModified", c_bool, 1),
		("WasRegenerating", c_bool, 1),
		("", c_ulong, 0),
		("AssociatedProvider", POINTER(UObject)),
		("HUDMaterialInstance", POINTER(UMaterialInstanceConstant)),
		("RegenerationPool", POINTER(UResourcePool)),
		("IsRegenerating", c_int),
	]

class  UResourcePool(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UResourcePool", UResourcePool_Data),
	]


class  UHealthResourcePool_Data(Structure):
	_fields_ = []

class  UHealthResourcePool(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UResourcePool", UResourcePool_Data),
		("UHealthResourcePool", UHealthResourcePool_Data),
	]


class  UTargetableList_Data(Structure):
	_fields_ = [
		("TargetableAllegianceMap", FMultiMap_Mirror),
		("FullTargetableList", TArray_FScriptInterface),
	]

class  UTargetableList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UTargetableList", UTargetableList_Data),
	]


class  AHybridNavigationArea_Data(Structure):
	_fields_ = [
		("CustomAreaName", FName),
		("AreaColor", FColor),
		("bShowArea", c_bool, 1),
		("", c_ulong, 0),
	]

class  AHybridNavigationArea(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AHybridNavigationArea", AHybridNavigationArea_Data),
	]


class  APickupableMeshActor_Data(Structure):
	_fields_ = [
		("MyTarget", POINTER(AActor)),
		("MoveSpeed", c_float),
		("RotateSpeed", c_int),
		("PawnEyeHeightAdjustment", c_float),
	]

class  APickupableMeshActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("APickupableMeshActor", APickupableMeshActor_Data),
	]


class  UHybridNavigationAreaDebugRenderingComponent_Data(Structure):
	_fields_ = [
		("DebugSphereRadius", c_float),
	]

class  UHybridNavigationAreaDebugRenderingComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UHybridNavigationAreaDebugRenderingComponent", UHybridNavigationAreaDebugRenderingComponent_Data),
	]


class  UHybridNavigationVisualizationComponent_Data(Structure):
	_fields_ = [
		("AllNavPoints", TArray_ANavigationPointPtr),
		("NavPointsToRepresent", TArray_ANavigationPointPtr),
		("NextNavPointToProcess", c_int),
		("bIsVisualizationInProgress", c_bool, 1),
		("bIsVisualizationReady", c_bool, 1),
		("", c_ulong, 0),
		("VisualizationVertsByNavPoint", TArray_FHybridNavVisualizationVertsForNavPoint),
		("VisualizationColor", FColor),
		("VisualizationStats", FHybridNavVisualizationPerfStats),
	]

class  UHybridNavigationVisualizationComponent(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UComponent", UComponent_Data),
		("UActorComponent", UActorComponent_Data),
		("UPrimitiveComponent", UPrimitiveComponent_Data),
		("UHybridNavigationVisualizationComponent", UHybridNavigationVisualizationComponent_Data),
	]


class  UInventoryCardPresentationDefinition_Data(Structure):
	_fields_ = [
		("ZippyFrame", FString),
		("ItemFrame", FString),
		("DescriptionLocReference", FString),
	]

class  UInventoryCardPresentationDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UInventoryCardPresentationDefinition", UInventoryCardPresentationDefinition_Data),
	]


class  UManufacturerDefinition_Data(Structure):
	_fields_ = [
		("Grades", TArray_FManufacturerGradeData),
		("FlashLabelName", FString),
		("IconX", c_int),
		("IconY", c_int),
		("StatId", FName),
	]

class  UManufacturerDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UManufacturerDefinition", UManufacturerDefinition_Data),
	]


class  ULevelStreamingDomino_Data(Structure):
	_fields_ = [
		("TilePossibilities", TArray_FName),
	]

class  ULevelStreamingDomino(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULevelStreaming", ULevelStreaming_Data),
		("ULevelStreamingKismet", ULevelStreamingKismet_Data),
		("ULevelStreamingDomino", ULevelStreamingDomino_Data),
	]


class  ULocalMessage_Data(Structure):
	_fields_ = [
		("bIsSpecial", c_bool, 1),
		("bIsUnique", c_bool, 1),
		("bIsPartiallyUnique", c_bool, 1),
		("bIsConsoleMessage", c_bool, 1),
		("bBeep", c_bool, 1),
		("bCountInstances", c_bool, 1),
		("", c_ulong, 0),
		("Lifetime", c_float),
		("DrawColor", FColor),
		("MsgType", c_ubyte),
	]

class  ULocalMessage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULocalMessage", ULocalMessage_Data),
	]


class  UEdgeDetectionPostProcessEffect_Data(Structure):
	_fields_ = [
		("HFilterAxisCoeff", c_float),
		("HFilterDiagCoeff", c_float),
		("VFilterAxisCoeff", c_float),
		("VFilterDiagCoeff", c_float),
		("FarDist", c_float),
		("NearDist", c_float),
		("SobelPower", c_float),
		("TexelOffset", c_float),
	]

class  UEdgeDetectionPostProcessEffect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UPostProcessEffect", UPostProcessEffect_Data),
		("UEdgeDetectionPostProcessEffect", UEdgeDetectionPostProcessEffect_Data),
	]


class  ADroppedPickup_Data(Structure):
	_fields_ = [
		("VfTable_IIPickupable", FPointer),
		("Inventory", POINTER(AWillowInventory)),
		("PickupCache", POINTER(ANavigationPoint)),
		("bFadeOut", c_bool, 1),
		("bUseRBPhysics", c_bool, 1),
		("bIsDiscovered", c_bool, 1),
		("bClientIsDiscovered", c_bool, 1),
		("bTorque", c_bool, 1),
		("bTorqueTemporary", c_bool, 1),
		("", c_ulong, 0),
		("Manufacturer", POINTER(UManufacturerDefinition)),
		("MeshBounds", FBoxSphereBounds),
		("Torque", FVector),
	]

class  ADroppedPickup(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADroppedPickup", ADroppedPickup_Data),
	]


class  AInventory_Data(Structure):
	_fields_ = [
		("Inventory", POINTER(AInventory)),
		("InvManager", POINTER(AInventoryManager)),
		("ItemName", FString),
		("bDropOnDeath", c_bool, 1),
		("bReadied", c_bool, 1),
		("bDelayedSpawn", c_bool, 1),
		("bPredictRespawns", c_bool, 1),
		("", c_ulong, 0),
		("RespawnTime", c_float),
		("MaxDesireability", c_float),
		("PickupMessage", FString),
		("MessageClass", POINTER(UClass)),
		("PickupSound", POINTER(USoundCue)),
		("DroppedPickupClass", POINTER(UClass)),
		("DroppedPickupMesh", POINTER(UPrimitiveComponent)),
		("PickupFactoryMesh", POINTER(UPrimitiveComponent)),
	]

class  AInventory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInventory", AInventory_Data),
	]


class  AWillowInventory_Data(Structure):
	_fields_ = [
		("VfTable_IIBalancedActor", FPointer),
		("VfTable_IIAttributeSlotEffectProvider", FPointer),
		("MonetaryValue", c_int),
		("MonetaryValueModifierTotal", c_float),
		("Quantity", c_int),
		("RarityLevel", c_int),
		("ExpLevel", c_int),
		("GameStage", c_int),
		("AwesomeLevel", c_int),
		("AdditionalQueryInterfaceSource", POINTER(UObject)),
		("ClonedForSharing", c_float),
		("LastCanBeUsedByResult", c_int),
		("ZippyFrame", FName),
		("ItemFrame", FString),
		("ElementalFrame", FName),
		("SourceDefinitionName", FName),
		("SourceResponsibleName", FName),
		("ItemLocation", c_ubyte),
		("Mark", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("bShopsHaveInfiniteQuantity", c_bool, 1),
		("bOnlyCompareStatsForMatchingAttributes", c_bool, 1),
		("", c_ulong, 0),
		("AttributeSlots", FAttributeSlotData * 19),
		("ReplicatedAttributeSlotModifierValues", c_float * 19),
		("RuntimeAttributeSlotSkill", POINTER(UGBXDefinition)),
		("TempStatModifier", c_float),
		("TempStatModifierBaseValue", c_float),
		("TempStatModifierModifierStack", TArray_UAttributeModifierPtr),
		("AppliedAttributeSlotEffects", TArray_FAppliedAttributeEffect),
		("ExternalLikenessConsumers", TArray_AActorPtr),
	]

class  AWillowInventory(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInventory", AInventory_Data),
		("AWillowInventory", AWillowInventory_Data),
	]


class  AWeapon_Data(Structure):
	_fields_ = [
		("CurrentFireMode", c_ubyte),
		("bOffHand", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("FiringStatesArray", TArray_FName),
		("WeaponFireTypes", TArray_unsigned_char),
		("WeaponProjectiles", TArray_UClassPtr),
		("FireInterval", c_float),
		("FireIntervalBaseValue", c_float),
		("FireIntervalModifierStack", TArray_UAttributeModifierPtr),
		("Spread", c_float),
		("SpreadBaseValue", c_float),
		("SpreadModifierStack", TArray_UAttributeModifierPtr),
		("InstantHitDamage", c_float),
		("InstantHitDamageBaseValue", c_float),
		("InstantHitDamageModifierStack", TArray_UAttributeModifierPtr),
		("InstantHitMomentum", c_float),
		("InstantHitMomentumBaseValue", c_float),
		("InstantHitMomentumModifierStack", TArray_UAttributeModifierPtr),
		("InstantHitDamageTypes", TArray_UClassPtr),
		("InstantHitDamageTypeDefinitions", TArray_UDamageTypeDefinitionPtr),
		("InstantHitImpactDefinitions", TArray_UImpactDefinitionPtr),
		("EquipTime", c_float),
		("EquipTimeBaseValue", c_float),
		("EquipTimeModifierStack", TArray_UAttributeModifierPtr),
		("PutDownTime", c_float),
		("PutDownTimeBaseValue", c_float),
		("PutDownTimeModifierStack", TArray_UAttributeModifierPtr),
		("FireOffset", FVector),
		("bWeaponPutDown", c_bool, 1),
		("bCanThrow", c_bool, 1),
		("bWasOptionalSet", c_bool, 1),
		("bWasDoNotActivate", c_bool, 1),
		("bInstantHit", c_bool, 1),
		("bMeleeWeapon", c_bool, 1),
		("bIsFiringWeapon", c_bool, 1),
		("", c_ulong, 0),
		("WeaponRange", c_float),
		("WeaponRangeBaseValue", c_float),
		("WeaponRangeModifierStack", TArray_UAttributeModifierPtr),
		("ClothImpulseRadius", c_float),
		("ClothImpulseScale", c_float),
		("FirstPersonMesh", POINTER(USkeletalMeshComponent)),
		("DefaultAnimSpeed", c_float),
		("Priority", c_float),
		("AIController", POINTER(AAIController)),
		("ShouldFireOnRelease", TArray_unsigned_char),
		("AIRating", c_float),
		("CachedMaxRange", c_float),
	]

class  AWeapon(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInventory", AInventory_Data),
		("AWillowInventory", AWillowInventory_Data),
		("AWeapon", AWeapon_Data),
	]


class  AInventoryManager_Data(Structure):
	_fields_ = [
		("InventoryChain", POINTER(AInventory)),
		("PendingWeapon", POINTER(AWeapon)),
		("PendingOffHandWeapon", POINTER(AWeapon)),
		("LastAttemptedSwitchToWeapon", POINTER(AWeapon)),
		("bMustHoldWeapon", c_bool, 1),
		("bInfiniteAmmo", c_bool, 1),
		("bForceOwnedItemsToBeRelevantToAll", c_bool, 1),
		("", c_ulong, 0),
		("PendingFire", TArray_int),
		("OffHandPendingFire", TArray_int),
	]

class  AInventoryManager(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInventoryManager", AInventoryManager_Data),
	]


class  UGearboxCalloutDefinition_Data(Structure):
	_fields_ = [
		("MaxCallOutDistance", c_float),
		("MinCallOutDistance", c_float),
		("bCheckRarity", c_bool, 1),
		("", c_ulong, 0),
		("MinRarityCallOutLevel", c_int),
	]

class  UGearboxCalloutDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UGearboxCalloutDefinition", UGearboxCalloutDefinition_Data),
	]


class  UWillowInventoryDefinition_Data(Structure):
	_fields_ = [
		("InventoryClass", POINTER(UClass)),
		("bAutomaticallyPickup", c_bool, 1),
		("bPickupInBulk", c_bool, 1),
		("bDisallowAIFromGrabbingPickup", c_bool, 1),
		("bDuplicatePickupJustAddsQuantity", c_bool, 1),
		("bSuppressPickupCard", c_bool, 1),
		("bTorque", c_bool, 1),
		("bNeverDisplayPickupMessage", c_bool, 1),
		("bShopsHaveInfiniteQuantity", c_bool, 1),
		("bCanCompare", c_bool, 1),
		("bUsesPlayerLevelRequirement", c_bool, 1),
		("bUIMeshRotationNeedsTransformFixup", c_bool, 1),
		("bIsConsumable", c_bool, 1),
		("bAllowInventoryDefToModifyPartWeight", c_bool, 1),
		("", c_ulong, 0),
		("PlayerDroppability", c_ubyte),
		("FormOfCurrency", c_ubyte),
		("OnUseConstraintsMode", c_ubyte),
		("AttributeSlotEffectMode", c_ubyte),
		("PickupLifeSpan", c_float),
		("PickupFlagScale", c_float),
		("PickupFlagIcon", POINTER(UTexture2D)),
		("PickupFlagOffset", FVector),
		("Torque", FVector),
		("ThirdPersonMeshScale", c_float),
		("PickupSounds", TArray_FConditionalSoundData),
		("PickupAndEquipSounds", TArray_FConditionalSoundData),
		("MaterialClass", POINTER(UClass)),
		("PhysicsAsset", POINTER(UPhysicsAsset)),
		("PickupMessage", FString),
		("UseFailureLevelMessage", FString),
		("UseFailureConstraintsMessage", FString),
		("NoManufacturerName", FString),
		("BaseRarity", FAttributeInitializationData),
		("MonetaryValue", FAttributeInitializationData),
		("BaseMonetaryValueModifier", c_float),
		("PlayerUseLevelBonus", FAttributeInitializationData),
		("OnUseConstraints", TArray_FAttributeExpressionData),
		("UIStatList", TArray_FUIStatData),
		("UIMeshRotation", FRotator),
		("Presentation", POINTER(UInventoryCardPresentationDefinition)),
		("CalloutDefinition", POINTER(UGearboxCalloutDefinition)),
		("PickedUpStatID", FName),
		("PurchasedStatID", FName),
		("FocusRadius", c_float),
		("FocusOffset", FVector),
		("AttributeSlotEffectSkillDuration", FAttributeInitializationData),
		("AttributeSlotBaseGrade", FAttributeInitializationData),
		("AttributeSlotMaxActivated", c_int),
		("AttributeSlotEffects", TArray_FAttributeSlotEffectData),
		("AttributeSlotUpgrades", TArray_FAttributeSlotUpgradeData),
		("LootBeamColorOverride", FColor),
	]

class  UWillowInventoryDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UWillowInventoryDefinition", UWillowInventoryDefinition_Data),
	]


class  UWillowInventoryPartDefinition_Data(Structure):
	_fields_ = [
		("Material", POINTER(UMaterialInstanceConstant)),
		("bIsGestaltMode", c_bool, 1),
		("", c_ulong, 0),
		("GestaltModeSkeletalMeshName", FName),
		("NongestaltSkeletalMesh", POINTER(USkeletalMesh)),
		("AdditionalGestaltModeSkeletalMeshNames", FName * 2),
		("AttributeSlotEffects", TArray_FAttributeSlotEffectData),
		("AttributeSlotUpgrades", TArray_FAttributeSlotUpgradeData),
		("MonetaryValueMod", POINTER(UAttributeDefinition)),
		("Rarity", FAttributeInitializationData),
		("MaterialVectorParameterValues", TArray_FVectorParameterValue),
	]

class  UWillowInventoryPartDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UWillowInventoryPartDefinition", UWillowInventoryPartDefinition_Data),
	]


class  UIPickupable_Data(Structure):
	_fields_ = []

class  UIPickupable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIPickupable", UIPickupable_Data),
	]


class  USeqEvent_HitWall_Data(Structure):
	_fields_ = []

class  USeqEvent_HitWall(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_HitWall", USeqEvent_HitWall_Data),
	]


class  USeqAct_Destroy_Data(Structure):
	_fields_ = [
		("bDestroyBasedActors", c_bool, 1),
		("", c_ulong, 0),
		("IgnoreBasedClasses", TArray_UClassPtr),
	]

class  USeqAct_Destroy(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Destroy", USeqAct_Destroy_Data),
	]


class  USeqAct_Teleport_Data(Structure):
	_fields_ = [
		("bUpdateRotation", c_bool, 1),
		("bCheckOverlap", c_bool, 1),
		("bSkipHoldingCell", c_bool, 1),
		("bTurnOffCinematicModeAfterTeleport", c_bool, 1),
		("bHideTeleportEffect", c_bool, 1),
		("", c_ulong, 0),
		("TeleportDistance", c_float),
		("TeleportVolumes", TArray_AVolumePtr),
		("Source", POINTER(UObject)),
		("ResurrectStation", POINTER(AActor)),
	]

class  USeqAct_Teleport(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Teleport", USeqAct_Teleport_Data),
	]


class  USeqAct_SetVelocity_Data(Structure):
	_fields_ = [
		("VelocityDir", FVector),
		("VelocityMag", c_float),
		("bVelocityRelativeToActorRotation", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_SetVelocity(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetVelocity", USeqAct_SetVelocity_Data),
	]


class  USeqAct_ToggleHidden_Data(Structure):
	_fields_ = [
		("bToggleBasedActors", c_bool, 1),
		("", c_ulong, 0),
		("IgnoreBasedClasses", TArray_UClassPtr),
	]

class  USeqAct_ToggleHidden(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Toggle", USeqAct_Toggle_Data),
		("USeqAct_ToggleHidden", USeqAct_ToggleHidden_Data),
	]


class  USeqAct_AttachToActor_Data(Structure):
	_fields_ = [
		("bDetach", c_bool, 1),
		("bHardAttach", c_bool, 1),
		("bUseRelativeOffset", c_bool, 1),
		("bUseRelativeRotation", c_bool, 1),
		("bUseConstructAttachment", c_bool, 1),
		("", c_ulong, 0),
		("BoneName", FName),
		("RelativeOffset", FVector),
		("RelativeRotation", FRotator),
	]

class  USeqAct_AttachToActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_AttachToActor", USeqAct_AttachToActor_Data),
	]


class  UIConsoleCommandBehavior_Data(Structure):
	_fields_ = []

class  UIConsoleCommandBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIConsoleCommandBehavior", UIConsoleCommandBehavior_Data),
	]


class  UIAppearanceBehavior_Data(Structure):
	_fields_ = []

class  UIAppearanceBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIAppearanceBehavior", UIAppearanceBehavior_Data),
	]


class  UIPhysicsBehavior_Data(Structure):
	_fields_ = []

class  UIPhysicsBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIPhysicsBehavior", UIPhysicsBehavior_Data),
	]


class  UIChangeCollisionBehavior_Data(Structure):
	_fields_ = []

class  UIChangeCollisionBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIChangeCollisionBehavior", UIChangeCollisionBehavior_Data),
	]


class  UIDestroyBehavior_Data(Structure):
	_fields_ = []

class  UIDestroyBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIDestroyBehavior", UIDestroyBehavior_Data),
	]


class  UISoundBehavior_Data(Structure):
	_fields_ = []

class  UISoundBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UISoundBehavior", UISoundBehavior_Data),
	]


class  UOnlineAuthInterface_Data(Structure):
	_fields_ = [
		("__OnAuthReady__Delegate", FScriptDelegate),
		("__OnAuthRequestClient__Delegate", FScriptDelegate),
		("__OnAuthRequestServer__Delegate", FScriptDelegate),
		("__OnAuthBlobReceivedClient__Delegate", FScriptDelegate),
		("__OnAuthBlobReceivedServer__Delegate", FScriptDelegate),
		("__OnAuthCompleteClient__Delegate", FScriptDelegate),
		("__OnAuthCompleteServer__Delegate", FScriptDelegate),
		("__OnAuthKillClient__Delegate", FScriptDelegate),
		("__OnAuthRetryServer__Delegate", FScriptDelegate),
		("__OnClientConnectionClose__Delegate", FScriptDelegate),
		("__OnServerConnectionClose__Delegate", FScriptDelegate),
	]

class  UOnlineAuthInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineAuthInterface", UOnlineAuthInterface_Data),
	]


class  UOnlineTitleFileInterface_Data(Structure):
	_fields_ = [
		("__OnReadTitleFileComplete__Delegate", FScriptDelegate),
		("__OnShareTitleFileComplete__Delegate", FScriptDelegate),
	]

class  UOnlineTitleFileInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineTitleFileInterface", UOnlineTitleFileInterface_Data),
	]


class  UOnlinePartyChatInterface_Data(Structure):
	_fields_ = [
		("__OnSendPartyGameInvitesComplete__Delegate", FScriptDelegate),
		("__OnPartyMemberListChanged__Delegate", FScriptDelegate),
		("__OnPartyMembersInfoChanged__Delegate", FScriptDelegate),
	]

class  UOnlinePartyChatInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlinePartyChatInterface", UOnlinePartyChatInterface_Data),
	]


class  UOnlineNewsInterface_Data(Structure):
	_fields_ = [
		("__OnReadNewsCompleted__Delegate", FScriptDelegate),
	]

class  UOnlineNewsInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineNewsInterface", UOnlineNewsInterface_Data),
	]


class  UOnlineStatsInterface_Data(Structure):
	_fields_ = [
		("__OnReadOnlineStatsComplete__Delegate", FScriptDelegate),
		("__OnFlushOnlineStatsComplete__Delegate", FScriptDelegate),
		("__OnRegisterHostStatGuidComplete__Delegate", FScriptDelegate),
	]

class  UOnlineStatsInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineStatsInterface", UOnlineStatsInterface_Data),
	]


class  UOnlineVoiceInterface_Data(Structure):
	_fields_ = [
		("__OnPlayerTalkingStateChange__Delegate", FScriptDelegate),
		("__OnRecognitionComplete__Delegate", FScriptDelegate),
	]

class  UOnlineVoiceInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineVoiceInterface", UOnlineVoiceInterface_Data),
	]


class  UOnlineContentInterface_Data(Structure):
	_fields_ = [
		("__OnContentChange__Delegate", FScriptDelegate),
		("__OnReadContentComplete__Delegate", FScriptDelegate),
		("__OnReadCrossTitleContentComplete__Delegate", FScriptDelegate),
		("__OnReadCrossTitleSaveGameDataComplete__Delegate", FScriptDelegate),
		("__OnQueryAvailableDownloadsComplete__Delegate", FScriptDelegate),
		("__OnReadSaveGameDataComplete__Delegate", FScriptDelegate),
		("__OnWriteSaveGameDataComplete__Delegate", FScriptDelegate),
		("__OnReadSaveGamesComplete__Delegate", FScriptDelegate),
		("__OnReadDownloadableContentListComplete__Delegate", FScriptDelegate),
		("__OnReadHiddenDownloadableContentListComplete__Delegate", FScriptDelegate),
		("__OnReadCriticalDownloadableContentListComplete__Delegate", FScriptDelegate),
		("__OnCheckDownloadableContentList__Delegate", FScriptDelegate),
	]

class  UOnlineContentInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineContentInterface", UOnlineContentInterface_Data),
	]


class  UOnlineGameInterface_Data(Structure):
	_fields_ = [
		("__OnCreateOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnUpdateOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnDestroyOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnFindOnlineGamesComplete__Delegate", FScriptDelegate),
		("__OnCancelFindOnlineGamesComplete__Delegate", FScriptDelegate),
		("__OnQosStatusChanged__Delegate", FScriptDelegate),
		("__OnJoinOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnRegisterPlayerComplete__Delegate", FScriptDelegate),
		("__OnUnregisterPlayerComplete__Delegate", FScriptDelegate),
		("__OnStartOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnEndOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnArbitrationRegistrationComplete__Delegate", FScriptDelegate),
		("__OnGameInviteAccepted__Delegate", FScriptDelegate),
		("__OnGameInviteProcessingStarted__Delegate", FScriptDelegate),
		("__OnRecalculateSkillRatingComplete__Delegate", FScriptDelegate),
		("__OnMigrateOnlineGameComplete__Delegate", FScriptDelegate),
		("__OnJoinMigratedOnlineGameComplete__Delegate", FScriptDelegate),
	]

class  UOnlineGameInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineGameInterface", UOnlineGameInterface_Data),
	]


class  UOnlineSystemInterface_Data(Structure):
	_fields_ = [
		("__OnLinkStatusChange__Delegate", FScriptDelegate),
		("__OnExternalUIChange__Delegate", FScriptDelegate),
		("__OnControllerChange__Delegate", FScriptDelegate),
		("__OnConnectionStatusChange__Delegate", FScriptDelegate),
		("__OnStorageDeviceChange__Delegate", FScriptDelegate),
		("__OnContentChange__Delegate", FScriptDelegate),
	]

class  UOnlineSystemInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineSystemInterface", UOnlineSystemInterface_Data),
	]


class  UOnlinePlayerInterfaceEx_Data(Structure):
	_fields_ = [
		("__OnDeviceSelectionComplete__Delegate", FScriptDelegate),
		("__OnProfileDataChanged__Delegate", FScriptDelegate),
		("__OnReadCrossTitleProfileSettingsComplete__Delegate", FScriptDelegate),
		("__OnUnlockAvatarAwardComplete__Delegate", FScriptDelegate),
	]

class  UOnlinePlayerInterfaceEx(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlinePlayerInterfaceEx", UOnlinePlayerInterfaceEx_Data),
	]


class  UOnlinePlayerInterface_Data(Structure):
	_fields_ = [
		("__OnLoginChange__Delegate", FScriptDelegate),
		("__OnLoginCancelled__Delegate", FScriptDelegate),
		("__OnMutingChange__Delegate", FScriptDelegate),
		("__OnFriendsChange__Delegate", FScriptDelegate),
		("__OnLoginFailed__Delegate", FScriptDelegate),
		("__OnLogoutCompleted__Delegate", FScriptDelegate),
		("__OnGetUserAgeGroup__Delegate", FScriptDelegate),
		("__OnLoginStatusChange__Delegate", FScriptDelegate),
		("__OnReadProfileSettingsComplete__Delegate", FScriptDelegate),
		("__OnWriteProfileSettingsComplete__Delegate", FScriptDelegate),
		("__OnReadPlayerStorageComplete__Delegate", FScriptDelegate),
		("__OnReadPlayerStorageForNetIdComplete__Delegate", FScriptDelegate),
		("__OnWritePlayerStorageComplete__Delegate", FScriptDelegate),
		("__OnReadFriendsComplete__Delegate", FScriptDelegate),
		("__OnKeyboardInputComplete__Delegate", FScriptDelegate),
		("__OnAddFriendByNameComplete__Delegate", FScriptDelegate),
		("__OnFriendInviteReceived__Delegate", FScriptDelegate),
		("__OnSentGameInvite__Delegate", FScriptDelegate),
		("__OnReceivedGameInvite__Delegate", FScriptDelegate),
		("__OnJoinFriendGameComplete__Delegate", FScriptDelegate),
		("__OnFriendMessageReceived__Delegate", FScriptDelegate),
		("__OnUnlockAchievementComplete__Delegate", FScriptDelegate),
		("__OnReadAchievementsComplete__Delegate", FScriptDelegate),
	]

class  UOnlinePlayerInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlinePlayerInterface", UOnlinePlayerInterface_Data),
	]


class  UOnlineAccountInterface_Data(Structure):
	_fields_ = [
		("__OnCreateOnlineAccountCompleted__Delegate", FScriptDelegate),
	]

class  UOnlineAccountInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineAccountInterface", UOnlineAccountInterface_Data),
	]


class  AAccessControl_Data(Structure):
	_fields_ = [
		("IPPolicies", TArray_FString),
		("BannedIDs", TArray_FUniqueNetId),
		("IPBanned", FString),
		("WrongPassword", FString),
		("NeedPassword", FString),
		("SessionBanned", FString),
		("KickedMsg", FString),
		("DefaultKickReason", FString),
		("IdleKickReason", FString),
		("AuthenticationFailed", FString),
		("AdminClass", POINTER(UClass)),
		("AdminPassword", FString),
		("GamePassword", FString),
		("ACDisplayText", FString * 3),
		("ACDescText", FString * 3),
		("bDontAddDefaultAdmin", c_bool, 1),
		("bPendingPostSeamlessInit", c_bool, 1),
		("bAuthenticateClients", c_bool, 1),
		("bAuthenticateServer", c_bool, 1),
		("bAuthenticateListenHost", c_bool, 1),
		("bPendingListenAuth", c_bool, 1),
		("", c_ulong, 0),
		("MaxAuthRetryCount", c_int),
		("AuthRetryDelay", c_int),
		("OnlineSub", POINTER(UOnlineSubsystem)),
		("CachedAuthInt", POINTER(UOnlineAuthInterfaceBaseImpl)),
		("ClientsPendingAuth", TArray_FPendingClientAuth),
		("ServerAuthRetries", TArray_FServerAuthRetry),
		("ListenAuthBlobUID", c_int),
		("ListenAuthRetryCount", c_int),
	]

class  AAccessControl(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AAccessControl", AAccessControl_Data),
	]


class  AAdmin_Data(Structure):
	_fields_ = []

class  AAdmin(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AController", AController_Data),
		("APlayerController", APlayerController_Data),
		("AAdmin", AAdmin_Data),
	]


class  UIScaleBehavior_Data(Structure):
	_fields_ = []

class  UIScaleBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIScaleBehavior", UIScaleBehavior_Data),
	]


class  AApexDestructibleActorSpawnable_Data(Structure):
	_fields_ = []

class  AApexDestructibleActorSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AApexDestructibleActor", AApexDestructibleActor_Data),
		("AApexDestructibleActorSpawnable", AApexDestructibleActorSpawnable_Data),
	]


class  AEmitterSpawnable_Data(Structure):
	_fields_ = [
		("ParticleTemplate", POINTER(UParticleSystem)),
	]

class  AEmitterSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AEmitter", AEmitter_Data),
		("AEmitterSpawnable", AEmitterSpawnable_Data),
	]


class  AKAssetSpawnable_Data(Structure):
	_fields_ = []

class  AKAssetSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AKAsset", AKAsset_Data),
		("AKAssetSpawnable", AKAssetSpawnable_Data),
	]


class  UActorFactorySkeletalMeshCinematic_Data(Structure):
	_fields_ = []

class  UActorFactorySkeletalMeshCinematic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactorySkeletalMesh", UActorFactorySkeletalMesh_Data),
		("UActorFactorySkeletalMeshCinematic", UActorFactorySkeletalMeshCinematic_Data),
	]


class  UActorFactorySkeletalMeshMAT_Data(Structure):
	_fields_ = []

class  UActorFactorySkeletalMeshMAT(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UActorFactory", UActorFactory_Data),
		("UActorFactorySkeletalMesh", UActorFactorySkeletalMesh_Data),
		("UActorFactorySkeletalMeshMAT", UActorFactorySkeletalMeshMAT_Data),
	]


class  USeqEvent_Death_Data(Structure):
	_fields_ = []

class  USeqEvent_Death(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_Death", USeqEvent_Death_Data),
	]


class  USeqAct_ToggleGodMode_Data(Structure):
	_fields_ = []

class  USeqAct_ToggleGodMode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ToggleGodMode", USeqAct_ToggleGodMode_Data),
	]


class  USeqAct_ControlMovieTexture_Data(Structure):
	_fields_ = [
		("MovieTexture", POINTER(UTextureMovie)),
	]

class  USeqAct_ControlMovieTexture(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ControlMovieTexture", USeqAct_ControlMovieTexture_Data),
	]


class  UIParameterBehavior_Data(Structure):
	_fields_ = []

class  UIParameterBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIParameterBehavior", UIParameterBehavior_Data),
	]


class  ACoverReplicator_Data(Structure):
	_fields_ = [
		("CoverReplicationData", TArray_FCoverReplicationInfo),
	]

class  ACoverReplicator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AReplicationInfo", AReplicationInfo_Data),
		("ACoverReplicator", ACoverReplicator_Data),
	]


class  UGameMessage_Data(Structure):
	_fields_ = [
		("SwitchLevelMessage", FString),
		("LeftMessage", FString),
		("FailedTeamMessage", FString),
		("FailedPlaceMessage", FString),
		("FailedSpawnMessage", FString),
		("EnteredMessage", FString),
		("MaxedOutMessage", FString),
		("ArbitrationMessage", FString),
		("OvertimeMessage", FString),
		("GlobalNameChange", FString),
		("NewTeamMessage", FString),
		("NewTeamMessageTrailer", FString),
		("NoNameChange", FString),
		("VoteStarted", FString),
		("VotePassed", FString),
		("MustHaveStats", FString),
		("CantBeSpectator", FString),
		("CantBePlayer", FString),
		("BecameSpectator", FString),
		("NewPlayerMessage", FString),
		("KickWarning", FString),
		("NewSpecMessage", FString),
		("SpecEnteredMessage", FString),
	]

class  UGameMessage(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULocalMessage", ULocalMessage_Data),
		("UGameMessage", UGameMessage_Data),
	]


class  UDmgType_Suicided_Data(Structure):
	_fields_ = []

class  UDmgType_Suicided(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageType", UDamageType_Data),
		("UKillZDamageType", UKillZDamageType_Data),
		("UDmgType_Suicided", UDmgType_Suicided_Data),
	]


class  USeqAct_ToggleInput_Data(Structure):
	_fields_ = [
		("bToggleMovement", c_bool, 1),
		("bToggleTurning", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_ToggleInput(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_Toggle", USeqAct_Toggle_Data),
		("USeqAct_ToggleInput", USeqAct_ToggleInput_Data),
	]


class  USeqAct_ToggleHUD_Data(Structure):
	_fields_ = []

class  USeqAct_ToggleHUD(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ToggleHUD", USeqAct_ToggleHUD_Data),
	]


class  USeqAct_ForceFeedback_Data(Structure):
	_fields_ = [
		("FFWaveform", POINTER(UForceFeedbackWaveform)),
		("PredefinedWaveForm", POINTER(UClass)),
	]

class  USeqAct_ForceFeedback(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ForceFeedback", USeqAct_ForceFeedback_Data),
	]


class  USeqAct_ToggleCinematicMode_Data(Structure):
	_fields_ = [
		("bDisableMovement", c_bool, 1),
		("bDisableTurning", c_bool, 1),
		("bHidePlayer", c_bool, 1),
		("bDisableInput", c_bool, 1),
		("bHideHUD", c_bool, 1),
		("bEnableGodMode", c_bool, 1),
		("bEnableNoTarget", c_bool, 1),
		("bPauseDialog", c_bool, 1),
		("bCinematicSplitScreen", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_ToggleCinematicMode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ToggleCinematicMode", USeqAct_ToggleCinematicMode_Data),
	]


class  USeqAct_FlyThroughHasEnded_Data(Structure):
	_fields_ = []

class  USeqAct_FlyThroughHasEnded(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_FlyThroughHasEnded", USeqAct_FlyThroughHasEnded_Data),
	]


class  USeqAct_SetSoundMode_Data(Structure):
	_fields_ = [
		("SoundMode", POINTER(USoundMode)),
		("bTopPriority", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_SetSoundMode(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSoundMode", USeqAct_SetSoundMode_Data),
	]


class  UAnimNotify_PlayFaceFXAnim_Data(Structure):
	_fields_ = [
		("FaceFXAnimSetRef", POINTER(UFaceFXAnimSet)),
		("GroupName", FString),
		("AnimName", FString),
		("SoundCueToPlay", POINTER(USoundCue)),
		("AkEventToPlay", POINTER(UAkEvent)),
		("bOverridePlayingAnim", c_bool, 1),
		("", c_ulong, 0),
		("PlayFrequency", c_float),
	]

class  UAnimNotify_PlayFaceFXAnim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAnimNotify", UAnimNotify_Data),
		("UAnimNotify_Scripted", UAnimNotify_Scripted_Data),
		("UAnimNotify_PlayFaceFXAnim", UAnimNotify_PlayFaceFXAnim_Data),
	]


class  UBehavior_ChangeAllegiance_Data(Structure):
	_fields_ = [
		("bResetAllegiance", c_bool, 1),
		("", c_ulong, 0),
		("Allegiance", POINTER(UPawnAllegiance)),
	]

class  UBehavior_ChangeAllegiance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeAllegiance", UBehavior_ChangeAllegiance_Data),
	]


class  UBehavior_ChangeBoneVisibility_Data(Structure):
	_fields_ = [
		("Status", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("BoneName", FName),
	]

class  UBehavior_ChangeBoneVisibility(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeBoneVisibility", UBehavior_ChangeBoneVisibility_Data),
	]


class  UBehavior_ChangeCollision_Data(Structure):
	_fields_ = [
		("NewCollisionType", c_ubyte),
	]

class  UBehavior_ChangeCollision(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeCollision", UBehavior_ChangeCollision_Data),
	]


class  UBehavior_ChangeCollisionSize_Data(Structure):
	_fields_ = [
		("Radius", c_float),
		("Height", c_float),
	]

class  UBehavior_ChangeCollisionSize(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeCollisionSize", UBehavior_ChangeCollisionSize_Data),
	]


class  UBehavior_ChangeCounter_Data(Structure):
	_fields_ = [
		("CounterId", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CounterAdjustment", c_int),
		("bSetNewCounterValue", c_bool, 1),
		("bSetNewCounterTarget", c_bool, 1),
		("", c_ulong, 0),
		("NewCounterValue", c_int),
		("NewCounterTarget", c_int),
	]

class  UBehavior_ChangeCounter(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeCounter", UBehavior_ChangeCounter_Data),
	]


class  UBehavior_ChangeParticleSystemActiveState_Data(Structure):
	_fields_ = [
		("Status", c_ubyte),
	]

class  UBehavior_ChangeParticleSystemActiveState(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeParticleSystemActiveState", UBehavior_ChangeParticleSystemActiveState_Data),
	]


class  UIParticleSystemBehavior_Data(Structure):
	_fields_ = []

class  UIParticleSystemBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIParticleSystemBehavior", UIParticleSystemBehavior_Data),
	]


class  UBehavior_ChangeScale_Data(Structure):
	_fields_ = [
		("Scale", c_float),
	]

class  UBehavior_ChangeScale(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeScale", UBehavior_ChangeScale_Data),
	]


class  UBehavior_ChangeSpin_Data(Structure):
	_fields_ = [
		("bApplyRandomScaleToSpin", c_bool, 1),
		("bInheritInstigatorRotation", c_bool, 1),
		("", c_ulong, 0),
		("YawRate", c_int),
		("PitchRate", c_int),
		("RollRate", c_int),
	]

class  UBehavior_ChangeSpin(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeSpin", UBehavior_ChangeSpin_Data),
	]


class  UIBasicBehavior_Data(Structure):
	_fields_ = []

class  UIBasicBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIBasicBehavior", UIBasicBehavior_Data),
	]


class  UBehavior_ChangeVisibility_Data(Structure):
	_fields_ = [
		("Status", c_ubyte),
	]

class  UBehavior_ChangeVisibility(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ChangeVisibility", UBehavior_ChangeVisibility_Data),
	]


class  UBehavior_ClientConsoleCommand_Data(Structure):
	_fields_ = [
		("Command", FString),
	]

class  UBehavior_ClientConsoleCommand(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ClientConsoleCommand", UBehavior_ClientConsoleCommand_Data),
	]


class  UBehavior_ConsoleCommand_Data(Structure):
	_fields_ = [
		("Command", FString),
	]

class  UBehavior_ConsoleCommand(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ConsoleCommand", UBehavior_ConsoleCommand_Data),
	]


class  UBehavior_CustomAnimation_Data(Structure):
	_fields_ = [
		("Reaction", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("CustomAnimNodeName", FName),
		("AnimName", FName),
		("AnimDuration", c_float),
		("BlendInTime", c_float),
		("BlendOutTime", c_float),
		("AnimRate", c_float),
		("bLooping", c_bool, 1),
		("", c_ulong, 0),
	]

class  UBehavior_CustomAnimation(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_CustomAnimation", UBehavior_CustomAnimation_Data),
	]


class  UBehavior_Destroy_Data(Structure):
	_fields_ = []

class  UBehavior_Destroy(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_Destroy", UBehavior_Destroy_Data),
	]


class  UBehavior_FollowAllegiance_Data(Structure):
	_fields_ = [
		("Action", c_ubyte),
		("Unknown1", c_ubyte, 0x),
		("AllegianceParent", FBehaviorContextData),
	]

class  UBehavior_FollowAllegiance(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_FollowAllegiance", UBehavior_FollowAllegiance_Data),
	]


class  UBehavior_RandomlyRunBehaviors_Data(Structure):
	_fields_ = [
		("ProbabilityContext", FBehaviorContextData),
		("ProbabilityLowerBound", c_float),
		("ProbabilityUpperBound", c_float),
		("Possibilities", TArray_FIndependentSelectionData),
	]

class  UBehavior_RandomlyRunBehaviors(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_RandomlyRunBehaviors", UBehavior_RandomlyRunBehaviors_Data),
	]


class  UBehavior_RunBehaviorCollection_Data(Structure):
	_fields_ = [
		("CollectionDefinition", POINTER(UBehaviorCollectionDefinition)),
		("OverrideName", FName),
		("OverrideContext", FBehaviorContextData),
	]

class  UBehavior_RunBehaviorCollection(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_RunBehaviorCollection", UBehavior_RunBehaviorCollection_Data),
	]


class  UBehaviorCollectionDefinition_Data(Structure):
	_fields_ = [
		("Behaviors", TArray_UBehaviorBasePtr),
	]

class  UBehaviorCollectionDefinition(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UGBXDefinition", UGBXDefinition_Data),
		("UBehaviorCollectionDefinition", UBehaviorCollectionDefinition_Data),
	]


class  UBehavior_SetMaterialParameters_Data(Structure):
	_fields_ = [
		("AttributeContext", FBehaviorContextData),
		("MeshSection", c_int),
		("ScalarParameterValues", TArray_FScalarMaterialParameter),
		("VectorParameterValues", TArray_FVectorMaterialParameter),
		("TextureParameterValues", TArray_FTextureMaterialParameter),
	]

class  UBehavior_SetMaterialParameters(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_SetMaterialParameters", UBehavior_SetMaterialParameters_Data),
	]


class  UIMaterialBehavior_Data(Structure):
	_fields_ = []

class  UIMaterialBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIMaterialBehavior", UIMaterialBehavior_Data),
	]


class  UBehavior_SetParticleSystemParameters_Data(Structure):
	_fields_ = [
		("AttributeContext", FBehaviorContextData),
		("ScalarParameterValues", TArray_FScalarParticleSystemParameter),
		("VectorParameterValues", TArray_FVectorParticleSystemParameter),
		("ColorParameterValues", TArray_FColorParticleSystemParameter),
		("MaterialParameterValues", TArray_FMaterialParticleSystemParameter),
		("ActorParameterValues", TArray_FActorParticleSystemParameter),
	]

class  UBehavior_SetParticleSystemParameters(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_SetParticleSystemParameters", UBehavior_SetParticleSystemParameters_Data),
	]


class  UBehavior_SetPhysics_Data(Structure):
	_fields_ = [
		("Physics", c_ubyte),
		("BodyAction", c_ubyte),
		("SimulationAction", c_ubyte),
	]

class  UBehavior_SetPhysics(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_SetPhysics", UBehavior_SetPhysics_Data),
	]


class  UBehavior_SetSkelControlActive_Data(Structure):
	_fields_ = [
		("SkelControlName", FName),
		("bActive", c_bool, 1),
		("", c_ulong, 0),
	]

class  UBehavior_SetSkelControlActive(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_SetSkelControlActive", UBehavior_SetSkelControlActive_Data),
	]


class  UBehavior_ToggleVisibility_Data(Structure):
	_fields_ = []

class  UBehavior_ToggleVisibility(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UBehavior_ToggleVisibility", UBehavior_ToggleVisibility_Data),
	]


class  ABroadcastHandler_Data(Structure):
	_fields_ = [
		("SentText", c_int),
		("bMuteSpectators", c_bool, 1),
		("", c_ulong, 0),
	]

class  ABroadcastHandler(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("ABroadcastHandler", ABroadcastHandler_Data),
	]


class  AColorScaleVolume_Data(Structure):
	_fields_ = [
		("ColorScale", FVector),
		("InterpTime", c_float),
	]

class  AColorScaleVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AColorScaleVolume", AColorScaleVolume_Data),
	]


class  ADebugCameraHUD_Data(Structure):
	_fields_ = []

class  ADebugCameraHUD(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AHUD", AHUD_Data),
		("ADebugCameraHUD", ADebugCameraHUD_Data),
	]


class  UDebugCameraInput_Data(Structure):
	_fields_ = []

class  UDebugCameraInput(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UInteraction", UInteraction_Data),
		("UInput", UInput_Data),
		("UPlayerInput", UPlayerInput_Data),
		("UDebugCameraInput", UDebugCameraInput_Data),
	]


class  AVolumeTimer_Data(Structure):
	_fields_ = [
		("V", POINTER(APhysicsVolume)),
	]

class  AVolumeTimer(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AVolumeTimer", AVolumeTimer_Data),
	]


class  USeqAct_SetDamageInstigator_Data(Structure):
	_fields_ = [
		("DamageInstigator", POINTER(AActor)),
	]

class  USeqAct_SetDamageInstigator(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetDamageInstigator", USeqAct_SetDamageInstigator_Data),
	]


class  UDmgType_Crushed_Data(Structure):
	_fields_ = []

class  UDmgType_Crushed(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageType", UDamageType_Data),
		("UDmgType_Crushed", UDmgType_Crushed_Data),
	]


class  UDmgType_Fell_Data(Structure):
	_fields_ = []

class  UDmgType_Fell(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageType", UDamageType_Data),
		("UDmgType_Fell", UDmgType_Fell_Data),
	]


class  UDmgType_Telefragged_Data(Structure):
	_fields_ = []

class  UDmgType_Telefragged(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UDamageType", UDamageType_Data),
		("UDmgType_Telefragged", UDmgType_Telefragged_Data),
	]


class  ADynamicPhysicsVolume_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  ADynamicPhysicsVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APhysicsVolume", APhysicsVolume_Data),
		("ADynamicPhysicsVolume", ADynamicPhysicsVolume_Data),
	]


class  ADynamicSMActor_Spawnable_Data(Structure):
	_fields_ = []

class  ADynamicSMActor_Spawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("ADynamicSMActor_Spawnable", ADynamicSMActor_Spawnable_Data),
	]


class  ADynamicTriggerVolume_Data(Structure):
	_fields_ = [
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  ADynamicTriggerVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("ATriggerVolume", ATriggerVolume_Data),
		("ADynamicTriggerVolume", ADynamicTriggerVolume_Data),
	]


class  USeqAct_SetParticleSysParam_Data(Structure):
	_fields_ = [
		("InstanceParameters", TArray_FParticleSysParam),
		("bOverrideScalar", c_bool, 1),
		("", c_ulong, 0),
		("ScalarValue", c_float),
	]

class  USeqAct_SetParticleSysParam(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetParticleSysParam", USeqAct_SetParticleSysParam_Data),
	]


class  AExponentialHeightFog_Data(Structure):
	_fields_ = [
		("Component", POINTER(UExponentialHeightFogComponent)),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  AExponentialHeightFog(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AExponentialHeightFog", AExponentialHeightFog_Data),
	]


class  UFailedConnect_Data(Structure):
	_fields_ = [
		("FailMessage", FString * 4),
	]

class  UFailedConnect(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("ULocalMessage", ULocalMessage_Data),
		("UFailedConnect", UFailedConnect_Data),
	]


class  USeqEvent_PlayerSpawned_Data(Structure):
	_fields_ = [
		("SpawnPoint", POINTER(UObject)),
	]

class  USeqEvent_PlayerSpawned(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_PlayerSpawned", USeqEvent_PlayerSpawned_Data),
	]


class  UGameReplicationInfoAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UGameReplicationInfoAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UGameReplicationInfoAttributeContextResolver", UGameReplicationInfoAttributeContextResolver_Data),
	]


class  AHoldingAreaDestination_Data(Structure):
	_fields_ = []

class  AHoldingAreaDestination(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATeleporterDestination", ATeleporterDestination_Data),
		("AHoldingAreaDestination", AHoldingAreaDestination_Data),
	]


class  AHeightFog_Data(Structure):
	_fields_ = [
		("Component", POINTER(UHeightFogComponent)),
		("bEnabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  AHeightFog(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AHeightFog", AHeightFog_Data),
	]


class  UIChangeBehaviorSetStateBehavior_Data(Structure):
	_fields_ = []

class  UIChangeBehaviorSetStateBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIChangeBehaviorSetStateBehavior", UIChangeBehaviorSetStateBehavior_Data),
	]


class  UIDamageBehavior_Data(Structure):
	_fields_ = []

class  UIDamageBehavior(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UIDamageBehavior", UIDamageBehavior_Data),
	]


class  AInterpActor_ForCinematic_Data(Structure):
	_fields_ = []

class  AInterpActor_ForCinematic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ADynamicSMActor", ADynamicSMActor_Data),
		("AInterpActor", AInterpActor_Data),
		("AInterpActor_ForCinematic", AInterpActor_ForCinematic_Data),
	]


class  AMaterialInstanceTimeVaryingActor_Data(Structure):
	_fields_ = [
		("MatInst", POINTER(UMaterialInstanceTimeVarying)),
	]

class  AMaterialInstanceTimeVaryingActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AMaterialInstanceTimeVaryingActor", AMaterialInstanceTimeVaryingActor_Data),
	]


class  USeqAct_AssignController_Data(Structure):
	_fields_ = [
		("ControllerClass", POINTER(UClass)),
	]

class  USeqAct_AssignController(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_AssignController", USeqAct_AssignController_Data),
	]


class  UOnlineCommunityContentInterface_Data(Structure):
	_fields_ = [
		("__OnReadContentListComplete__Delegate", FScriptDelegate),
		("__OnReadFriendsContentListComplete__Delegate", FScriptDelegate),
		("__OnUploadContentComplete__Delegate", FScriptDelegate),
		("__OnDownloadContentComplete__Delegate", FScriptDelegate),
		("__OnGetContentPayloadComplete__Delegate", FScriptDelegate),
	]

class  UOnlineCommunityContentInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineCommunityContentInterface", UOnlineCommunityContentInterface_Data),
	]


class  UOnlineEventsInterface_Data(Structure):
	_fields_ = []

class  UOnlineEventsInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineEventsInterface", UOnlineEventsInterface_Data),
	]


class  UOnlinePlaylistGameTypeProvider_Data(Structure):
	_fields_ = [
		("PlaylistGameTypeName", FName),
		("DisplayName", FString),
		("Description", FString),
		("GameTypeId", c_int),
	]

class  UOnlinePlaylistGameTypeProvider(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
		("UOnlinePlaylistGameTypeProvider", UOnlinePlaylistGameTypeProvider_Data),
	]


class  UOnlineRecentPlayersList_Data(Structure):
	_fields_ = [
		("RecentPlayers", TArray_FUniqueNetId),
		("RecentParties", TArray_FRecentParty),
		("LastParty", FRecentParty),
		("MaxRecentPlayers", c_int),
		("MaxRecentParties", c_int),
		("RecentPlayersAddIndex", c_int),
		("RecentPartiesAddIndex", c_int),
		("CurrentPlayers", TArray_FCurrentPlayerMet),
	]

class  UOnlineRecentPlayersList(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UOnlineRecentPlayersList", UOnlineRecentPlayersList_Data),
	]


class  UOnlineSuppliedUIInterface_Data(Structure):
	_fields_ = [
		("__OnShowOnlineStatsUIComplete__Delegate", FScriptDelegate),
	]

class  UOnlineSuppliedUIInterface(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UInterface", UInterface_Data),
		("UOnlineSuppliedUIInterface", UOnlineSuppliedUIInterface_Data),
	]


class  UOwnerAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UOwnerAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UOwnerAttributeContextResolver", UOwnerAttributeContextResolver_Data),
	]


class  UParameterBehaviorBase_Data(Structure):
	_fields_ = [
		("ParameterName", FName),
		("SectionIndex", c_int),
	]

class  UParameterBehaviorBase(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UBehaviorBase", UBehaviorBase_Data),
		("UParameterBehaviorBase", UParameterBehaviorBase_Data),
	]


class  UParticleModuleForceFieldCylindrical_Data(Structure):
	_fields_ = []

class  UParticleModuleForceFieldCylindrical(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleForceFieldBase", UParticleModuleForceFieldBase_Data),
		("UParticleModuleForceFieldCylindrical", UParticleModuleForceFieldCylindrical_Data),
	]


class  UParticleModuleForceFieldGeneric_Data(Structure):
	_fields_ = []

class  UParticleModuleForceFieldGeneric(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleForceFieldBase", UParticleModuleForceFieldBase_Data),
		("UParticleModuleForceFieldGeneric", UParticleModuleForceFieldGeneric_Data),
	]


class  UParticleModuleForceFieldRadial_Data(Structure):
	_fields_ = []

class  UParticleModuleForceFieldRadial(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleForceFieldBase", UParticleModuleForceFieldBase_Data),
		("UParticleModuleForceFieldRadial", UParticleModuleForceFieldRadial_Data),
	]


class  UParticleModuleForceFieldTornado_Data(Structure):
	_fields_ = []

class  UParticleModuleForceFieldTornado(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UParticleModule", UParticleModule_Data),
		("UParticleModuleForceFieldBase", UParticleModuleForceFieldBase_Data),
		("UParticleModuleForceFieldTornado", UParticleModuleForceFieldTornado_Data),
	]


class  APathNode_Dynamic_Data(Structure):
	_fields_ = []

class  APathNode_Dynamic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("APathNode", APathNode_Data),
		("APathNode_Dynamic", APathNode_Dynamic_Data),
	]


class  USeqEvent_PickupStatusChange_Data(Structure):
	_fields_ = []

class  USeqEvent_PickupStatusChange(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_PickupStatusChange", USeqEvent_PickupStatusChange_Data),
	]


class  UProjectileAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UProjectileAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UProjectileAttributeContextResolver", UProjectileAttributeContextResolver_Data),
	]


class  ARadialBlurActor_Data(Structure):
	_fields_ = [
		("RadialBlur", POINTER(URadialBlurComponent)),
	]

class  ARadialBlurActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARadialBlurActor", ARadialBlurActor_Data),
	]


class  USeqAct_ToggleConstraintDrive_Data(Structure):
	_fields_ = [
		("bEnableAngularPositionDrive", c_bool, 1),
		("bEnableAngularVelocityDrive", c_bool, 1),
		("bEnableLinearPositionDrive", c_bool, 1),
		("bEnableLinearvelocityDrive", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqAct_ToggleConstraintDrive(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_ToggleConstraintDrive", USeqAct_ToggleConstraintDrive_Data),
	]


class  ARB_BSJointActor_Data(Structure):
	_fields_ = []

class  ARB_BSJointActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_ConstraintActor", ARB_ConstraintActor_Data),
		("ARB_BSJointActor", ARB_BSJointActor_Data),
	]


class  ARB_ConstraintActorSpawnable_Data(Structure):
	_fields_ = []

class  ARB_ConstraintActorSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_ConstraintActor", ARB_ConstraintActor_Data),
		("ARB_ConstraintActorSpawnable", ARB_ConstraintActorSpawnable_Data),
	]


class  ARB_HingeActor_Data(Structure):
	_fields_ = []

class  ARB_HingeActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_ConstraintActor", ARB_ConstraintActor_Data),
		("ARB_HingeActor", ARB_HingeActor_Data),
	]


class  ARB_PrismaticActor_Data(Structure):
	_fields_ = []

class  ARB_PrismaticActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_ConstraintActor", ARB_ConstraintActor_Data),
		("ARB_PrismaticActor", ARB_PrismaticActor_Data),
	]


class  ARB_PulleyJointActor_Data(Structure):
	_fields_ = []

class  ARB_PulleyJointActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ARigidBodyBase", ARigidBodyBase_Data),
		("ARB_ConstraintActor", ARB_ConstraintActor_Data),
		("ARB_PulleyJointActor", ARB_PulleyJointActor_Data),
	]


class  AReverbVolumeToggleable_Data(Structure):
	_fields_ = []

class  AReverbVolumeToggleable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("AReverbVolume", AReverbVolume_Data),
		("AReverbVolumeToggleable", AReverbVolumeToggleable_Data),
	]


class  USeqAct_AddRemoveFaceFXAnimSet_Data(Structure):
	_fields_ = [
		("FaceFXAnimSets", TArray_UFaceFXAnimSetPtr),
	]

class  USeqAct_AddRemoveFaceFXAnimSet(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_AddRemoveFaceFXAnimSet", USeqAct_AddRemoveFaceFXAnimSet_Data),
	]


class  USeqAct_AIAbortMoveToActor_Data(Structure):
	_fields_ = []

class  USeqAct_AIAbortMoveToActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_AIAbortMoveToActor", USeqAct_AIAbortMoveToActor_Data),
	]


class  USeqAct_MITV_Activate_Data(Structure):
	_fields_ = [
		("DurationOfMITV", c_float),
	]

class  USeqAct_MITV_Activate(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_MITV_Activate", USeqAct_MITV_Activate_Data),
	]


class  USeqAct_SetSkelControlTarget_Data(Structure):
	_fields_ = [
		("SkelControlName", FName),
		("TargetActors", TArray_UObjectPtr),
	]

class  USeqAct_SetSkelControlTarget(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSkelControlTarget", USeqAct_SetSkelControlTarget_Data),
	]


class  USeqAct_SetVector_Data(Structure):
	_fields_ = [
		("DefaultValue", FVector),
	]

class  USeqAct_SetVector(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_SetSequenceVariable", USeqAct_SetSequenceVariable_Data),
		("USeqAct_SetVector", USeqAct_SetVector_Data),
	]


class  USeqAct_UpdatePhysBonesFromAnim_Data(Structure):
	_fields_ = []

class  USeqAct_UpdatePhysBonesFromAnim(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceAction", USequenceAction_Data),
		("USeqAct_UpdatePhysBonesFromAnim", USeqAct_UpdatePhysBonesFromAnim_Data),
	]


class  USeqEvent_AIReachedRouteActor_Data(Structure):
	_fields_ = []

class  USeqEvent_AIReachedRouteActor(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_AIReachedRouteActor", USeqEvent_AIReachedRouteActor_Data),
	]


class  USeqEvent_LOS_Data(Structure):
	_fields_ = [
		("ScreenCenterDistance", c_float),
		("TriggerDistance", c_float),
		("bCheckForObstructions", c_bool, 1),
		("", c_ulong, 0),
	]

class  USeqEvent_LOS(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceOp", USequenceOp_Data),
		("USequenceEvent", USequenceEvent_Data),
		("USeqEvent_LOS", USeqEvent_LOS_Data),
	]


class  USeqVar_Byte_Data(Structure):
	_fields_ = []

class  USeqVar_Byte(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Byte", USeqVar_Byte_Data),
	]


class  USeqVar_Name_Data(Structure):
	_fields_ = []

class  USeqVar_Name(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Name", USeqVar_Name_Data),
	]


class  USeqVar_Union_Data(Structure):
	_fields_ = []

class  USeqVar_Union(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("USequenceObject", USequenceObject_Data),
		("USequenceVariable", USequenceVariable_Data),
		("USeqVar_Union", USeqVar_Union_Data),
	]


class  ASkeletalMeshActorMATSpawnable_Data(Structure):
	_fields_ = []

class  ASkeletalMeshActorMATSpawnable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
		("ASkeletalMeshCinematicActor", ASkeletalMeshCinematicActor_Data),
		("ASkeletalMeshActorMAT", ASkeletalMeshActorMAT_Data),
		("ASkeletalMeshActorMATSpawnable", ASkeletalMeshActorMATSpawnable_Data),
	]


class  ASkeletalMeshActorMATWalkable_Data(Structure):
	_fields_ = []

class  ASkeletalMeshActorMATWalkable(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ASkeletalMeshActor", ASkeletalMeshActor_Data),
		("ASkeletalMeshCinematicActor", ASkeletalMeshCinematicActor_Data),
		("ASkeletalMeshActorMAT", ASkeletalMeshActorMAT_Data),
		("ASkeletalMeshActorMATWalkable", ASkeletalMeshActorMATWalkable_Data),
	]


class  ATrigger_Dynamic_Data(Structure):
	_fields_ = []

class  ATrigger_Dynamic(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATrigger", ATrigger_Data),
		("ATrigger_Dynamic", ATrigger_Dynamic_Data),
	]


class  ATrigger_LOS_Data(Structure):
	_fields_ = [
		("PCsWithLOS", TArray_APlayerControllerPtr),
	]

class  ATrigger_LOS(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATrigger", ATrigger_Data),
		("ATrigger_LOS", ATrigger_LOS_Data),
	]


class  ATriggeredPath_Data(Structure):
	_fields_ = [
		("bOpen", c_bool, 1),
		("", c_ulong, 0),
		("MyTrigger", POINTER(AActor)),
	]

class  ATriggeredPath(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ANavigationPoint", ANavigationPoint_Data),
		("ATriggeredPath", ATriggeredPath_Data),
	]


class  ATriggerStreamingLevel_Data(Structure):
	_fields_ = [
		("Levels", TArray_FLevelStreamingData),
	]

class  ATriggerStreamingLevel(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ATrigger", ATrigger_Data),
		("ATriggerStreamingLevel", ATriggerStreamingLevel_Data),
	]


class  UUICharacterSummary_Data(Structure):
	_fields_ = [
		("ClassPathName", FString),
		("CharacterName", FString),
		("CharacterBio", FString),
		("bIsDisabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  UUICharacterSummary(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
		("UUICharacterSummary", UUICharacterSummary_Data),
	]


class  UUIGameInfoSummary_Data(Structure):
	_fields_ = [
		("ClassName", FString),
		("GameAcronym", FString),
		("MapPrefix", FString),
		("bIsTeamGame", c_bool, 1),
		("bIsDisabled", c_bool, 1),
		("", c_ulong, 0),
		("GameSettingsClassName", FString),
		("GameName", FString),
		("Description", FString),
	]

class  UUIGameInfoSummary(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
		("UUIGameInfoSummary", UUIGameInfoSummary_Data),
	]


class  UUIWeaponSummary_Data(Structure):
	_fields_ = [
		("ClassPathName", FString),
		("FriendlyName", FString),
		("WeaponDescription", FString),
		("bIsDisabled", c_bool, 1),
		("", c_ulong, 0),
	]

class  UUIWeaponSummary(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UUIRoot", UUIRoot_Data),
		("UUIDataProvider", UUIDataProvider_Data),
		("UUIPropertyDataProvider", UUIPropertyDataProvider_Data),
		("UUIResourceDataProvider", UUIResourceDataProvider_Data),
		("UUIWeaponSummary", UUIWeaponSummary_Data),
	]


class  UVehicleAttributeContextResolver_Data(Structure):
	_fields_ = []

class  UVehicleAttributeContextResolver(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("UAttributeContextResolver", UAttributeContextResolver_Data),
		("UVehicleAttributeContextResolver", UVehicleAttributeContextResolver_Data),
	]


class  AWaterVolume_Data(Structure):
	_fields_ = [
		("EntrySound", POINTER(USoundCue)),
		("EntryActor", POINTER(UClass)),
		("ExitSound", POINTER(USoundCue)),
		("ExitActor", POINTER(UClass)),
	]

class  AWaterVolume(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("ABrush", ABrush_Data),
		("AVolume", AVolume_Data),
		("APhysicsVolume", APhysicsVolume_Data),
		("AWaterVolume", AWaterVolume_Data),
	]


class  AWindDirectionalSource_Data(Structure):
	_fields_ = [
		("Component", POINTER(UWindDirectionalSourceComponent)),
	]

class  AWindDirectionalSource(Structure):
	_fields_ = [
		("UObject", UObject_Data),
		("AActor", AActor_Data),
		("AInfo", AInfo_Data),
		("AWindDirectionalSource", AWindDirectionalSource_Data),
	]


BL2SDK.g_loadedClasses += [("UIWorldBody", 143, "UInterface")]
BL2SDK.g_loadedClasses += [("AActor", 145, "UObject")]
BL2SDK.g_loadedClasses += [("AInfo", 147, "AActor")]
BL2SDK.g_loadedClasses += [("AZoneInfo", 149, "AInfo")]
BL2SDK.g_loadedClasses += [("AWorldInfo", 151, "AZoneInfo")]
BL2SDK.g_loadedClasses += [("UDownloadableContentEnumerator", 153, "UObject")]
BL2SDK.g_loadedClasses += [("UDownloadableContentManager", 155, "UObject")]
BL2SDK.g_loadedClasses += [("UDownloadableContentOfferEnumerator", 157, "UObject")]
BL2SDK.g_loadedClasses += [("UEngine", 159, "USubsystem")]
BL2SDK.g_loadedClasses += [("UGameEngine", 161, "UEngine")]
BL2SDK.g_loadedClasses += [("UInGameAdManager", 163, "UObject")]
BL2SDK.g_loadedClasses += [("UEngineBaseTypes", 165, "UObject")]
BL2SDK.g_loadedClasses += [("ABrush", 167, "AActor")]
BL2SDK.g_loadedClasses += [("ABrushShape", 169, "ABrush")]
BL2SDK.g_loadedClasses += [("AVolume", 171, "ABrush")]
BL2SDK.g_loadedClasses += [("ABlockingVolume", 173, "AVolume")]
BL2SDK.g_loadedClasses += [("ADynamicBlockingVolume", 175, "ABlockingVolume")]
BL2SDK.g_loadedClasses += [("ACullDistanceVolume", 177, "AVolume")]
BL2SDK.g_loadedClasses += [("ALevelGridVolume", 179, "AVolume")]
BL2SDK.g_loadedClasses += [("ALevelStreamingVolume", 181, "AVolume")]
BL2SDK.g_loadedClasses += [("ALightmassCharacterIndirectDetailVolume", 183, "AVolume")]
BL2SDK.g_loadedClasses += [("ALightmassImportanceVolume", 185, "AVolume")]
BL2SDK.g_loadedClasses += [("AMassiveLODOverrideVolume", 187, "AVolume")]
BL2SDK.g_loadedClasses += [("ANavMeshBoundsVolume", 189, "AVolume")]
BL2SDK.g_loadedClasses += [("APathBlockingVolume", 191, "AVolume")]
BL2SDK.g_loadedClasses += [("APhysicsVolume", 193, "AVolume")]
BL2SDK.g_loadedClasses += [("ADefaultPhysicsVolume", 195, "APhysicsVolume")]
BL2SDK.g_loadedClasses += [("AGravityVolume", 197, "APhysicsVolume")]
BL2SDK.g_loadedClasses += [("ALadderVolume", 199, "APhysicsVolume")]
BL2SDK.g_loadedClasses += [("APortalVolume", 201, "AVolume")]
BL2SDK.g_loadedClasses += [("APostProcessVolume", 203, "AVolume")]
BL2SDK.g_loadedClasses += [("APrecomputedVisibilityOverrideVolume", 205, "AVolume")]
BL2SDK.g_loadedClasses += [("APrecomputedVisibilityVolume", 207, "AVolume")]
BL2SDK.g_loadedClasses += [("AReverbVolume", 209, "AVolume")]
BL2SDK.g_loadedClasses += [("AShadowRelevanceVolume", 211, "AVolume")]
BL2SDK.g_loadedClasses += [("ATriggerVolume", 213, "AVolume")]
BL2SDK.g_loadedClasses += [("ADynamicSMActor", 215, "AActor")]
BL2SDK.g_loadedClasses += [("AInterpActor", 217, "ADynamicSMActor")]
BL2SDK.g_loadedClasses += [("AEmitterPool", 219, "AActor")]
BL2SDK.g_loadedClasses += [("AGBXNavMesh", 221, "AActor")]
BL2SDK.g_loadedClasses += [("AHUD", 223, "AActor")]
BL2SDK.g_loadedClasses += [("AIDestructibleObject", 225, "AActor")]
BL2SDK.g_loadedClasses += [("AAutoTestManager", 227, "AInfo")]
BL2SDK.g_loadedClasses += [("ACoverGroup", 229, "AInfo")]
BL2SDK.g_loadedClasses += [("AFileWriter", 231, "AInfo")]
BL2SDK.g_loadedClasses += [("AFileLog", 233, "AFileWriter")]
BL2SDK.g_loadedClasses += [("AGameInfo", 235, "AInfo")]
BL2SDK.g_loadedClasses += [("AMutator", 237, "AInfo")]
BL2SDK.g_loadedClasses += [("APotentialClimbWatcher", 239, "AInfo")]
BL2SDK.g_loadedClasses += [("ARoute", 241, "AInfo")]
BL2SDK.g_loadedClasses += [("AWindPointSource", 243, "AInfo")]
BL2SDK.g_loadedClasses += [("AKeypoint", 245, "AActor")]
BL2SDK.g_loadedClasses += [("ATargetPoint", 247, "AKeypoint")]
BL2SDK.g_loadedClasses += [("ALevelLandmark", 249, "AActor")]
BL2SDK.g_loadedClasses += [("APersistentTransitionLandmark", 251, "ALevelLandmark")]
BL2SDK.g_loadedClasses += [("AMaterialInstanceActor", 253, "AActor")]
BL2SDK.g_loadedClasses += [("AMatineeActor", 255, "AActor")]
BL2SDK.g_loadedClasses += [("ANavigationPoint", 257, "AActor")]
BL2SDK.g_loadedClasses += [("ACoverLink", 259, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("ADoorMarker", 261, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("ADynamicAnchor", 263, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("ALadder", 265, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("AAutoLadder", 267, "ALadder")]
BL2SDK.g_loadedClasses += [("ALiftCenter", 269, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("ALiftExit", 271, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("APathNode", 273, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("AVolumePathNode", 275, "APathNode")]
BL2SDK.g_loadedClasses += [("APickupFactory", 277, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("APlayerStart", 279, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("APortalMarker", 281, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("APylon", 283, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("AAISwitchablePylon", 285, "APylon")]
BL2SDK.g_loadedClasses += [("ADynamicPylon", 287, "APylon")]
BL2SDK.g_loadedClasses += [("ATeleporter", 289, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("ANote", 291, "AActor")]
BL2SDK.g_loadedClasses += [("AProjectile", 293, "AActor")]
BL2SDK.g_loadedClasses += [("ARigidBodyBase", 295, "AActor")]
BL2SDK.g_loadedClasses += [("ASceneCaptureActor", 297, "AActor")]
BL2SDK.g_loadedClasses += [("ASceneCapture2DActor", 299, "ASceneCaptureActor")]
BL2SDK.g_loadedClasses += [("ASceneCaptureCubeMapActor", 301, "ASceneCaptureActor")]
BL2SDK.g_loadedClasses += [("ASceneCaptureReflectActor", 303, "ASceneCaptureActor")]
BL2SDK.g_loadedClasses += [("ASceneCapturePortalActor", 305, "ASceneCaptureReflectActor")]
BL2SDK.g_loadedClasses += [("APortalTeleporter", 307, "ASceneCapturePortalActor")]
BL2SDK.g_loadedClasses += [("AStaticMeshActorBase", 309, "AActor")]
BL2SDK.g_loadedClasses += [("ABlockingMeshCollectionActor", 311, "AStaticMeshActorBase")]
BL2SDK.g_loadedClasses += [("AStaticMeshActor", 313, "AStaticMeshActorBase")]
BL2SDK.g_loadedClasses += [("AStaticMeshCollectionActor", 315, "AStaticMeshActorBase")]
BL2SDK.g_loadedClasses += [("AStaticMeshActorBasedOnExtremeContent", 317, "AActor")]
BL2SDK.g_loadedClasses += [("ATeleporterDestination", 319, "AActor")]
BL2SDK.g_loadedClasses += [("ATrigger", 321, "AActor")]
BL2SDK.g_loadedClasses += [("ATrigger_PawnsOnly", 323, "ATrigger")]
BL2SDK.g_loadedClasses += [("UActorComponent", 325, "UComponent")]
BL2SDK.g_loadedClasses += [("UAkComponent", 327, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UAudioComponent", 329, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UHeightFogComponent", 331, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UPrimitiveComponent", 333, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UArrowComponent", 335, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UBrushComponent", 337, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UCameraConeComponent", 339, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UCylinderComponent", 341, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("USphereComponent", 343, "UCylinderComponent")]
BL2SDK.g_loadedClasses += [("UDrawBoxComponent", 345, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawCapsuleComponent", 347, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawConeComponent", 349, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawCylinderComponent", 351, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawFrustumComponent", 353, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawQuadComponent", 355, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawSphereComponent", 357, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDrawPylonRadiusComponent", 359, "UDrawSphereComponent")]
BL2SDK.g_loadedClasses += [("UDrawSoundRadiusComponent", 361, "UDrawSphereComponent")]
BL2SDK.g_loadedClasses += [("UGBXNavMeshRenderingComponent", 363, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("ULevelGridVolumeRenderingComponent", 365, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("ULineBatchComponent", 367, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UModelComponent", 369, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("USocketComponent", 371, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UHomingTargetComponent", 373, "USocketComponent")]
BL2SDK.g_loadedClasses += [("USpriteComponent", 375, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("USpriteRTTComponent", 377, "USpriteComponent")]
BL2SDK.g_loadedClasses += [("URadialBlurComponent", 379, "UActorComponent")]
BL2SDK.g_loadedClasses += [("USceneCaptureComponent", 381, "UActorComponent")]
BL2SDK.g_loadedClasses += [("USceneCapture2DComponent", 383, "USceneCaptureComponent")]
BL2SDK.g_loadedClasses += [("USceneCapture2DHitMaskComponent", 385, "USceneCaptureComponent")]
BL2SDK.g_loadedClasses += [("USceneCaptureCubeMapComponent", 387, "USceneCaptureComponent")]
BL2SDK.g_loadedClasses += [("USceneCapturePortalComponent", 389, "USceneCaptureComponent")]
BL2SDK.g_loadedClasses += [("USceneCaptureReflectComponent", 391, "USceneCaptureComponent")]
BL2SDK.g_loadedClasses += [("UWindDirectionalSourceComponent", 393, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UWindPointSourceComponent", 395, "UWindDirectionalSourceComponent")]
BL2SDK.g_loadedClasses += [("UActorFactory", 397, "UObject")]
BL2SDK.g_loadedClasses += [("UActorFactoryActor", 399, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryAI", 401, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryApexDestructible", 403, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryArchetype", 405, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryCoverLink", 407, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryDominantDirectionalLight", 409, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryDominantDirectionalLightMovable", 411, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryDynamicSM", 413, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryMover", 415, "UActorFactoryDynamicSM")]
BL2SDK.g_loadedClasses += [("UActorFactoryRigidBody", 417, "UActorFactoryDynamicSM")]
BL2SDK.g_loadedClasses += [("UActorFactoryEmitter", 419, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryLensFlare", 421, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryLight", 423, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryPathNode", 425, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryPhysicsAsset", 427, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryPlayerStart", 429, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryPylon", 431, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactorySkeletalMesh", 433, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryStaticMesh", 435, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryTrigger", 437, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryVehicle", 439, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryCustomPropertyEditorDelegate", 441, "UObject")]
BL2SDK.g_loadedClasses += [("UAkAudioDevice", 443, "USubsystem")]
BL2SDK.g_loadedClasses += [("UAkBaseSoundObject", 445, "UObject")]
BL2SDK.g_loadedClasses += [("USoundCue", 447, "UAkBaseSoundObject")]
BL2SDK.g_loadedClasses += [("UAkObject", 449, "UObject")]
BL2SDK.g_loadedClasses += [("UAkBank", 451, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkDialogueEvent", 453, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkEffect", 455, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkEvent", 457, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkRtpc", 459, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkState", 461, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkStateGroup", 463, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkSwitch", 465, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkSwitchGroup", 467, "UAkObject")]
BL2SDK.g_loadedClasses += [("UAkTrigger", 469, "UAkObject")]
BL2SDK.g_loadedClasses += [("UBookMark", 471, "UObject")]
BL2SDK.g_loadedClasses += [("UBookMark2D", 473, "UObject")]
BL2SDK.g_loadedClasses += [("UKismetBookMark", 475, "UBookMark2D")]
BL2SDK.g_loadedClasses += [("UCanvas", 477, "UObject")]
BL2SDK.g_loadedClasses += [("UChannel", 479, "UObject")]
BL2SDK.g_loadedClasses += [("UActorChannel", 481, "UChannel")]
BL2SDK.g_loadedClasses += [("UControlChannel", 483, "UChannel")]
BL2SDK.g_loadedClasses += [("UFileChannel", 485, "UChannel")]
BL2SDK.g_loadedClasses += [("UVoiceChannel", 487, "UChannel")]
BL2SDK.g_loadedClasses += [("AController", 489, "AActor")]
BL2SDK.g_loadedClasses += [("APlayerController", 491, "AController")]
BL2SDK.g_loadedClasses += [("UCheatManager", 493, "UObject")]
BL2SDK.g_loadedClasses += [("UClient", 495, "UObject")]
BL2SDK.g_loadedClasses += [("UClipPadEntry", 501, "UObject")]
BL2SDK.g_loadedClasses += [("UCodecMovie", 503, "UObject")]
BL2SDK.g_loadedClasses += [("UCodecMovieBink", 505, "UCodecMovie")]
BL2SDK.g_loadedClasses += [("UCodecMovieFallback", 507, "UCodecMovie")]
BL2SDK.g_loadedClasses += [("UCurveEdPresetCurve", 509, "UObject")]
BL2SDK.g_loadedClasses += [("UCustomPropertyItemHandler", 511, "UInterface")]
BL2SDK.g_loadedClasses += [("UDamageAdjuster", 513, "UObject")]
BL2SDK.g_loadedClasses += [("UDamagePipeline", 515, "UObject")]
BL2SDK.g_loadedClasses += [("UDamageType", 517, "UObject")]
BL2SDK.g_loadedClasses += [("UKillZDamageType", 519, "UDamageType")]
BL2SDK.g_loadedClasses += [("UDistributionFloatConstant", 521, "UDistributionFloat")]
BL2SDK.g_loadedClasses += [("UDistributionFloatParameterBase", 523, "UDistributionFloatConstant")]
BL2SDK.g_loadedClasses += [("UDistributionFloatConstantCurve", 525, "UDistributionFloat")]
BL2SDK.g_loadedClasses += [("UDistributionFloatUniform", 527, "UDistributionFloat")]
BL2SDK.g_loadedClasses += [("UDistributionFloatUniformCurve", 529, "UDistributionFloat")]
BL2SDK.g_loadedClasses += [("UDistributionVectorConstant", 531, "UDistributionVector")]
BL2SDK.g_loadedClasses += [("UDistributionVectorParameterBase", 533, "UDistributionVectorConstant")]
BL2SDK.g_loadedClasses += [("UDistributionVectorConstantCurve", 535, "UDistributionVector")]
BL2SDK.g_loadedClasses += [("UDistributionVectorUniform", 537, "UDistributionVector")]
BL2SDK.g_loadedClasses += [("UDistributionVectorUniformCurve", 539, "UDistributionVector")]
BL2SDK.g_loadedClasses += [("UDownload", 541, "UObject")]
BL2SDK.g_loadedClasses += [("UChannelDownload", 543, "UDownload")]
BL2SDK.g_loadedClasses += [("UEdCoordSystem", 545, "UObject")]
BL2SDK.g_loadedClasses += [("UEditorLinkSelectionInterface", 547, "UInterface")]
BL2SDK.g_loadedClasses += [("UEngineTypes", 549, "UObject")]
BL2SDK.g_loadedClasses += [("UFacebookIntegration", 551, "UObject")]
BL2SDK.g_loadedClasses += [("UFaceFXAnimSet", 553, "UObject")]
BL2SDK.g_loadedClasses += [("UFaceFXAsset", 555, "UObject")]
BL2SDK.g_loadedClasses += [("UFont", 557, "UObject")]
BL2SDK.g_loadedClasses += [("UMultiFont", 559, "UFont")]
BL2SDK.g_loadedClasses += [("UFontImportOptions", 561, "UObject")]
BL2SDK.g_loadedClasses += [("UForceFeedbackManager", 563, "UObject")]
BL2SDK.g_loadedClasses += [("UForceFeedbackWaveform", 565, "UObject")]
BL2SDK.g_loadedClasses += [("UGameplayEvents", 567, "UObject")]
BL2SDK.g_loadedClasses += [("UGameplayEventsReader", 569, "UGameplayEvents")]
BL2SDK.g_loadedClasses += [("UGameplayEventsWriter", 571, "UGameplayEvents")]
BL2SDK.g_loadedClasses += [("UGameplayEventsHandler", 573, "UObject")]
BL2SDK.g_loadedClasses += [("UGameViewportClient", 575, "UObject")]
BL2SDK.g_loadedClasses += [("UGBXCrossLevelReferenceContainer", 577, "UObject")]
BL2SDK.g_loadedClasses += [("UGBXDefinition", 579, "UObject")]
BL2SDK.g_loadedClasses += [("UBaseHitRegionDefinition", 581, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UDamageTypeDefinition", 583, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UEngineInteractionIconDefinition", 585, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UPawnAllegiance", 587, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UPawnInteractionDefinition", 589, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UGBXNavMeshPathModifier", 591, "UObject")]
BL2SDK.g_loadedClasses += [("UGBXNavMeshPathModifier_Simplify", 593, "UGBXNavMeshPathModifier")]
BL2SDK.g_loadedClasses += [("UGBXNavMeshPathModifier_SmoothTurns", 595, "UGBXNavMeshPathModifier")]
BL2SDK.g_loadedClasses += [("UGearboxEngineGlobals", 597, "UObject")]
BL2SDK.g_loadedClasses += [("UGenericParamListStatEntry", 599, "UObject")]
BL2SDK.g_loadedClasses += [("UGuidCache", 601, "UObject")]
BL2SDK.g_loadedClasses += [("UIAnimBehavior", 603, "UInterface")]
BL2SDK.g_loadedClasses += [("UIAttributeSlotEffectProvider", 605, "UInterface")]
BL2SDK.g_loadedClasses += [("UIBalancedActor", 607, "UInterface")]
BL2SDK.g_loadedClasses += [("UIBodyCompositionInstance", 609, "UInterface")]
BL2SDK.g_loadedClasses += [("UIBodyInfoProvider", 611, "UInterface")]
BL2SDK.g_loadedClasses += [("UIDamageCauser", 613, "UInterface")]
BL2SDK.g_loadedClasses += [("UIDialogBox", 615, "UInterface")]
BL2SDK.g_loadedClasses += [("UIFaceFXActor", 617, "UInterface")]
BL2SDK.g_loadedClasses += [("UIGBXNavMeshBuildEvents", 619, "UInterface")]
BL2SDK.g_loadedClasses += [("UIGBXNavMeshSeed", 621, "UInterface")]
BL2SDK.g_loadedClasses += [("UIGBXNavMeshSpecialMove", 623, "UInterface")]
BL2SDK.g_loadedClasses += [("UIKilledBehavior", 625, "UInterface")]
BL2SDK.g_loadedClasses += [("UIniLocPatcher", 627, "UObject")]
BL2SDK.g_loadedClasses += [("UInterface_NavigationHandle", 629, "UInterface")]
BL2SDK.g_loadedClasses += [("UInterface_Speaker", 631, "UInterface")]
BL2SDK.g_loadedClasses += [("UInterpCurveEdSetup", 633, "UObject")]
BL2SDK.g_loadedClasses += [("UInterpTrack", 635, "UObject")]
BL2SDK.g_loadedClasses += [("UIResourcePoolProvider", 637, "UInterface")]
BL2SDK.g_loadedClasses += [("UISpawnActor", 639, "UInterface")]
BL2SDK.g_loadedClasses += [("UISpecialOcclusionProvider", 641, "UInterface")]
BL2SDK.g_loadedClasses += [("UITargetable", 643, "UInterface")]
BL2SDK.g_loadedClasses += [("UJsonObject", 645, "UObject")]
BL2SDK.g_loadedClasses += [("UKMeshProps", 647, "UObject")]
BL2SDK.g_loadedClasses += [("ULevelBase", 649, "UObject")]
BL2SDK.g_loadedClasses += [("ULevel", 651, "ULevelBase")]
BL2SDK.g_loadedClasses += [("UPendingLevel", 655, "ULevelBase")]
BL2SDK.g_loadedClasses += [("UDemoPlayPendingLevel", 657, "UPendingLevel")]
BL2SDK.g_loadedClasses += [("UNetPendingLevel", 659, "UPendingLevel")]
BL2SDK.g_loadedClasses += [("ULevelStreaming", 661, "UObject")]
BL2SDK.g_loadedClasses += [("ULevelStreamingAlwaysLoaded", 663, "ULevelStreaming")]
BL2SDK.g_loadedClasses += [("ULevelStreamingDistance", 665, "ULevelStreaming")]
BL2SDK.g_loadedClasses += [("ULevelStreamingKismet", 667, "ULevelStreaming")]
BL2SDK.g_loadedClasses += [("ULevelStreamingPersistent", 669, "ULevelStreaming")]
BL2SDK.g_loadedClasses += [("ULightmappedSurfaceCollection", 671, "UObject")]
BL2SDK.g_loadedClasses += [("ULightmassPrimitiveSettingsObject", 673, "UObject")]
BL2SDK.g_loadedClasses += [("ULine", 675, "UObject")]
BL2SDK.g_loadedClasses += [("ULineData", 677, "UObject")]
BL2SDK.g_loadedClasses += [("ULineSegment", 679, "UObject")]
BL2SDK.g_loadedClasses += [("UMapInfo", 681, "UObject")]
BL2SDK.g_loadedClasses += [("USurface", 683, "UObject")]
BL2SDK.g_loadedClasses += [("UMaterialInterface", 685, "USurface")]
BL2SDK.g_loadedClasses += [("UMaterial", 687, "UMaterialInterface")]
BL2SDK.g_loadedClasses += [("UMaterialExpression", 689, "UObject")]
BL2SDK.g_loadedClasses += [("UModel", 691, "UObject")]
BL2SDK.g_loadedClasses += [("UMusicTrackDataStructures", 693, "UObject")]
BL2SDK.g_loadedClasses += [("UNavigationMeshBase", 695, "UObject")]
BL2SDK.g_loadedClasses += [("UNetDriver", 697, "USubsystem")]
BL2SDK.g_loadedClasses += [("UDemoRecDriver", 716, "UNetDriver")]
BL2SDK.g_loadedClasses += [("UObjectReferencer", 722, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineSubsystem", 724, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineAuthInterfaceBaseImpl", 726, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineMatchmakingStats", 728, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlinePlayerStorage", 730, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineProfileSettings", 732, "UOnlinePlayerStorage")]
BL2SDK.g_loadedClasses += [("UOnlineStats", 734, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineStatsRead", 736, "UOnlineStats")]
BL2SDK.g_loadedClasses += [("UOnlineStatsWrite", 738, "UOnlineStats")]
BL2SDK.g_loadedClasses += [("UPackageMapLevel", 740, "UPackageMap")]
BL2SDK.g_loadedClasses += [("UPackageMapSeekFree", 742, "UPackageMapLevel")]
BL2SDK.g_loadedClasses += [("UPatchScriptCommandlet", 744, "UCommandlet")]
BL2SDK.g_loadedClasses += [("UPlayer", 746, "UObject")]
BL2SDK.g_loadedClasses += [("ULocalPlayer", 748, "UPlayer")]
BL2SDK.g_loadedClasses += [("UNetConnection", 750, "UPlayer")]
BL2SDK.g_loadedClasses += [("UChildConnection", 754, "UNetConnection")]
BL2SDK.g_loadedClasses += [("UDemoRecConnection", 757, "UNetConnection")]
BL2SDK.g_loadedClasses += [("UPolys", 759, "UObject")]
BL2SDK.g_loadedClasses += [("UPostProcessChain", 761, "UObject")]
BL2SDK.g_loadedClasses += [("UPostProcessEffect", 763, "UObject")]
BL2SDK.g_loadedClasses += [("UAccumulateAlphaEffect", 765, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UAmbientOcclusionEffect", 767, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UBlurEffect", 769, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UDOFEffect", 771, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UDOFAndBloomEffect", 773, "UDOFEffect")]
BL2SDK.g_loadedClasses += [("UDOFBloomMotionBlurEffect", 775, "UDOFAndBloomEffect")]
BL2SDK.g_loadedClasses += [("UUberPostProcessEffect", 777, "UDOFBloomMotionBlurEffect")]
BL2SDK.g_loadedClasses += [("UDwTriovizImplEffect", 779, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UFXAAEffect", 781, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UMaterialEffect", 783, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UMotionBlurEffect", 785, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("UPrimitiveComponentFactory", 787, "UObject")]
BL2SDK.g_loadedClasses += [("UMeshComponentFactory", 789, "UPrimitiveComponentFactory")]
BL2SDK.g_loadedClasses += [("UStaticMeshComponentFactory", 791, "UMeshComponentFactory")]
BL2SDK.g_loadedClasses += [("UReachSpec", 793, "UObject")]
BL2SDK.g_loadedClasses += [("UAdvancedReachSpec", 795, "UReachSpec")]
BL2SDK.g_loadedClasses += [("UCeilingReachSpec", 797, "UReachSpec")]
BL2SDK.g_loadedClasses += [("UForcedReachSpec", 799, "UReachSpec")]
BL2SDK.g_loadedClasses += [("UCoverSlipReachSpec", 801, "UForcedReachSpec")]
BL2SDK.g_loadedClasses += [("UFloorToCeilingReachSpec", 803, "UForcedReachSpec")]
BL2SDK.g_loadedClasses += [("UMantleReachSpec", 805, "UForcedReachSpec")]
BL2SDK.g_loadedClasses += [("USlotToSlotReachSpec", 807, "UForcedReachSpec")]
BL2SDK.g_loadedClasses += [("USwatTurnReachSpec", 809, "UForcedReachSpec")]
BL2SDK.g_loadedClasses += [("UWallTransReachSpec", 811, "UForcedReachSpec")]
BL2SDK.g_loadedClasses += [("ULadderReachSpec", 813, "UReachSpec")]
BL2SDK.g_loadedClasses += [("UProscribedReachSpec", 815, "UReachSpec")]
BL2SDK.g_loadedClasses += [("UTeleportReachSpec", 817, "UReachSpec")]
BL2SDK.g_loadedClasses += [("USavedMove", 819, "UObject")]
BL2SDK.g_loadedClasses += [("USaveGameSummary", 821, "UObject")]
BL2SDK.g_loadedClasses += [("USelection", 823, "UObject")]
BL2SDK.g_loadedClasses += [("UServerCommandlet", 825, "UCommandlet")]
BL2SDK.g_loadedClasses += [("USettings", 827, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineGameSearch", 829, "USettings")]
BL2SDK.g_loadedClasses += [("UOnlineGameSettings", 831, "USettings")]
BL2SDK.g_loadedClasses += [("UShaderCache", 833, "UObject")]
BL2SDK.g_loadedClasses += [("UShadowMap1D", 835, "UObject")]
BL2SDK.g_loadedClasses += [("UShadowMap2D", 837, "UObject")]
BL2SDK.g_loadedClasses += [("USmokeTestCommandlet", 839, "UCommandlet")]
BL2SDK.g_loadedClasses += [("USnapshotInterface", 841, "UObject")]
BL2SDK.g_loadedClasses += [("USpeechRecognition", 843, "UObject")]
BL2SDK.g_loadedClasses += [("UStaticMesh", 845, "UObject")]
BL2SDK.g_loadedClasses += [("URB_BodySetup", 871, "UKMeshProps")]
BL2SDK.g_loadedClasses += [("UTexture", 873, "USurface")]
BL2SDK.g_loadedClasses += [("UTexture2D", 875, "UTexture")]
BL2SDK.g_loadedClasses += [("ULightMapTexture2D", 877, "UTexture2D")]
BL2SDK.g_loadedClasses += [("UShadowMapTexture2D", 879, "UTexture2D")]
BL2SDK.g_loadedClasses += [("UTranslationContext", 881, "UObject")]
BL2SDK.g_loadedClasses += [("UTranslatorTag", 883, "UObject")]
BL2SDK.g_loadedClasses += [("UStringsTag", 885, "UTranslatorTag")]
BL2SDK.g_loadedClasses += [("UUIRoot", 887, "UObject")]
BL2SDK.g_loadedClasses += [("UInteraction", 889, "UUIRoot")]
BL2SDK.g_loadedClasses += [("UUIInteraction", 891, "UInteraction")]
BL2SDK.g_loadedClasses += [("UUIManager", 893, "UObject")]
BL2SDK.g_loadedClasses += [("UVertex", 895, "UObject")]
BL2SDK.g_loadedClasses += [("UWaveFormBase", 897, "UObject")]
BL2SDK.g_loadedClasses += [("UWorld", 899, "UObject")]
BL2SDK.g_loadedClasses += [("AEnvironmentVolume", 901, "AVolume")]
BL2SDK.g_loadedClasses += [("ATestSplittingVolume", 903, "AVolume")]
BL2SDK.g_loadedClasses += [("AAIController", 905, "AController")]
BL2SDK.g_loadedClasses += [("APathTargetPoint", 907, "AKeypoint")]
BL2SDK.g_loadedClasses += [("ANavMeshObstacle", 909, "AActor")]
BL2SDK.g_loadedClasses += [("APylonSeed", 911, "AActor")]
BL2SDK.g_loadedClasses += [("ABlockingMeshActor", 913, "AStaticMeshActorBase")]
BL2SDK.g_loadedClasses += [("ABlockingMeshReplicatedActor", 915, "ABlockingMeshActor")]
BL2SDK.g_loadedClasses += [("UCoverGroupRenderingComponent", 917, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UMeshComponent", 919, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UStaticMeshComponent", 921, "UMeshComponent")]
BL2SDK.g_loadedClasses += [("UCoverMeshComponent", 923, "UStaticMeshComponent")]
BL2SDK.g_loadedClasses += [("UNavMeshRenderingComponent", 925, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UPathRenderingComponent", 927, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("URouteRenderingComponent", 929, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UAutoNavMeshPathObstacleUnregister", 931, "UObject")]
BL2SDK.g_loadedClasses += [("UGBXNavMeshPathFinder", 933, "UObject")]
BL2SDK.g_loadedClasses += [("UIGBXNavMeshObstacle", 935, "UInterface")]
BL2SDK.g_loadedClasses += [("UInterface_NavMeshPathObject", 937, "UInterface")]
BL2SDK.g_loadedClasses += [("UInterface_NavMeshPathSwitch", 939, "UInterface_NavMeshPathObject")]
BL2SDK.g_loadedClasses += [("UInterface_NavMeshPathObstacle", 941, "UInterface")]
BL2SDK.g_loadedClasses += [("UNavigationHandle", 943, "UObject")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_Filter", 945, "UObject")]
BL2SDK.g_loadedClasses += [("UNavMeshGoalFilter_MinPathDistance", 947, "UNavMeshGoal_Filter")]
BL2SDK.g_loadedClasses += [("UNavMeshGoalFilter_NotNearOtherAI", 949, "UNavMeshGoal_Filter")]
BL2SDK.g_loadedClasses += [("UNavMeshGoalFilter_OutOfViewFrom", 951, "UNavMeshGoal_Filter")]
BL2SDK.g_loadedClasses += [("UNavMeshGoalFilter_OutSideOfDotProductWedge", 953, "UNavMeshGoal_Filter")]
BL2SDK.g_loadedClasses += [("UNavMeshGoalFilter_PolyEncompassesAI", 955, "UNavMeshGoal_Filter")]
BL2SDK.g_loadedClasses += [("UNavMeshPathConstraint", 957, "UObject")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_AlongLine", 959, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_EnforceTwoWayEdges", 961, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_MinDistBetweenSpecsOfType", 963, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_SameCoverLink", 965, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_Toward", 967, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_WithinDistanceEnvelope", 969, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPath_WithinTraversalDist", 971, "UNavMeshPathConstraint")]
BL2SDK.g_loadedClasses += [("UNavMeshPathGoalEvaluator", 973, "UObject")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_At", 975, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_ClosestActorInList", 977, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_GenericFilterContainer", 979, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_Null", 981, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_PolyEncompassesAI", 983, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_Random", 985, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UNavMeshGoal_WithinDistanceEnvelope", 987, "UNavMeshPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UPathConstraint", 989, "UObject")]
BL2SDK.g_loadedClasses += [("UPath_AlongLine", 991, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPath_AvoidInEscapableNodes", 993, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPath_MinDistBetweenSpecsOfType", 995, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPath_TowardGoal", 997, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPath_TowardPoint", 999, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPath_WithinDistanceEnvelope", 1001, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPath_WithinTraversalDist", 1003, "UPathConstraint")]
BL2SDK.g_loadedClasses += [("UPathGoalEvaluator", 1005, "UObject")]
BL2SDK.g_loadedClasses += [("UGoal_AtActor", 1007, "UPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("UGoal_Null", 1009, "UPathGoalEvaluator")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshActor", 1011, "AActor")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshActorBasedOnExtremeContent", 1013, "ASkeletalMeshActor")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshActorSpawnable", 1015, "ASkeletalMeshActor")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshCinematicActor", 1017, "ASkeletalMeshActor")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshActorMAT", 1019, "ASkeletalMeshCinematicActor")]
BL2SDK.g_loadedClasses += [("UHeadTrackingComponent", 1021, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm", 1023, "UObject")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_Automatic", 1025, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_BitwiseCompressOnly", 1027, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_GBXCustom", 1029, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_LeastDestructive", 1031, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_RemoveEverySecondKey", 1033, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_RemoveLinearKeys", 1035, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_PerTrackCompression", 1037, "UAnimationCompressionAlgorithm_RemoveLinearKeys")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_RemoveTrivialKeys", 1039, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimationCompressionAlgorithm_RevertToRaw", 1041, "UAnimationCompressionAlgorithm")]
BL2SDK.g_loadedClasses += [("UAnimMetaData", 1043, "UObject")]
BL2SDK.g_loadedClasses += [("UAnimMetaData_SkelControl", 1045, "UAnimMetaData")]
BL2SDK.g_loadedClasses += [("UAnimMetaData_SkelControlKeyFrame", 1047, "UAnimMetaData_SkelControl")]
BL2SDK.g_loadedClasses += [("UAnimNotify", 1049, "UObject")]
BL2SDK.g_loadedClasses += [("UAnimNotify_AkEvent", 1051, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_CameraEffect", 1053, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_ClothingMaxDistanceScale", 1055, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Footstep", 1057, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_ForceField", 1059, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Kismet", 1061, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_PlayParticleEffect", 1063, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Rumble", 1065, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Script", 1067, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Scripted", 1069, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_PawnMaterialParam", 1071, "UAnimNotify_Scripted")]
BL2SDK.g_loadedClasses += [("UAnimNotify_ViewShake", 1073, "UAnimNotify_Scripted")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Sound", 1075, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_SoundSpatial", 1077, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimNotify_Trails", 1079, "UAnimNotify")]
BL2SDK.g_loadedClasses += [("UAnimObject", 1081, "UObject")]
BL2SDK.g_loadedClasses += [("UAnimNode", 1083, "UAnimObject")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendBase", 1085, "UAnimNode")]
BL2SDK.g_loadedClasses += [("UAnimNode_MultiBlendPerBone", 1087, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeAimOffset", 1089, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlend", 1091, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeAdditiveBlending", 1093, "UAnimNodeBlend")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendPerBone", 1095, "UAnimNodeBlend")]
BL2SDK.g_loadedClasses += [("UAnimNodeCrossfader", 1097, "UAnimNodeBlend")]
BL2SDK.g_loadedClasses += [("UAnimNodePlayCustomAnim", 1099, "UAnimNodeBlend")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendDirectional", 1101, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendList", 1103, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendByBase", 1105, "UAnimNodeBlendList")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendByPhysics", 1107, "UAnimNodeBlendList")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendByPosture", 1109, "UAnimNodeBlendList")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendByProperty", 1111, "UAnimNodeBlendList")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendBySpeed", 1113, "UAnimNodeBlendList")]
BL2SDK.g_loadedClasses += [("UAnimNodeRandom", 1115, "UAnimNodeBlendList")]
BL2SDK.g_loadedClasses += [("UAnimNodeBlendMultiBone", 1117, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeMirror", 1119, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeScalePlayRate", 1121, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeScaleRateBySpeed", 1123, "UAnimNodeScalePlayRate")]
BL2SDK.g_loadedClasses += [("UAnimNodeSlot", 1125, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeSynch", 1127, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimTree", 1129, "UAnimNodeBlendBase")]
BL2SDK.g_loadedClasses += [("UAnimNodeSequence", 1131, "UAnimNode")]
BL2SDK.g_loadedClasses += [("UAnimNodeSequenceBlendBase", 1133, "UAnimNodeSequence")]
BL2SDK.g_loadedClasses += [("UAnimNodeSequenceBlendByAim", 1135, "UAnimNodeSequenceBlendBase")]
BL2SDK.g_loadedClasses += [("UMorphNodeBase", 1137, "UAnimObject")]
BL2SDK.g_loadedClasses += [("UMorphNodeMultiPose", 1139, "UMorphNodeBase")]
BL2SDK.g_loadedClasses += [("UMorphNodePose", 1141, "UMorphNodeBase")]
BL2SDK.g_loadedClasses += [("UMorphNodeWeightBase", 1143, "UMorphNodeBase")]
BL2SDK.g_loadedClasses += [("UMorphNodeWeight", 1145, "UMorphNodeWeightBase")]
BL2SDK.g_loadedClasses += [("UMorphNodeWeightByBoneAngle", 1147, "UMorphNodeWeightBase")]
BL2SDK.g_loadedClasses += [("UMorphNodeWeightByBoneRotation", 1149, "UMorphNodeWeightBase")]
BL2SDK.g_loadedClasses += [("USkelControlBase", 1151, "UAnimObject")]
BL2SDK.g_loadedClasses += [("USkelControl_CCD_IK", 1153, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControl_Multiply", 1155, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControl_TwistBone", 1157, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControlLimb", 1159, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControlFootPlacement", 1161, "USkelControlLimb")]
BL2SDK.g_loadedClasses += [("USkelControlLookAt", 1163, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControlSingleBone", 1165, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControlHandlebars", 1167, "USkelControlSingleBone")]
BL2SDK.g_loadedClasses += [("USkelControlWheel", 1169, "USkelControlSingleBone")]
BL2SDK.g_loadedClasses += [("USkelControlSpline", 1171, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("USkelControlTrail", 1173, "USkelControlBase")]
BL2SDK.g_loadedClasses += [("UAnimSequence", 1175, "UObject")]
BL2SDK.g_loadedClasses += [("UAnimSet", 1177, "UObject")]
BL2SDK.g_loadedClasses += [("UMorphTarget", 1179, "UObject")]
BL2SDK.g_loadedClasses += [("UMorphTargetSet", 1181, "UObject")]
BL2SDK.g_loadedClasses += [("UMorphWeightSequence", 1183, "UObject")]
BL2SDK.g_loadedClasses += [("ADecalActorBase", 1185, "AActor")]
BL2SDK.g_loadedClasses += [("ADecalActor", 1187, "ADecalActorBase")]
BL2SDK.g_loadedClasses += [("ADecalActorMovable", 1189, "ADecalActorBase")]
BL2SDK.g_loadedClasses += [("ADecalManager", 1191, "AActor")]
BL2SDK.g_loadedClasses += [("UDecalComponent", 1193, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UActorFactoryDecal", 1195, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryDecalMovable", 1197, "UActorFactoryDecal")]
BL2SDK.g_loadedClasses += [("UDecalMaterial", 1199, "UMaterial")]
BL2SDK.g_loadedClasses += [("AFogVolumeDensityInfo", 1201, "AInfo")]
BL2SDK.g_loadedClasses += [("AFogVolumeConeDensityInfo", 1203, "AFogVolumeDensityInfo")]
BL2SDK.g_loadedClasses += [("AFogVolumeConstantDensityInfo", 1205, "AFogVolumeDensityInfo")]
BL2SDK.g_loadedClasses += [("AFogVolumeLinearHalfspaceDensityInfo", 1207, "AFogVolumeDensityInfo")]
BL2SDK.g_loadedClasses += [("AFogVolumeSphericalDensityInfo", 1209, "AFogVolumeDensityInfo")]
BL2SDK.g_loadedClasses += [("UExponentialHeightFogComponent", 1211, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UFogVolumeDensityComponent", 1213, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UFogVolumeConeDensityComponent", 1215, "UFogVolumeDensityComponent")]
BL2SDK.g_loadedClasses += [("UFogVolumeConstantDensityComponent", 1217, "UFogVolumeDensityComponent")]
BL2SDK.g_loadedClasses += [("UFogVolumeLinearHalfspaceDensityComponent", 1219, "UFogVolumeDensityComponent")]
BL2SDK.g_loadedClasses += [("UFogVolumeSphericalDensityComponent", 1221, "UFogVolumeDensityComponent")]
BL2SDK.g_loadedClasses += [("UActorFactoryFogVolumeConstantDensityInfo", 1223, "UActorFactory")]
BL2SDK.g_loadedClasses += [("UActorFactoryFogVolumeLinearHalfspaceDensityInfo", 1225, "UActorFactoryFogVolumeConstantDensityInfo")]
BL2SDK.g_loadedClasses += [("UActorFactoryFogVolumeSphericalDensityInfo", 1227, "UActorFactoryFogVolumeConstantDensityInfo")]
BL2SDK.g_loadedClasses += [("AApexDestructibleActor", 1229, "AActor")]
BL2SDK.g_loadedClasses += [("UApexComponentBase", 1231, "UMeshComponent")]
BL2SDK.g_loadedClasses += [("UApexDynamicComponent", 1233, "UApexComponentBase")]
BL2SDK.g_loadedClasses += [("UApexStaticComponent", 1235, "UApexComponentBase")]
BL2SDK.g_loadedClasses += [("UApexStaticDestructibleComponent", 1237, "UApexStaticComponent")]
BL2SDK.g_loadedClasses += [("UBlockingMeshComponent", 1239, "UStaticMeshComponent")]
BL2SDK.g_loadedClasses += [("UInstancedStaticMeshComponent", 1241, "UStaticMeshComponent")]
BL2SDK.g_loadedClasses += [("USplineMeshComponent", 1243, "UStaticMeshComponent")]
BL2SDK.g_loadedClasses += [("UApexAsset", 1245, "UObject")]
BL2SDK.g_loadedClasses += [("UApexClothingAsset", 1247, "UApexAsset")]
BL2SDK.g_loadedClasses += [("UApexDestructibleAsset", 1249, "UApexAsset")]
BL2SDK.g_loadedClasses += [("UApexGenericAsset", 1251, "UApexAsset")]
BL2SDK.g_loadedClasses += [("UInterpFilter", 1253, "UObject")]
BL2SDK.g_loadedClasses += [("UInterpFilter_Classes", 1255, "UInterpFilter")]
BL2SDK.g_loadedClasses += [("UInterpFilter_Custom", 1257, "UInterpFilter")]
BL2SDK.g_loadedClasses += [("UInterpGroup", 1259, "UObject")]
BL2SDK.g_loadedClasses += [("UInterpGroupAI", 1261, "UInterpGroup")]
BL2SDK.g_loadedClasses += [("UInterpGroupDirector", 1263, "UInterpGroup")]
BL2SDK.g_loadedClasses += [("UInterpGroupInst", 1265, "UObject")]
BL2SDK.g_loadedClasses += [("UInterpGroupInstAI", 1267, "UInterpGroupInst")]
BL2SDK.g_loadedClasses += [("UInterpGroupInstDirector", 1269, "UInterpGroupInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackBoolProp", 1271, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackComment", 1273, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackDirector", 1275, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackEvent", 1277, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackFaceFX", 1279, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackFloatBase", 1281, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackAnimControl", 1283, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackFade", 1285, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackFloatMaterialParam", 1287, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackFloatParticleParam", 1289, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackFloatProp", 1291, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackMorphWeight", 1293, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackMoveAxis", 1295, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackSkelControlScale", 1297, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackSkelControlStrength", 1299, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackSlomo", 1301, "UInterpTrackFloatBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackHeadTracking", 1303, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackLinearColorBase", 1305, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackLinearColorProp", 1307, "UInterpTrackLinearColorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackMove", 1309, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackParticleReplay", 1311, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackTeleport", 1313, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackToggle", 1315, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackVectorBase", 1317, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackAudioMaster", 1319, "UInterpTrackVectorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackColorProp", 1321, "UInterpTrackVectorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackColorScale", 1323, "UInterpTrackVectorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackSound", 1325, "UInterpTrackVectorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackVectorMaterialParam", 1327, "UInterpTrackVectorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackVectorProp", 1329, "UInterpTrackVectorBase")]
BL2SDK.g_loadedClasses += [("UInterpTrackVisibility", 1331, "UInterpTrack")]
BL2SDK.g_loadedClasses += [("UInterpTrackInst", 1333, "UObject")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstAnimControl", 1335, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstAudioMaster", 1337, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstColorScale", 1339, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstComment", 1341, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstDirector", 1343, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstEvent", 1345, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstFaceFX", 1347, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstFade", 1349, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstFloatMaterialParam", 1351, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstFloatParticleParam", 1353, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstHeadTracking", 1355, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstMorphWeight", 1357, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstMove", 1359, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstParticleReplay", 1361, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstProperty", 1363, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstBoolProp", 1365, "UInterpTrackInstProperty")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstColorProp", 1367, "UInterpTrackInstProperty")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstFloatProp", 1369, "UInterpTrackInstProperty")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstLinearColorProp", 1371, "UInterpTrackInstProperty")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstVectorProp", 1373, "UInterpTrackInstProperty")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstSkelControlScale", 1375, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstSkelControlStrength", 1377, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstSlomo", 1379, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstSound", 1381, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstTeleport", 1383, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstToggle", 1385, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstVectorMaterialParam", 1387, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UInterpTrackInstVisibility", 1389, "UInterpTrackInst")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionAbs", 1391, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionAdd", 1393, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionAppendVector", 1395, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionArcCosine", 1397, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionArcSine", 1399, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionArcTangent", 1401, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionArcTangent2", 1403, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionBlendModeBase", 1405, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzColorBurn", 1407, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzColorDodge", 1409, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzExclusion", 1411, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzHardLight", 1413, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzLinearBurn", 1415, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzLinearLight", 1417, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzOverlay", 1419, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzPinLight", 1421, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzScreen", 1423, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzSoftLight", 1425, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionzVividLight", 1427, "UMaterialExpressionBlendModeBase")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionBumpOffset", 1429, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionBumpOffsetEx", 1431, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionBumpOffsetSloped", 1433, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCameraVector", 1435, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCameraWorldPosition", 1437, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCeil", 1439, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionClamp", 1441, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionComment", 1443, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionComponentMask", 1445, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCompound", 1447, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionConstant", 1449, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionConstant2Vector", 1451, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionConstant3Vector", 1453, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionConstant4Vector", 1455, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionConstantBiasScale", 1457, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionConstantClamp", 1459, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCosine", 1461, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCrossProduct", 1463, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCustom", 1465, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionCustomTexture", 1467, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDdx", 1469, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDdy", 1471, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDegrees", 1473, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDepthBiasedAlpha", 1475, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDepthBiasedBlend", 1477, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDepthOfFieldFunction", 1479, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDeriveNormalZ", 1481, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDesaturation", 1483, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDestColor", 1485, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDestDepth", 1487, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDistance", 1489, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDivide", 1491, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDominantSkyLight", 1493, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDotProduct", 1495, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDynamicParameter", 1497, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMeshEmitterDynamicParameter", 1499, "UMaterialExpressionDynamicParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionExp", 1501, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionExp2", 1503, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFloor", 1505, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFluidNormal", 1507, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFmod", 1509, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFoliageImpulseDirection", 1511, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFoliageNormalizedRotationAxisAndAngle", 1513, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFontSample", 1515, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFontSampleParameter", 1517, "UMaterialExpressionFontSample")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFrac", 1519, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFresnel", 1521, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionGradient", 1523, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionIf", 1525, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLength", 1527, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLensFlareIntensity", 1529, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLensFlareOcclusion", 1531, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLensFlareRadialDistance", 1533, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLensFlareRayDistance", 1535, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLensFlareSourceDistance", 1537, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLightmapUVs", 1539, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLightmassReplace", 1541, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLightVector", 1543, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLinearInterpolate", 1545, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLog", 1547, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLog10", 1549, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionLog2", 1551, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMax", 1553, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMeshEmitterVertexColor", 1555, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMin", 1557, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMultiply", 1559, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMultiplyAndAdd", 1561, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionNormalize", 1563, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionObjectOrientation", 1565, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionObjectRadius", 1567, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionObjectWorldPosition", 1569, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionOcclusionPercentage", 1571, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionOneMinus", 1573, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionPanner", 1575, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionParameter", 1577, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionScalarParameter", 1579, "UMaterialExpressionParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionStaticComponentMaskParameter", 1581, "UMaterialExpressionParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionStaticSwitchParameter", 1583, "UMaterialExpressionParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionVectorParameter", 1585, "UMaterialExpressionParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionParticleMacroUV", 1587, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionPerInstanceRandom", 1589, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionPixelDepth", 1591, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionPower", 1593, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionRadians", 1595, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionRecipSquareRoot", 1597, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionReflectionVector", 1599, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionRotate3D", 1601, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionRotateAboutAxis", 1603, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionRotator", 1605, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSaturate", 1607, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSceneDepth", 1609, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSceneTexture", 1611, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionScreenPosition", 1613, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSine", 1615, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSphereMask", 1617, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSPHFluidNormal", 1619, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSPHFluidThickness", 1621, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSPHFluidVertexColor", 1623, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSquareRoot", 1625, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSteepParallaxOffset", 1627, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSubtract", 1629, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionSwizzle", 1631, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTangent", 1633, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTerrainLayerCoords", 1635, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTerrainLayerWeight", 1637, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTerrainTextureCoordinate", 1639, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureCoordinate", 1641, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureDimensions", 1643, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSample", 1645, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionDepthBiasBlend", 1647, "UMaterialExpressionTextureSample")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionFlipBookSample", 1649, "UMaterialExpressionTextureSample")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMeshSubUV", 1651, "UMaterialExpressionTextureSample")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionMeshSubUVBlend", 1653, "UMaterialExpressionMeshSubUV")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionParticleSubUV", 1655, "UMaterialExpressionTextureSample")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameter", 1657, "UMaterialExpressionTextureSample")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameter2D", 1659, "UMaterialExpressionTextureSampleParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionAntialiasedTextureMask", 1661, "UMaterialExpressionTextureSampleParameter2D")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameterMeshSubUV", 1663, "UMaterialExpressionTextureSampleParameter2D")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameterMeshSubUVBlend", 1665, "UMaterialExpressionTextureSampleParameterMeshSubUV")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameterSubUV", 1667, "UMaterialExpressionTextureSampleParameter2D")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameterCube", 1669, "UMaterialExpressionTextureSampleParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameterMovie", 1671, "UMaterialExpressionTextureSampleParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSampleParameterNormal", 1673, "UMaterialExpressionTextureSampleParameter")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTextureSplat", 1675, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTime", 1677, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTransform", 1679, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTransformPosition", 1681, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionTwoSidedSign", 1683, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionVectorIf", 1685, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionVertexColor", 1687, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionWindDirectionAndSpeed", 1689, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionWorldAmbientColor", 1691, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionWorldLightColor", 1693, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionWorldNormal", 1695, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialExpressionWorldPosition", 1697, "UMaterialExpression")]
BL2SDK.g_loadedClasses += [("UMaterialInstance", 1699, "UMaterialInterface")]
BL2SDK.g_loadedClasses += [("UMaterialInstanceConstant", 1701, "UMaterialInstance")]
BL2SDK.g_loadedClasses += [("UMaterialInstanceTimeVarying", 1703, "UMaterialInstance")]
BL2SDK.g_loadedClasses += [("AEmitter", 1705, "AActor")]
BL2SDK.g_loadedClasses += [("AEmitterCameraLensEffectBase", 1707, "AEmitter")]
BL2SDK.g_loadedClasses += [("AParticleEventManager", 1709, "AActor")]
BL2SDK.g_loadedClasses += [("UParticleSystemComponent", 1711, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UDistributionFloatParticleParameter", 1713, "UDistributionFloatParameterBase")]
BL2SDK.g_loadedClasses += [("UDistributionVectorParticleParameter", 1715, "UDistributionVectorParameterBase")]
BL2SDK.g_loadedClasses += [("UParticleEmitter", 1717, "UObject")]
BL2SDK.g_loadedClasses += [("UParticleSpriteEmitter", 1719, "UParticleEmitter")]
BL2SDK.g_loadedClasses += [("UParticleLODLevel", 1721, "UObject")]
BL2SDK.g_loadedClasses += [("UParticleModule", 1723, "UObject")]
BL2SDK.g_loadedClasses += [("UParticleModuleAccelerationBase", 1725, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleAcceleration", 1727, "UParticleModuleAccelerationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleAccelerationOverLifetime", 1729, "UParticleModuleAccelerationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleAttractorBase", 1731, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleAttractorLine", 1733, "UParticleModuleAttractorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleAttractorParticle", 1735, "UParticleModuleAttractorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleAttractorPoint", 1737, "UParticleModuleAttractorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleBeamBase", 1739, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleBeamModifier", 1741, "UParticleModuleBeamBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleBeamNoise", 1743, "UParticleModuleBeamBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleBeamSource", 1745, "UParticleModuleBeamBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleBeamTarget", 1747, "UParticleModuleBeamBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleBeamTrace", 1749, "UParticleModuleBeamTarget")]
BL2SDK.g_loadedClasses += [("UParticleModuleCameraBase", 1751, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleCameraOffset", 1753, "UParticleModuleCameraBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleCollisionBase", 1755, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleCollision", 1757, "UParticleModuleCollisionBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleCollisionActor", 1759, "UParticleModuleCollision")]
BL2SDK.g_loadedClasses += [("UParticleModuleColorBase", 1761, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleColor", 1763, "UParticleModuleColorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleColor_Seeded", 1765, "UParticleModuleColor")]
BL2SDK.g_loadedClasses += [("UParticleModuleColorByParameter", 1767, "UParticleModuleColorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleColorOverLife", 1769, "UParticleModuleColorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleColorScaleOverDensity", 1771, "UParticleModuleColorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleColorScaleOverLife", 1773, "UParticleModuleColorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventBase", 1775, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventGenerator", 1777, "UParticleModuleEventBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventGeneratorDecal", 1779, "UParticleModuleEventGenerator")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventReceiverBase", 1781, "UParticleModuleEventBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventReceiverKillParticles", 1783, "UParticleModuleEventReceiverBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventReceiverSpawn", 1785, "UParticleModuleEventReceiverBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleForceFieldBase", 1787, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleKillBase", 1789, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleKillBox", 1791, "UParticleModuleKillBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleKillHeight", 1793, "UParticleModuleKillBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLifetimeBase", 1795, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleLifetime", 1797, "UParticleModuleLifetimeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLifetime_Seeded", 1799, "UParticleModuleLifetime")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationBase", 1801, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocation", 1803, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocation_Seeded", 1805, "UParticleModuleLocation")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationBoneSocket", 1807, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationDirect", 1809, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationEmitter", 1811, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationEmitterDirect", 1813, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationPrimitiveBase", 1815, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationPrimitiveCylinder", 1817, "UParticleModuleLocationPrimitiveBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationPrimitiveCylinder_Seeded", 1819, "UParticleModuleLocationPrimitiveCylinder")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationPrimitiveSphere", 1821, "UParticleModuleLocationPrimitiveBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationPrimitiveSphere_Seeded", 1823, "UParticleModuleLocationPrimitiveSphere")]
BL2SDK.g_loadedClasses += [("UParticleModuleLocationSkelVertSurface", 1825, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSourceMovement", 1827, "UParticleModuleLocationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleMaterialBase", 1829, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleMaterialByParameter", 1831, "UParticleModuleMaterialBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshMaterial", 1833, "UParticleModuleMaterialBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleOrbitBase", 1835, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleOrbit", 1837, "UParticleModuleOrbitBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleOrientationBase", 1839, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleOrientationAxisLock", 1841, "UParticleModuleOrientationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleParameterBase", 1843, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleParameterDynamic", 1845, "UParticleModuleParameterBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleParameterDynamic_Seeded", 1847, "UParticleModuleParameterDynamic")]
BL2SDK.g_loadedClasses += [("UParticleModuleRequired", 1849, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotationBase", 1851, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshRotation", 1853, "UParticleModuleRotationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshRotation_Seeded", 1855, "UParticleModuleMeshRotation")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotation", 1857, "UParticleModuleRotationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotation_Seeded", 1859, "UParticleModuleRotation")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotationOverLifetime", 1861, "UParticleModuleRotationBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotationRateBase", 1863, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshRotationRate", 1865, "UParticleModuleRotationRateBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshRotationRate_Seeded", 1867, "UParticleModuleMeshRotationRate")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshRotationRateMultiplyLife", 1869, "UParticleModuleRotationRateBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleMeshRotationRateOverLife", 1871, "UParticleModuleRotationRateBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotationRate", 1873, "UParticleModuleRotationRateBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotationRate_Seeded", 1875, "UParticleModuleRotationRate")]
BL2SDK.g_loadedClasses += [("UParticleModuleRotationRateMultiplyLife", 1877, "UParticleModuleRotationRateBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSizeBase", 1879, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleSize", 1881, "UParticleModuleSizeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSize_Seeded", 1883, "UParticleModuleSize")]
BL2SDK.g_loadedClasses += [("UParticleModuleSizeMultiplyLife", 1885, "UParticleModuleSizeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSizeMultiplyVelocity", 1887, "UParticleModuleSizeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSizeScale", 1889, "UParticleModuleSizeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSizeScaleByTime", 1891, "UParticleModuleSizeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSizeScaleOverDensity", 1893, "UParticleModuleSizeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSpawnBase", 1895, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleSpawn", 1897, "UParticleModuleSpawnBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSpawnPerUnit", 1899, "UParticleModuleSpawnBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleStoreSpawnTimeBase", 1901, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleStoreSpawnTime", 1903, "UParticleModuleStoreSpawnTimeBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSubUVBase", 1905, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleSubUV", 1907, "UParticleModuleSubUVBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSubUVMovie", 1909, "UParticleModuleSubUV")]
BL2SDK.g_loadedClasses += [("UParticleModuleSubUVDirect", 1911, "UParticleModuleSubUVBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleSubUVSelect", 1913, "UParticleModuleSubUVBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTrailBase", 1915, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleTrailSource", 1917, "UParticleModuleTrailBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTrailSpawn", 1919, "UParticleModuleTrailBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTrailTaper", 1921, "UParticleModuleTrailBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataBase", 1923, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataAnimTrail", 1925, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataApex", 1927, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataBeam", 1929, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataBeam2", 1931, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataMesh", 1933, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataMeshPhysX", 1935, "UParticleModuleTypeDataMesh")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataPhysX", 1937, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataRibbon", 1939, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataTrail", 1941, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleTypeDataTrail2", 1943, "UParticleModuleTypeDataBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberBase", 1945, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberLTISIVCL", 1947, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberLTISIVCLIL", 1949, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberLTISIVCLILIRSSBLIRR", 1951, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberRainDrops", 1953, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberRainImpacts", 1955, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberRainSplashA", 1957, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleUberRainSplashB", 1959, "UParticleModuleUberBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleVelocityBase", 1961, "UParticleModule")]
BL2SDK.g_loadedClasses += [("UParticleModuleVelocity", 1963, "UParticleModuleVelocityBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleVelocity_Seeded", 1965, "UParticleModuleVelocity")]
BL2SDK.g_loadedClasses += [("UParticleModuleVelocityInheritParent", 1967, "UParticleModuleVelocityBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleVelocityOverLifetime", 1969, "UParticleModuleVelocityBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleEventSendToGame", 1971, "UObject")]
BL2SDK.g_loadedClasses += [("UParticleSystem", 1973, "UObject")]
BL2SDK.g_loadedClasses += [("UParticleSystemReplay", 1975, "UObject")]
BL2SDK.g_loadedClasses += [("UPhysXParticleSystem", 1977, "UObject")]
BL2SDK.g_loadedClasses += [("AKActor", 1979, "ADynamicSMActor")]
BL2SDK.g_loadedClasses += [("AKActorFromStatic", 1981, "AKActor")]
BL2SDK.g_loadedClasses += [("AKActorSpawnable", 1983, "AKActor")]
BL2SDK.g_loadedClasses += [("AKActorPizazz", 1985, "AKActorSpawnable")]
BL2SDK.g_loadedClasses += [("AKAsset", 1987, "AActor")]
BL2SDK.g_loadedClasses += [("APawn", 1989, "AActor")]
BL2SDK.g_loadedClasses += [("AVehicle", 1991, "APawn")]
BL2SDK.g_loadedClasses += [("ASVehicle", 1993, "AVehicle")]
BL2SDK.g_loadedClasses += [("ARB_ConstraintActor", 1995, "ARigidBodyBase")]
BL2SDK.g_loadedClasses += [("ARB_LineImpulseActor", 1997, "ARigidBodyBase")]
BL2SDK.g_loadedClasses += [("ARB_RadialImpulseActor", 1999, "ARigidBodyBase")]
BL2SDK.g_loadedClasses += [("ARB_Thruster", 2001, "ARigidBodyBase")]
BL2SDK.g_loadedClasses += [("URB_ConstraintDrawComponent", 2003, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("URB_RadialImpulseComponent", 2005, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("URB_Handle", 2007, "UActorComponent")]
BL2SDK.g_loadedClasses += [("URB_Spring", 2009, "UActorComponent")]
BL2SDK.g_loadedClasses += [("USVehicleSimBase", 2011, "UActorComponent")]
BL2SDK.g_loadedClasses += [("USVehicleSimCar", 2013, "USVehicleSimBase")]
BL2SDK.g_loadedClasses += [("USVehicleSimTank", 2015, "USVehicleSimCar")]
BL2SDK.g_loadedClasses += [("UActorFactoryApexClothing", 2017, "UActorFactorySkeletalMesh")]
BL2SDK.g_loadedClasses += [("UApexDestructibleDamageParameters", 2019, "UObject")]
BL2SDK.g_loadedClasses += [("UFractureMaterial", 2021, "UObject")]
BL2SDK.g_loadedClasses += [("UPhysicalMaterial", 2023, "UObject")]
BL2SDK.g_loadedClasses += [("UPhysicalMaterialPropertyBase", 2025, "UObject")]
BL2SDK.g_loadedClasses += [("UPhysicsAsset", 2027, "UObject")]
BL2SDK.g_loadedClasses += [("UPhysicsAssetInstance", 2029, "UObject")]
BL2SDK.g_loadedClasses += [("UPhysicsLODVerticalEmitter", 2031, "UObject")]
BL2SDK.g_loadedClasses += [("URB_BodyInstance", 2033, "UObject")]
BL2SDK.g_loadedClasses += [("URB_ConstraintInstance", 2035, "UObject")]
BL2SDK.g_loadedClasses += [("URB_ConstraintSetup", 2037, "UObject")]
BL2SDK.g_loadedClasses += [("URB_BSJointSetup", 2039, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("URB_DistanceJointSetup", 2041, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("URB_HingeSetup", 2043, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("URB_PrismaticSetup", 2045, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("URB_PulleyJointSetup", 2047, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("URB_SkelJointSetup", 2049, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("URB_StayUprightSetup", 2051, "URB_ConstraintSetup")]
BL2SDK.g_loadedClasses += [("USVehicleWheel", 2053, "UComponent")]
BL2SDK.g_loadedClasses += [("ANxGenericForceFieldBrush", 2055, "AVolume")]
BL2SDK.g_loadedClasses += [("ARB_ForceFieldExcludeVolume", 2057, "AVolume")]
BL2SDK.g_loadedClasses += [("ANxForceField", 2059, "AActor")]
BL2SDK.g_loadedClasses += [("ANxCylindricalForceField", 2061, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxCylindricalForceFieldCapsule", 2063, "ANxCylindricalForceField")]
BL2SDK.g_loadedClasses += [("ANxForceFieldGeneric", 2065, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxForceFieldRadial", 2067, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxForceFieldTornado", 2069, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxGenericForceField", 2071, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxGenericForceFieldBox", 2073, "ANxGenericForceField")]
BL2SDK.g_loadedClasses += [("ANxGenericForceFieldCapsule", 2075, "ANxGenericForceField")]
BL2SDK.g_loadedClasses += [("ANxRadialForceField", 2077, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxRadialCustomForceField", 2079, "ANxRadialForceField")]
BL2SDK.g_loadedClasses += [("ANxTornadoAngularForceField", 2081, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxTornadoAngularForceFieldCapsule", 2083, "ANxTornadoAngularForceField")]
BL2SDK.g_loadedClasses += [("ANxTornadoForceField", 2085, "ANxForceField")]
BL2SDK.g_loadedClasses += [("ANxTornadoForceFieldCapsule", 2087, "ANxTornadoForceField")]
BL2SDK.g_loadedClasses += [("ANxForceFieldSpawnable", 2089, "AActor")]
BL2SDK.g_loadedClasses += [("ARB_CylindricalForceActor", 2091, "ARigidBodyBase")]
BL2SDK.g_loadedClasses += [("ARB_RadialForceActor", 2093, "ARigidBodyBase")]
BL2SDK.g_loadedClasses += [("UNxForceFieldComponent", 2095, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UNxForceFieldCylindricalComponent", 2097, "UNxForceFieldComponent")]
BL2SDK.g_loadedClasses += [("UNxForceFieldGenericComponent", 2099, "UNxForceFieldComponent")]
BL2SDK.g_loadedClasses += [("UNxForceFieldRadialComponent", 2101, "UNxForceFieldComponent")]
BL2SDK.g_loadedClasses += [("UNxForceFieldTornadoComponent", 2103, "UNxForceFieldComponent")]
BL2SDK.g_loadedClasses += [("UForceFieldShape", 2105, "UObject")]
BL2SDK.g_loadedClasses += [("UForceFieldShapeBox", 2107, "UForceFieldShape")]
BL2SDK.g_loadedClasses += [("UForceFieldShapeCapsule", 2109, "UForceFieldShape")]
BL2SDK.g_loadedClasses += [("UForceFieldShapeSphere", 2111, "UForceFieldShape")]
BL2SDK.g_loadedClasses += [("APrefabInstance", 2113, "AActor")]
BL2SDK.g_loadedClasses += [("UPrefab", 2115, "UObject")]
BL2SDK.g_loadedClasses += [("USequenceObject", 2117, "UObject")]
BL2SDK.g_loadedClasses += [("USequenceOp", 2119, "USequenceObject")]
BL2SDK.g_loadedClasses += [("USequenceEvent", 2121, "USequenceOp")]
BL2SDK.g_loadedClasses += [("USequenceEventCustomEnableCondition", 2123, "UObject")]
BL2SDK.g_loadedClasses += [("USequenceFrame", 2125, "USequenceObject")]
BL2SDK.g_loadedClasses += [("USavingSequenceFrame", 2127, "USequenceFrame")]
BL2SDK.g_loadedClasses += [("USequenceFrameWrapped", 2129, "USequenceFrame")]
BL2SDK.g_loadedClasses += [("USeqDef_Base", 2131, "USequenceOp")]
BL2SDK.g_loadedClasses += [("USequence", 2133, "USequenceOp")]
BL2SDK.g_loadedClasses += [("UPrefabSequence", 2135, "USequence")]
BL2SDK.g_loadedClasses += [("UPrefabSequenceContainer", 2137, "USequence")]
BL2SDK.g_loadedClasses += [("USequenceDefinition", 2139, "USequence")]
BL2SDK.g_loadedClasses += [("USequenceAction", 2141, "USequenceOp")]
BL2SDK.g_loadedClasses += [("USeqAct_ActivateRemoteEvent", 2143, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_AndGate", 2145, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ApplyBehavior", 2147, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ApplySoundNode", 2149, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_AttachToEvent", 2151, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_CameraFade", 2153, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_CameraLookAt", 2155, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ChangeCollision", 2157, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_CommitMapChange", 2159, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ConsoleCommand", 2161, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ConvertToString", 2163, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_DrawText", 2165, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_FinishSequence", 2167, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Gate", 2169, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_GetDistance", 2171, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_GetLocationAndRotation", 2173, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_GetProperty", 2175, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_GetVectorComponents", 2177, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_GetVelocity", 2179, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_HeadTrackingControl", 2181, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_IsInObjectList", 2183, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Latent", 2185, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ActorFactory", 2187, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_ActorFactoryEx", 2189, "USeqAct_ActorFactory")]
BL2SDK.g_loadedClasses += [("USeqAct_ProjectileFactory", 2191, "USeqAct_ActorFactory")]
BL2SDK.g_loadedClasses += [("USeqAct_AIMoveToActor", 2193, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_Delay", 2195, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_DelaySwitch", 2197, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_ForceGarbageCollection", 2199, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_Interp", 2201, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_LevelStreamingBase", 2203, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_LevelStreaming", 2205, "USeqAct_LevelStreamingBase")]
BL2SDK.g_loadedClasses += [("USeqAct_MultiLevelStreaming", 2207, "USeqAct_LevelStreamingBase")]
BL2SDK.g_loadedClasses += [("USeqAct_LevelVisibility", 2209, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_PlaySound", 2211, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_PrepareMapChange", 2213, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_SetDOFParams", 2215, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_SetMotionBlurParams", 2217, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_StreamInTextures", 2219, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_WaitForLevelsVisible", 2221, "USeqAct_Latent")]
BL2SDK.g_loadedClasses += [("USeqAct_Log", 2223, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ModifyCover", 2225, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ModifyHealth", 2227, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ParticleEventGenerator", 2229, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_PhysXSwitch", 2231, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_PlayCameraAnim", 2233, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_PlayFaceFXAnim", 2235, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_PlayMusicTrack", 2237, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Possess", 2239, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetApexClothingParam", 2241, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetBlockRigidBody", 2243, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetCameraTarget", 2245, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetMaterial", 2247, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetMatInstScalarParam", 2249, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetMesh", 2251, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetPhysics", 2253, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetRigidBodyIgnoreVehicles", 2255, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetSequenceVariable", 2257, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_AccessObjectList", 2259, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_AddFloat", 2261, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_AddInt", 2263, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_CastToFloat", 2265, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_CastToInt", 2267, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_DivideFloat", 2269, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_DivideInt", 2271, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_ModifyObjectList", 2273, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_MultiplyFloat", 2275, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_MultiplyInt", 2277, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetBool", 2279, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetFloat", 2281, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetInt", 2283, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetLocation", 2285, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetObject", 2287, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetString", 2289, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SubtractFloat", 2291, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SubtractInt", 2293, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_SetVectorComponents", 2295, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Switch", 2297, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_RandomSwitch", 2299, "USeqAct_Switch")]
BL2SDK.g_loadedClasses += [("USeqAct_Timer", 2301, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Toggle", 2303, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Trace", 2305, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USequenceCondition", 2307, "USequenceOp")]
BL2SDK.g_loadedClasses += [("USeqCond_CompareBool", 2309, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_CompareFloat", 2311, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_CompareInt", 2313, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_CompareObject", 2315, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_GetServerType", 2317, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_Increment", 2319, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IncrementFloat", 2321, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsAlive", 2323, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsBenchmarking", 2325, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsConsole", 2327, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsInCombat", 2329, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsLoggedIn", 2331, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsPIE", 2333, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_IsSameTeam", 2335, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_MatureLanguage", 2337, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_ShowGore", 2339, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_SwitchBase", 2341, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqCond_SwitchClass", 2343, "USeqCond_SwitchBase")]
BL2SDK.g_loadedClasses += [("USeqCond_SwitchObject", 2345, "USeqCond_SwitchBase")]
BL2SDK.g_loadedClasses += [("USeqCond_SwitchPlatform", 2347, "USequenceCondition")]
BL2SDK.g_loadedClasses += [("USeqEvent_AISeeEnemy", 2349, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_AnimNotify", 2351, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_Console", 2353, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_ConstraintBroken", 2355, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_Destroyed", 2357, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_LevelLoaded", 2359, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_Mover", 2361, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_ParticleEvent", 2363, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_ProjectileLanded", 2365, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_RemoteEvent", 2367, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_RigidBodyCollision", 2369, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_SeeDeath", 2371, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_SequenceActivated", 2373, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_TakeDamage", 2375, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_Touch", 2377, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_Used", 2379, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USequenceVariable", 2381, "USequenceObject")]
BL2SDK.g_loadedClasses += [("UInterpData", 2383, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Bool", 2385, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_External", 2387, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Float", 2389, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_RandomFloat", 2391, "USeqVar_Float")]
BL2SDK.g_loadedClasses += [("USeqVar_Int", 2393, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_RandomInt", 2395, "USeqVar_Int")]
BL2SDK.g_loadedClasses += [("USeqVar_Named", 2397, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Object", 2399, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Character", 2401, "USeqVar_Object")]
BL2SDK.g_loadedClasses += [("USeqVar_Group", 2403, "USeqVar_Object")]
BL2SDK.g_loadedClasses += [("USeqVar_ObjectList", 2405, "USeqVar_Object")]
BL2SDK.g_loadedClasses += [("USeqVar_ObjectVolume", 2407, "USeqVar_Object")]
BL2SDK.g_loadedClasses += [("USeqVar_Player", 2409, "USeqVar_Object")]
BL2SDK.g_loadedClasses += [("USeqVar_String", 2411, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Vector", 2413, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("AAmbientSound", 2415, "AKeypoint")]
BL2SDK.g_loadedClasses += [("UDistributionFloatSoundParameter", 2417, "UDistributionFloatParameterBase")]
BL2SDK.g_loadedClasses += [("USoundNode", 2419, "UObject")]
BL2SDK.g_loadedClasses += [("USoundNodeWave", 2421, "USoundNode")]
BL2SDK.g_loadedClasses += [("ALandscapeProxy", 2423, "AInfo")]
BL2SDK.g_loadedClasses += [("ALandscape", 2425, "ALandscapeProxy")]
BL2SDK.g_loadedClasses += [("ATerrain", 2427, "AInfo")]
BL2SDK.g_loadedClasses += [("ULandscapeComponent", 2429, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("ULandscapeHeightfieldCollisionComponent", 2431, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UTerrainComponent", 2433, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UTerrainWeightMapTexture", 2435, "UTexture2D")]
BL2SDK.g_loadedClasses += [("UTerrainLayerSetup", 2437, "UObject")]
BL2SDK.g_loadedClasses += [("UTerrainMaterial", 2439, "UObject")]
BL2SDK.g_loadedClasses += [("UDataStoreClient", 2441, "UUIRoot")]
BL2SDK.g_loadedClasses += [("UConsole", 2443, "UInteraction")]
BL2SDK.g_loadedClasses += [("UInput", 2445, "UInteraction")]
BL2SDK.g_loadedClasses += [("UPlayerInput", 2447, "UInput")]
BL2SDK.g_loadedClasses += [("UPlayerManagerInteraction", 2449, "UInteraction")]
BL2SDK.g_loadedClasses += [("UUISceneClient", 2451, "UUIRoot")]
BL2SDK.g_loadedClasses += [("UUISoundTheme", 2453, "UObject")]
BL2SDK.g_loadedClasses += [("UUIDataStoreSubscriber", 2455, "UInterface")]
BL2SDK.g_loadedClasses += [("UUIDataStorePublisher", 2457, "UUIDataStoreSubscriber")]
BL2SDK.g_loadedClasses += [("UUIListElementCellProvider", 2459, "UInterface")]
BL2SDK.g_loadedClasses += [("UUIListElementProvider", 2461, "UInterface")]
BL2SDK.g_loadedClasses += [("UUIDataProvider", 2463, "UUIRoot")]
BL2SDK.g_loadedClasses += [("UUIConfigProvider", 2465, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIConfigFileProvider", 2467, "UUIConfigProvider")]
BL2SDK.g_loadedClasses += [("UUIConfigSectionProvider", 2469, "UUIConfigProvider")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlinePlayerDataBase", 2471, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlineFriendMessages", 2473, "UUIDataProvider_OnlinePlayerDataBase")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlineFriends", 2475, "UUIDataProvider_OnlinePlayerDataBase")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlinePartyChatList", 2477, "UUIDataProvider_OnlinePlayerDataBase")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlinePlayerStorage", 2479, "UUIDataProvider_OnlinePlayerDataBase")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlineProfileSettings", 2481, "UUIDataProvider_OnlinePlayerStorage")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_PlayerAchievements", 2483, "UUIDataProvider_OnlinePlayerDataBase")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_OnlinePlayerStorageArray", 2485, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_SettingsArray", 2487, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDataStore", 2489, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDataStore_DynamicResource", 2491, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_Fonts", 2493, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_GameResource", 2495, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_MenuItems", 2497, "UUIDataStore_GameResource")]
BL2SDK.g_loadedClasses += [("UUIDataStore_GameState", 2499, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_Registry", 2501, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_Remote", 2503, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_OnlineGameSearch", 2505, "UUIDataStore_Remote")]
BL2SDK.g_loadedClasses += [("UUIDataStore_OnlinePlayerData", 2507, "UUIDataStore_Remote")]
BL2SDK.g_loadedClasses += [("UUIDataStore_OnlineStats", 2509, "UUIDataStore_Remote")]
BL2SDK.g_loadedClasses += [("UUIDataStore_Settings", 2511, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_OnlineGameSettings", 2513, "UUIDataStore_Settings")]
BL2SDK.g_loadedClasses += [("UUIDataStore_StringBase", 2515, "UUIDataStore")]
BL2SDK.g_loadedClasses += [("UUIDataStore_InputAlias", 2517, "UUIDataStore_StringBase")]
BL2SDK.g_loadedClasses += [("UUIDataStore_StringAliasMap", 2519, "UUIDataStore_StringBase")]
BL2SDK.g_loadedClasses += [("UUIDataStore_Strings", 2521, "UUIDataStore_StringBase")]
BL2SDK.g_loadedClasses += [("UUIDynamicFieldProvider", 2523, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIPropertyDataProvider", 2525, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDynamicDataProvider", 2527, "UUIPropertyDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_Settings", 2529, "UUIDynamicDataProvider")]
BL2SDK.g_loadedClasses += [("UUIResourceDataProvider", 2531, "UUIPropertyDataProvider")]
BL2SDK.g_loadedClasses += [("UUIDataProvider_MenuItem", 2533, "UUIResourceDataProvider")]
BL2SDK.g_loadedClasses += [("UUIMapSummary", 2535, "UUIResourceDataProvider")]
BL2SDK.g_loadedClasses += [("UUIResourceCombinationProvider", 2537, "UUIDataProvider")]
BL2SDK.g_loadedClasses += [("UGameUISceneClient", 2539, "UUISceneClient")]
BL2SDK.g_loadedClasses += [("UScene", 2541, "UObject")]
BL2SDK.g_loadedClasses += [("AFoliageFactory", 2543, "AVolume")]
BL2SDK.g_loadedClasses += [("AInstancedFoliageActor", 2545, "AActor")]
BL2SDK.g_loadedClasses += [("AInteractiveFoliageActor", 2547, "AStaticMeshActor")]
BL2SDK.g_loadedClasses += [("UFoliageComponent", 2549, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UInteractiveFoliageComponent", 2551, "UStaticMeshComponent")]
BL2SDK.g_loadedClasses += [("UActorFactoryInteractiveFoliage", 2553, "UActorFactoryStaticMesh")]
BL2SDK.g_loadedClasses += [("AFluidInfluenceActor", 2555, "AActor")]
BL2SDK.g_loadedClasses += [("AFluidSurfaceActor", 2557, "AActor")]
BL2SDK.g_loadedClasses += [("AFluidSurfaceActorMovable", 2559, "AFluidSurfaceActor")]
BL2SDK.g_loadedClasses += [("UFluidInfluenceComponent", 2561, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UFluidSurfaceComponent", 2563, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("ALensFlareSource", 2565, "AActor")]
BL2SDK.g_loadedClasses += [("ULensFlareComponent", 2567, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("ULensFlare", 2569, "UObject")]
BL2SDK.g_loadedClasses += [("UTextureFlipBook", 2571, "UTexture2D")]
BL2SDK.g_loadedClasses += [("UTexture2DComposite", 2573, "UTexture")]
BL2SDK.g_loadedClasses += [("UTexture2DDynamic", 2575, "UTexture")]
BL2SDK.g_loadedClasses += [("UTextureCube", 2577, "UTexture")]
BL2SDK.g_loadedClasses += [("UTextureMovie", 2579, "UTexture")]
BL2SDK.g_loadedClasses += [("UTextureRenderTarget", 2581, "UTexture")]
BL2SDK.g_loadedClasses += [("UTextureRenderTarget2D", 2583, "UTextureRenderTarget")]
BL2SDK.g_loadedClasses += [("UScriptedTexture", 2585, "UTextureRenderTarget2D")]
BL2SDK.g_loadedClasses += [("UTextureRenderTargetCube", 2587, "UTextureRenderTarget")]
BL2SDK.g_loadedClasses += [("UAudioDevice", 2589, "USubsystem")]
BL2SDK.g_loadedClasses += [("USoundClass", 2591, "UObject")]
BL2SDK.g_loadedClasses += [("USoundMode", 2593, "UObject")]
BL2SDK.g_loadedClasses += [("ADebugCameraController", 2595, "APlayerController")]
BL2SDK.g_loadedClasses += [("AMatineePawn", 2597, "APawn")]
BL2SDK.g_loadedClasses += [("AScout", 2599, "APawn")]
BL2SDK.g_loadedClasses += [("ALight", 2601, "AActor")]
BL2SDK.g_loadedClasses += [("ADirectionalLight", 2603, "ALight")]
BL2SDK.g_loadedClasses += [("ADirectionalLightToggleable", 2605, "ADirectionalLight")]
BL2SDK.g_loadedClasses += [("ADominantDirectionalLight", 2607, "ADirectionalLight")]
BL2SDK.g_loadedClasses += [("ADominantDirectionalLightMovable", 2609, "ADominantDirectionalLight")]
BL2SDK.g_loadedClasses += [("ALightShafts", 2611, "ALight")]
BL2SDK.g_loadedClasses += [("APointLight", 2613, "ALight")]
BL2SDK.g_loadedClasses += [("ADominantPointLight", 2615, "APointLight")]
BL2SDK.g_loadedClasses += [("APointLightMovable", 2617, "APointLight")]
BL2SDK.g_loadedClasses += [("APointLightToggleable", 2619, "APointLight")]
BL2SDK.g_loadedClasses += [("ASkyLight", 2621, "ALight")]
BL2SDK.g_loadedClasses += [("ASkyLightToggleable", 2623, "ASkyLight")]
BL2SDK.g_loadedClasses += [("ASpotLight", 2625, "ALight")]
BL2SDK.g_loadedClasses += [("ADominantSpotLight", 2627, "ASpotLight")]
BL2SDK.g_loadedClasses += [("AGeneratedMeshAreaLight", 2629, "ASpotLight")]
BL2SDK.g_loadedClasses += [("ASpotLightMovable", 2631, "ASpotLight")]
BL2SDK.g_loadedClasses += [("ASpotLightToggleable", 2633, "ASpotLight")]
BL2SDK.g_loadedClasses += [("AStaticLightCollectionActor", 2635, "ALight")]
BL2SDK.g_loadedClasses += [("ULightComponent", 2637, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UDirectionalLightComponent", 2639, "ULightComponent")]
BL2SDK.g_loadedClasses += [("UDominantDirectionalLightComponent", 2641, "UDirectionalLightComponent")]
BL2SDK.g_loadedClasses += [("ULightShaftComponent", 2643, "ULightComponent")]
BL2SDK.g_loadedClasses += [("UPointLightComponent", 2645, "ULightComponent")]
BL2SDK.g_loadedClasses += [("UDominantPointLightComponent", 2647, "UPointLightComponent")]
BL2SDK.g_loadedClasses += [("USpotLightComponent", 2649, "UPointLightComponent")]
BL2SDK.g_loadedClasses += [("UDominantSpotLightComponent", 2651, "USpotLightComponent")]
BL2SDK.g_loadedClasses += [("USkyLightComponent", 2653, "ULightComponent")]
BL2SDK.g_loadedClasses += [("USphericalHarmonicLightComponent", 2655, "ULightComponent")]
BL2SDK.g_loadedClasses += [("ULightEnvironmentComponent", 2657, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UDynamicLightEnvironmentComponent", 2659, "ULightEnvironmentComponent")]
BL2SDK.g_loadedClasses += [("UParticleLightEnvironmentComponent", 2661, "UDynamicLightEnvironmentComponent")]
BL2SDK.g_loadedClasses += [("UDrawLightConeComponent", 2663, "UDrawConeComponent")]
BL2SDK.g_loadedClasses += [("UDrawLightRadiusComponent", 2665, "UDrawSphereComponent")]
BL2SDK.g_loadedClasses += [("ULightFunction", 2667, "UObject")]
BL2SDK.g_loadedClasses += [("USkeletalMeshComponent", 2669, "UMeshComponent")]
BL2SDK.g_loadedClasses += [("USkeletalMesh", 2671, "UObject")]
BL2SDK.g_loadedClasses += [("USkeletalMeshSocket", 2673, "UObject")]
BL2SDK.g_loadedClasses += [("ASplineActor", 2675, "AActor")]
BL2SDK.g_loadedClasses += [("ASplineLoftActor", 2677, "ASplineActor")]
BL2SDK.g_loadedClasses += [("ASplineLoftActorMovable", 2679, "ASplineLoftActor")]
BL2SDK.g_loadedClasses += [("USplineComponent", 2681, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("AReplicationInfo", 2683, "AInfo")]
BL2SDK.g_loadedClasses += [("AGameReplicationInfo", 2685, "AReplicationInfo")]
BL2SDK.g_loadedClasses += [("APlayerReplicationInfo", 2687, "AReplicationInfo")]
BL2SDK.g_loadedClasses += [("ATeamInfo", 2689, "AReplicationInfo")]
BL2SDK.g_loadedClasses += [("ACamera", 2691, "AActor")]
BL2SDK.g_loadedClasses += [("ACameraActor", 2693, "AActor")]
BL2SDK.g_loadedClasses += [("ADynamicCameraActor", 2695, "ACameraActor")]
BL2SDK.g_loadedClasses += [("UCameraAnim", 2697, "UObject")]
BL2SDK.g_loadedClasses += [("UCameraAnimInst", 2699, "UObject")]
BL2SDK.g_loadedClasses += [("UCameraModifier", 2701, "UObject")]
BL2SDK.g_loadedClasses += [("UCameraModifier_CameraShake", 2703, "UCameraModifier")]
BL2SDK.g_loadedClasses += [("UCameraShake", 2705, "UObject")]
BL2SDK.g_loadedClasses += [("AResourcePoolManager", 2707, "AReplicationInfo")]
BL2SDK.g_loadedClasses += [("AWorldSoundManager", 2709, "AInfo")]
BL2SDK.g_loadedClasses += [("UComponentLifetimeManagerComponent", 2711, "UActorComponent")]
BL2SDK.g_loadedClasses += [("UAttributeContextResolver", 2713, "UObject")]
BL2SDK.g_loadedClasses += [("UBalancedActorAttributeContextResolver", 2715, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UCharacterClassAttributeContextResolver", 2717, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UControllerAttributeContextResolver", 2719, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UGameInfoAttributeContextResolver", 2721, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UOffHandWeaponAttributeContextResolver", 2723, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UPawnAttributeContextResolver", 2725, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UResourcePoolAttributeContextResolver", 2727, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UWeaponAttributeContextResolver", 2729, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UWeaponResourcePoolAttributeContextResolver", 2731, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UAttributeEffect", 2733, "UObject")]
BL2SDK.g_loadedClasses += [("UAttributeExpression", 2735, "UObject")]
BL2SDK.g_loadedClasses += [("UAttributeMultiContextResolver", 2737, "UObject")]
BL2SDK.g_loadedClasses += [("UWeaponAttributeMultiContextResolver", 2739, "UAttributeMultiContextResolver")]
BL2SDK.g_loadedClasses += [("UAttributeValueResolver", 2741, "UObject")]
BL2SDK.g_loadedClasses += [("UObjectPropertyAttributeValueResolver", 2743, "UAttributeValueResolver")]
BL2SDK.g_loadedClasses += [("UReadOnlyObjectPropertyAttributeValueResolver", 2745, "UObjectPropertyAttributeValueResolver")]
BL2SDK.g_loadedClasses += [("UBehaviorBase", 2747, "UObject")]
BL2SDK.g_loadedClasses += [("UBehavior_Kill", 2749, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_PlaySound", 2751, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_RemoteEvent", 2753, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UExpressionEvaluator", 2755, "UObject")]
BL2SDK.g_loadedClasses += [("UExpressionTree", 2757, "UExpressionEvaluator")]
BL2SDK.g_loadedClasses += [("UAttributeDefinitionBase", 2759, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UAttributeDefinition", 2761, "UAttributeDefinitionBase")]
BL2SDK.g_loadedClasses += [("UNestedAttributeDefinition", 2763, "UAttributeDefinition")]
BL2SDK.g_loadedClasses += [("UAttributeDefinitionMultiContext", 2765, "UAttributeDefinitionBase")]
BL2SDK.g_loadedClasses += [("UAttributeInitializationDefinition", 2767, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UBaseBalanceDefinition", 2769, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UCharacterClassDefinition", 2771, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UExpressionEvaluatorDefinition", 2773, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UGestaltPartMatricesCollectionDefinition", 2775, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UImpactDefinition", 2777, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UResourceDefinition", 2779, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UResourcePoolDefinition", 2781, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UGestaltPartMatrices", 2783, "UObject")]
BL2SDK.g_loadedClasses += [("UICounterBehavior", 2785, "UInterface")]
BL2SDK.g_loadedClasses += [("UIInstanceData", 2787, "UInterface")]
BL2SDK.g_loadedClasses += [("UInstanceDataHelper", 2789, "UObject")]
BL2SDK.g_loadedClasses += [("UPackageReferencer", 2791, "UObject")]
BL2SDK.g_loadedClasses += [("UPersistentGameDataManager", 2793, "UObject")]
BL2SDK.g_loadedClasses += [("UPersistentSequenceData", 2795, "UObject")]
BL2SDK.g_loadedClasses += [("UResourcePool", 2797, "UObject")]
BL2SDK.g_loadedClasses += [("UHealthResourcePool", 2799, "UResourcePool")]
BL2SDK.g_loadedClasses += [("UTargetableList", 2801, "UObject")]
BL2SDK.g_loadedClasses += [("AHybridNavigationArea", 2803, "AInfo")]
BL2SDK.g_loadedClasses += [("APickupableMeshActor", 2805, "AActor")]
BL2SDK.g_loadedClasses += [("UHybridNavigationAreaDebugRenderingComponent", 2807, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UHybridNavigationVisualizationComponent", 2809, "UPrimitiveComponent")]
BL2SDK.g_loadedClasses += [("UInventoryCardPresentationDefinition", 2811, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UManufacturerDefinition", 2813, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("ULevelStreamingDomino", 2815, "ULevelStreamingKismet")]
BL2SDK.g_loadedClasses += [("ULocalMessage", 2817, "UObject")]
BL2SDK.g_loadedClasses += [("UEdgeDetectionPostProcessEffect", 2819, "UPostProcessEffect")]
BL2SDK.g_loadedClasses += [("ADroppedPickup", 2821, "AActor")]
BL2SDK.g_loadedClasses += [("AInventory", 2823, "AActor")]
BL2SDK.g_loadedClasses += [("AWillowInventory", 2825, "AInventory")]
BL2SDK.g_loadedClasses += [("AWeapon", 2827, "AWillowInventory")]
BL2SDK.g_loadedClasses += [("AInventoryManager", 2829, "AActor")]
BL2SDK.g_loadedClasses += [("UGearboxCalloutDefinition", 2831, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UWillowInventoryDefinition", 2833, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UWillowInventoryPartDefinition", 2835, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UIPickupable", 2837, "UInterface")]
BL2SDK.g_loadedClasses += [("USeqEvent_HitWall", 7250, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqAct_Destroy", 7890, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_Teleport", 7935, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetVelocity", 7950, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ToggleHidden", 7976, "USeqAct_Toggle")]
BL2SDK.g_loadedClasses += [("USeqAct_AttachToActor", 7983, "USequenceAction")]
BL2SDK.g_loadedClasses += [("UIConsoleCommandBehavior", 8459, "UInterface")]
BL2SDK.g_loadedClasses += [("UIAppearanceBehavior", 8460, "UInterface")]
BL2SDK.g_loadedClasses += [("UIPhysicsBehavior", 8461, "UInterface")]
BL2SDK.g_loadedClasses += [("UIChangeCollisionBehavior", 8462, "UInterface")]
BL2SDK.g_loadedClasses += [("UIDestroyBehavior", 8463, "UInterface")]
BL2SDK.g_loadedClasses += [("UISoundBehavior", 8464, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineAuthInterface", 8798, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineTitleFileInterface", 8803, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlinePartyChatInterface", 8808, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineNewsInterface", 8813, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineStatsInterface", 8818, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineVoiceInterface", 8823, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineContentInterface", 8828, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineGameInterface", 8833, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineSystemInterface", 8838, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlinePlayerInterfaceEx", 8843, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlinePlayerInterface", 8848, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineAccountInterface", 8853, "UInterface")]
BL2SDK.g_loadedClasses += [("AAccessControl", 9242, "AInfo")]
BL2SDK.g_loadedClasses += [("AAdmin", 9270, "APlayerController")]
BL2SDK.g_loadedClasses += [("UIScaleBehavior", 9859, "UInterface")]
BL2SDK.g_loadedClasses += [("AApexDestructibleActorSpawnable", 9868, "AApexDestructibleActor")]
BL2SDK.g_loadedClasses += [("AEmitterSpawnable", 9880, "AEmitter")]
BL2SDK.g_loadedClasses += [("AKAssetSpawnable", 9895, "AKAsset")]
BL2SDK.g_loadedClasses += [("UActorFactorySkeletalMeshCinematic", 9906, "UActorFactorySkeletalMesh")]
BL2SDK.g_loadedClasses += [("UActorFactorySkeletalMeshMAT", 9908, "UActorFactorySkeletalMesh")]
BL2SDK.g_loadedClasses += [("USeqEvent_Death", 10282, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqAct_ToggleGodMode", 10597, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ControlMovieTexture", 11268, "USequenceAction")]
BL2SDK.g_loadedClasses += [("UIParameterBehavior", 11347, "UInterface")]
BL2SDK.g_loadedClasses += [("ACoverReplicator", 12216, "AReplicationInfo")]
BL2SDK.g_loadedClasses += [("UGameMessage", 12345, "ULocalMessage")]
BL2SDK.g_loadedClasses += [("UDmgType_Suicided", 12603, "UKillZDamageType")]
BL2SDK.g_loadedClasses += [("USeqAct_ToggleInput", 13582, "USeqAct_Toggle")]
BL2SDK.g_loadedClasses += [("USeqAct_ToggleHUD", 13657, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ForceFeedback", 13693, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_ToggleCinematicMode", 13717, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_FlyThroughHasEnded", 14077, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetSoundMode", 14120, "USequenceAction")]
BL2SDK.g_loadedClasses += [("UAnimNotify_PlayFaceFXAnim", 16156, "UAnimNotify_Scripted")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeAllegiance", 17126, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeBoneVisibility", 17138, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeCollision", 17150, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeCollisionSize", 17161, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeCounter", 17195, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeParticleSystemActiveState", 17213, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UIParticleSystemBehavior", 17217, "UInterface")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeScale", 17225, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeSpin", 17236, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UIBasicBehavior", 17245, "UInterface")]
BL2SDK.g_loadedClasses += [("UBehavior_ChangeVisibility", 17255, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ClientConsoleCommand", 17266, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ConsoleCommand", 17277, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_CustomAnimation", 17288, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_Destroy", 17310, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_FollowAllegiance", 17320, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_RandomlyRunBehaviors", 17362, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_RunBehaviorCollection", 17389, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehaviorCollectionDefinition", 17393, "UGBXDefinition")]
BL2SDK.g_loadedClasses += [("UBehavior_SetMaterialParameters", 17417, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UIMaterialBehavior", 17420, "UInterface")]
BL2SDK.g_loadedClasses += [("UBehavior_SetParticleSystemParameters", 17451, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_SetPhysics", 17495, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_SetSkelControlActive", 17517, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UBehavior_ToggleVisibility", 17529, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("ABroadcastHandler", 17626, "AInfo")]
BL2SDK.g_loadedClasses += [("AColorScaleVolume", 18275, "AVolume")]
BL2SDK.g_loadedClasses += [("ADebugCameraHUD", 19223, "AHUD")]
BL2SDK.g_loadedClasses += [("UDebugCameraInput", 19255, "UPlayerInput")]
BL2SDK.g_loadedClasses += [("AVolumeTimer", 19827, "AInfo")]
BL2SDK.g_loadedClasses += [("USeqAct_SetDamageInstigator", 19859, "USequenceAction")]
BL2SDK.g_loadedClasses += [("UDmgType_Crushed", 19993, "UDamageType")]
BL2SDK.g_loadedClasses += [("UDmgType_Fell", 19995, "UDamageType")]
BL2SDK.g_loadedClasses += [("UDmgType_Telefragged", 19998, "UDamageType")]
BL2SDK.g_loadedClasses += [("ADynamicPhysicsVolume", 20480, "APhysicsVolume")]
BL2SDK.g_loadedClasses += [("ADynamicSMActor_Spawnable", 20531, "ADynamicSMActor")]
BL2SDK.g_loadedClasses += [("ADynamicTriggerVolume", 20540, "ATriggerVolume")]
BL2SDK.g_loadedClasses += [("USeqAct_SetParticleSysParam", 20881, "USequenceAction")]
BL2SDK.g_loadedClasses += [("AExponentialHeightFog", 21372, "AInfo")]
BL2SDK.g_loadedClasses += [("UFailedConnect", 21466, "ULocalMessage")]
BL2SDK.g_loadedClasses += [("USeqEvent_PlayerSpawned", 22175, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("UGameReplicationInfoAttributeContextResolver", 23013, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("AHoldingAreaDestination", 23408, "ATeleporterDestination")]
BL2SDK.g_loadedClasses += [("AHeightFog", 24210, "AInfo")]
BL2SDK.g_loadedClasses += [("UIChangeBehaviorSetStateBehavior", 24363, "UInterface")]
BL2SDK.g_loadedClasses += [("UIDamageBehavior", 24379, "UInterface")]
BL2SDK.g_loadedClasses += [("AInterpActor_ForCinematic", 24821, "AInterpActor")]
BL2SDK.g_loadedClasses += [("AMaterialInstanceTimeVaryingActor", 26744, "AActor")]
BL2SDK.g_loadedClasses += [("USeqAct_AssignController", 27232, "USequenceAction")]
BL2SDK.g_loadedClasses += [("UOnlineCommunityContentInterface", 28620, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlineEventsInterface", 28970, "UInterface")]
BL2SDK.g_loadedClasses += [("UOnlinePlaylistGameTypeProvider", 30041, "UUIResourceDataProvider")]
BL2SDK.g_loadedClasses += [("UOnlineRecentPlayersList", 30090, "UObject")]
BL2SDK.g_loadedClasses += [("UOnlineSuppliedUIInterface", 30335, "UInterface")]
BL2SDK.g_loadedClasses += [("UOwnerAttributeContextResolver", 30523, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("UParameterBehaviorBase", 30531, "UBehaviorBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleForceFieldCylindrical", 30842, "UParticleModuleForceFieldBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleForceFieldGeneric", 30845, "UParticleModuleForceFieldBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleForceFieldRadial", 30848, "UParticleModuleForceFieldBase")]
BL2SDK.g_loadedClasses += [("UParticleModuleForceFieldTornado", 30851, "UParticleModuleForceFieldBase")]
BL2SDK.g_loadedClasses += [("APathNode_Dynamic", 31587, "APathNode")]
BL2SDK.g_loadedClasses += [("USeqEvent_PickupStatusChange", 31864, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("UProjectileAttributeContextResolver", 32281, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("ARadialBlurActor", 32313, "AActor")]
BL2SDK.g_loadedClasses += [("USeqAct_ToggleConstraintDrive", 32531, "USequenceAction")]
BL2SDK.g_loadedClasses += [("ARB_BSJointActor", 32574, "ARB_ConstraintActor")]
BL2SDK.g_loadedClasses += [("ARB_ConstraintActorSpawnable", 32579, "ARB_ConstraintActor")]
BL2SDK.g_loadedClasses += [("ARB_HingeActor", 32639, "ARB_ConstraintActor")]
BL2SDK.g_loadedClasses += [("ARB_PrismaticActor", 32656, "ARB_ConstraintActor")]
BL2SDK.g_loadedClasses += [("ARB_PulleyJointActor", 32661, "ARB_ConstraintActor")]
BL2SDK.g_loadedClasses += [("AReverbVolumeToggleable", 32815, "AReverbVolume")]
BL2SDK.g_loadedClasses += [("USeqAct_AddRemoveFaceFXAnimSet", 33041, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_AIAbortMoveToActor", 33045, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_MITV_Activate", 33257, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetSkelControlTarget", 33399, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqAct_SetVector", 33413, "USeqAct_SetSequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqAct_UpdatePhysBonesFromAnim", 33493, "USequenceAction")]
BL2SDK.g_loadedClasses += [("USeqEvent_AIReachedRouteActor", 33582, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqEvent_LOS", 33590, "USequenceEvent")]
BL2SDK.g_loadedClasses += [("USeqVar_Byte", 33692, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Name", 33706, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("USeqVar_Union", 33735, "USequenceVariable")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshActorMATSpawnable", 34308, "ASkeletalMeshActorMAT")]
BL2SDK.g_loadedClasses += [("ASkeletalMeshActorMATWalkable", 34313, "ASkeletalMeshActorMAT")]
BL2SDK.g_loadedClasses += [("ATrigger_Dynamic", 35452, "ATrigger")]
BL2SDK.g_loadedClasses += [("ATrigger_LOS", 35456, "ATrigger")]
BL2SDK.g_loadedClasses += [("ATriggeredPath", 35472, "ANavigationPoint")]
BL2SDK.g_loadedClasses += [("ATriggerStreamingLevel", 35485, "ATrigger")]
BL2SDK.g_loadedClasses += [("UUICharacterSummary", 35528, "UUIResourceDataProvider")]
BL2SDK.g_loadedClasses += [("UUIGameInfoSummary", 36329, "UUIResourceDataProvider")]
BL2SDK.g_loadedClasses += [("UUIWeaponSummary", 36510, "UUIResourceDataProvider")]
BL2SDK.g_loadedClasses += [("UVehicleAttributeContextResolver", 36518, "UAttributeContextResolver")]
BL2SDK.g_loadedClasses += [("AWaterVolume", 36537, "APhysicsVolume")]
BL2SDK.g_loadedClasses += [("AWindDirectionalSource", 37367, "AInfo")]
