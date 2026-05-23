# Available random number generator modes
prng_modes = [
    "ThreadLocalRandom",
    "Random",
    "SecureRandom",
    "Well512a",
    "Well1024a",
    "Well19937a",
    "Well19937c",
    "Well44497a",
    "Well44497b",
    "MersenneTwister",
    "SFC64",
    "ISAAC",
    "XoRoShiRo128++",
    "XoRoShiRo128**",
    "XoRoShiRo64**",
	"XoRoShiRo256++",
	"XoRoShiRo1024++",
	"XoRoShiRo1024*",
	"XoRoShiRo1024**",
    "L32X64Mix",
    "L64X128Mix",
	"L64X128**",
	"L64X256Mix",
	"L64X1024Mix",
	"L128X128Mix",
	"L128X256Mix",
	"L128X1024Mix",
	"PcgRxsMXs64",
	"Philox4x64",
    "Drand48",
    "Drand48Mix",
    # "ThreadLocalRandomSlow"  # Only for speed comparison, same generator as "ThreadLocalRandom" above
]

# Connection settings
host = "localhost"
port = 10000

# Number of arrival times to be simulated
arrival_count = 100_000_000
