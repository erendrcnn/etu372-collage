// test/module_test.ts
import { assertEquals } from "https://deno.land/std/testing/asserts.ts";
import { add, subtract } from "../app/module.ts";

Deno.test("add function should add two numbers", () => {
  const result = add(3, 5);
  assertEquals(result, 8);
});

Deno.test("subtract function should subtract two numbers", () => {
  const result = subtract(8, 3);
  assertEquals(result, 5);
});
