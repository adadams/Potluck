# Default Settings

name = "example"  # Bundled example file
mode = 0  # Emission spectrum
modestr = "Resolved"  # Needed for output file name
parallel = True  # Parallel operation
datain = "examples/example.obs.dat"  # Bundled example file
polyfit = False  # Switch to normalize the spectrum to a polynomial fit
norm = False  # Dummy variable if polyfit is false
samples_file = None
num_samples = 0
dataconv = 1  # Factor to convolve the observations to blur the spectrum or account for actual resolving power
databin = 1  # Factor to bin down the observations for simpler fitting
degrade = 1  # Factor to degrade the model spectrum for faster calculation
prior = "Uniform"  # Uniform priors
nwalkers = 0  # Placeholder for later adjustment
nsteps = 30000  # Tested minimum required number of steps
tstar = 5770.0  # Solar temperature
rstar = 1.0  # Solar radius
sma = 1.0  # Semi-Major Axis
starspec = ""  # Optional stellar spectrum file
dist = 10.0  # Standardized distance, 10 pc
RA = 0.0  # Right ascension
dec = 0.0  # Declination
minmass = 0.5  # Minimum mass in Jupiter masses
maxmass = 80.0  # Maximum mass in Jupiter masses
hires = ""  # Default set of opacity tables to compute the spectra
lores = "lores"  # Default low-resolution tables to compute Teff
minP = 0.0  # Pressure range to integrate over in cgs, default 1 mubar to 1 kbar.
maxP = 9.0
gray = False  # Used to create a gray atmosphere for testing
vres = 71  # Number of layers for radiative transfer
streams = 1  # Use 1-stream by default
wavei = 10000.0 / 0.60  # Full NIR wavelength range
wavef = 10000.0 / 5.00
outmode = ""  # JWST observing mode
exptime = 1000.0  # Exposure time in seconds
outdir = "/nfs/arthurad/samples"  # Default output directory
short = False  # Switch to create short output file names
printfull = False  # Switch to print the full sample array instead of the last 10%
opacdir = "/nfs/arthurad/Opacities_0v10"  # Default opacities directory
minT = 75  # Minimum temperature for opacity tables
maxT = 4000  # Maximum temperature for opacity tables

norad = False  # Flags if no radius variable is in the input file
natm = 0  # Placeholder in case T-P profile is omitted
verbatim = False  # Interpolate the T-P profile
tgray = 1500  # Temperature of gray atmosphere
hazetype = 0  # No Clouds
hazestr = "None"  # No Clouds
cloudmod = 0  # No Clouds

hazelist = [
    "None",
    "H2SO4",
    "Polyacetylene",
    "Tholin",
    "Corundum",
    "Enstatite",
    "Forsterite",
    "Iron",
    "KCl",
    "Na2S",
    "NH3Ice",
    "Soot",
    "H2OCirrus",
    "H2OIce",
    "ZnS",
]
