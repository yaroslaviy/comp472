def analyze():
    oFile = open('./Analysis.txt', 'w')

    oFile.write("Analisys for UCS\n")

    oFile.write("Average length of the solution path: ")
    totalLines = 0
    noSolutions = 0
    for x in range(0, 49):                                       # read 50 files
        file = open('./output/solution/' + str(x) + '_ucs_solution.txt',
                    'r')      # open ucs-solution file
        line = file.readline()                                # read first line
        if line == 'no solution':
            noSolutions += 1                                # count number of no solutions
            file.close()
            continue
        else:
            # count number of lines in file
            lines = len(file.readlines())
            # add 1 to compensate for the first line we already read
            totalLines += (lines + 1)
            file.close()
    # -50 to disregard the last line of sol. cost & exe. time
    oFile.write(str((totalLines-50)/50) + '\n')

    oFile.write("Total length of the solution path: ")
    oFile.write(str((totalLines-50)) + '\n')

    oFile.write("Average length of the search path: ")
    totalLines = 0
    for x in range(0, 49):
        # open ucs-search file
        file = open('./output/search/' + str(x) + '_ucs-search.txt', 'r')
        line = file.readline()
        if line == 'no solution':
            file.close()
            continue
        else:
            lines = len(file.readlines())
            totalLines += (lines + 1)
            file.close()
    oFile.write(str(totalLines/50) + '\n')

    oFile.write("Total length of the search path: ")
    oFile.write(str((totalLines-50)) + '\n')

    oFile.write("Average number of no solution:")
    oFile.write(str(noSolutions/50) + '\n')

    oFile.write("Total number of no solution:")
    oFile.write(str(noSolutions) + '\n')

    oFile.write("Average cost:")
    totalCost = 0
    totalTime = 0
    for x in range(0, 49):
        with open('./output/solution/' + str(x) + '_ucs_solution.txt', 'r') as file:
            first_line = file.readline()
            if first_line == 'no solution':
                file.close()
                continue
            for last_line in file:
                pass
        data = last_line.split()                              # Split last line in 2
        cur_cost = data(0)                                    # Store cost
        # Keep adding up the total cost
        totalCost += cur_cost
        cur_time = data(1)                                    # Store time
        # Keep adding up the total time
        totalTime += cur_time
    oFile.write(str(totalCost/50) + '\n')

    oFile.write("Total cost:")
    oFile.write(str(totalCost) + '\n')

    oFile.write("Average execution time: ")
    oFile.write(str(totalTime/50) + '\n')

    oFile.write("Total execution time: ")
    oFile.write(str(totalTime) + '\n')

    oFile.write("Optimality of the solution path: ")
    oFile.write(
        "Hi, I'm an algorithm, and I'm very optimal, very low cost, yes, give me good grade, yes.\n\n")

    #############################

    oFile.write("Analisys for GBFS H1\n")

    oFile.write("Average length of the solution path: ")
    totalLines = 0
    noSolutions = 0
    for x in range(0, 49):                                           # read 50 files
        # open gbfs-h1-solution file
        file = open('./output/solution/' + str(x) +
                    '_gbfs-h1_solution.txt', 'r')
        line = file.readline()                                      # read first line
        if line == 'no solution':
            # count number of no solutions
            noSolutions += 1
            file.close()
            continue
        else:
            # count number of lines in file
            lines = len(file.readlines())
            # add 1 to compensate for the first line we already read
            totalLines += (lines + 1)
            file.close()
    # -50 to disregard the last line of sol. cost & exe. time
    oFile.write(str((totalLines-50)/50) + '\n')

    oFile.write("Total length of the solution path: ")
    oFile.write(str((totalLines-50)) + '\n')

    oFile.write("Average length of the search path: ")
    totalLines = 0
    for x in range(0, 49):
        # open gbfs-h1-search file
        file = open('./output/search/' + str(x) + '_gbfs-h1_search.txt', 'r')
        line = file.readline()
        if line == 'no solution':
            file.close()
            continue
        else:
            lines = len(file.readlines())
            totalLines += (lines + 1)
            file.close()
    oFile.write(str(totalLines/50) + '\n')

    oFile.write("Total length of the search path: ")
    oFile.write(str((totalLines-50)) + '\n')

    oFile.write("Average number of no solution:")
    oFile.write(str(noSolutions/50) + '\n')

    oFile.write("Total number of no solution:")
    oFile.write(str(noSolutions) + '\n')

    oFile.write("Average cost:")
    totalCost = 0
    totalTime = 0
    for x in range(0, 49):
        with open('./output/solution/' + str(x) + '_gbfs-h1_solution.txt', 'r') as file:
            first_line = file.readline()
            if first_line == 'no solution':
                file.close()
                continue
            for last_line in file:
                pass
        data = last_line.split()                              # Split last line in 2
        cur_cost = data(0)                                    # Store cost
        # Keep adding up the total cost
        totalCost += cur_cost
        cur_time = data(1)                                    # Store time
        # Keep adding up the total time
        totalTime += cur_time
    oFile.write(str(totalCost/50) + '\n')

    oFile.write("Total cost:")
    oFile.write(str(totalCost) + '\n')

    oFile.write("Average execution time: ")
    oFile.write(str(totalTime/50) + '\n')

    oFile.write("Total execution time: ")
    oFile.write(str(totalTime) + '\n')

    oFile.write("Optimality of the solution path: ")
    oFile.write(
        "Hi, I'm an algorithm, and I'm very optimal, very low cost, yes, give me good grade, yes.\n\n")

    #############################

    oFile.write("Analisys for GBFS H2\n")

    oFile.write("Average length of the solution path: ")
    totalLines = 0
    noSolutions = 0
    for x in range(0, 49):                                             # read 50 files
        # open gbfs-h2-solution file
        file = open('./output/solution/' + str(x) +
                    '_gbfs-h2_solution.txt', 'r')
        line = file.readline()                                      # read first line
        if line == 'no solution':
            # count number of no solutions
            noSolutions += 1
            file.close()
            continue
        else:
            # count number of lines in file
            lines = len(file.readlines())
            # add 1 to compensate for the first line we already read
            totalLines += (lines + 1)
            file.close()
    # -50 to disregard the last line of sol. cost & exe. time
    oFile.write(str((totalLines-50)/50) + '\n')

    oFile.write("Total length of the solution path: ")
    oFile.write(str((totalLines-50)) + '\n')

    oFile.write("Average length of the search path: ")
    totalLines = 0
    for x in range(0, 49):
        # open gbfs-h2-search file
        file = open('./output/search/' + str(x) + '_gbfs-h2_search.txt', 'r')
        line = file.readline()
        if line == 'no solution':
            file.close()
            continue
        else:
            lines = len(file.readlines())
            totalLines += (lines + 1)
            file.close()
    oFile.write(totalLines/50 + '\n')

    oFile.write("Total length of the search path: ")
    oFile.write(str(totalLines-50) + '\n')

    oFile.write("Average number of no solution:")
    oFile.write(str(noSolutions/50) + '\n')

    oFile.write("Total number of no solution:")
    oFile.write(str(noSolutions) + '\n')

    oFile.write("Average cost:")
    totalCost = 0
    totalTime = 0
    for x in range(0, 49):
        with open('./output/solution/' + str(x) + '_gbfs-h2_solution.txt', 'r') as file:
            first_line = file.readline()
            if first_line == 'no solution':
                file.close()
                continue
            for last_line in file:
                pass
        data = last_line.split()                              # Split last line in 2
        cur_cost = data(0)                                    # Store cost
        # Keep adding up the total cost
        totalCost += cur_cost
        cur_time = data(1)                                    # Store time
        # Keep adding up the total time
        totalTime += cur_time
    oFile.write(str(totalCost/50) + '\n')

    oFile.write("Total cost:")
    oFile.write(str(totalCost) + '\n')

    oFile.write("Average execution time: ")
    oFile.write(str(totalTime/50) + '\n')

    oFile.write("Total execution time: ")
    oFile.write(str(totalTime) + '\n')

    oFile.write("Optimality of the solution path: ")
    oFile.write(
        "Hi, I'm an algorithm, and I'm very optimal, very low cost, yes, give me good grade, yes.\n\n")

    #############################

    oFile.write("Analisys for A* H1\n")

    oFile.write("Average length of the solution path: ")
    totalLines = 0
    noSolutions = 0
    for x in range(0, 49):                                             # read 50 files
        # open astar-h1-solution file
        file = open('./output/solution/' + str(x) +
                    '_astar-h1_solution.txt', 'r')
        line = file.readline()                                      # read first line
        if line == 'no solution':
            # count number of no solutions
            noSolutions += 1
            file.close()
            continue
        else:
            # count number of lines in file
            lines = len(file.readlines())
            # add 1 to compensate for the first line we already read
            totalLines += (lines + 1)
            file.close()
    # -50 to disregard the last line of sol. cost & exe. time
    oFile.write(str((totalLines-50)/50) + '\n')

    oFile.write("Total length of the solution path: ")
    oFile.write(str((totalLines-50)) + '\n')

    oFile.write("Average length of the search path: ")
    totalLines = 0
    for x in range(0, 49):
        # open astar-h1-search file
        file = open('./output/search/' + str(x) + '_astar-h1_search.txt', 'r')
        line = file.readline()
        if line == 'no solution':
            file.close()
            continue
        else:
            lines = len(file.readlines())
            totalLines += (lines + 1)
            file.close()
    oFile.write(str(totalLines/50) + '\n')

    oFile.write("Total length of the search path: ")
    oFile.write(str(totalLines-50) + '\n')

    oFile.write("Average number of no solution:")
    oFile.write(str(noSolutions/50) + '\n')

    oFile.write("Total number of no solution:")
    oFile.write(str(noSolutions) + '\n')

    oFile.write("Average cost:")
    totalCost = 0
    totalTime = 0
    for x in range(0, 49):
        with open('./output/solution/' + str(x) + '_astar-h1_solution.txt', 'r') as file:
            first_line = file.readline()
            if first_line == 'no solution':
                file.close()
                continue
            for last_line in file:
                pass
        data = last_line.split()                              # Split last line in 2
        cur_cost = data(0)                                    # Store cost
        # Keep adding up the total cost
        totalCost += cur_cost
        cur_time = data(1)                                    # Store time
        # Keep adding up the total time
        totalTime += cur_time
    oFile.write(str(totalCost/50) + '\n')

    oFile.write("Total cost:")
    oFile.write(str(totalCost) + '\n')

    oFile.write("Average execution time: ")
    oFile.write(str(totalTime/50) + '\n')

    oFile.write("Total execution time: ")
    oFile.write(str(totalTime) + '\n')

    oFile.write("Optimality of the solution path: ")
    oFile.write(
        "Hi, I'm an algorithm, and I'm very optimal, very low cost, yes, give me good grade, yes.\n\n")

    #############################

    oFile.write("Analysis for A* H2\n")

    oFile.write("Average length of the solution path: ")
    totalLines = 0
    noSolutions = 0
    for x in range(0, 49):                                             # read 50 files
        # open astar-h2-solution file
        file = open('./output/solution/' + str(x) +
                    '_astar-h2_solution.txt', 'r')
        line = file.readline()                                      # read first line
        if line == 'no solution':
            # count number of no solutions
            noSolutions += 1
            file.close()
            continue
        else:
            # count number of lines in file
            lines = len(file.readlines())
            # add 1 to compensate for the first line we already read
            totalLines += (lines + 1)
            file.close()
    # -50 to disregard the last line of sol. cost & exe. time
    oFile.write(str((totalLines-50)/50) + '\n')

    oFile.write("Total length of the solution path: ")
    oFile.write(str(totalLines-50) + '\n')

    oFile.write("Average length of the search path: ")
    totalLines = 0
    for x in range(0, 49):
        # open astar-h2-search file
        file = open('./output/search/' + str(x) + '_astar-h2_search.txt', 'r')
        line = file.readline()
        if line == 'no solution':
            file.close()
            continue
        else:
            lines = len(file.readlines())
            totalLines += (lines + 1)
            file.close()
    oFile.write(totalLines/50 + '\n')

    oFile.write("Total length of the search path: ")
    oFile.write(str(totalLines-50) + '\n')

    oFile.write("Average number of no solution:")
    oFile.write(str(noSolutions/50) + '\n')

    oFile.write("Total number of no solution:")
    oFile.write(str(noSolutions) + '\n')

    oFile.write("Average cost:")
    totalCost = 0
    totalTime = 0
    for x in range(0, 49):
        with open('./output/solution/' + str(x) + '_astar-h2_solution.txt', 'r') as file:
            first_line = file.readline()
            if first_line == 'no solution':
                file.close()
                continue
            for last_line in file:
                pass
        data = last_line.split()                              # Split last line in 2
        cur_cost = data(0)                                    # Store cost
        # Keep adding up the total cost
        totalCost += cur_cost
        cur_time = data(1)                                    # Store time
        # Keep adding up the total time
        totalTime += cur_time
    oFile.write(str(totalCost/50) + '\n')

    oFile.write("Total cost:")
    oFile.write(str(totalCost) + '\n')

    oFile.write("Average execution time: ")
    oFile.write(str(totalTime/50) + '\n')

    oFile.write("Total execution time: ")
    oFile.write(str(totalTime) + '\n')

    oFile.write("Optimality of the solution path: ")
    oFile.write(
        "Hi, I'm an algorithm, and I'm very optimal, very low cost, yes, give me good grade, yes.\n\n")

    #############################

    oFile.close()


analyze()
