from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(build_types=["Release"])
    builder.add_common_builds()
    builder.run()