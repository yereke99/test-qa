import SwiftUI

struct ContentView: View {
    @State private var display = "0"
    @State private var firstNumber: String = ""
    @State private var secondNumber: String = ""
    @State private var operation: String = ""

    var body: some View {
        VStack {
            Spacer()
            Text(display)
                .font(.largeTitle)
                .padding()
                .accessibilityIdentifier("display")
            
            HStack {
                Button(action: { self.tapDigit("1") }) {
                    Text("1")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("1")
                }
                Button(action: { self.tapDigit("2") }) {
                    Text("2")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("2")
                }
                Button(action: { self.tapDigit("3") }) {
                    Text("3")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("3")
                }
                Button(action: { self.clear() }) {
                    Text("C")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.red)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("clear")
                }
            }
            .padding(.bottom, 10)
            
            HStack {
                Button(action: { self.tapDigit("4") }) {
                    Text("4")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("4")
                }
                Button(action: { self.tapDigit("5") }) {
                    Text("5")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("5")
                }
                Button(action: { self.tapDigit("6") }) {
                    Text("6")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("6")
                }
                Button(action: { self.tapOperation("-") }) {
                    Text("-")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.orange)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("subtract")
                }
            }
            .padding(.bottom, 10)
            
            HStack {
                Button(action: { self.tapDigit("7") }) {
                    Text("7")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("7")
                }
                Button(action: { self.tapDigit("8") }) {
                    Text("8")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("8")
                }
                Button(action: { self.tapDigit("9") }) {
                    Text("9")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("9")
                }
                Button(action: { self.tapOperation("+") }) {
                    Text("+")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.orange)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("add")
                }
            }
            .padding(.bottom, 10)
            
            HStack {
                Button(action: { self.tapOperation("/") }) {
                    Text("/")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.orange)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("divide")
                }
                Button(action: { self.tapDigit("0") }) {
                    Text("0")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.gray)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("0")
                }
                Button(action: { self.tapOperation("%") }) {
                    Text("%")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.orange)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("modulus")
                }
                Button(action: { self.tapEquals() }) {
                    Text("=")
                        .font(.largeTitle)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .accessibilityIdentifier("equals")
                }
            }
        }
        .padding()
    }
    
    private func tapDigit(_ digit: String) {
        if operation.isEmpty {
            firstNumber += digit
            display = firstNumber
        } else {
            secondNumber += digit
            display = secondNumber
        }
    }
    
    private func tapOperation(_ operation: String) {
        if !firstNumber.isEmpty {
            self.operation = operation
        }
    }
    
    private func tapEquals() {
        if let firstValue = Int(firstNumber), let secondValue = Int(secondNumber) {
            switch operation {
            case "+":
                display = "\(firstValue + secondValue)"
            case "-":
                display = "\(firstValue - secondValue)"
            case "*":
                display = "\(firstValue * secondValue)"
            case "/":
                if secondValue != 0 {
                    display = "\(firstValue / secondValue)"
                } else {
                    display = "Error"
                }
            case "%":
                display = "\(firstValue % secondValue)"
            default:
                break
            }
        }
        
        // Reset the values for the next operation
        firstNumber = ""
        secondNumber = ""
        operation = ""
    }
    
    private func clear() {
        firstNumber = ""
        secondNumber = ""
        operation = ""
        display = "0"
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
