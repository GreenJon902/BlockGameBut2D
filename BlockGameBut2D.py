from App import logger_setup, logger, name, version, author

if __name__ == "__main__":
    logger_setup()
    logger.info("Setup", "Logger has been setup")

    import OpenGL
    import OpenGL.GL
    import OpenGL.GLUT
    import OpenGL.GLU

    logger.info("Setup", "OpenGL has been setup")
    logger.empty()
    logger.info(" ", "---", name, "---")
    logger.info(" ", "Version", version)
    logger.info(" ", "By", author)
    logger.info(" ", "----" + str().join(["-" for _ in name]) + "----")
    logger.empty()
    logger.info(name, "Starting!")
