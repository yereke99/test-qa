import XCTest

class CalculatorUITests: XCTestCase {
    
    var app: XCUIApplication!

    override func setUpWithError() throws {
        // Launch the application
        app = XCUIApplication()
        app.launch()
    }

    override func tearDownWithError() throws {
        // Close the application
        app.terminate()
    }

    func testAddition() throws {
        // Tap the buttons to enter numbers and perform addition
        app.buttons["1"].tap()
        app.buttons["+"].tap()
        app.buttons["2"].tap()
        app.buttons["="].tap()
        
        // Check if the result label displays the correct sum
        let resultLabel = app.staticTexts["resultLabel"]
        XCTAssertEqual(resultLabel.label, "3")
    }

    func testSubtraction() throws {
        // Tap the buttons to enter numbers and perform subtraction
        app.buttons["5"].tap()
        app.buttons["-"].tap()
        app.buttons["3"].tap()
        app.buttons["="].tap()
        
        // Check if the result label displays the correct difference
        let resultLabel = app.staticTexts["resultLabel"]
        XCTAssertEqual(resultLabel.label, "2")
    }

    func testMultiplication() throws {
        // Tap the buttons to enter numbers and perform multiplication
        app.buttons["3"].tap()
        app.buttons["*"].tap()
        app.buttons["4"].tap()
        app.buttons["="].tap()
        
        // Check if the result label displays the correct product
        let resultLabel = app.staticTexts["resultLabel"]
        XCTAssertEqual(resultLabel.label, "12")
    }

    func testDivision() throws {
        // Tap the buttons to enter numbers and perform division
        app.buttons["8"].tap()
        app.buttons["÷"].tap()
        app.buttons["2"].tap()
        app.buttons["="].tap()
        
        // Check if the result label displays the correct quotient
        let resultLabel = app.staticTexts["resultLabel"]
        XCTAssertEqual(resultLabel.label, "4")
    }

    func testDivisionByZero() throws {
        // Tap the buttons to enter numbers and perform division by zero
        app.buttons["5"].tap()
        app.buttons["÷"].tap()
        app.buttons["0"].tap()
        app.buttons["="].tap()
        
        // Check if the alert is displayed with the correct message
        let alert = app.alerts.firstMatch
        XCTAssertTrue(alert.waitForExistence(timeout: 1))
        XCTAssertEqual(alert.staticTexts.firstMatch.label, "Error: Division by zero")
        alert.buttons["OK"].tap()
    }

    func testInvalidInput() throws {
        // Tap the buttons to enter an invalid input
        app.buttons["+"].tap()
        app.buttons["="].tap()
        
        // Check if the alert is displayed with the correct message
        let alert = app.alerts.firstMatch
        XCTAssertTrue(alert.waitForExistence(timeout: 1))
        XCTAssertEqual(alert.staticTexts.firstMatch.label, "Error: Invalid input")
        alert.buttons["OK"].tap()
    }
}
