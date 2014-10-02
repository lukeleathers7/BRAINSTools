# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class fcsv_to_hdf5InputSpec(CommandLineInputSpec):
    versionID = traits.Str(desc=",         Current version ID. It should be match with the version of BCD that will be using the output model file,       ", argstr="--versionID %s")
    landmarksInformationFile = traits.Either(traits.Bool, File(), hash_files=False, desc=",         name of HDF5 file to write matrices into,       ", argstr="--landmarksInformationFile %s")
    landmarkTypesList = File(desc=",         file containing list of landmark types,       ", exists=True, argstr="--landmarkTypesList %s")
    modelFile = traits.Either(traits.Bool, File(), hash_files=False, desc=",         name of HDF5 file containing BRAINSConstellationDetector Model file (LLSMatrices, LLSMeans and LLSSearchRadii),       ", argstr="--modelFile %s")
    landmarkGlobPattern = traits.Str(desc="Glob pattern to select fcsv files", argstr="--landmarkGlobPattern %s")
    numberOfThreads = traits.Int(desc="Explicitly specify the maximum number of threads to use.", argstr="--numberOfThreads %d")


class fcsv_to_hdf5OutputSpec(TraitedSpec):
    landmarksInformationFile = File(desc=",         name of HDF5 file to write matrices into,       ", exists=True)
    modelFile = File(desc=",         name of HDF5 file containing BRAINSConstellationDetector Model file (LLSMatrices, LLSMeans and LLSSearchRadii),       ", exists=True)


class fcsv_to_hdf5(SEMLikeCommandLine):

    """title: fcsv_to_hdf5 (BRAINS)

category: Utility.BRAINS

description: Convert a collection of fcsv files to a HDF5 format file

"""

    input_spec = fcsv_to_hdf5InputSpec
    output_spec = fcsv_to_hdf5OutputSpec
    _cmd = " fcsv_to_hdf5 "
    _outputs_filenames = {'modelFile': 'modelFile', 'landmarksInformationFile': 'landmarksInformationFile.h5'}


class FindCenterOfBrainInputSpec(CommandLineInputSpec):
    inputVolume = File(desc="The image in which to find the center.", exists=True, argstr="--inputVolume %s")
    imageMask = File(exists=True, argstr="--imageMask %s")
    clippedImageMask = traits.Either(traits.Bool, File(), hash_files=False, argstr="--clippedImageMask %s")
    maximize = traits.Bool(argstr="--maximize ")
    axis = traits.Int(argstr="--axis %d")
    otsuPercentileThreshold = traits.Float(argstr="--otsuPercentileThreshold %f")
    closingSize = traits.Int(argstr="--closingSize %d")
    headSizeLimit = traits.Float(argstr="--headSizeLimit %f")
    headSizeEstimate = traits.Float(argstr="--headSizeEstimate %f")
    backgroundValue = traits.Int(argstr="--backgroundValue %d")
    generateDebugImages = traits.Bool(argstr="--generateDebugImages ")
    debugDistanceImage = traits.Either(traits.Bool, File(), hash_files=False, argstr="--debugDistanceImage %s")
    debugGridImage = traits.Either(traits.Bool, File(), hash_files=False, argstr="--debugGridImage %s")
    debugAfterGridComputationsForegroundImage = traits.Either(traits.Bool, File(), hash_files=False, argstr="--debugAfterGridComputationsForegroundImage %s")
    debugClippedImageMask = traits.Either(traits.Bool, File(), hash_files=False, argstr="--debugClippedImageMask %s")
    debugTrimmedImage = traits.Either(traits.Bool, File(), hash_files=False, argstr="--debugTrimmedImage %s")


class FindCenterOfBrainOutputSpec(TraitedSpec):
    clippedImageMask = File(exists=True)
    debugDistanceImage = File(exists=True)
    debugGridImage = File(exists=True)
    debugAfterGridComputationsForegroundImage = File(exists=True)
    debugClippedImageMask = File(exists=True)
    debugTrimmedImage = File(exists=True)


class FindCenterOfBrain(SEMLikeCommandLine):

    """title: Center Of Brain (BRAINS)

category: Utility.BRAINS

description: Finds the center point of a brain

version: 3.0.0

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Hans J. Johnson, hans-johnson -at- uiowa.edu, http://wwww.psychiatry.uiowa.edu

acknowledgements: Hans Johnson(1,3,4); Kent Williams(1);  (1=University of Iowa Department of Psychiatry, 3=University of Iowa Department of Biomedical Engineering, 4=University of Iowa Department of Electrical and Computer Engineering

"""

    input_spec = FindCenterOfBrainInputSpec
    output_spec = FindCenterOfBrainOutputSpec
    _cmd = " FindCenterOfBrain "
    _outputs_filenames = {'debugClippedImageMask': 'debugClippedImageMask.nii', 'debugTrimmedImage': 'debugTrimmedImage.nii', 'debugDistanceImage': 'debugDistanceImage.nii',
                          'debugGridImage': 'debugGridImage.nii', 'clippedImageMask': 'clippedImageMask.nii', 'debugAfterGridComputationsForegroundImage': 'debugAfterGridComputationsForegroundImage.nii'}
