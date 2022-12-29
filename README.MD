# Chess Position Evaluator

The only relevant folder is the "Important Files" folder

The `tester.py` file is used to create the CSV dataset file from the downloaded file from https://database.lichess.org/

Note that the tester.py file writes the data to chessData.csv but the header (first line) needs to be manually added:
`result,materialDifference,totalWhiteMaterial,totalBlackMaterial,colour,plyNumber,whiteInCheck,blackInCheck,whiteQueenExists,blackQueenExists,numSquaresWhiteAttacks,numSquaresBlackAttacks`

The `KNN.py` file runs the KNN model

The `SVM.py` file runs the SVM model

Note that the `SVM.py` file takes quite a few minutes to run


<img src="READMEfiles/ECE4553TermProjectReportRyanWhitney1.png" />
<img src="READMEfiles/ECE4553TermProjectReportRyanWhitney2.png" />
<img src="READMEfiles/ECE4553TermProjectReportRyanWhitney3.png" />
<img src="READMEfiles/ECE4553TermProjectReportRyanWhitney4.png" />
<img src="READMEfiles/ECE4553TermProjectReportRyanWhitney5.png" />
