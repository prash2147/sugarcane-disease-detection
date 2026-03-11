// import Razorpay from "razorpay";
// import { NextResponse } from "next/server";

// const razorpay = new Razorpay({
//   key_id: "YOUR_KEY_ID",
//   key_secret: "YOUR_SECRET"
// });

// export async function POST(req: Request) {

//   const options = {
//     amount: 4900,
//     currency: "INR"
//   };

//   const order = await razorpay.orders.create(options);

//   return NextResponse.json(order);
// }

import { NextResponse } from "next/server";

export async function POST() {

  return NextResponse.json({
    id: "order_test_123",
    amount: 9900
  });

}

