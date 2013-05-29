# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class BRAINSConstellationModelerInputSpec(CommandLineInputSpec):
    verbose = traits.Bool(desc=",               Show more verbose output,             ", argstr="--verbose ")
    inputTrainingList = File(desc=",               Setup file, giving all parameters for training up a template model for each landmark.,             ", exists=True, argstr="--inputTrainingList %s")
    outputModel = traits.Either(traits.Bool, File(), hash_files=False, desc=",               The full filename of the output model file.,             ", argstr="--outputModel %s")
    saveOptimizedLandmarks = traits.Bool(
        desc=",               Flag to make a new subject-specific landmark definition file in the same format produced by Slicer3 with the optimized landmark (the detected RP, AC, and PC) in it.  Useful to tighten the variances in the ConstellationModeler.,             ", argstr="--saveOptimizedLandmarks ")
    optimizedLandmarksFilenameExtender = traits.Str(
        desc=",                If the trainingList is (indexFullPathName) and contains landmark data filenames [path]/[filename].fcsv ,  make the optimized landmarks filenames out of [path]/[filename](thisExtender) and the optimized version of the input trainingList out of (indexFullPathName)(thisExtender) , when you rewrite all the landmarks according to the saveOptimizedLandmarks flag.,             ", argstr="--optimizedLandmarksFilenameExtender %s")
    resultsDir = traits.Either(traits.Bool, Directory(), hash_files=False, desc=",               The directory for the results to be written.,             ", argstr="--resultsDir %s")
    mspQualityLevel = traits.Int(desc=",                 Flag cotrols how agressive the MSP is estimated.  0=quick estimate (9 seconds), 1=normal estimate (11 seconds), 2=great estimate (22 seconds), 3=best estimate (58 seconds).,             ", argstr="--mspQualityLevel %d")
    rescaleIntensities = traits.Bool(desc=",                 Flag to turn on rescaling image intensities on input.,             ", argstr="--rescaleIntensities ")
    trimRescaledIntensities = traits.Float(
        desc=",                 Turn on clipping the rescaled image one-tailed on input.  Units of standard deviations above the mean.  Very large values are very permissive.  Non-positive value turns clipping off.  Defaults to removing 0.00001 of a normal tail above the mean.,             ", argstr="--trimRescaledIntensities %f")
    rescaleIntensitiesOutputRange = InputMultiPath(
        traits.Int, desc=",                 This pair of integers gives the lower and upper bounds on the signal portion of the output image.  Out-of-field voxels are taken from BackgroundFillValue.,             ", sep=",", argstr="--rescaleIntensitiesOutputRange %s")
    BackgroundFillValue = traits.Str(desc="Fill the background of image with specified short int value. Enter number or use BIGNEG for a large negative number.", argstr="--BackgroundFillValue %s")
    writedebuggingImagesLevel = traits.Int(desc=",                 This flag controls if debugging images are produced.  By default value of 0 is no images.  Anything greater than zero will be increasing level of debugging images.,             ", argstr="--writedebuggingImagesLevel %d")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSConstellationModelerOutputSpec(TraitedSpec):
    outputModel = File(desc=",               The full filename of the output model file.,             ", exists=True)
    resultsDir = Directory(desc=",               The directory for the results to be written.,             ", exists=True)


class BRAINSConstellationModeler(SEMLikeCommandLine):

    """title: Generate Landmarks Model (BRAINS)

category: Utilities.BRAINS

description: Train up a model for BRAINSConstellationDetector

"""

    input_spec = BRAINSConstellationModelerInputSpec
    output_spec = BRAINSConstellationModelerOutputSpec
    _cmd = " BRAINSConstellationModeler "
    _outputs_filenames = {'outputModel': 'outputModel.mdl', 'resultsDir': 'resultsDir'}


class landmarksConstellationWeightsInputSpec(CommandLineInputSpec):
    inputTrainingList = File(desc=",                 Setup file, giving all parameters for training up a Weight list for landmark.,             ", exists=True, argstr="--inputTrainingList %s")
    inputTemplateModel = File(desc="User-specified template model.,             ", exists=True, argstr="--inputTemplateModel %s")
    LLSModel = File(desc="Linear least squares model filename in HD5 format", exists=True, argstr="--LLSModel %s")
    outputWeightsList = traits.Either(traits.Bool, File(), hash_files=False, desc=",                 The filename of a csv file which is a list of landmarks and their corresponding weights.,             ", argstr="--outputWeightsList %s")


class landmarksConstellationWeightsOutputSpec(TraitedSpec):
    outputWeightsList = File(desc=",                 The filename of a csv file which is a list of landmarks and their corresponding weights.,             ", exists=True)


class landmarksConstellationWeights(SEMLikeCommandLine):

    """title: Generate Landmarks Weights (BRAINS)

category: Utilities.BRAINS

description: Train up a list of Weights for the Landmarks in BRAINSConstellationDetector

"""

    input_spec = landmarksConstellationWeightsInputSpec
    output_spec = landmarksConstellationWeightsOutputSpec
    _cmd = " landmarksConstellationWeights "
    _outputs_filenames = {'outputWeightsList': 'outputWeightsList.wts'}


class BRAINSTrimForegroundInDirectionInputSpec(CommandLineInputSpec):
    inputVolume = File(desc="Input image to trim off the neck (and also air-filling noise.)", exists=True, argstr="--inputVolume %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="Output image with neck and air-filling noise trimmed isotropic image with AC at center of image.", argstr="--outputVolume %s")
    directionCode = traits.Int(desc=",                 This flag chooses which dimension to compare.  The sign lets you flip direction.,             ", argstr="--directionCode %d")
    otsuPercentileThreshold = traits.Float(desc=",                 This is a parameter to FindLargestForegroundFilledMask, which is employed to trim off air-filling noise.,             ", argstr="--otsuPercentileThreshold %f")
    closingSize = traits.Int(desc=",                 This is a parameter to FindLargestForegroundFilledMask,             ", argstr="--closingSize %d")
    headSizeLimit = traits.Float(desc=",                 Use this to vary from the command line our search for how much upper tissue is head for the center-of-mass calculation.  Units are CCs, not cubic millimeters.,             ", argstr="--headSizeLimit %f")
    BackgroundFillValue = traits.Str(desc="Fill the background of image with specified short int value. Enter number or use BIGNEG for a large negative number.", argstr="--BackgroundFillValue %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSTrimForegroundInDirectionOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output image with neck and air-filling noise trimmed isotropic image with AC at center of image.", exists=True)


class BRAINSTrimForegroundInDirection(SEMLikeCommandLine):

    """title: Trim Foreground In Direction (BRAINS)

category: Utilities.BRAINS

description: This program will trim off the neck and also air-filling noise from the inputImage.

version: 0.1

documentation-url: http://www.nitrc.org/projects/art/

"""

    input_spec = BRAINSTrimForegroundInDirectionInputSpec
    output_spec = BRAINSTrimForegroundInDirectionOutputSpec
    _cmd = " BRAINSTrimForegroundInDirection "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class BRAINSLmkTransformInputSpec(CommandLineInputSpec):
    inputMovingLandmarks = File(desc="Input Moving Landmark list file in fcsv,             ", exists=True, argstr="--inputMovingLandmarks %s")
    inputFixedLandmarks = File(desc="Input Fixed Landmark list file in fcsv,             ", exists=True, argstr="--inputFixedLandmarks %s")
    outputAffineTransform = traits.Either(traits.Bool, File(), hash_files=False, desc="The filename for the estimated affine transform,             ", argstr="--outputAffineTransform %s")
    inputMovingVolume = File(desc="The filename of input moving volume", exists=True, argstr="--inputMovingVolume %s")
    inputReferenceVolume = File(desc="The filename of the reference volume", exists=True, argstr="--inputReferenceVolume %s")
    outputResampledVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="The filename of the output resampled volume", argstr="--outputResampledVolume %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSLmkTransformOutputSpec(TraitedSpec):
    outputAffineTransform = File(desc="The filename for the estimated affine transform,             ", exists=True)
    outputResampledVolume = File(desc="The filename of the output resampled volume", exists=True)


class BRAINSLmkTransform(SEMLikeCommandLine):

    """title: Landmark Transform (BRAINS)

category: Utilities.BRAINS

description:
      This utility program estimates the affine transform to align the fixed landmarks to the moving landmarks, and then generate the resampled moving image to the same physical space as that of the reference image.


version: 1.0

documentation-url: http://www.nitrc.org/projects/brainscdetector/

"""

    input_spec = BRAINSLmkTransformInputSpec
    output_spec = BRAINSLmkTransformOutputSpec
    _cmd = " BRAINSLmkTransform "
    _outputs_filenames = {'outputResampledVolume': 'outputResampledVolume.nii', 'outputAffineTransform': 'outputAffineTransform.h5'}


class BRAINSMushInputSpec(CommandLineInputSpec):
    inputFirstVolume = File(desc="Input image (1) for mixture optimization", exists=True, argstr="--inputFirstVolume %s")
    inputSecondVolume = File(desc="Input image (2) for mixture optimization", exists=True, argstr="--inputSecondVolume %s")
    inputMaskVolume = File(desc="Input label image for mixture optimization", exists=True, argstr="--inputMaskVolume %s")
    outputWeightsFile = traits.Either(traits.Bool, File(), hash_files=False, desc="Output Weights File", argstr="--outputWeightsFile %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="The MUSH image produced from the T1 and T2 weighted images", argstr="--outputVolume %s")
    outputMask = traits.Either(traits.Bool, File(), hash_files=False, desc="The brain volume mask generated from the MUSH image", argstr="--outputMask %s")
    seed = InputMultiPath(traits.Int, desc="Seed Point for Brain Region Filling", sep=",", argstr="--seed %s")
    desiredMean = traits.Float(desc="Desired mean within the mask for weighted sum of both images.", argstr="--desiredMean %f")
    desiredVariance = traits.Float(desc="Desired variance within the mask for weighted sum of both images.", argstr="--desiredVariance %f")
    lowerThresholdFactorPre = traits.Float(desc="Lower threshold factor for finding an initial brain mask", argstr="--lowerThresholdFactorPre %f")
    upperThresholdFactorPre = traits.Float(desc="Upper threshold factor for finding an initial brain mask", argstr="--upperThresholdFactorPre %f")
    lowerThresholdFactor = traits.Float(desc="Lower threshold factor for defining the brain mask", argstr="--lowerThresholdFactor %f")
    upperThresholdFactor = traits.Float(desc="Upper threshold factor for defining the brain mask", argstr="--upperThresholdFactor %f")
    boundingBoxSize = InputMultiPath(traits.Int, desc="Size of the cubic bounding box mask used when no brain mask is present", sep=",", argstr="--boundingBoxSize %s")
    boundingBoxStart = InputMultiPath(traits.Int, desc="XYZ point-coordinate for the start of the cubic bounding box mask used when no brain mask is present", sep=",", argstr="--boundingBoxStart %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSMushOutputSpec(TraitedSpec):
    outputWeightsFile = File(desc="Output Weights File", exists=True)
    outputVolume = File(desc="The MUSH image produced from the T1 and T2 weighted images", exists=True)
    outputMask = File(desc="The brain volume mask generated from the MUSH image", exists=True)


class BRAINSMush(SEMLikeCommandLine):

    """title:  Brain Extraction from T1/T2 image (BRAINS)

category: Utilities.BRAINS

description:
  This program: 1) generates a weighted mixture image optimizing the mean and variance and 2) produces a mask of the brain volume


version: 0.1.0.$Revision: 1.4 $(alpha)

documentation-url: http:://mri.radiology.uiowa.edu

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor:
  This tool is a modification by Steven Dunn of a program developed by Greg Harris and Ron Pierson.


acknowledgements:
  This work was developed by the University of Iowa Departments of Radiology and Psychiatry. This software was supported in part of NIH/NINDS award NS050568.


"""

    input_spec = BRAINSMushInputSpec
    output_spec = BRAINSMushOutputSpec
    _cmd = " BRAINSMush "
    _outputs_filenames = {'outputMask': 'outputMask.nii.gz', 'outputWeightsFile': 'outputWeightsFile.txt', 'outputVolume': 'outputVolume.nii.gz'}


class BRAINSAlignMSPInputSpec(CommandLineInputSpec):
    inputVolume = File(desc=",         The Image to be resampled,       ", exists=True, argstr="--inputVolume %s")
    OutputresampleMSP = traits.Either(traits.Bool, File(), hash_files=False, desc=",         The image to be output.,       ", argstr="--OutputresampleMSP %s")
    verbose = traits.Bool(desc=",         Show more verbose output,       ", argstr="--verbose ")
    resultsDir = traits.Either(traits.Bool, Directory(), hash_files=False, desc=",         The directory for the results to be written.,       ", argstr="--resultsDir %s")
    writedebuggingImagesLevel = traits.Int(desc=",           This flag controls if debugging images are produced.  By default value of 0 is no images.  Anything greater than zero will be increasing level of debugging images.,       ", argstr="--writedebuggingImagesLevel %d")
    mspQualityLevel = traits.Int(desc=",           Flag cotrols how agressive the MSP is estimated.  0=quick estimate (9 seconds), 1=normal estimate (11 seconds), 2=great estimate (22 seconds), 3=best estimate (58 seconds).,       ", argstr="--mspQualityLevel %d")
    rescaleIntensities = traits.Bool(desc=",           Flag to turn on rescaling image intensities on input.,       ", argstr="--rescaleIntensities ")
    trimRescaledIntensities = traits.Float(
        desc=",           Turn on clipping the rescaled image one-tailed on input.  Units of standard deviations above the mean.  Very large values are very permissive.  Non-positive value turns clipping off.  Defaults to removing 0.00001 of a normal tail above the mean.,       ", argstr="--trimRescaledIntensities %f")
    rescaleIntensitiesOutputRange = InputMultiPath(traits.Int, desc=",           This pair of integers gives the lower and upper bounds on the signal portion of the output image.  Out-of-field voxels are taken from BackgroundFillValue.,       ", sep=",", argstr="--rescaleIntensitiesOutputRange %s")
    BackgroundFillValue = traits.Str(desc="Fill the background of image with specified short int value. Enter number or use BIGNEG for a large negative number.", argstr="--BackgroundFillValue %s")
    interpolationMode = traits.Enum("NearestNeighbor", "Linear", "ResampleInPlace", "BSpline", "WindowedSinc", "Hamming", "Cosine", "Welch", "Lanczos", "Blackman",
                                    desc="Type of interpolation to be used when applying transform to moving volume.  Options are Linear, ResampleInPlace, NearestNeighbor, BSpline, or WindowedSinc", argstr="--interpolationMode %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSAlignMSPOutputSpec(TraitedSpec):
    OutputresampleMSP = File(desc=",         The image to be output.,       ", exists=True)
    resultsDir = Directory(desc=",         The directory for the results to be written.,       ", exists=True)


class BRAINSAlignMSP(SEMLikeCommandLine):

    """title: Align Mid Saggital Brain (BRAINS)

category: Utilities.BRAINS

description: Resample an image into ACPC alignement ACPCDetect

"""

    input_spec = BRAINSAlignMSPInputSpec
    output_spec = BRAINSAlignMSPOutputSpec
    _cmd = " BRAINSAlignMSP "
    _outputs_filenames = {'OutputresampleMSP': 'OutputresampleMSP.nii', 'resultsDir': 'resultsDir'}


class BRAINSTransformConvertInputSpec(CommandLineInputSpec):
    inputTransform = File(exists=True, argstr="--inputTransform %s")
    referenceVolume = File(exists=True, argstr="--referenceVolume %s")
    outputTransformType = traits.Enum("Affine", "VersorRigid", "ScaleVersor", "ScaleSkewVersor", "DisplacementField", "Same", desc="The target transformation type. Must be conversion-compatible with the input transform type", argstr="--outputTransformType %s")
    displacementVolume = traits.Either(traits.Bool, File(), hash_files=False, argstr="--displacementVolume %s")
    outputTransform = traits.Either(traits.Bool, File(), hash_files=False, argstr="--outputTransform %s")


class BRAINSTransformConvertOutputSpec(TraitedSpec):
    displacementVolume = File(exists=True)
    outputTransform = File(exists=True)


class BRAINSTransformConvert(SEMLikeCommandLine):

    """title: BRAINS Transform Convert

category: Utilities.BRAINS

description: Convert ITK transforms to higher order transforms

version: 1.0

documentation-url: A utility to convert between transform file formats.

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Hans J. Johnson,Kent Williams

acknowledgements:


"""

    input_spec = BRAINSTransformConvertInputSpec
    output_spec = BRAINSTransformConvertOutputSpec
    _cmd = " BRAINSTransformConvert "
    _outputs_filenames = {'displacementVolume': 'displacementVolume.nii', 'outputTransform': 'outputTransform.mat'}


class landmarksConstellationAlignerInputSpec(CommandLineInputSpec):
    inputLandmarksPaired = File(desc="Input landmark file (.fcsv)", exists=True, argstr="--inputLandmarksPaired %s")
    outputLandmarksPaired = traits.Either(traits.Bool, File(), hash_files=False, desc="Output landmark file (.fcsv)", argstr="--outputLandmarksPaired %s")


class landmarksConstellationAlignerOutputSpec(TraitedSpec):
    outputLandmarksPaired = File(desc="Output landmark file (.fcsv)", exists=True)


class landmarksConstellationAligner(SEMLikeCommandLine):

    """title: MidACPC Landmark Insertion

category: Utilities.BRAINS

description:
  This program converts the original landmark files to the acpc-aligned landmark files


version:

documentation-url:

license:

contributor: Ali Ghayoor

acknowledgements:


"""

    input_spec = landmarksConstellationAlignerInputSpec
    output_spec = landmarksConstellationAlignerOutputSpec
    _cmd = " landmarksConstellationAligner "
    _outputs_filenames = {'outputLandmarksPaired': 'outputLandmarksPaired'}


class BRAINSEyeDetectorInputSpec(CommandLineInputSpec):
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")
    inputVolume = File(desc="The input volume", exists=True, argstr="--inputVolume %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="The output volume", argstr="--outputVolume %s")
    debugDir = traits.Str(desc="A place for debug information", argstr="--debugDir %s")


class BRAINSEyeDetectorOutputSpec(TraitedSpec):
    outputVolume = File(desc="The output volume", exists=True)


class BRAINSEyeDetector(SEMLikeCommandLine):

    """title: Eye Detector (BRAINS)

category: Utilities.BRAINS

description:


version: 1.0

documentation-url: http://www.nitrc.org/projects/brainscdetector/

"""

    input_spec = BRAINSEyeDetectorInputSpec
    output_spec = BRAINSEyeDetectorOutputSpec
    _cmd = " BRAINSEyeDetector "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class BRAINSLinearModelerEPCAInputSpec(CommandLineInputSpec):
    inputTrainingList = File(desc="Input Training Landmark List Filename,             ", exists=True, argstr="--inputTrainingList %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSLinearModelerEPCAOutputSpec(TraitedSpec):
    pass


class BRAINSLinearModelerEPCA(SEMLikeCommandLine):

    """title: Landmark Linear Modeler (BRAINS)

category: Utilities.BRAINS

description:
      Training linear model using EPCA. Implementation based on my MS thesis, "A METHOD FOR AUTOMATED LANDMARK CONSTELLATION DETECTION USING EVOLUTIONARY PRINCIPAL COMPONENTS AND STATISTICAL SHAPE MODELS"



version: 1.0

documentation-url: http://www.nitrc.org/projects/brainscdetector/

"""

    input_spec = BRAINSLinearModelerEPCAInputSpec
    output_spec = BRAINSLinearModelerEPCAOutputSpec
    _cmd = " BRAINSLinearModelerEPCA "
    _outputs_filenames = {}


class BRAINSInitializedControlPointsInputSpec(CommandLineInputSpec):
    inputVolume = File(desc="Input Volume", exists=True, argstr="--inputVolume %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="Output Volume", argstr="--outputVolume %s")
    splineGridSize = InputMultiPath(traits.Int, desc="The number of subdivisions of the BSpline Grid to be centered on the image space.  Each dimension must have at least 3 subdivisions for the BSpline to be correctly computed. ", sep=",", argstr="--splineGridSize %s")
    permuteOrder = InputMultiPath(traits.Int, desc="The permutation order for the images.  The default is 0,1,2 (i.e. no permutation)", sep=",", argstr="--permuteOrder %s")
    outputLandmarksFile = traits.Str(desc="Output filename", argstr="--outputLandmarksFile %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSInitializedControlPointsOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output Volume", exists=True)


class BRAINSInitializedControlPoints(SEMLikeCommandLine):

    """title: Initialized Control Points (BRAINS)

category:  Utilities.BRAINS

description:
  Outputs bspline control points as landmarks


version: 0.1.0.$Revision: 916 $(alpha)

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Mark Scully

acknowledgements:
This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.  Additional support for Mark Scully and Hans Johnson at the University of Iowa.


"""

    input_spec = BRAINSInitializedControlPointsInputSpec
    output_spec = BRAINSInitializedControlPointsOutputSpec
    _cmd = " BRAINSInitializedControlPoints "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class CleanUpOverlapLabelsInputSpec(CommandLineInputSpec):
    inputBinaryVolumes = InputMultiPath(File(exists=True), desc="The list of binary images to be checked and cleaned up. Order is important. Binary volume given first always wins out. ", argstr="--inputBinaryVolumes %s...")
    outputBinaryVolumes = traits.Either(traits.Bool, InputMultiPath(File(), ), hash_files=False, desc="The output label map images, with integer values in it. Each label value specified in the inputLabels is combined into this output label map volume", argstr="--outputBinaryVolumes %s...")


class CleanUpOverlapLabelsOutputSpec(TraitedSpec):
    outputBinaryVolumes = OutputMultiPath(File(exists=True), desc="The output label map images, with integer values in it. Each label value specified in the inputLabels is combined into this output label map volume", exists=True)


class CleanUpOverlapLabels(SEMLikeCommandLine):

    """title:  Clean Up Overla Labels

category: Utilities.BRAINS

description:  Take a series of input binary images and clean up for those overlapped area. Binary volumes given first always wins out

version: 0.1.0

contributor: Eun Young Kim

"""

    input_spec = CleanUpOverlapLabelsInputSpec
    output_spec = CleanUpOverlapLabelsOutputSpec
    _cmd = " CleanUpOverlapLabels "
    _outputs_filenames = {'outputBinaryVolumes': 'outputBinaryVolumes.nii'}


class BRAINSClipInferiorInputSpec(CommandLineInputSpec):
    inputVolume = File(desc="Input image to make a clipped short int copy from.", exists=True, argstr="--inputVolume %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="Output image, a short int copy of the upper portion of the input image, filled with BackgroundFillValue.", argstr="--outputVolume %s")
    acLowerBound = traits.Float(
        desc=",                 When the input image to the output image, replace the image with the BackgroundFillValue everywhere below the plane This Far in physical units (millimeters) below (inferior to) the AC point (assumed to be the voxel field middle.)  The oversize default was chosen to have no effect.  Based on visualizing a thousand masks in the IPIG study, we recommend a limit no smaller than 80.0 mm.,             ", argstr="--acLowerBound %f")
    BackgroundFillValue = traits.Str(desc="Fill the background of image with specified short int value. Enter number or use BIGNEG for a large negative number.", argstr="--BackgroundFillValue %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSClipInferiorOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output image, a short int copy of the upper portion of the input image, filled with BackgroundFillValue.", exists=True)


class BRAINSClipInferior(SEMLikeCommandLine):

    """title: Clip Inferior of Center of Brain (BRAINS)

category: Utilities.BRAINS

description: This program will read the inputVolume as a short int image, write the BackgroundFillValue everywhere inferior to the lower bound, and write the resulting clipped short int image in the outputVolume.


version: 1.0

"""

    input_spec = BRAINSClipInferiorInputSpec
    output_spec = BRAINSClipInferiorOutputSpec
    _cmd = " BRAINSClipInferior "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class GenerateLabelMapFromProbabilityMapInputSpec(CommandLineInputSpec):
    inputVolumes = InputMultiPath(File(exists=True), desc="The Input probaiblity images to be computed for lable maps", argstr="--inputVolumes %s...")
    outputLabelVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="The Input binary image for region of interest", argstr="--outputLabelVolume %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class GenerateLabelMapFromProbabilityMapOutputSpec(TraitedSpec):
    outputLabelVolume = File(desc="The Input binary image for region of interest", exists=True)


class GenerateLabelMapFromProbabilityMap(SEMLikeCommandLine):

    """title: Label Map from Probability Images

category: Utilities.BRAINS

description:
    Given a list of probability maps for labels, create a discrete label map where only the highest probability region is used for the labeling.


version: 0.1

contributor: University of Iowa Department of Psychiatry, http:://www.psychiatry.uiowa.edu


"""

    input_spec = GenerateLabelMapFromProbabilityMapInputSpec
    output_spec = GenerateLabelMapFromProbabilityMapOutputSpec
    _cmd = " GenerateLabelMapFromProbabilityMap "
    _outputs_filenames = {'outputLabelVolume': 'outputLabelVolume.nii.gz'}


class BRAINSLandmarkInitializerInputSpec(CommandLineInputSpec):
    inputFixedLandmarkFilename = File(desc="input fixed landmark. *.fcsv", exists=True, argstr="--inputFixedLandmarkFilename %s")
    inputMovingLandmarkFilename = File(desc="input moving landmark. *.fcsv", exists=True, argstr="--inputMovingLandmarkFilename %s")
    inputWeightFilename = File(desc="Input weight file name for landmarks. Higher weighted landmark will be considered more heavily. Weights are propotional, that is the magnitude of weights will be normalized by its minimum and maximum value. ", exists=True, argstr="--inputWeightFilename %s")
    outputTransformFilename = traits.Either(traits.Bool, File(), hash_files=False, desc="output transform file name (ex: ./outputTransform.mat) ", argstr="--outputTransformFilename %s")


class BRAINSLandmarkInitializerOutputSpec(TraitedSpec):
    outputTransformFilename = File(desc="output transform file name (ex: ./outputTransform.mat) ", exists=True)


class BRAINSLandmarkInitializer(SEMLikeCommandLine):

    """title: BRAINSLandmarkInitializer

category: Utilities.BRAINS

description: Create transformation file (*mat) from a pair of landmarks (*fcsv) files.

version:  1.0

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Eunyoung Regina Kim

"""

    input_spec = BRAINSLandmarkInitializerInputSpec
    output_spec = BRAINSLandmarkInitializerOutputSpec
    _cmd = " BRAINSLandmarkInitializer "
    _outputs_filenames = {'outputTransformFilename': 'outputTransformFilename'}


class BRAINSMultiModeSegmentInputSpec(CommandLineInputSpec):
    inputVolumes = InputMultiPath(File(exists=True), desc="The input image volumes for finding the largest region filled mask.", argstr="--inputVolumes %s...")
    inputMaskVolume = File(desc="The ROI for region to compute histogram levels.", exists=True, argstr="--inputMaskVolume %s")
    outputROIMaskVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="The ROI automatically found from the input image.", argstr="--outputROIMaskVolume %s")
    outputClippedVolumeROI = traits.Either(traits.Bool, File(), hash_files=False, desc="The inputVolume clipped to the region of the brain mask.", argstr="--outputClippedVolumeROI %s")
    lowerThreshold = InputMultiPath(traits.Float, desc="Lower thresholds on the valid histogram regions for each modality", sep=",", argstr="--lowerThreshold %s")
    upperThreshold = InputMultiPath(traits.Float, desc="Upper thresholds on the valid histogram regions for each modality", sep=",", argstr="--upperThreshold %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class BRAINSMultiModeSegmentOutputSpec(TraitedSpec):
    outputROIMaskVolume = File(desc="The ROI automatically found from the input image.", exists=True)
    outputClippedVolumeROI = File(desc="The inputVolume clipped to the region of the brain mask.", exists=True)


class BRAINSMultiModeSegment(SEMLikeCommandLine):

    """title: Segment based on rectangular region of joint histogram (BRAINS)

category: Utilities.BRAINS

description: This tool creates binary regions based on segmenting multiple image modalitities at once.


version: 2.4.1

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Hans J. Johnson, hans-johnson -at- uiowa.edu, http://www.psychiatry.uiowa.edu

acknowledgements: Hans Johnson(1,3,4); Gregory Harris(1), Vincent Magnotta(1,2,3);   (1=University of Iowa Department of Psychiatry, 2=University of Iowa Department of Radiology, 3=University of Iowa Department of Biomedical Engineering, 4=University of Iowa Department of Electrical and Computer Engineering)

"""

    input_spec = BRAINSMultiModeSegmentInputSpec
    output_spec = BRAINSMultiModeSegmentOutputSpec
    _cmd = " BRAINSMultiModeSegment "
    _outputs_filenames = {'outputROIMaskVolume': 'outputROIMaskVolume.nii', 'outputClippedVolumeROI': 'outputClippedVolumeROI.nii'}


class insertMidACPCpointInputSpec(CommandLineInputSpec):
    inputLandmarkFile = File(desc="Input landmark file (.fcsv)", exists=True, argstr="--inputLandmarkFile %s")
    outputLandmarkFile = traits.Either(traits.Bool, File(), hash_files=False, desc="Output landmark file (.fcsv)", argstr="--outputLandmarkFile %s")


class insertMidACPCpointOutputSpec(TraitedSpec):
    outputLandmarkFile = File(desc="Output landmark file (.fcsv)", exists=True)


class insertMidACPCpoint(SEMLikeCommandLine):

    """title: MidACPC Landmark Insertion

category: Utilities.BRAINS

description:
  This program gets a landmark fcsv file and adds a new landmark as the midpoint between AC and PC points to the output landmark fcsv file


version:

documentation-url:

license:

contributor: Ali Ghayoor

acknowledgements:


"""

    input_spec = insertMidACPCpointInputSpec
    output_spec = insertMidACPCpointOutputSpec
    _cmd = " insertMidACPCpoint "
    _outputs_filenames = {'outputLandmarkFile': 'outputLandmarkFile'}


class BRAINSSnapShotWriterInputSpec(CommandLineInputSpec):
    inputVolumes = InputMultiPath(File(exists=True), desc="Input image volume list to be extracted as 2D image. Multiple input is possible. At least one input is required.", argstr="--inputVolumes %s...")
    inputBinaryVolumes = InputMultiPath(File(exists=True), desc="Input mask (binary) volume list to be extracted as 2D image. Multiple input is possible.", argstr="--inputBinaryVolumes %s...")
    inputSliceToExtractInPhysicalPoint = InputMultiPath(traits.Float, desc="2D slice number of input images. For autoWorkUp output, which AC-PC aligned, 0,0,0 will be the center.", sep=",", argstr="--inputSliceToExtractInPhysicalPoint %s")
    inputSliceToExtractInIndex = InputMultiPath(traits.Int, desc="2D slice number of input images. For size of 256*256*256 image, 128 is usually used.", sep=",", argstr="--inputSliceToExtractInIndex %s")
    inputSliceToExtractInPercent = InputMultiPath(traits.Int, desc="2D slice number of input images. Percentage input from 0%-100%. (ex. --inputSliceToExtractInPercent 50,50,50", sep=",", argstr="--inputSliceToExtractInPercent %s")
    inputPlaneDirection = InputMultiPath(traits.Int, desc="Plane to display. In general, 0=saggital, 1=coronal, and 2=axial plane.", sep=",", argstr="--inputPlaneDirection %s")
    outputFilename = traits.Either(traits.Bool, File(), hash_files=False, desc="2D file name of input images. Required.", argstr="--outputFilename %s")


class BRAINSSnapShotWriterOutputSpec(TraitedSpec):
    outputFilename = File(desc="2D file name of input images. Required.", exists=True)


class BRAINSSnapShotWriter(SEMLikeCommandLine):

    """title: BRAINSSnapShotWriter

category: Utilities.BRAINS

description: Create 2D snapshot of input images. Mask images are color-coded

version:  1.0

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Eunyoung Regina Kim

"""

    input_spec = BRAINSSnapShotWriterInputSpec
    output_spec = BRAINSSnapShotWriterOutputSpec
    _cmd = " BRAINSSnapShotWriter "
    _outputs_filenames = {'outputFilename': 'outputFilename'}


class JointHistogramInputSpec(CommandLineInputSpec):
    inputVolumeInXAxis = File(desc="The Input image to be computed for statistics", exists=True, argstr="--inputVolumeInXAxis %s")
    inputVolumeInYAxis = File(desc="The Input image to be computed for statistics", exists=True, argstr="--inputVolumeInYAxis %s")
    inputMaskVolumeInXAxis = File(desc="Input mask volume for inputVolumeInXAxis. Histogram will be computed just for the masked region", exists=True, argstr="--inputMaskVolumeInXAxis %s")
    inputMaskVolumeInYAxis = File(desc="Input mask volume for inputVolumeInYAxis. Histogram will be computed just for the masked region", exists=True, argstr="--inputMaskVolumeInYAxis %s")
    outputJointHistogramImage = traits.Str(desc=" output joint histogram image file name. Histogram is usually 2D image. ", argstr="--outputJointHistogramImage %s")
    verbose = traits.Bool(desc=" print debugging information,       ", argstr="--verbose ")


class JointHistogramOutputSpec(TraitedSpec):
    pass


class JointHistogram(SEMLikeCommandLine):

    """title: Write Out Image Intensities


category: Utilities.BRAINS

description:
    For Analysis


version: 0.1

contributor: University of Iowa Department of Psychiatry, http:://www.psychiatry.uiowa.edu


"""

    input_spec = JointHistogramInputSpec
    output_spec = JointHistogramOutputSpec
    _cmd = " JointHistogram "
    _outputs_filenames = {}


class ShuffleVectorsModuleInputSpec(CommandLineInputSpec):
    inputVectorFileBaseName = File(desc="input vector file name prefix. Usually end with .txt and header file has prost fix of .txt.hdr", exists=True, argstr="--inputVectorFileBaseName %s")
    outputVectorFileBaseName = traits.Either(traits.Bool, File(), hash_files=False, desc="output vector file name prefix. Usually end with .txt and header file has prost fix of .txt.hdr", argstr="--outputVectorFileBaseName %s")
    resampleProportion = traits.Float(desc="downsample size of 1 will be the same size as the input images, downsample size of 3 will throw 2/3 the vectors away.", argstr="--resampleProportion %f")


class ShuffleVectorsModuleOutputSpec(TraitedSpec):
    outputVectorFileBaseName = File(desc="output vector file name prefix. Usually end with .txt and header file has prost fix of .txt.hdr", exists=True)


class ShuffleVectorsModule(SEMLikeCommandLine):

    """title: ShuffleVectors

category: Utilities.BRAINS

description: Automatic Segmentation using neural networks

version:  1.0

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Hans Johnson

"""

    input_spec = ShuffleVectorsModuleInputSpec
    output_spec = ShuffleVectorsModuleOutputSpec
    _cmd = " ShuffleVectorsModule "
    _outputs_filenames = {'outputVectorFileBaseName': 'outputVectorFileBaseName'}


class ImageRegionPlotterInputSpec(CommandLineInputSpec):
    inputVolume1 = File(desc="The Input image to be computed for statistics", exists=True, argstr="--inputVolume1 %s")
    inputVolume2 = File(desc="The Input image to be computed for statistics", exists=True, argstr="--inputVolume2 %s")
    inputBinaryROIVolume = File(desc="The Input binary image for region of interest", exists=True, argstr="--inputBinaryROIVolume %s")
    inputLabelVolume = File(desc="The Label Image", exists=True, argstr="--inputLabelVolume %s")
    numberOfHistogramBins = traits.Int(desc=" the number of histogram levels", argstr="--numberOfHistogramBins %d")
    outputJointHistogramData = traits.Str(desc=" output data file name", argstr="--outputJointHistogramData %s")
    useROIAUTO = traits.Bool(desc=" Use ROIAUTO to compute region of interest. This cannot be used with inputLabelVolume", argstr="--useROIAUTO ")
    useIntensityForHistogram = traits.Bool(desc=" Create Intensity Joint Histogram instead of Quantile Joint Histogram", argstr="--useIntensityForHistogram ")
    verbose = traits.Bool(desc=" print debugging information,       ", argstr="--verbose ")


class ImageRegionPlotterOutputSpec(TraitedSpec):
    pass


class ImageRegionPlotter(SEMLikeCommandLine):

    """title: Write Out Image Intensities


category: Utilities.BRAINS

description:  For Analysis

version: 0.1

contributor: University of Iowa Department of Psychiatry, http:://www.psychiatry.uiowa.edu


"""

    input_spec = ImageRegionPlotterInputSpec
    output_spec = ImageRegionPlotterOutputSpec
    _cmd = " ImageRegionPlotter "
    _outputs_filenames = {}
